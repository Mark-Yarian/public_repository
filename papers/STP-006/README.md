# STP-006 — The Probe Is Part of the Process

*Observation-induced change, causal confounding, and safe telemetry budgets in industrial edge intelligence*

**Mark Yarian** · Yarian Works, LLC / SynapticSteel

**Author-released working paper · Not peer reviewed**

[Read the complete PDF](manuscript.pdf) · [Abstract](abstract.md) · [Citation](citation.bib) · [Metadata](metadata.json)

| Record | Value |
| --- | --- |
| Version | 1.0 |
| GitHub publication | 2026-11-11 |
| Manuscript date | 2026-11-11 |
| Pages | 11 |
| Rights | Copyright Mark Yarian. All rights reserved; public reading and citation permitted. |
| DOI | None assigned to this GitHub edition |

## Abstract

Industrial intelligence systems often treat observation as an external, low-cost operation. Yet a sensor mount can alter a structure's measured dynamics; an active network probe can affect a controller; a telemetry collector can compete for compute resources; and a change-triggered polling policy can make the observer respond to the very behavior it seeks to explain. These mechanisms differ: some change the physical or computational system, others distort the observation channel, and still others introduce selection bias. This paper argues that observation policy should be modeled as an explicit, bounded intervention rather than invisible infrastructure. It proposes an Observation Impact Contract (OIC): a claim-specific record of probe identity, modality, schedule, permitted operating regimes, resource and safety budgets, independent witness signals, causal uncertainty, and stop conditions. A causal model and a controlled, randomized switchback evaluation protocol are developed to distinguish probe-induced effects from regime drift and normal process variation. The proposal is grounded in OT safety guidance, SNMP and OPC UA protocol semantics, vibration-metrology standards, and experimental-design literature. It is an architectural argument and test plan, not evidence that any particular production system has suffered probe-induced faults. The proposed contract has not been implemented or empirically validated in this paper.

## Evidence and limitations

Causal model, architectural proposal, and switchback evaluation protocol; no measured observer effect. The manuscript distinguishes its proposals, analytical examples, and future evaluation from established results. Full references are in the PDF.

## Supporting research notes

[Read the integrated research notes](research-notes.md) — Neuromorphic routing, representation costs, instrumentation, and resource accounting.

Companion notes version 1.0, added 2026-11-12 UTC. They distinguish cited background from proposed tests and contain no new empirical results. The PDF, manuscript version, citation, and DOI record remain unchanged.

## Indexed research articles

- [RA-001 — Inference service boundaries and reproducible hosts](../../research-articles/RA-001.md): Separate the cost of a client, collector, host, and remote service.
- [RA-003 — Actuator observations, torque, timing, and health labels](../../research-articles/RA-003.md): Measure whether sensing changes the observed system.
- [RA-007 — Swarm coordination under partial observations](../../research-articles/RA-007.md): Account for communication and observation cost.
- [RA-008 — Environmental feedback, confounding, and task fitness](../../research-articles/RA-008.md): Treat an observation policy as a possible intervention.
- [RA-013 — Plasticity, maintenance, and retained capability](../../research-articles/RA-013.md): Include maintenance and instrumentation in the resource boundary.
- [RA-014 — Biological inspiration as a computational comparison](../../research-articles/RA-014.md): Match observation and resource boundaries in alternative designs.
- [RA-015 — Multirate computation and temporal evidence](../../research-articles/RA-015.md): Measure complete encoding, routing, and observation cost.
- [RA-016 — Useful throughput, memory, and communication costs](../../research-articles/RA-016.md): Include the observer, host, conversion, and waiting cost.
- [RA-020 — Reconstruction, identifiability, and physical source attribution](../../research-articles/RA-020.md): Control the effect of the sensor and observer on the system.

These links identify topic or method relevance. The linked articles are initial research syntheses or proposed evaluations; they do not establish manuscript ancestry, new empirical support, or a change to this manuscript edition.

## Citation

Yarian, M. (2026). The Probe Is Part of the Process: Observation-induced change, causal confounding, and safe telemetry budgets in industrial edge intelligence. SynapticSteel Technical Papers, STP-006, version 1.0. https://github.com/Mark-Yarian/public_repository/blob/main/papers/STP-006/manuscript.pdf

## Edition note

This GitHub edition carries the author’s release approval. Preparation labels were reconciled with public release; its research claims remain limited to the evidence stated in the manuscript. No new Zenodo deposit or DOI is claimed.

**PDF SHA-256:** `021383984963362ec623e79b07f90f90fc5b7906506ae63d1625584e0a5d1d2c`

[All scientific works](../INDEX.md) · [Publication policy](../../PUBLICATION_POLICY.md)
