# STP-003 — The Timestamp Is Not the Event

*Uncertainty-aware temporal fusion for asynchronous industrial sensors at the physical edge*

**Mark Yarian** · Yarian Works, LLC / SynapticSteel

**Author-released working paper · Not peer reviewed**

[Read the complete PDF](manuscript.pdf) · [Abstract](abstract.md) · [Citation](citation.bib) · [Metadata](metadata.json)

| Record | Value |
| --- | --- |
| Version | 0.1-github |
| GitHub publication | 2026-11-11 |
| Manuscript date | 2026-11-11 |
| Pages | 7 |
| Rights | Copyright Mark Yarian. All rights reserved; public reading and citation permitted. |
| DOI | None assigned to this GitHub edition |

## Abstract

Industrial edge systems increasingly combine vibration, acoustic, thermal, image, distance, environmental, network, and maintenance data whose sampling cadence, transport path, buffering behavior, and timestamp origin differ. STP-003 argues that a scalar timestamp can create false physical correlations and proposes uncertainty-aware event time: each observation carries a best estimate of physical event time together with bounded uncertainty, clock domain, timestamp origin, acquisition support, and transformation provenance. Fusion then evaluates temporal compatibility rather than merely comparing scalar timestamps inside a fixed window.

## Evidence and limitations

Conceptual temporal-fusion architecture and proposed evaluation; no original timing benchmark. The manuscript distinguishes its proposals, analytical examples, and future evaluation from established results. Full references are in the PDF.

## Supporting research notes

[Read the integrated research notes](research-notes.md) — Multirate schedules, timing uncertainty, event identity, and replay boundaries.

Companion notes version 1.0, added 2026-11-12 UTC. They distinguish cited background from proposed tests and contain no new empirical results. The PDF, manuscript version, citation, and DOI record remain unchanged.

## Citation

Yarian, M. (2026). The Timestamp Is Not the Event: Uncertainty-aware temporal fusion for asynchronous industrial sensors at the physical edge. SynapticSteel Technical Papers, STP-003, version 0.1-github. https://github.com/Mark-Yarian/public_repository/blob/main/papers/STP-003/manuscript.pdf

## Edition note

This GitHub edition carries the author’s release approval. Preparation labels were reconciled with public release; its research claims remain limited to the evidence stated in the manuscript. No new Zenodo deposit or DOI is claimed.

**PDF SHA-256:** `c4839c98f18b8266c3871a4c612d9f8c51eed3d4a7c65083c9c430346014f2ac`

[All scientific works](../INDEX.md) · [Publication policy](../../PUBLICATION_POLICY.md)
