# STP-009 — The Nullspace Has No Name

*Identifiability, Source Attribution, and Refusal in Multi-Machine Vibration Monitoring*

**Mark Yarian** · Yarian Works, LLC / SynapticSteel

**Author-released working paper · Not peer reviewed**

[Read the complete PDF](manuscript.pdf) · [Abstract](abstract.md) · [Citation](citation.bib) · [Metadata](metadata.json)

| Record | Value |
| --- | --- |
| Version | 1.0 |
| GitHub publication | 2026-11-11 |
| Manuscript date | 2026-11-11 |
| Pages | 10 |
| Rights | Copyright Mark Yarian. All rights reserved; public reading and citation permitted. |
| DOI | None assigned to this GitHub edition |

## Abstract

When several rotating machines excite the same structure, a vibration sensor measures a mixture rather than a machine. Blind source separation, spectral features, and even an apparently perfect multichannel reconstruction can produce plausible components without proving which physical motor generated them. This paper formalizes that gap using a frequency-domain transfer model and two elementary identifiability results: a square full-rank model can fit every observed mixture while hiding an unmodeled source, and residual-based detection is blind to interference lying inside the calibrated transfer subspace. It proposes a Source Attribution Evidence Contract (SAEC) that binds each attribution claim to sensor identity, timing quality, transfer-path calibration, numerical conditioning, independent source references, counterfactual tests, and an explicit right to abstain. The contract is examined as a research proposal, not a deployed capability, against blind separation, order tracking, nonnegative factorization, and supervised diagnosis. A falsifiable three-motor/fourth-source protocol specifies the evidence needed to move from synthetic reconstruction to defensible industrial attribution. SynapticSteel dual-node engineering experiments motivate the problem but do not constitute field validation.

## Evidence and limitations

Elementary mathematical identifiability analysis and a proposed attribution protocol; no field validation. The manuscript distinguishes its proposals, analytical examples, and future evaluation from established results. Full references are in the PDF.

## Indexed research articles

- [RA-003 — Actuator observations, torque, timing, and health labels](../../research-articles/RA-003.md): Use independent source references when attributing shared vibration.
- [RA-020 — Reconstruction, identifiability, and physical source attribution](../../research-articles/RA-020.md): Explain why fitting a mixture can leave its physical sources unidentified.

These links identify topic or method relevance. The linked articles are initial research syntheses or proposed evaluations; they do not establish manuscript ancestry, new empirical support, or a change to this manuscript edition.

## Citation

Yarian, M. (2026). The Nullspace Has No Name: Identifiability, Source Attribution, and Refusal in Multi-Machine Vibration Monitoring. SynapticSteel Technical Papers, STP-009, version 1.0. https://github.com/Mark-Yarian/public_repository/blob/main/papers/STP-009/manuscript.pdf

## Edition note

This GitHub edition carries the author’s release approval. Preparation labels were reconciled with public release; its research claims remain limited to the evidence stated in the manuscript. No new Zenodo deposit or DOI is claimed.

**PDF SHA-256:** `19e48a28059aecac3d695931ad46edd98fbf3a4f1ded63b93b6ccea2103cfa27`

[All scientific works](../INDEX.md) · [Publication policy](../../PUBLICATION_POLICY.md)
