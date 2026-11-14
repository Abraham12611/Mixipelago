# 03 — Entrepreneur XP Curve, Levels, Caps and Pacing

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Proposed formula for the initial economy (v0.4.0 candidate)
Let **L** be the current integer player level, starting at 1. The XP needed to advance from L to L+1 is:

`xp_to_next(L) = 100 + 35*(L-1) + 5*(L-1)^2`.

The cumulative XP threshold for reaching level L is `sum(xp_to_next(k) for k=1..L-1)`; compute from a published table or integer-only loop, never floats. At level 1 cumulative XP is 0. First-upgrade threshold is 100 XP; level 3 cumulative XP is 240 XP. Values are **tuning hypotheses** and must be tested on real first-clear pacing.

## Caps and overflow
- v0.4.0 cap: player level **20**; no XP beyond a capped progression track until a new version explicitly raises the cap. We should preserve at-cap source receipts without retroactively granting unseen rewards; possible 'overflow XP' must be explicitly designed later.
- Later releases may raise the cap by content version. Newly published thresholds may not silently lower a player's level. Create a migration ADR for changed curves.
- XP total is `BIGINT` nonnegative, awarded once per eligible event. Reputation, scores, preview coins and game currency are not convertible into XP.
- A verified mission must carry a published `rewardPolicyVersion`. XP amount is frozen for that receipt; tuning changes apply to future receipts only.

## Levels vs points
Level 1 starts at zero points. Every first attainment of levels 2 through 20 grants **one point** (19 earnable by level 20). This candidate curve allows six early published nodes without exhausting point supply, but node rank cost and level gates regulate pace. A level milestone record prevents duplicate point grants during concurrent XP claims.

## Pacing tests
Model 1000 simulated campaign progressions with 20th/50th/80th percentile successful clear rates. Compare hours to first point and first specialization, stalled-player rate, and rate of point scarcity. The desired feeling is an early meaningful choice after a small set of missions, followed by spaced unlock decisions—not an XP pop-up after every shot.

## Offline and reconnect
No trusted XP is granted from an unsigned local simulation. If a completed level has a validated, durable result receipt queued for sync, award XP on reconciliation exactly once. An unverified local completion may show `XP pending verification` but cannot grant spendable points. UI must handle rejected receipts without silently claiming success.

## Abuse and edge cases
Negative rewards, huge integer values, duplicated first-clear attempts, simultaneous device grants, mission deletion, migration cap changes, save rollback, and paid account migration all have explicit failure tests. An invalid XP policy rejects the publication before reaching users.
