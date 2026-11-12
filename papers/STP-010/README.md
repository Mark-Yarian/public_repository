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

## Citation

Yarian, M. (2026). The Model Was Nearby, Not Involved: Revision-Exact Evidence Attribution for Asynchronous Industrial Intelligence. SynapticSteel Technical Papers, STP-010, version 1.0. https://github.com/Mark-Yarian/public_repository/blob/main/papers/STP-010/manuscript.pdf

## Edition note

This GitHub edition carries the author’s release approval. Preparation labels were reconciled with public release; its research claims remain limited to the evidence stated in the manuscript. No new Zenodo deposit or DOI is claimed.

**PDF SHA-256:** `1cb043bcaac6b41199e8cd88f28e875239f96f592c70f52e0f558763ad2dfb5e`

[All scientific works](../INDEX.md) · [Publication policy](../../PUBLICATION_POLICY.md)
