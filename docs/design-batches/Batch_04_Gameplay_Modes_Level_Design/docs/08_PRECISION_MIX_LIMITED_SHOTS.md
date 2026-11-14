# 08 — Precision Mix: Limited-Shot Puzzle Mode

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Concept
The challenge is to solve an authored physics puzzle in a fixed number of legal launches. This emphasizes geometry, collisions, wall banks, and merge sequencing. No hidden random spawn draws in a competitive/three-star Precision mission.

## Base contract
`mode='precision'`, `budget.shotsMax=N`, `spawn.firstItems` of length ≥N, `spawn.pool` unused or seeded to a fixed sequence. `shotsFired` increments on committed legal launches, never on aiming, cancelled gestures, blocked spawn attempts or overlay interaction. If the goal is satisfied by the final shot, victory takes precedence over `shots_exhausted`.

## Shot exhaustion policy
Do NOT instantly end as the last drink leaves the launcher; there may still be several seconds of collisions. After `shotsFired >= N`, enter `awaiting_resolution`; continue fixed stepping until all relevant bodies settle or `settleMaxTicks` is reached. If goal completed, win; else lose `shots_exhausted`. The shooter controls are disabled during awaiting_resolution. Other modes with per-shot cooldown can use this settlement state for all shots.

## Puzzle design rules
Use a fixed starting field with intentional collision geometry. A designer must maintain a recorded winning command sequence with stable timing and bounded aim tolerance. Include near-miss alternate solutions where possible. Difficulty rises from direct pair contact to bank deflection to chain setup, not merely reducing shots to an arbitrary number.

## Stars
1 star win; 2 stars within designer-specified threshold; 3 stars meet lower threshold (must be ≤ `shotsMax` and demonstrated). More optional medals can reward no booster use or elegant rebounds, without gating primary completion.

## Author constraints
- Never require an output tier impossible given sum of available tier-equivalent resources and shot allotment.
- Auto-serve can break a planned chain; ensure initial customer orders do not consume the central puzzle output unless serving is itself the objective.
- Prevent last-shot softlock by defining settle timeout and stuck detection.
- Avoid micro-precision tolerances below typical mobile input resolution.

## Technical tests
One cancelled drag does not consume shot. Winning merge occurring 120 ticks after last shot still wins. An impossible level fails offline feasibility check or is rejected in content review. Reload during unresolved final shot either restores a compatible snapshot or prompts safe retry. Show shot counter before first move.
