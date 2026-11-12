# Research notes: transformed inputs, hidden state, and execution ancestry

Companion to [STP-010 — The Model Was Nearby, Not Involved](README.md).

**Version 1.0 · Added 2026-11-12 UTC · Research synthesis and proposed protocols · Not peer reviewed**

## Research question

Which exact state and input transformation produced a displayed prediction or agent action? Distributed inference, latent-space composition, compiler pipelines, and multirate routing make this a practical provenance question.

## Evidence and relevance

[LLVM's language reference](https://www.llvm.org/docs/LangRef.html) supplies a concrete example of an intermediate representation with explicit validity requirements. Those requirements do not establish a downstream prediction's input ancestry. STP-010's proposed attribution contract addresses that separate relationship.

A representation transform should be treated as a new derived artifact with recorded parents. Placing vectors in one space, displaying a latent trajectory, or showing a model beside an observation does not identify the transformation used in an actual execution. A cached result also needs its own original execution record.

## Proposed lineage record

| Stage | Identity to preserve |
| --- | --- |
| Acquisition | Observation revision, sensor identity, support interval, and clock uncertainty |
| Preprocessing | Parent digests, transform revision, parameters, and output digest |
| Representation alignment | Source representation revisions and the exact alignment transform |
| Routing | Routing decision, policy/model revision, and selected input identities |
| Execution | Consumed-input digest, model artifact, relevant state revision, and result digest |
| Display or case assembly | Result identity, displayed observation identity, and attribution class |

Relevant state includes prompts, retrieval results, conversation history, memory selection, caches, seeds where controlled, model weights, and execution settings. A missing record should produce an explicit limit on attribution rather than an assumed match from wall-clock proximity.

## Proposed comparisons

Replay fixed model/input/state combinations while independently changing retrieval, history, cache, or routing. Distinguish stochastic variability from a changed recorded input. Inject stale results, reordered messages, altered preprocessing, and model replacement. Test whether exact-input, derived-input, temporally adjacent, and indeterminate cases retain the correct classification.

For a proposed latent-space composition, compare the stated transformation with matched simple alignment baselines. Measure held-out transfer, reconstruction error, interference, and task quality. Record the transform as a distinct revision. A favorable representation comparison would support that tested operation, not a claim that an independently functioning new model has appeared.

For message protocols, compare fixed codes, shuffled messages, and learned messages under equal bandwidth. Bind each action to the message revision actually consumed, including delayed or discarded messages. State restoration and replay must retain original event ancestry as well as their new execution identities.

**Data status:** Proposed provenance and replay tests; no measured attribution accuracy or validated model-composition result is added.

[Event-time uncertainty](../STP-003/research-notes.md) · [Recovery epochs](../STP-007/research-notes.md) · [Context drift](../SS-LAB-CC-001/research-notes.md)

Rights in these notes: Copyright 2026 Mark Yarian. All rights reserved; public reading and citation permitted. The manuscript retains its own published license and version.
