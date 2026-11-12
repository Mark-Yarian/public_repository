# Research notes: multirate timing and replay boundaries

Companion to [STP-003 — The Timestamp Is Not the Event](README.md).

**Version 1.0 · Added 2026-11-12 UTC · Research synthesis and proposed protocols · Not peer reviewed**

## Research question

When fast events, slower summaries, and asynchronous model updates interact, which temporal relationships survive acquisition uncertainty and buffering? Multirate controllers and spike-based communication supply architectural candidates. Their usefulness must be tested against ordinary event queues and hierarchical controllers.

## Evidence and relevance

[Davies and colleagues' Loihi paper](https://ieeexplore.ieee.org/document/8259423) documents a particular spiking processor, including temporal processing features. It supplies a hardware example, not evidence that a brainwave-inspired schedule improves industrial fusion.

STP-003 supplies the governing distinction: physical acquisition support, timestamp origin, and clock uncertainty must remain attached to observations. A model's update interval is a separate property. Replaying a stored state also needs a separate replay clock; restoration of software state does not change the original acquisition record.

## Proposed comparison

Compare a single-rate controller, a conventional hierarchical controller, and a multirate/event-driven design on the same input trace and resource budget. Vary transport delay, packet reordering, clock offset, missing samples, and changes in update cadence independently. Keep event-time ground truth in the simulator separate from the timestamps exposed to the tested systems.

| Record | Why it matters |
| --- | --- |
| Acquisition interval and sample support | A summary can cover an interval rather than an instant |
| Clock domain, origin, offset estimate, and uncertainty | Similar displayed times may conceal incompatible observations |
| Queue entry, transformation, and execution times | Transport and processing delays must remain distinguishable |
| State revision used by each controller | Fast and slow lanes may use different evidence |
| Replay sequence and original event identity | Reprocessing must not appear to be a new physical observation |

Score incorrect temporal joins, missed compatible events, state staleness, task quality, and end-to-end latency. Predefine the comparison windows and uncertainty treatment. Frequency labels or visually synchronized traces should not replace these measurements.

## Claim boundary

The proposed test concerns scheduling, state coherence, and measurement timing. Neither an improved score nor a useful temporal encoding would establish a theory of consciousness. Correlation, prediction, and the effect of an intervention remain separate claims.

**Data status:** Proposed protocol; no timing benchmark or multirate advantage has been measured for these notes.

[Execution attribution](../STP-010/research-notes.md) · [Observer and communication cost](../STP-006/research-notes.md)

Rights in these notes: Copyright 2026 Mark Yarian. All rights reserved; public reading and citation permitted. The manuscript retains its own published license and version.
