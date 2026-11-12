# STP-007 — A Reconnection Is Not a Recovery

*Epoch-Fenced Reacquisition and Recovery Budgets for Unattended Industrial Sensors*

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

Unattended industrial sensors often fail in ways that invite a simple operational response: reconnect the radio, restart the worker, or power-cycle the node. Such actions can restore a data stream while leaving its epistemic state unresolved. Buffered samples may reappear out of order; a restarted process may inherit stale calibration; a peripheral may advertise while its sensing element remains stuck; and repeated resets can deplete power or conceal a persistent fault. This paper argues that autonomous sensor recovery should be specified as a bounded, evidence-producing protocol rather than a sequence of restart commands. It proposes Epoch-Fenced Reacquisition (EFR): a per-source acquisition epoch that invalidates predecessor streams, a layered recovery ladder with persistent action budgets, and a separate warmup/validation gate before observations regain model authority. The proposal is derived from failure-detector theory, Bluetooth link semantics, operating-system watchdog and restart mechanisms, OT safety guidance, and measurement-uncertainty practice. A fault-injection protocol is specified to compare EFR against naive reconnect and service-level restart baselines. No new recovery algorithm is claimed as validated, and no autonomous firmware or hardware recovery capability is asserted for SynapticSteel TelePod. The contribution is a testable integration contract for remote sensing where physical access may be expensive or impossible.

## Evidence and limitations

Architecture and fault-injection evaluation protocol; no measured recovery or reliability benefit. The manuscript distinguishes its proposals, analytical examples, and future evaluation from established results. Full references are in the PDF.

## Supporting research notes

[Read the integrated research notes](research-notes.md) — Checkpoint boundaries, recovery epochs, state continuity, and stale-data rejection.

Companion notes version 1.0, added 2026-11-12 UTC. They distinguish cited background from proposed tests and contain no new empirical results. The PDF, manuscript version, citation, and DOI record remain unchanged.

## Indexed research articles

- [RA-002 — Peer discovery, leader election, and recovery](../../research-articles/RA-002.md): Test recovery after a connection resumes and reject stale predecessor work.
- [RA-006 — Continuity through restart and long-running state](../../research-articles/RA-006.md): Distinguish restored execution from validated current service.
- [RA-007 — Swarm coordination under partial observations](../../research-articles/RA-007.md): Test useful recovery after participant and transport failures.
- [RA-019 — Attributable communication and bounded agency](../../research-articles/RA-019.md): Handle retries and delayed actions across recovery boundaries.

These links identify topic or method relevance. The linked articles are initial research syntheses or proposed evaluations; they do not establish manuscript ancestry, new empirical support, or a change to this manuscript edition.

## Citation

Yarian, M. (2026). A Reconnection Is Not a Recovery: Epoch-Fenced Reacquisition and Recovery Budgets for Unattended Industrial Sensors. SynapticSteel Technical Papers, STP-007, version 1.0. https://github.com/Mark-Yarian/public_repository/blob/main/papers/STP-007/manuscript.pdf

## Edition note

This GitHub edition carries the author’s release approval. Preparation labels were reconciled with public release; its research claims remain limited to the evidence stated in the manuscript. No new Zenodo deposit or DOI is claimed.

**PDF SHA-256:** `b840302adb8403be958cb4ed3a4fded47cd496ed7c2a0b096ae8f38c1daebb86`

[All scientific works](../INDEX.md) · [Publication policy](../../PUBLICATION_POLICY.md)
