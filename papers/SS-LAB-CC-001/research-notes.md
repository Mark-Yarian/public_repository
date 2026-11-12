# Research notes: observable context drift and controlled reconstruction

Companion to [Conceptual Compression and Context Fidelity in Human–LLM Collaboration](README.md).

**Version 1.0 · Added 2026-11-12 UTC · Research synthesis and proposed protocols · Not peer reviewed**

## Research question

When a model fills gaps in a compressed instruction, which inferred relationships become accepted context, and what causes subsequent drift? Questions about behavioral stability, latent trajectories, curiosity, and apparent preference change become testable when translated into observable task and state variables.

## Relevant evidence and definitions

[Butlin and colleagues' 2023 report, version 3](https://arxiv.org/abs/2308.08708v3), offers theory-based consciousness indicators. Its framework is background for keeping consciousness interpretation separate from a context-fidelity experiment. These notes use task behavior and recorded context as observables; they do not infer subjective intent from fluent responses or changing style.

The parent paper proposes that unverified inferences can accumulate into accepted context. The extension here is to distinguish that process from changes in retrieval, conversation history, cache, model revision, or the user's authorized goal. A changed result is a phenomenon to attribute before naming a new underlying mechanism.

## Proposed comparison

Construct task families with a full specification, a recoverably compressed version, and a version that genuinely lacks needed information. Independently record the user's intended relationships and permitted goal changes. Use the same model revision and budget across conditions.

| Condition | Reconstruction rule | Contrast |
| --- | --- | --- |
| Direct specification | All required relationships supplied | Reference performance |
| Unchecked reconstruction | Inferred relationships can enter later context | Proposed drift pathway |
| Explicit inference ledger | Separate stated facts, guesses, and unresolved gaps | Effect of keeping evidence status visible |
| Confirmed reconstruction | Resolve specified gaps against the intended task | Effect of verification |
| Reset or shuffled-history control | Remove or disrupt accumulated context | Dependence on prior conversational structure |

Score task-weighted distortion, unsupported relationship insertion, lost constraints, correction cost, and downstream use of earlier guesses. Keep authorized revisions separate from errors. Use blinded scoring where feasible, and evaluate on held-out tasks rather than selected compelling dialogues.

## State and trajectory controls

Record prompts, conversation revisions, retrieval results, memory selection, caches, model artifact, execution settings, and seeds when controlled. Change one recorded factor at a time. For an apparent idle-time effect, preserve process state and the full input history; include reset and surrogate-trajectory controls. Missing state is an attribution limit.

A latent-state plot must specify the representation, projection, statistic, and reference population. Compare its ability to predict later task error with simpler context-length, retrieval, and history features. Visual motion, geometric overlap, or recurring response patterns alone cannot establish a distinct cognitive mechanism or an independently functioning modular model.

## Curiosity and biological analogies

Measure exploration through novelty, task correctness, retained knowledge, and transfer under a fixed budget. Compare an exploratory policy with an ordinary task policy. A developmental metaphor does not supply a maturity scale. Similarly, an explanation at the neuronal scale does not automatically validate an interpretation at the dialogue scale.

For multiscale or layered descriptions, define one observable per proposed layer and test whether the additional layer improves held-out explanation beyond a simpler state-and-feedback account. Keep correlational, predictive, and intervention-based conclusions distinct.

**Data status:** Proposed controlled study; no new dialogue dataset, measured context-fidelity improvement, emergent-mechanism finding, or consciousness result is reported.

[Exact execution and hidden-state lineage](../STP-010/research-notes.md) · [Computational phenotype and inheritance](../Digital-Mitosis/research-notes.md) · [Selection-aware evaluation](../STP-008/research-notes.md)

Rights in these notes: Copyright 2026 Mark Yarian. All rights reserved; public reading and citation permitted. The manuscript retains its own published license and version.
