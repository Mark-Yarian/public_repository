# Research notes: restored state, recovery epochs, and continuity

Companion to [STP-007 — A Reconnection Is Not a Recovery](README.md).

**Version 1.0 · Added 2026-11-12 UTC · Research synthesis and proposed protocols · Not peer reviewed**

## Research question

After a link resumes or a process checkpoint is restored, what evidence is needed before its observations can regain authority? Distributed simulations, computational inheritance, and replay proposals share this continuity problem.

## Relevant synthesis

A useful distinction is between the ability to resume execution and the ability to produce valid current observations. A checkpoint may preserve local memory while external queues, leases, clocks, sensor state, or physical conditions have changed. An inverse operation or replay step also needs a stated boundary: lost external input cannot be recovered merely by labeling the local transition reversible.

STP-007's proposed recovery contract supplies the appropriate home for these ideas. Recovery epochs separate predecessor streams from newly admitted observations; a warmup and validation gate can remain unresolved after the connection returns. These notes extend the comparison design rather than claiming that such recovery has been implemented.

## Proposed comparison

Compare naive reconnect, process restart, checkpoint restore, and epoch-fenced recovery under the same fault schedule. Include packet loss, duplicate or delayed predecessor messages, a changed clock, corrupted retained state, and restart during a partially completed action. Preserve a single-process reference trace where available.

| Evidence to retain | Continuity question |
| --- | --- |
| Predecessor and successor epoch IDs | Which stream is entitled to produce current evidence? |
| Checkpoint digest and excluded state | What was actually restored? |
| Outstanding messages and external I/O boundary | Which effects may be duplicated, lost, or unreplayable? |
| Clock and acquisition-state revalidation | Can new observations be temporally admitted? |
| Warmup criteria and validation result | Has resumed execution produced valid measurements? |
| Persistent recovery-action budget | How many attempts and resources were consumed? |

Measure stale-data admission, duplicate effects, state divergence, time to valid observation, failed recovery attempts, and cost. Report connection time separately from time to validated service. A system that remains connected while emitting invalid or indeterminate data has not passed the proposed recovery criterion.

## Relationship to computational reproduction

The [Digital Mitosis notes](../Digital-Mitosis/research-notes.md) address parentage and inherited state. Those records can help explain continuity, but inheriting a valid identity does not establish the present quality of a sensor stream. Recovery and ancestry need separate admission decisions.

**Data status:** Proposed fault-injection protocol; no measured recovery advantage or deployed autonomous recovery is added.

[Execution lineage](../STP-010/research-notes.md) · [Baseline revision and validation](../STP-002/research-notes.md)

Rights in these notes: Copyright 2026 Mark Yarian. All rights reserved; public reading and citation permitted. The manuscript retains its own published license and version.
