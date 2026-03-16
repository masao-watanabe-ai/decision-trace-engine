from src.ledger import DecisionLedger, DecisionLedgerEntry

ledger = DecisionLedger("ledger.json")

entry = DecisionLedgerEntry(
    event_id="evt-001",
    signal_id="sig-001",
    contract_id="decision-contract-v1",
    behavior_tree_id="bt-approval-v1",
    boundary_id="human-boundary-v1",
    decision="approved",
    actor="system",
    trace_ref="trace-001",
    metadata={
        "score": 0.82,
        "comment": "approved under current contract"
    }
)

ledger.record(entry)

print(ledger.to_dict())
