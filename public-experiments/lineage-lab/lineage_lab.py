"""A finite, in-memory teaching model for computational inheritance.

This model has no network, tool calls, background execution, or autonomous
reproduction. A caller explicitly creates each child and observes its record.
"""

from dataclasses import dataclass, replace
from hashlib import sha256
import json


@dataclass(frozen=True)
class Cell:
    identity: str
    parent: str | None
    generation: int
    weight: int
    memory: tuple[str, ...]


@dataclass(frozen=True)
class BirthRecord:
    parent: str
    child: str
    inherited_digest: str
    child_digest: str
    weight_change: int


def digest(cell: Cell) -> str:
    """Checksum the declared state. A checksum is not an authenticity proof."""
    data = {
        "identity": cell.identity,
        "parent": cell.parent,
        "generation": cell.generation,
        "weight": cell.weight,
        "memory": list(cell.memory),
    }
    return sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()


def response(cell: Cell, signal: int) -> int:
    """An intentionally trivial observable behavior, not an AI model."""
    return cell.weight * signal + len(cell.memory)


def make_child(parent: Cell, *, label: str, weight_change: int = 0) -> tuple[Cell, BirthRecord]:
    """Create exactly one explicitly requested descendant."""
    if label not in {"a", "b"}:
        raise ValueError("This teaching example accepts only child labels a and b")
    if weight_change not in {-1, 0, 1}:
        raise ValueError("Change exceeds the declared teaching budget")
    child = Cell(
        identity=f"{parent.identity}.{label}",
        parent=parent.identity,
        generation=parent.generation + 1,
        weight=parent.weight + weight_change,
        memory=parent.memory,
    )
    record = BirthRecord(
        parent=parent.identity,
        child=child.identity,
        inherited_digest=digest(parent),
        child_digest=digest(child),
        weight_change=weight_change,
    )
    return child, record


def inspect_record(parent: Cell, child: Cell, record: BirthRecord) -> bool:
    """Detect a changed snapshot in this example; no identity authentication."""
    return (
        record.parent == parent.identity
        and record.child == child.identity
        and child.parent == parent.identity
        and child.generation == parent.generation + 1
        and child.memory == parent.memory
        and child.weight - parent.weight == record.weight_change
        and record.weight_change in {-1, 0, 1}
        and record.inherited_digest == digest(parent)
        and record.child_digest == digest(child)
    )


if __name__ == "__main__":
    parent = Cell("P", None, 0, 2, ("observed:A",))
    faithful, faithful_record = make_child(parent, label="a")
    variant, variant_record = make_child(parent, label="b", weight_change=1)
    print(json.dumps({
        "parent": parent.identity,
        "children": [faithful.identity, variant.identity],
        "lineage_checks": [
            inspect_record(parent, faithful, faithful_record),
            inspect_record(parent, variant, variant_record),
        ],
        "held_out_signals": [0, 2, 5],
        "parent_responses": [response(parent, x) for x in (0, 2, 5)],
        "faithful_responses": [response(faithful, x) for x in (0, 2, 5)],
        "variant_responses": [response(variant, x) for x in (0, 2, 5)],
        "tampered_record_matches": inspect_record(
            parent, replace(variant, memory=()), variant_record
        ),
    }, indent=2))
