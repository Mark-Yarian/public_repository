# Research notes: failure memory and controlled adaptation

Companion to [STP-001 — Failure Metabolism](README.md).

**Version 1.0 · Added 2026-11-12 UTC · Research synthesis and proposed protocols · Not peer reviewed**

## Research question

When an agent or distributed system fails, which retained information reduces recurrence on a new, comparable task? This connects failure memory to controlled reasoning benchmarks, network simulation, and bounded adaptation. A saved error message alone cannot show whether a later success came from useful memory, an easier task, more compute, or a changed environment.

## Evidence and relevance

Shojaee and colleagues studied reasoning-model failures using puzzles with controlled complexity. Their reported limits motivate recording task difficulty and inference budget alongside outcomes; they do not establish that adding external memory repairs those failures. See [the primary study, version 3](https://arxiv.org/abs/2506.06941v3).

For STP-001, the useful unit is a linked failure episode: intended action, exact inputs, execution state, observed failure, recovery attempt, and subsequent outcome. The proposed extension is to retain the unsuccessful recoveries and the opportunity to fail again, as well as successful examples. This is an evaluation design, not an observed improvement.

## Proposed comparison

Use the same task families, seeds, model revisions, and resource limits for four conditions:

| Condition | Retained information | Question tested |
| --- | --- | --- |
| Fixed inference | No cross-episode memory | What is the base recurrence rate? |
| Retrieval memory | Prior episodes without a recovery rule | Does retrieval alone help? |
| Failure memory | Episodes linked to attempted recovery and outcome | Does outcome-linked memory add value? |
| Bounded adaptation | Failure memory plus a separately versioned policy change | Is any gain attributable to adaptation? |

Score recurrence on held-out episodes, recovery correctness, newly introduced failures, and total task cost. Separate invalid outputs, misunderstood rules, search exhaustion, unavailable state, and tool failures. A system that avoids a failure by declining every task must also disclose its completion rate.

For a simulated network, inject delay, loss, reordering, duplicate delivery, and a failed participant. Start with a single-process reference and independently acting agents before testing a coordinated swarm. Coordination quality, message cost, and state divergence are separate outcomes.

## Data to retain

Record episode and parent-episode identities, task version and difficulty, input digest, model and policy revisions, memory selection, execution budget, injected fault, action trace, result, recovery result, and held-out recurrence. Preserve all comparison arms and failed descendants. A later policy revision must not overwrite the episode that motivated it.

**Data status:** Proposed protocol; no new experiment, dataset, or measured benefit accompanies these notes.

## Related research

[Sampling and the opportunity denominator](../STP-008/research-notes.md) governs recurrence estimates. [Exact execution lineage](../STP-010/research-notes.md) governs attribution of a changed result. [Computational inheritance](../Digital-Mitosis/research-notes.md) governs descendant comparisons.

## Historical case: accumulated work without verified completion (2026-11-13)

A Cognitive Metabolism snapshot reports 66,407 generated tasks, 66,203 queued, 1,032 failed dispatches and zero completed model inferences at the checkpoint. A separate source review preserves several malformed historical Python scripts. These records support studying error taxonomy and failure recurrence, not claiming that the system learned a successful repair.

A follow-up should link each attempted action to model availability, failure, proposed recovery and later useful completion under matched resource exposure. See [RA-009](../../research-articles/RA-009.md), [RA-017](../../research-articles/RA-017.md) and the [historical evidence ledger](../../research-articles/HISTORICAL_CLUSTER_EVIDENCE.md). The published manuscript is unchanged.

Rights in these notes: Copyright 2026 Mark Yarian. All rights reserved; public reading and citation permitted. The manuscript retains its own published license and version.
