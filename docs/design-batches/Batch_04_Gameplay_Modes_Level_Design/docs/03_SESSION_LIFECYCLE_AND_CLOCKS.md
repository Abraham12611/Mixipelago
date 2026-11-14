# 03 — Session Lifecycle, Clocks, Transitions and Event Ordering

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Session state graph
`created → loading → ready → running ↔ paused → resolving → won|lost|abandoned → archived`.
- `loading`: load pinned catalog, board asset manifest, mission config; validate prerequisites. Never debit shots, clocks or coins.
- `ready`: present goals, controls, exit; do not advance physics yet.
- `running`: consume legal player input, fixed-step physics, semantic events, mode plugin, objective and danger logic.
- `paused`: freeze physics, active-time, danger counters, wave clocks, and launch input. Persist checkpoint if supported.
- `resolving`: flush legal pending contact and service events for current tick, then finalize terminal outcome once. No new shots.
- `won/lost`: immutable result receipt; display summary and next options.
- `abandoned`: deliberate exit or invalid recoverable session; by default no victory rewards.
- `archived`: immutable debug/replay record retained per privacy policy.

## Three time sources, never confuse them
1. `simulationTick`: integer increment per fixed physics step, authoritative to physical, danger and deterministic active-time mode rules. `1 tick = 1/60 s` under default preset.
2. `activeElapsedTicks`: ticks while session is actively running. A paused or hidden tab has no increments; can differ from `simulationTick` if debugger steps simulation outside normal play.
3. `wallClockUtc`: event publication, campaign seasons and real-time external quests. NEVER use wall clock for puzzle Rush Hour countdown by default; real-world incident windows belong to Batch 10.

## Order per running fixed tick
1. Accept at most one queued legal input command at an authoritative tick boundary.
2. Advance Rapier step; collect collision pairs and body changes.
3. Apply deterministic merge pair arbitration; mark claimed bodies; commit production/consumption at safe point.
4. Apply auto-serving of newly created eligible outputs, oldest order then stable ID, BEFORE follow-on chain eligibility.
5. Emit ordered semantic events, score once by unique event ID, update objectives/mode progress.
6. Evaluate victory (win has priority over same-tick danger / shot-budget / active-time expiration); if won, freeze.
7. Otherwise evaluate terminal failure conditions with explicit priority: invalid session → danger → mode-specific timeout/shot exhaustion (exact priorities in level config, validated).
8. Advance scheduled arrivals/waves/next queue to be visible next tick. Presentation reacts but does not affect simulation.

## Timers
Rush Hour proposal: `remainingTicks = max(0, limitTicks - activeElapsedTicks)`. Choose 60 or 90 seconds only via authored level config. The HUD may show rounded seconds, but terminal evaluation uses ticks. In a hidden tab, pause immediately and do not catch up upon foregrounding.

## Idempotent terminalization
`finishSession({sessionId, outcome, terminalTick, resultHash})` uses idempotency `sessionId:terminal:v1`. If win and lose actions race, reducer priority chooses one. Subsequent calls return the previous immutable receipt. One summary, no duplicate preview coins, no ghost analytics counts.

## Persistence
- v0.1: local persisted profile and completed missions are for preview use only; session snapshot may be unavailable if physics snapshot serialization not implemented. Never promise mid-shot reload recovery.
- Later: mode-aware checkpoint includes pinned mission/catalog/physics versions, RNG state, active timers, order queue, unique event IDs, engine snapshot and content hash.
- An incompatible checkpoint must prompt restart or preserve safe history, never silently load with today's changed rules.

## Testing
Pause for 10 minutes and resume; no active time lost. Win and danger on same tick yields one win. Two session-finalize commands emit only one receipt. Exit during in-flight merge FX cannot resurrect objects. Restart creates new run ID and cancels old subscribers. Invalid state transition is a structured error, not a silent no-op.
