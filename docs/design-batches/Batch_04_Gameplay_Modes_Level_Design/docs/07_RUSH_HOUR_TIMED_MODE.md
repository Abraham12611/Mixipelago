# 07 — Rush Hour: Time-Pressure Mode

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Goal
Serve as many valid customer orders as possible before the **active-time** limit expires, or satisfy a required minimum for mission victory. Intended as a short burst (proposed 60–120 active seconds) that rewards speed, not arbitrary grinding.

## Rules proposal
`mode='rush_hour'`, `clock.type='active_ticks'`, `limitTicks` explicit. One to three visible orders. A bounded request pool replenishes on order fulfillment. No real-time wall-clock expiry during paused or hidden sessions. Speed bonus based on committed orders and residual active ticks is future rule, not inherited automatically by alpha scoring.

## Outcomes
- Campaign variant: primary `orders_served >= target` wins immediately; timer expiration before target loses with reason `timed_out`.
- Arcade variant: timer expiration ends run with a score summary but may be `completed` rather than `lost`; score/leaderboard eligibility requires explicit tournament rules. Do not conflate arcade time-up with fail.
- Danger pressure remains unless a mode-specific `disableDanger` override is justified and visible before start.

## Difficulty controls
`limitTicks`, starting support, spawn weights, order tiers, `orderArrivalDelayTicks`, `maxVisibleOrders`, board capacity, preview queue length, booster policy. Do not increase physics speed mid-session behind the player's back.

## UX
Clock must remain clearly visible, with audio cues at 30/10/5 remaining seconds and visual alternatives. Use an accessible urgency state, reduced-motion friendly. Exiting to another tab freezes active-time session with an explicit Paused badge; mobile browser interruption should not cost player progress. Players must know whether finishing the last order wins before time-up.

## Test cases
Timer no decrement during pause, hidden tab, loading, win FX; exact boundary event produces win before timeout; no negative remaining ticks; order replenishment deterministic with seed; output serving persists even when timer reaches zero on same tick; client clock changes cannot extend verified competitive sessions.

## Release gate
Only after Classic Service and active-tick instrumentation are stable; controlled beta with mission-specific `modeRulesVersion`. Ranked Rush Hour later requires verified replay and standardized input/hardware assumptions.
