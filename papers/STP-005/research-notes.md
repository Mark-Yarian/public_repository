# Research notes: agreement, independence, and claim-specific support

Companion to [STP-005 — Trust Is Not Agreement](README.md).

**Version 1.0 · Added 2026-11-12 UTC · Research synthesis and proposed protocols · Not peer reviewed**

## Research question

Does agreement among agents or channels add independent evidence, or merely repeat a shared source, prompt, transformation, or failure? Distributed coordination and generative-model evaluation suggest useful stress tests for the paper's sensor-trust contract.

## Relevant synthesis

The paper already separates intrinsic quality, timing, calibration, plausibility, history, independence, and model-specific usefulness. The proposed extension is to make shared ancestry visible when assessing corroboration. Several answers derived from one measurement are several transformations of that measurement; their agreement alone does not create an independent physical observation.

Likewise, recurrent strings in agent messages are insufficient to establish useful communication. An operational test should ask whether those messages improve a defined task beyond fixed-code, shuffled-message, and bandwidth-matched alternatives. Linguistic appearance is a separate observation from coordination performance.

## Proposed comparison

| Comparison | Variable held fixed | Outcome of interest |
| --- | --- | --- |
| Independent observations versus duplicated observations | Target condition and downstream decision rule | Sensitivity to common-source error |
| Diverse pipelines versus shared preprocessing | Input population and task | Dependence on a common transformation |
| Fixed code versus learned communication | Available bandwidth and agent budget | Task benefit and partner generalization |
| Real messages versus shuffled messages | Message count and size | Whether content carries useful task information |
| Evidence-based answer versus fluent unsupported answer | Question and scoring rubric | Calibration and unsupported-claim rate |

Inject a fault into a shared ancestor as well as into a single channel. Record source ancestry, timing quality, transformations, agent/model revisions, abstentions, and task outcomes. Test new partners and environments rather than scoring only the conditions in which a communication convention was learned.

## Interpretation

Keep evidence of successful coordination separate from evidence of sensor health, physical truth, or subjective experience. For any admission decision, state the claim being supported and the missing evidence that would change it. A unanimous result with a shared unresolved failure should remain unresolved under the proposed test.

**Data status:** Proposed evaluation derived from the [published trust framework](manuscript.pdf); no sensor-health or swarm-performance result is added.

[Exact input ancestry](../STP-010/research-notes.md) · [Independent evaluation opportunities](../STP-008/research-notes.md)

Rights in these notes: Copyright 2026 Mark Yarian. All rights reserved; public reading and citation permitted. The manuscript retains its own published license and version.
