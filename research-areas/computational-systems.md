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

[Browse research areas](README.md) · [Public paper index](../papers/INDEX.md) · [How to read this library](../docs/READER_GUIDE.md)
