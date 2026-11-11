# The Model Was Nearby, Not Involved

An industrial diagnostic interface may display a sensor observation beside a model prediction and thereby imply that the prediction was computed from that observation. In asynchronous edge systems, this inference is frequently invalid: acquisition, buffering, feature generation, model execution, caching, and case assembly advance on different schedules. We argue that proximity in wall-clock time is not sufficient evidence of computational attribution. We propose a Revision-Exact Attribution Contract (REAC), a compact provenance and decision protocol that classifies a displayed model result as exact-input, derived-input, temporally adjacent, or unrelated/indeterminate. The contract combines immutable acquisition identities, canonical input digests, execution attestations, clock-uncertainty intervals, and explicit abstention. We derive failure examples, compare provenance graphs, distributed tracing, and timestamp joins, and specify falsifiable replay and fault-injection tests. This is an architectural proposal, not an empirical demonstration of improved diagnostic accuracy.

**Evidence:** Architectural proposal and falsifiable replay/fault-injection plan; no measured diagnostic-accuracy benefit.

**Review status:** Author-released working paper; not peer reviewed.
