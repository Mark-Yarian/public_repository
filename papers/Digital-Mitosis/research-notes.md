# Research notes: inheritance, plasticity, and bounded computational organisms

Companion to [Digital Mitosis](README.md).

**Version 1.1 · Added 2026-11-12 UTC · Research synthesis and proposed protocols · Not peer reviewed**

## Scope

These notes consolidate research questions about persistent computational identity, inherited state, controlled variation, adaptive maintenance, biological inspiration, and behavioral phenotypes. They extend the paper's proposed experimental agenda. They contain no demonstration that a computational system is alive or conscious.

## Relevant primary evidence

| Work | Evidence available | Relevance and limit |
| --- | --- | --- |
| [Ofria and Wilke, Avida, 2004](https://authors.library.caltech.edu/records/2h3br-gvn73) | A platform for experiments with self-replicating, evolving programs | Provides experimental methods; does not validate this architecture |
| [Evci et al., RigL, 2020](https://proceedings.mlr.press/v119/evci20a.html) | A sparse-training method with topology updates and reported evaluations | Motivates a concrete adaptation comparison; not evidence for a combined biological maintenance analogy |
| [Gidon et al., 2020](https://doi.org/10.1126/science.aax6239) | Particular active dendritic computations in human cortical neurons | Motivates explicit computational comparisons; tree geometry alone does not inherit those results |
| [Kagan et al., DishBrain, 2022](https://doi.org/10.1016/j.neuron.2022.09.001) | Closed-loop learning experiments with cultured neurons | A biological preparation and task, distinct from software reproduction or subjective-experience claims |
| [Butlin et al., 2023, version 3](https://arxiv.org/abs/2308.08708v3) | A theory-based framework of consciousness indicators | Structures an assessment; does not certify later systems or turn self-report into proof |
| [LLVM language reference](https://www.llvm.org/docs/LangRef.html) | An explicit program representation and validity requirements | Useful for transformation records; validity does not prove preserved behavior |

These are background sources and methodological precedents. Their reported results belong to their authors and settings. The proposed comparisons below have not been run for Digital Mitosis.

## Inheritance and independently executing descendants

Define the inherited partitions before creating a descendant: executable configuration, memory, model state, identity/lineage records, resource limits, and excluded transient or external state. Compare ordinary cloning, checkpoint migration, and controlled variation under identical task and resource limits. Record both failed and successful descendants.

A descendant should have an independently checkable parent record and a stated continuity criterion. Shared initial files are insufficient to establish inherited behavioral continuity; similar outputs are insufficient to establish a shared execution history. Test restart, changed inputs, missing memory, and corrupted inheritance partitions separately.

| Measurement | Interpretation sought |
| --- | --- |
| Parent/child identities and inherited-state digests | Traceable ancestry |
| Independent restart and task completion | Execution continuity under the specified boundary |
| Held-out behavioral profile | Retained and changed phenotype |
| Mutation operator, target, and budget | Bounded variation rather than unexplained change |
| Failed descendants and consumed resources | Selection exposure and cost |
| Capability checks before and after transfer | Whether stated invariants survived |

## Plasticity and maintenance

Separate weight adaptation, structural adaptation, memory changes, and data changes. Compare fixed topology, weight-only updates, and topology-changing updates on the same workload. For a maintenance cycle, ablate pruning, regrowth, consolidation, and data filtering independently before testing their combination.

Measure held-out performance, retention of earlier tasks, recovery after distribution shift, and complete maintenance cost. Biological terms can motivate which variables to test; they do not establish that an algorithm reproduces glial or neuronal physiology. A lower training error also cannot establish persistence or identity continuity.

## Biological inspiration and observation scale

A neuron-to-gate or dendrite-to-tree analogy should identify the input, operation, output, task, and observation scale it proposes to explain. Compare a threshold unit with a compartmental or graded model under stated capacity and data constraints. Separate morphology, active properties, and learning rules rather than attributing every improvement to a tree-shaped layout.

For closed-loop adaptation, specify the feedback contingency and appropriate controls. A biological culture result can suggest a design question, but transferring its interpretation to a software system requires a new operational definition and evidence. Learning, embodiment, inheritance, and subjective experience remain separate claims.

## Executable variation and semantic checks

Define a finite candidate set, the information available to the selection procedure, its decision rule, and its cost. A statement that a selection exists is not an implementation of that selection. Specify how the procedure terminates and how unsuccessful candidates are recorded.

When variation changes code or an intermediate representation, retain the parent artifact, transform revision, verifier result, build identity, and behavioral tests. A valid representation can still have unwanted behavior. Compare task outcomes and invariant violations against an unchanged parent and an ordinary clone. Compilation should be described as a transformation with measurable consequences, not accepted as a biological mechanism by analogy.

## Behavioral phenotype and system-level drift

Use the paper's behavioral definition of phenotype: measured response distributions, state transitions, memory associations, tool choices, and calibration. A latent visualization or attractor-like trace is an observation to explain, not an independent entity. Hold weights, prompts, retrieval, history, caches, seeds where controlled, and environment fixed before assigning changes to a new mechanism.

For distributed agents, vary topology, delay, and bandwidth while holding participants and tasks fixed. Compare an independent-agent baseline and an ordinary coordinator. Measure coordination, state consistency, failure recovery, and message cost. For representation composition, require a specified alignment transform and held-out task comparison; geometric overlap alone does not demonstrate a working descendant.

## Curiosity and consciousness questions

Define exploration through novelty, correctness, retention, and transfer under an explicit budget. Compare it with a nonadaptive policy and evaluate on a separate task set. Human developmental or maturity metaphors should not supply the ground-truth label.

If consciousness indicators are investigated, state the framework and assumptions separately from the inheritance experiment. Control prompting and learned self-descriptions, retain negative cases, and disclose unresolved interpretation. Neither an affirmative self-report nor the absence of a decisive test settles subjective experience.

**Data status:** Proposed research agenda; no new reproduction experiment, adaptation benchmark, biological measurement, or consciousness result accompanies these notes.

## Public teaching companion

The [lineage lab](../../public-experiments/lineage-lab/README.md) is a small, bounded Python illustration of state inheritance, a child identity, a recorded change and checksum failure. Its tests check the sample's behavior only; they do not establish any experimental result for the paper. The [terminology crosswalk](../../docs/TERMINOLOGY_CROSSWALK.md) maps the public Yarian vocabulary to operational questions and distinguishes the site's concept labels from verified implementation.

[Failure-memory protocol](../STP-001/research-notes.md) · [Recovery continuity](../STP-007/research-notes.md) · [Exact state ancestry](../STP-010/research-notes.md) · [Context-fidelity controls](../SS-LAB-CC-001/research-notes.md)

Rights in these notes: Copyright 2026 Mark Yarian. All rights reserved; public reading and citation permitted. The manuscript retains its own published license and version.
