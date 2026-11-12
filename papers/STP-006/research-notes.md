# Research notes: end-to-end cost of observation and representation

Companion to [STP-006 — The Probe Is Part of the Process](README.md).

**Version 1.0 · Added 2026-11-12 UTC · Research synthesis and proposed protocols · Not peer reviewed**

## Research question

Can a proposed sensing, routing, or encoding design improve task performance within a measured observation budget? Neuromorphic communication, alternative number representations, compiler transformations, and model-maintenance cycles all require explicit measurement boundaries.

## Evidence and relevance

[The original Loihi study](https://ieeexplore.ieee.org/document/8259423), by Davies and colleagues, reports a specific processor and workload results. It does not establish a universal energy advantage for every event-driven or swarm application. [LLVM's language reference](https://www.llvm.org/docs/LangRef.html) defines an intermediate representation and its requirements; a representation's validity is different from the cost of an entire task.

These distinctions matter to STP-006 because preprocessing, collection, conversion, queueing, logging, and validation may themselves alter the system being observed. A lower cost inside one component can coexist with a higher cost at the system boundary.

## Proposed comparison

Use an ordinary event queue, a conventional learned router, and a spike-based router on the same recorded input stream. Include input encoding, decoding, host/device transfer, communication, idle operation, and measurement overhead. Report task success, deadline misses, latency distribution, memory, and energy over the same observation interval.

| Candidate change | Control needed | Evidence required before claiming benefit |
| --- | --- | --- |
| Spike-based messaging | Bandwidth- and task-matched ordinary messages | End-to-end task quality and cost |
| Ternary representation | Binary implementation with stated hardware assumptions | Conversion cost, error margins, area, and completed-task energy |
| Pruning or consolidation | Unchanged model and isolated maintenance operations | Retention, maintenance cost, and disruption during updates |
| Richer instrumentation | Minimal observer plus an independent witness | Whether measurement changes the workload or event rate |

For arithmetic checks, balanced ternary still requires carry handling: decimal two is represented as `1,-1`, since `1 × 3 - 1 = 2`. Representation compactness alone therefore cannot settle a processor-level efficiency claim.

## Observation policy

Predefine permitted probe schedules, resource ceilings, and stop conditions for the proposed experiment. Randomize bounded observation schedules where the experimental setting permits it, retain an independent witness, and distinguish physical disturbance, resource contention, channel distortion, and selective capture. Preserve the measurement configuration with the result.

**Data status:** Proposed benchmark and intervention controls; no energy saving, observer-induced fault, or hardware advantage is reported here.

[Multirate timing](../STP-003/research-notes.md) · [Selection-aware capture](../STP-008/research-notes.md)

Rights in these notes: Copyright 2026 Mark Yarian. All rights reserved; public reading and citation permitted. The manuscript retains its own published license and version.
