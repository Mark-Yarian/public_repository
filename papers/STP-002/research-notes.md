# Research notes: adaptive baselines and independent validation

Companion to [STP-002 — Baseline Is Not Health](README.md).

**Version 1.0 · Added 2026-11-12 UTC · Research synthesis and proposed protocols · Not peer reviewed**

## Research question

Can adaptation improve prediction while preserving evidence that a machine's new baseline is healthy? Work on structural adaptation and maintenance cycles suggests useful comparisons, but predictive adjustment and physical health require different evidence.

## Evidence and relevance

[RigL, by Evci and colleagues](https://proceedings.mlr.press/v119/evci20a.html), is a concrete example of changing sparse-network connectivity during training. Its reported evaluations concern learning performance and computational cost. They do not establish that an adapted industrial baseline describes healthy equipment.

The relevant hypothesis for STP-002 is that an adaptive system can become more familiar with a deteriorating regime. A smaller prediction residual after adaptation would then be compatible with either successful tracking or loss of diagnostic sensitivity. This is a reason to separate the baseline revision from its health evidence.

## Proposed comparison

Replay an independently labeled sequence containing operating-regime changes, gradual deterioration, and a documented maintenance boundary. Compare a frozen model, memory-only updates, weight updates, and topology updates using the same admissible information and compute budget. Maintenance labels should describe what was done and what was verified; the intervention alone does not prove its cause or success.

| Evidence to preserve | Purpose |
| --- | --- |
| Immutable pre-adaptation baseline | Permit later reinterpretation of the earlier regime |
| Update boundary and training interval | Distinguish learning from a physical change |
| Independent health assessment and uncertainty | Avoid using the model's own agreement as its health label |
| Held-out fault and normal episodes | Measure diagnostic retention and false alarms |
| Retention test after each update | Detect forgetting or absorbed deterioration |

Measure predictive error and diagnostic sensitivity separately. Test maintenance operations such as pruning, regrowth, consolidation, and data filtering individually before evaluating their combination. Report failure to preserve an earlier validated distinction even when average prediction error improves.

## Connection to the paper

Treat a changed input population, memory corpus, model, or preprocessing rule as a documented revision with a stated scope. An observed baseline may be retained for comparison while its health status remains unknown. This preserves STP-002's distinction between repeatability and independently supported health.

**Data status:** Proposed protocol; no new field labels, adaptation benchmark, or diagnostic improvement is reported here.

[Failure-memory evaluation](../STP-001/research-notes.md) · [Computational adaptation controls](../Digital-Mitosis/research-notes.md)

Rights in these notes: Copyright 2026 Mark Yarian. All rights reserved; public reading and citation permitted. The manuscript retains its own published license and version.
