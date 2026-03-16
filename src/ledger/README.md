# ledger

`ledger` is a minimal reference implementation of a Decision Ledger.

A Decision Ledger preserves decision outcomes as explicit records,
instead of leaving them hidden inside application logs or model outputs.

## Purpose

The ledger is used to record:

- which event triggered the decision
- which signal was used
- which contract and behavior tree were involved
- whether a boundary or human intervention existed
- what final decision was made
- when the decision was recorded

## Example

```python
from src.ledger import DecisionLedger, DecisionLedgerEntry

ledger = DecisionLedger("data/ledger.json")

entry = DecisionLedgerEntry(
    event_id="evt-1001",
    signal_id="sig-risk-01",
    contract_id="contract-fraud-v1",
    behavior_tree_id="bt-fraud-review-v1",
    boundary_id="human-review-threshold-v1",
    decision="escalate_to_human",
    actor="system",
    trace_ref="trace-1001",
    metadata={
        "risk_score": 0.91,
        "reason": "fraud_probability exceeded threshold"
    }
)

ledger.record(entry)

for item in ledger.all():
    print(item.to_dict())
```
Design policy
This module is intentionally simple.
It is not a production ledger implementation.
Its purpose is to make the idea of a Decision Ledger visible,
portable, and easy to understand in a conceptual repository.
