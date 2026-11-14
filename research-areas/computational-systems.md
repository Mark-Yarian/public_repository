# Computational Systems: Coordination, Observability, and Evidence

**Public research area · Conceptual overview · Not a product specification**

Computational systems become difficult to understand when work spans machines, processes, networks, and changing state. Reliable analysis separates what a system was **configured** to do, what it **reported**, and what independent observation can establish.

## Questions worth investigating
- What evidence confirms a component is operating, rather than merely responding?
- How can a distributed system recover when a participant fails or a message arrives late?
- Which state is authoritative when multiple copies disagree?
- What changes when computation happens near a physical sensor instead of in a remote data center?

## Useful vocabulary
| Term | Plain-language meaning |
| --- | --- |
| **Distributed system** | Several independent components cooperating across communication boundaries. |
| **Liveness** | Evidence that something can still make progress. |
| **State machine** | A description of permitted states and the transitions between them. |
| **Provenance** | A record of where information came from and how it was transformed. |
| **Edge computing** | Processing data closer to where it is produced or used. |

## Reading this area
This page explains general concepts, not the topology, implementation, credentials, or operational condition of any SynapticSteel or customer system. A status label is not by itself proof of live operation. Specific findings appear only when a separate public release passes the repository's review policy.

### Digital lineage as a research question

When a process is copied or restored, record the actual operation and the identity of each execution before claiming that a descendant exists. The [Digital Mitosis paper](../papers/Digital-Mitosis/README.md) proposes a formal inheritance framework; [RA-005](../research-articles/RA-005.md) separates copying, migration and reproduction; and the [lineage lab](../public-experiments/lineage-lab/README.md) shows a finite example whose checks can fail. The [terminology crosswalk](../docs/TERMINOLOGY_CROSSWALK.md) links these measurements to the public Yarian definitions.

[Browse research areas](README.md) · [Public paper index](../papers/INDEX.md) · [How to read this library](../docs/READER_GUIDE.md)


## Historical cluster cases and open research

The [2025–2026 historical cluster evidence ledger](../research-articles/HISTORICAL_CLUSTER_EVIDENCE.md) collects sanitized, source-linked observations from Code Genome, Cognitive Metabolism, Glial Equilibrium, Temporal readiness, distributed-model attempts and ContinuityNode. It differentiates archived status reports from demonstrated completed work, and gives falsifiable follow-up protocols. This is retrospective research evidence, **not** a current cluster architecture, reproducible performance benchmark or a consciousness result. See [RA-004](../research-articles/RA-004.md), [RA-006](../research-articles/RA-006.md), [RA-016](../research-articles/RA-016.md) and [RA-017](../research-articles/RA-017.md).

## Indexed research articles

- [RA-001 — Inference service boundaries and reproducible hosts](../research-articles/RA-001.md)
- [RA-002 — Peer discovery, leader election, and recovery](../research-articles/RA-002.md)
- [RA-003 — Actuator observations, torque, timing, and health labels](../research-articles/RA-003.md)
- [RA-004 — Behavioral evidence for generated and transformed code](../research-articles/RA-004.md)
- [RA-005 — Computational reproduction and bounded inheritance](../research-articles/RA-005.md)
- [RA-006 — Continuity through restart and long-running state](../research-articles/RA-006.md)
- [RA-007 — Swarm coordination under partial observations](../research-articles/RA-007.md)
- [RA-011 — Representation alignment, routing, and model composition](../research-articles/RA-011.md)
- [RA-015 — Multirate computation and temporal evidence](../research-articles/RA-015.md)
- [RA-016 — Useful throughput, memory, and communication costs](../research-articles/RA-016.md)
- [RA-019 — Attributable communication and bounded agency](../research-articles/RA-019.md)
- [RA-020 — Reconstruction, identifiability, and physical source attribution](../research-articles/RA-020.md)
- [RA-024 — Formal simulations and physical explanations](../research-articles/RA-024.md)
- [RA-026 — Post-quantum primitives and implementation claims](../research-articles/RA-026.md)

[Browse all articles](../research-articles/README.md) · [Browse by method or paper](../research-articles/CROSS_INDEX.md)
