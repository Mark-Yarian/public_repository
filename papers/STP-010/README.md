# STP-010 — The Model Was Nearby, Not Involved

*Revision-Exact Evidence Attribution for Asynchronous Industrial Intelligence*

**Mark Yarian** · Yarian Works, LLC / SynapticSteel

**Author-released working paper · Not peer reviewed**

[Read the complete PDF](manuscript.pdf) · [Abstract](abstract.md) · [Citation](citation.bib) · [Metadata](metadata.json)

| Record | Value |
| --- | --- |
| Version | 1.0 |
| GitHub publication | 2026-11-11 |
| Manuscript date | 2026-11-11 |
| Pages | 5 |
| Rights | Copyright Mark Yarian. All rights reserved; public reading and citation permitted. |
| DOI | None assigned to this GitHub edition |

## Abstract

An industrial diagnostic interface may display a sensor observation beside a model prediction and thereby imply that the prediction was computed from that observation. In asynchronous edge systems, this inference is frequently invalid: acquisition, buffering, feature generation, model execution, caching, and case assembly advance on different schedules. We argue that proximity in wall-clock time is not sufficient evidence of computational attribution. We propose a Revision-Exact Attribution Contract (REAC), a compact provenance and decision protocol that classifies a displayed model result as exact-input, derived-input, temporally adjacent, or unrelated/indeterminate. The contract combines immutable acquisition identities, canonical input digests, execution attestations, clock-uncertainty intervals, and explicit abstention. We derive failure examples, compare provenance graphs, distributed tracing, and timestamp joins, and specify falsifiable replay and fault-injection tests. This is an architectural proposal, not an empirical demonstration of improved diagnostic accuracy.

## Evidence and limitations

Architectural proposal and falsifiable replay/fault-injection plan; no measured diagnostic-accuracy benefit. The manuscript distinguishes its proposals, analytical examples, and future evaluation from established results. Full references are in the PDF.

## Supporting research notes

[Read the integrated research notes](research-notes.md) — Transform revisions, hidden state, latent alignment, and exact execution ancestry.

Companion notes version 1.0, added 2026-11-12 UTC. They distinguish cited background from proposed tests and contain no new empirical results. The PDF, manuscript version, citation, and DOI record remain unchanged.

## Indexed research articles

- [RA-001 — Inference service boundaries and reproducible hosts](../../research-articles/RA-001.md): Bind each result to the service, model revision, and exact input that produced it.
- [RA-002 — Peer discovery, leader election, and recovery](../../research-articles/RA-002.md): Preserve message and execution ancestry across retries.
- [RA-004 — Behavioral evidence for generated and transformed code](../../research-articles/RA-004.md): Identify the exact generated artifact, compiler transform, and execution.
- [RA-006 — Continuity through restart and long-running state](../../research-articles/RA-006.md): Separate original event ancestry from a new replay execution.
- [RA-007 — Swarm coordination under partial observations](../../research-articles/RA-007.md): Attribute each action to the messages and state actually consumed.
- [RA-009 — Failure memory from logs to later decisions](../../research-articles/RA-009.md): Identify the exact model and evidence involved in a later decision.
- [RA-010 — Behavioral drift across model, memory, and environment](../../research-articles/RA-010.md): Attribute changed behavior to exact inputs and recorded state.
- [RA-011 — Representation alignment, routing, and model composition](../../research-articles/RA-011.md): Record the transform and input revision actually used.
- [RA-015 — Multirate computation and temporal evidence](../../research-articles/RA-015.md): Bind each controller action to the state revision it consumed.
- [RA-018 — Context reconstruction and verified intent](../../research-articles/RA-018.md): Record the exact context and execution revision behind an answer.
- [RA-019 — Attributable communication and bounded agency](../../research-articles/RA-019.md): Bind each action to the message, model, and authority used.
- [RA-027 — Controllability in reference-conditioned generation](../../research-articles/RA-027.md): Identify the exact reference images, prompt, model, and transforms used to generate an output.

These links identify topic or method relevance. The linked articles are initial research syntheses or proposed evaluations; they do not establish manuscript ancestry, new empirical support, or a change to this manuscript edition.

## Citation

Yarian, M. (2026). The Model Was Nearby, Not Involved: Revision-Exact Evidence Attribution for Asynchronous Industrial Intelligence. SynapticSteel Technical Papers, STP-010, version 1.0. https://github.com/Mark-Yarian/public_repository/blob/main/papers/STP-010/manuscript.pdf

## Edition note

This GitHub edition carries the author’s release approval. Preparation labels were reconciled with public release; its research claims remain limited to the evidence stated in the manuscript. No new Zenodo deposit or DOI is claimed.

**PDF SHA-256:** `1cb043bcaac6b41199e8cd88f28e875239f96f592c70f52e0f558763ad2dfb5e`

[All scientific works](../INDEX.md) · [Publication policy](../../PUBLICATION_POLICY.md)
