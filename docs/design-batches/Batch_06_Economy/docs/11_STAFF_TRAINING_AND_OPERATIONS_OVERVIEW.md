# 11 — Staff, Training and Shop Operations — Later Design

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Deferred systems
Staff, shifts, training, fatigue, salaries and shop automation are not in v0.3. They belong to a later business/management expansion. Begin with documented entity boundaries so shops can support them without database rewrites.

## Candidate roles
Mixologist, Cashier, Host, Maintenance Specialist, Marketing Agent and Delivery Runner. Each role has skill bands, hiring requirements, visible benefits, compensation obligations and capacity limits. Staff never control or fake the player's direct puzzle input without an expressly separate automation mode.

## Operating modes
`PLAYER_RUN` always lets the player play a normal puzzle; later `DELEGATED` modes could produce limited background income based on infrastructure, but must be bounded and clearly not competitive score. Distinguish live player order service from hypothetical simulated shop operations.

## Ethical safeguards
No involuntary time pressure to check in or fear-of-loss reminders. Deferred wages cannot cause irreversible negative balances. Staff cannot permanently leave solely because a player takes time away from the game. Prefer opt-in strategic contracts and forgiving pause/return behaviors.

## Integration contracts
Shop-owned employee slots, task schedules and staff effects feed the same modifier resolution layer as upgrades, but a different provenance. Add a separate background simulation worker only when product evidence justifies it.
