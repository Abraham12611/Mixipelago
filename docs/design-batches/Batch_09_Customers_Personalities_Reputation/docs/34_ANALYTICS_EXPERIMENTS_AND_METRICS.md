# 34 — Analytics, Feedback Loops and Experimentation

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Measurement goals
Determine whether customer presence improves enjoyment and clarity, rather than merely maximizing time spent. Track order comprehension, service completion, customer-card opens, portrait load failures, confusion around auto-serving, relationship journal adoption, verified satisfaction distribution, reputation change rates and effect on short-session engagement.

## Suggested events
`customer_card_seen`, `customer_order_details_opened`, `order_progressed_local`, `order_fulfilled_local`, `encounter_reserved_trusted`, `satisfaction_observation_settled`, `relationship_tier_changed`, `reputation_projection_updated`, `guest_journal_viewed`, `customer_content_fallback_shown`. Distinguish client diagnostic events from trusted settlement events. Correlation by run/encounter IDs; minimize identifiers in exported analytics.

## KPIs / guardrails
Order fulfillment rate by difficulty/segment, median shots per fulfilled order, unexpectedly difficult guest-target rates, VIP realized probability vs expected, player comprehension from qualitative owner tests, retention among players with journal vs without, satisfaction distribution and low-reputation recovery. Monitor negative tail where penalties repeatedly hit beginners.

## Safe experiments
Use versioned A/B flags for portrait density, order-card layout, feedback pacing and optional tutorial hints. Do not mix scoreboards or change published competitive target pools between cohorts. Monetization effects require separate economic balance and fairness review.

## Incident diagnostics
Alert on VIP share exceeding cap, guest reroll spikes, duplicate source credits, large negative reputation outliers, stale catalog clients, and order mismatch/softlock rates. Keep audit-rich server logs separate from privacy-filtered product analytics.
