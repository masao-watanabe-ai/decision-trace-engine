from src.trace import Event, Signal, Decision, build_trace, trace_to_json, validate_trace


event = Event(
    event_id="design_proposal_102",
    type="material_selection",
    timestamp="2026-03-16T09:29:00Z",
    source="engineering_review_system",
    payload={
        "component": "heat_exchanger_pipe",
        "candidate_material": "SUS304"
    }
)

signals = [
    Signal(
        signal_id="sig_corrosion_001",
        name="corrosion_risk_score",
        value=0.65,
        value_type="number",
        source="corrosion_model",
        confidence=0.84,
        timestamp="2026-03-16T09:29:20Z"
    )
]

decision = Decision(
    outcome="APPROVE",
    decision_type="automated",
    reason="Corrosion risk below escalation threshold",
    issued_by="engine",
    confidence=0.84
)

trace = build_trace(
    trace_id="trace_mfg_001",
    event=event,
    signals=signals,
    decision=decision,
    domain="manufacturing"
)

validate_trace(trace)
print(trace_to_json(trace))
