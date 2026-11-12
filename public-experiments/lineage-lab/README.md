# Lineage lab: a bounded inheritance exercise

**Educational demonstration · Python 3.10+ · No model, network, tools, or autonomous execution**

This small exercise accompanies [Digital Mitosis](../../papers/Digital-Mitosis/README.md) and the [computational reproduction article](../../research-articles/RA-005.md). It illustrates declared inheritance, an independently named child, one bounded change, a retained parent snapshot and a test that catches a modified child. It is intentionally much smaller than the paper's proposed architecture.

Run from this directory:

```bash
python3 lineage_lab.py
python3 -m unittest -v test_lineage_lab.py
```

The caller asks for two children explicitly. `P.a` receives the same weight and memory; `P.b` receives a weight change of one. Each child has a different identity and a parent pointer. The program compares outputs on signals 0, 2 and 5. On signal 0 the variant produces the same output as its parent, demonstrating why one matching response cannot establish continuity. Altering a child's memory invalidates its recorded checksum.

The five tests check: faithful state and behavior; observable variation; rejection of changes outside the stated budget; a corrupted snapshot; and an accidental match on one input. Read each failure before treating a successful test run as evidence for a larger system.

**Limits:** The record is a local checksum, not a signed ancestry claim. A caller can fabricate the parent and child records. A single function call does not establish persistence across process restarts, selection in a population, evolutionary fitness, autonomous reproduction, artificial life, or consciousness. There is no inference model or tool authority. Turning this sketch into a scientific experiment would require independent processes, stored histories, population denominators, resource accounting, predeclared controls and held-out tasks.

**Source distinction:** [Ofria and Wilke's Avida](https://authors.library.caltech.edu/records/2h3br-gvn73) describes an experimental platform for evolving self-replicating programs; its results do not validate this teaching sketch. The [Digital Mitosis paper](../../papers/Digital-Mitosis/README.md) is the author's proposed framework, not a published result for the toy program.

[Public experiments](../README.md) · [Research article](../../research-articles/RA-005.md) · [How to read claims](../../docs/READER_GUIDE.md)
