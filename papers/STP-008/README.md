# STP-008 — The Archive Is Not the Population

*Selection-Aware Event Memory for Industrial Edge Intelligence*

**Mark Yarian** · Yarian Works, LLC / SynapticSteel

**Author-released working paper · Not peer reviewed**

[Read the complete PDF](manuscript.pdf) · [Abstract](abstract.md) · [Citation](citation.bib) · [Metadata](metadata.json)

| Record | Value |
| --- | --- |
| Version | 1.0 |
| GitHub publication | 2026-11-11 |
| Manuscript date | 2026-11-11 |
| Pages | 12 |
| Rights | Copyright Mark Yarian. All rights reserved; public reading and citation permitted. |
| DOI | None assigned to this GitHub edition |

## Abstract

An event-triggered industrial archive is often treated as the history of a machine, although it is actually the output of a selection policy. Thresholds, model alerts, buffer limits, sensor outages, operator actions, and retention rules determine which intervals survive. The resulting collection may be useful for forensic review yet unsuitable for estimating event prevalence, calibrating false-alarm rates, or comparing detectors: its inclusion mechanism is coupled to the behavior being inferred. This paper develops a Selection-Aware Memory Contract (SAMC) that treats capture eligibility, inclusion probability, acquisition coverage, retention transformations, and evidence provenance as separate first-class records. It combines deterministic event preservation with a bounded, randomized background audit lane and an explicit opportunity/coverage ledger. A worked numerical example shows how an archive can exaggerate apparent anomaly prevalence even when no data are fabricated; probability-weighted estimation is possible only under stated sampling and observability assumptions. The proposal synthesizes classical survey sampling and missing-data theory with modern anomaly-benchmark criticism, industrial data practice, and provenance standards. No empirical performance improvement or deployed SAMC capability is claimed. A falsifiable replay-and-field evaluation plan specifies when the architecture would justify further development.

## Evidence and limitations

Sampling-theory synthesis and a worked numerical counterexample; the example is not an experiment. The manuscript distinguishes its proposals, analytical examples, and future evaluation from established results. Full references are in the PDF.

## Citation

Yarian, M. (2026). The Archive Is Not the Population: Selection-Aware Event Memory for Industrial Edge Intelligence. SynapticSteel Technical Papers, STP-008, version 1.0. https://github.com/Mark-Yarian/public_repository/blob/main/papers/STP-008/manuscript.pdf

## Edition note

This GitHub edition carries the author’s release approval. Preparation labels were reconciled with public release; its research claims remain limited to the evidence stated in the manuscript. No new Zenodo deposit or DOI is claimed.

**PDF SHA-256:** `c144db3215e037ff09ac69181afd4e2f4f8836c2dc2549793259939a3fe474da`

[All scientific works](../INDEX.md) · [Publication policy](../../PUBLICATION_POLICY.md)
