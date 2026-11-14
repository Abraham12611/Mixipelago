# 28 — Skill Economy Telemetry, Balance and Experiments

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Observability events
`skill_tree_viewed`, `skill_node_viewed`, `skill_purchase_requested`, `skill_purchase_accepted`, `skill_purchase_rejected`, `skill_points_granted`, `player_leveled_up`, `skill_respec_previewed`, `skill_respec_completed`, `loadout_changed`, `skill_disabled_in_mode`, `modifier_cap_applied`, `xp_receipt_reconciled`.

## Metric definitions
- Activation = percentage of eligible players who allocate ≥1 point within seven days of first entitlement.
- Utilization = percentage of unlocked skills that affect at least one eligible session/shop transaction within fourteen days.
- Build diversity = entropy and concentration of investment by branch, cohort and content version.
- Expected vs actual VIP arrival rate = compare seeded statistical outcome within confidence intervals; avoid claiming certainty on small samples.
- Economy impact = verified incremental coin income and discount savings per cohort, excluding preview coins and refunded transactions.
- Fairness = competitive rank variance should be unrelated to noncompetitive unlocked talents under standardized profile.

## Experiments
Split by immutable player assignment, freeze content version per experiment, track attrition and unintended locks, provide a kill switch. Never run live tests that silently debit skill points or trusted coins. Experiments affecting player allocations require a migration and clear player communication.

## Balance response
If one skill dominates use or produces excessive income, first investigate incentives and projection correctness. Caps/percentages may be tuned for future transactions via versioned catalog; do not rewrite historical receipts or revoke previously completed campaign progress.
