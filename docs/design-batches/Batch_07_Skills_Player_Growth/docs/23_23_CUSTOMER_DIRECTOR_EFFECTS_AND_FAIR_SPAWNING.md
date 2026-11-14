# 23 — Hospitality Modifiers and the Customer Director

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Director contract
The server-side Customer Director receives eligible shop context, a published customer-pool distribution, verified player skill effects, a seeded encounter ID, event modifiers and reputation sources. It samples from an explicit weighted table and persists the result.

## Probability math
Start from eligible `vipBaseProbability`, add absolute points from shop and skill sources, then clamp to published global probability cap (candidate 0.20). Within VIP/non-VIP class, choose a customer using normalized category weights; no negative or NaN weights allowed. The expected rate is testable across 100,000 seeded simulations.

## Mission compatibility
Classic Service story missions authored with fixed named orders are **not** changed by VIP talents. Automatic serving and order-eligibility remain owned by Batch 3. Player skills do not reroll pending orders that are already shown.

## Reconnect and exploit prevention
Generate and persist encounter before returning response. A fresh browser tab, reload, or invalid request cannot mint a fresh high-value customer without a completed legal session transition. Rate-limit creation and bind seed/encounter to shop and session.

## Telemetry
Capture aggregate intended vs realized VIP rates by eligible skill rank and shop tier, plus service rewards, but avoid storing sensitive customer demographics or making inferences about real player characteristics.
