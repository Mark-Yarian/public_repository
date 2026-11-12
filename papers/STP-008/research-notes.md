# Research notes: selection rules, comparison populations, and failed trials

Companion to [STP-008 — The Archive Is Not the Population](README.md).

**Version 1.0 · Added 2026-11-12 UTC · Research synthesis and proposed protocols · Not peer reviewed**

## Research question

How does selecting memorable events, interesting outputs, or successful descendants alter the conclusion of a research evaluation? The useful connection across these topics is the selection mechanism, not a shared explanation for their underlying phenomena.

## Evidence and relevance

[Shojaee and colleagues' controlled-puzzle study](https://arxiv.org/abs/2506.06941v3) is a bounded reasoning-model evaluation. Its experimental setting motivates documenting difficulty and selection criteria when transferring a benchmark question to another system. It is not a population estimate of every task a model might encounter.

STP-008's [published analytical argument](manuscript.pdf) explains why a retained event collection can differ from the population that generated it. These notes apply that distinction to event windows, curiosity-driven exploration, and failure-memory evaluation. No separate empirical dataset is supplied.

## Proposed records

| Selection decision | Required denominator or comparison |
| --- | --- |
| Announce an unusual event window | All eligible windows and the rule used to select them |
| Retain only high-novelty outputs | The complete attempted task population, including ordinary outputs |
| Report a repaired failure | Comparable opportunities for recurrence and unsuccessful repairs |
| Promote a successful computational descendant | All eligible descendants, exclusions, and failed runs |
| Inspect many signals or time ranges | The full family of comparisons considered |

Fix event definitions, exclusions, task strata, scoring, and comparison families before inspecting confirmatory outcomes. Record exposure and missing coverage separately from stored events. Account for dependence among overlapping windows, repeated agents, and related descendants. Keep exploratory findings labeled exploratory until evaluated on a separate opportunity set.

## Proposed comparison

Replay the same full trace through event-only capture and a selection-aware capture policy with a bounded background audit sample. Compare the apparent event rate and detector ranking with a full-trace reference, explicitly recording coverage and the assumptions needed by any weighting scheme. For adaptive exploration, preserve the selection probability when it is known and disclose when it cannot be reconstructed.

Report trial counts, excluded trials and reasons, missed observation intervals, and all specified comparisons. A compelling selected example can remain useful for mechanism discovery without becoming evidence of prevalence.

**Data status:** Proposed selection audit; no new prevalence estimate, statistical significance result, or replication is claimed.

[Failure recurrence](../STP-001/research-notes.md) · [Observation policy](../STP-006/research-notes.md) · [Context-fidelity evaluation](../SS-LAB-CC-001/research-notes.md)

Rights in these notes: Copyright 2026 Mark Yarian. All rights reserved; public reading and citation permitted. The manuscript retains its own published license and version.
