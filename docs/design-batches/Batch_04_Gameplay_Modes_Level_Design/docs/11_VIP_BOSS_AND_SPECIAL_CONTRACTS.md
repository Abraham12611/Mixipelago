# 11 — VIP Service, Boss Challenges and Special Customer Contracts

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Design identity
A customer- or rival-centered mode with complex orders and special mission constraints. Story/dialogue/characters are deferred to Batch 9/11; Batch 4 defines only the gameplay contract.

## VIP mission contract
VIP request may include multi-line order, e.g., `[{tier:3, quantity:2}, {tier:4, quantity:1}]`, plus a transparent optional service time/shot budget. Alpha customer schema uses single `requestedTier`; a new `orderLines` schema requires explicit migration and UI support before shipping. Multi-line order completes only when every line is satisfied; `orders_served` counts the whole order once.

## Boss design without unfair physics
A named rival or critic is represented by a collection of challenge phases with declared constraints, not an AI agent that spontaneously alters physical laws. Example: phase 1 serve two t2 orders; phase 2 score threshold with seeded board; phase 3 finish one VIP contract within available shots. Between phases, present recap and allow safe transition. A boss may change customer preferences or board layout only on clearly announced phase boundaries.

## Rewards
Stars, reputation (future Batch 9), unique cosmetics (future Batch 8), and preview coin totals. No real currency minting in alpha. Cosmetics cannot increase ranked score unless normalized out.

## Accessibility and fairness
VIP characters cannot be distinguished only by clothing/wealth stereotypes; order tier and constraints must be explicit. Provide predictable requests, readable icons and sufficient time to interpret. Any “tip” or pay-to-skip must never be necessary to pass a core campaign gate.

## Validation
No impossible order for a capped tier-8 chain without enough resources; line quantities available; exactly-once order fulfillment; no double VIP reward on retry; terminal transition after multiple phases; order cancellation/refund policy future documented before any real spend.
