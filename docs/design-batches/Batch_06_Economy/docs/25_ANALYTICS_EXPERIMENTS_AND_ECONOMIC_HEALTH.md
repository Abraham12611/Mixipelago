# 25 — Economy Analytics, Experiments and Live Balancing

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Canonical events
`wallet_opened`, `upgrade_seen`, `upgrade_previewed`, `upgrade_purchased`, `upgrade_purchase_failed`, `cosmetic_equipped`, `reward_pending`, `reward_granted`, `reward_rejected`, `shop_opened`, `shop_stat_viewed`, `economy_catalog_published` with source version, player cohort ID, mode, price, outcome reason and latency; do not put raw PII in telemetry.

## Funnel questions
Can players afford the first upgrade at an enjoyable moment? Do cosmetically focused players find long-term goals? Are VIP upgrades worth choosing? Are players with low balance trapped? Does the introduction of a sink reduce retention? How do whales/high-time players compare with ordinary users absent monetary purchase pressure?

## Dashboard metrics
Faucet totals and sink totals by source category; balances percentiles; expected versus actual upgrade affordability; replays that generate income; economic exploit anomalies; purchase conversion by upgrade and tier; upgrade ROI; fraud rejection rate; ledger reconcile drift.

## Experiment safety
All prices/reward rules are versioned and subject to rollout cohorts; don't silently alter stored historical receipts. Experimental changes must define minimum sample size, guardrail metrics and a kill switch. Disable a problematic faucet by policy gate rather than modifying the client UI only.

## Support/feedback
Player reporting option for missing coins; transaction receipt lookup; clear pending verification states. Never claim a loss or grant based solely on analytics logs.
