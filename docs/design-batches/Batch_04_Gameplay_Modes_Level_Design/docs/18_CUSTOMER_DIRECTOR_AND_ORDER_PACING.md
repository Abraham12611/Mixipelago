# 18 — Customer Director, Order Pacing and Mode Integration

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Contract boundaries
The Customer Director chooses WHICH orders exist. The order reducer decides WHICH newly produced drink fulfills which active order. Rapier sees only bodies and collisions. The mode defines allowed order count, target difficulty and arrival cadence. The player-visible UI presents order demand and progress.

## Priority and atomicity
For each eligible newly merged output, resolve matching active order by ascending `issuedTick`, then `orderId`; reserve drink exactly once; update order line; if fulfilled, emit one `order_fulfilled`. A single output cannot satisfy two orders. Serving occurs before same-output remerge. When multiple eligible outputs arrive in one tick, process their merge event sequence and stable IDs.

## Templates
An order template includes tier/recipe requirement, quantity, preview coin reward, priority class, optional `arrivalDelayTicks`, `deadlineTicks` future, and customer skin ID. In v0.1 use `requestedTier`, `quantity=1`; named customer personalities are cosmetic/abstract until Batch 9.

## Mission complexity controls
- Beginner: two visible orders, tiers 2 and 3, scripted queue.
- Intermediate: tiers 2–4, more than two orders over session, optional quantity 2.
- Advanced: multi-line orders, 3 visible slots, a VIP requirement, alternate special recipe family.
- Timed: fast turnovers; every new order generated with enough active ticks and queue resources to be feasible.

## Timed order consequences
A timer for an INDIVIDUAL customer is not the same as Rush Hour session timer. Proposal: deadlines not introduced until advanced customer systems. When introduced, expired order should carry clear consequences (score reduction, replacement, reputation effect) governed by named rules, and must never silently charge coins. Expiry only advances on active ticks unless explicitly a world-simulation timer.

## Customer fairness
Do not generate a tier-8 request in an early board where there are insufficient equivalent input resources. Store an `orderPoolVersion` and record chosen order IDs in replay. Replenishment at end-of-tick avoids a new order immediately consuming the just-created output retroactively. Clarify if newly created order can match same-tick subsequent merges; proposed yes when sequenced after creation, no retroactive matches.

## API sketch
`selectInitialOrders(mission,seed)`; `resolveNewOutputToOrder(orderState,drink,sequence)`; `onOrderCompleted` schedules replacement for next tick; `isOrderSetFeasible` performs necessary checks.

## Acceptance
Exactly-once order progress, stable oldest-order selection, multi-line counted once, no order arrival during paused sessions, no new order if mission already won, UI progress identical to reducer state, fast successive merges do not grant same reward twice.
