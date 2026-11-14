#!/usr/bin/env python3
"""Rebuild the existing research cross-index from its released catalog.

Paper rationales, article prose and reference evidence remain editorial work.
This script rebuilds only article metadata and the four derived index tables.
It can audit without writing using --check.
"""

import argparse
from collections import defaultdict
from hashlib import sha256
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
ARTICLES = ROOT / "research-articles"
CATALOG = ARTICLES / "catalog.json"
CROSS = ARTICLES / "CROSS_INDEX.md"
METHOD_TITLE = "## Method index"
REF_TITLE = "## Primary-reference index"
DERIVED_START = "## Research-area index\n"
DERIVED_END = "## Standalone reviews\n"


def fail_if(condition, message):
    if condition:
        raise ValueError(message)


def table_rows(section):
    return [line for line in section.splitlines() if line.startswith("| ") and not line.startswith("| ---")]


def from_heading(text, start, end):
    return text.split(start, 1)[1].split(end, 1)[0]


def current_names(text):
    methods = {}
    for row in table_rows(from_heading(text, METHOD_TITLE, REF_TITLE)):
        parts = [p.strip() for p in row.strip("|").split("|")]
        if len(parts) == 3 and parts[0] != "Method":
            methods[parts[0]] = parts[1]
    refs = {}
    for row in table_rows(from_heading(text, REF_TITLE, DERIVED_END)):
        match = re.match(r"\| \[(.+?)\]\(REFERENCES\.md#([\w-]+)\)", row)
        if match:
            refs[match.group(2).upper()] = match.group(1)
    return methods, refs


def link_ids(ids):
    return " · ".join(f"[{item}]({item}.md)" for item in sorted(ids))


def derive_tables(catalog, existing):
    method_names, reference_names = current_names(existing)
    areas, topics, methods, refs = (defaultdict(set) for _ in range(4))
    for article in catalog["articles"]:
        aid = article["article_id"]
        for area in article["research_areas"]:
            areas[area].add(aid)
        for topic in article["topics"]:
            topics[topic].add(aid)
        for method in article["methods"]:
            methods[method].add(aid)
        for reference in article["primary_reference_ids"]:
            refs[reference].add(aid)

    lines = ["## Research-area index", "", "| Area | Articles |", "| --- | --- |"]
    for slug, ids in sorted(areas.items()):
        path = ROOT / "research-areas" / f"{slug}.md"
        fail_if(not path.exists(), f"Unknown area: {slug}")
        label = slug.replace("-", " ").capitalize()
        if slug == "human-machine-research":
            label = "Human–machine research"
        lines.append(f"| [{label}](../research-areas/{slug}.md) | {link_ids(ids)} |")

    lines += ["", "## Topic index", "", "| Topic | Articles |", "| --- | --- |"]
    lines += [f"| {topic} | {link_ids(ids)} |" for topic, ids in sorted(topics.items())]

    lines += ["", METHOD_TITLE, "", "| Method | Meaning | Articles |", "| --- | --- | --- |"]
    fail_if(set(method_names) != set(methods), "Method descriptions require editorial reconciliation")
    for method, description in method_names.items():
        lines.append(f"| {method} | {description} | {link_ids(methods[method])} |")

    lines += ["", REF_TITLE, "", "| Reference | Articles using it |", "| --- | --- |"]
    fail_if(set(reference_names) != set(refs), "Reference names require editorial reconciliation")
    ledger = (ARTICLES / "REFERENCES.md").read_text()
    for reference, label in reference_names.items():
        fail_if(f"## {reference}\n" not in ledger, f"Missing primary-reference record: {reference}")
        lines.append(f"| [{label}](REFERENCES.md#{reference.lower()}) | {link_ids(refs[reference])} |")
    return "\n".join(lines) + "\n\n", (len(areas), len(topics), len(methods), len(refs))


def check_links():
    checked = 0
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        for url in re.findall(r"(?<!!)\[[^]]+\]\(([^)]+)\)", md.read_text()):
            if url.startswith(("http:", "https:", "mailto:", "#")):
                continue
            path = unquote(url.split("#", 1)[0])
            if not path:
                continue
            target = (md.parent / path).resolve()
            fail_if(not target.exists() or not target.is_relative_to(ROOT),
                    f"Broken local link: {md.relative_to(ROOT)} -> {url}")
            checked += 1
    return checked


def run(write):
    catalog = json.loads(CATALOG.read_text())
    articles = catalog["articles"]
    ids = [a["article_id"] for a in articles]
    fail_if(len(ids) != len(set(ids)), "Duplicate article IDs")
    fail_if(sorted(ids) != sorted(p.stem for p in ARTICLES.glob("RA-*.md")),
            "Article files and catalog IDs differ")
    for item in articles:
        path = ARTICLES / item["artifact_path"]
        content = path.read_bytes()
        name = item["article_id"]
        fail_if(not content.decode().startswith(f"# {name} —"), f"Wrong article header: {name}")
        current = {"sha256": sha256(content).hexdigest(), "bytes": len(content),
                   "words": len(content.decode().split())}
        if write:
            item.update(current)
            header = re.search(
                r"Version ([0-9.]+) · (Published|Expanded|Updated) (\d{4}-\d{2}-\d{2})",
                content.decode("utf-8").splitlines()[2],
            )
            fail_if(header is None, f"Unrecognized version/date header: {name}")
            item["version"] = header.group(1)
            if header.group(2) in {"Expanded", "Updated"}:
                item["expanded_on"] = header.group(3)
            else:
                item.pop("expanded_on", None)
        else:
            fail_if(any(item[key] != value for key, value in current.items()),
                    f"Catalog digest, bytes or words differ: {name}")
        for other in item["related_article_ids"]:
            fail_if(other not in ids, f"Unresolved article relation: {name} -> {other}")
        for paper in item["paper_relations"]:
            fail_if(not (ROOT / "papers" / paper["paper_id"] / "README.md").exists(),
                    f"Unknown paper for {name}: {paper['paper_id']}")

    if write:
        catalog["release_version"] = "0.3"
        catalog["index_rebuilt_on"] = "2026-11-13"
        catalog["terminology_crosswalk"] = {
            "path": "../docs/TERMINOLOGY_CROSSWALK.md", "selected_public_terms": 12,
            "source": "https://yarian.com/terminology",
            "scope": "Curated definitions; terminology status does not establish implementation",
        }
    existing = CROSS.read_text()
    derived, counts = derive_tables(catalog, existing)
    prefix, remainder = existing.split(DERIVED_START, 1)
    _, suffix = remainder.split(DERIVED_END, 1)
    rebuilt = prefix + derived + DERIVED_END + suffix
    expected = (len(articles), len(list((ROOT / "papers").glob("*/manuscript.pdf"))),
                counts[3], counts[0], counts[1], counts[2], len(catalog["article_relations"]))
    count_keys = ("articles", "linked_papers", "primary_references", "research_areas",
                  "topics", "methods", "article_relations")
    for key, actual in zip(count_keys, expected):
        if write:
            catalog["counts"][key] = actual
        else:
            fail_if(catalog["counts"][key] != actual, f"Count mismatch: {key}")
    if write:
        CROSS.write_text(rebuilt, encoding="utf-8", newline="\n")
        CATALOG.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
                           encoding="utf-8", newline="\n")
    else:
        fail_if(existing != rebuilt, "Cross-index is stale; run --write")
    links = check_links()
    print(f"Audited {expected[0]} articles, {expected[1]} manuscripts, {counts[0]} areas, "
          f"{counts[1]} topics, {counts[2]} methods, {counts[3]} references, "
          f"{expected[-1]} article relations; {links} local link targets exist.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true", help="Rebuild derived tables and article checksums")
    group.add_argument("--check", action="store_true", help="Verify catalog, derived tables and links")
    opts = parser.parse_args()
    try:
        run(opts.write)
    except (ValueError, KeyError, OSError) as exc:
        print(f"Index audit failed: {exc}", file=sys.stderr)
        sys.exit(1)
