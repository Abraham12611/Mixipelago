# 06 — Classic Service: Campaign Mode Full Specification

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Definition
The primary Mixipelago experience: shoot drinks onto a near-frictionless table, merge compatible tier pairs, produce drinks customers request, and prevent the board from overflowing. A successful session fulfills a visible mission goal and awards a result screen. This mode serves both newcomers and the long-term island campaign.

## Alpha contract
`mode='service'`, target `orders_served count=2` for `coconut-cove-001`; two visible customer orders; automatic serving of eligible NEW outputs; one linear eight-tier chain; low-damping Rapier physics; preview coins; score; retry and pause; visual danger line. Existing Batch 3 fixture is canonical example, not proven solvable.

## Core state
Maintain ordered `activeOrders`: {orderId, customerId optional, requestedTier, quantity, fulfilled, coinReward, issuedTick}, maxVisible 2. Only completed fulfillment yields an `order_fulfilled` event. Replacement orders enter after a completed order at a defined tick boundary if mission allows; do not generate orders that make the mandatory goal impossible with current queue and board state.

## Loop
1. Start session; show two open orders and mission target.
2. Preview next tier-1 drink. Drag from launcher toward desired direction, release to apply a fixed impulse.
3. Rapier steps; same-tier pairs merge. New outputs are checked for oldest matching unfilled order after merge commit.
4. If matched, mark result served, award order points and preview coins; otherwise leave drink on board for further planning.
5. Continue until target completed or configured loss (persistent danger intrusion; optional shot budget) occurs.
6. Show stars, session score, earned preview coins, best score, Retry, Next/Map.

## Order generation fairness
First mission's orders are authored, not random. Use `replacementPoolId` only after all initial target counts are feasible; every generated order tier must be reachable under current mission budget and available future pool. Delayed replacement is allowed to prevent a newly introduced order stealing a carefully prepared merge chain. Record order creation tick/ID for replay.

## Examples of progression
Cove 001: teaching tier 1→2 and 2→3; generous board, no timer. Cove 002: two tier-2 requests, teaches oldest-order priority. Cove 003: one tier-4 order, seeded tier-2 support for resource economy. Cove 004: optional merge-count goal, no conflicting order blocking chain. Cove 005: higher density and danger hints. All are design concepts until executable solver/playtest confirms.

## Accessibility/UI
Customer bubbles show tier/icon, quantity, reward, and textual label; do not rely solely on color or cup silhouette. Mini mission bar shows `Orders 1/2`. Provide pause, replay tutorial, and aim guidance. On small phones, the board stays dominant; customers compress into horizontally scrollable small cards without covering launch line.

## Acceptance
- Serving a new t2 against oldest matching order increments count once, removes body once.
- Different-tier impact never advances an order.
- An earlier order has priority over a later order asking same tier.
- A new t3 served immediately cannot remerge to t4; tests and content proofs respect this.
- Completing second order ends run once; same-tick danger cannot override win.
- All rewards labeled preview-only until trusted economy release.
