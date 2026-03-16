# Decision Trace Reference

This directory contains a minimal reference implementation
for building and serializing Decision Traces used in the
Decision Trace Model.

A Decision Trace records the reasoning path that produced
a final decision.

It typically includes:

- event context
- generated signals
- contract evaluation
- behavior tree execution
- boundary checks
- human review
- final decision

The purpose of this code is not to provide a full production
runtime, but to illustrate how decision traces can be
represented as explicit structured objects.

---

## Example Usage

```python
from src.trace import Event, Signal, Decision, build_trace, trace_to_json

event = Event(
    event_id="promotion_request_001",
    type="store_promotion",
    timestamp="2026-03-16T10:14:00Z",
    source="store_ops_system",
    payload={"store_id": "TOKYO_01"}
)

signals = [
    Signal(
        signal_id="sig_inventory_001",
        name="inventory_risk",
        value="high",
        value_type="string",
        source="rule_engine"
    )
]

decision = Decision(
    outcome="APPLY_PROMOTION",
    decision_type="automated",
    issued_by="engine"
)

trace = build_trace(
    trace_id="trace_retail_001",
    event=event,
    signals=signals,
    decision=decision,
    domain="retail"
)

print(trace_to_json(trace))

```

Purpose
This implementation serves as a reference example showing:
how a decision trace can be structured
how trace data can be represented in Python
how traces can be serialized into JSON
For a full runtime implementation see:
decision-trace-engine
