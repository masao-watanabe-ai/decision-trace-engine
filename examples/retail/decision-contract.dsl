contract:
  name: milk_promotion
  version: 1.0
  domain: retail
  description: Store decision contract for milk promotion and display actions

inputs:

  event:
    store_id
    target_product
    timestamp

  context:
    weather
    day_type
    inventory_level
    competitor_activity
    local_event

  signals:
    waste_risk
    stockout_risk
    profit_impact
    customer_demand_signal

options:

  - id: milk_discount
    type: promotion
    description: Apply discount to milk products
    expected_effect: reduce excess inventory

  - id: front_display
    type: display_change
    description: Move milk products to front display
    expected_effect: increase customer visibility

  - id: extra_order
    type: ordering
    description: Place an additional milk order
    expected_effect: avoid stockout

concerns:

  - waste_risk
  - stockout_risk
  - profit_drop
  - operational_load

evaluation:

  inventory_level:
    type: categorical
    values: [low, medium, high]

  waste_risk:
    type: categorical
    values: [low, medium, high]

  stockout_risk:
    type: categorical
    values: [low, medium, high]

  profit_impact:
    type: categorical
    values: [positive, neutral, negative]

rules:

  - rule_id: R1
    description: Use milk discount when inventory is high and waste risk is low
    condition:
      inventory_level: high
      waste_risk: low
    decision:
      select_option: milk_discount
      reason: reduce_excess_inventory

  - rule_id: R2
    description: Use front display when waste risk is high
    condition:
      waste_risk: high
    decision:
      select_option: front_display
      reason: avoid_aggressive_discounting

  - rule_id: R3
    description: Place extra order when stockout risk is high and demand is strong
    condition:
      stockout_risk: high
      customer_demand_signal: high
    decision:
      select_option: extra_order
      reason: prevent_stockout

rejected_option_rules:

  - rejected_option: milk_discount
    when:
      waste_risk: high
    reason: excessive_waste_risk

  - rejected_option: extra_order
    when:
      inventory_level: high
    reason: overstock_risk

stop_conditions:

  - id: SC1
    description: Inventory data is unavailable
    trigger: inventory_unknown

  - id: SC2
    description: Supply status is unstable
    trigger: supply_delay

  - id: SC3
    description: Promotion budget is not approved
    trigger: promotion_budget_unapproved

  - id: SC4
    description: Waste rate already exceeds operational threshold
    trigger: waste_rate_above_threshold

output:

  decision:
    selected_option
    decision_reason
    rule_applied

  outcome_targets:
    sales_change
    waste_change
    inventory_turnover
    customer_count_change

ledger_record:

  record_event: true
  record_context: true
  record_signals: true
  record_concerns: true
  record_rejected_options: true
  record_decision: true
  record_rule: true
  record_outcome_targets: true
  record_timestamp: true
