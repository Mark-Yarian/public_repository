# The Timestamp Is Not the Event

Industrial edge systems increasingly combine vibration, acoustic, thermal, image, distance, environmental, network, and maintenance data whose sampling cadence, transport path, buffering behavior, and timestamp origin differ. STP-003 argues that a scalar timestamp can create false physical correlations and proposes uncertainty-aware event time: each observation carries a best estimate of physical event time together with bounded uncertainty, clock domain, timestamp origin, acquisition support, and transformation provenance. Fusion then evaluates temporal compatibility rather than merely comparing scalar timestamps inside a fixed window.

**Evidence:** Conceptual temporal-fusion architecture and proposed evaluation; no original timing benchmark.

**Review status:** Author-released working paper; not peer reviewed.
