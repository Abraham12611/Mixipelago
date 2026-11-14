# 09 — Board Pressure, Danger Boundary, Win/Loss and Recovery

## Design intent

A near-frictionless board needs clear pressure to prevent indefinite stacking, but a momentary collision across the bottom line should not unfairly cause loss. The reference screenshots show a dashed line; we design it as a **warning/overflow boundary** rather than assuming its exact source-game meaning. Boundaries and timing are in world coordinates and fixed simulation steps.

## Boundary model

- Play area has a lower danger threshold at `dangerLineY = 12.8` (proposed).
- A launched body while still in spawn/arming phase is exempt; it must first cross an arming threshold or complete a bounded arming interval before becoming a dangerous board occupant.
- For active non-exempt bodies, evaluate **footprint intrusion** rather than just sprite center: `bodyCenter.y + radius > dangerLineY` is one candidate rule. An alternate center-only policy is an owner decision because the line reads differently visually.
- Intrusion accumulates across **consecutive fixed steps**; reset when body is clearly clear of the zone. Add hysteresis threshold to prevent rapid warning blinking near the line.
- Proposal: `dangerGraceMs=850` corresponding to 51 steps at 60Hz. Visual warning begins before terminal loss, with red pulse and gentle sound. If no body remains intruding continuously for grace, warning clears.

## Multiple bodies and counters

Each active body has `dangerConsecutiveSteps`. On each step with intrusion, increment that body's counter; reset on exit. Loss if any eligible body counter reaches configured grace. This prevents a succession of different bodies each intruding for <grace from being accidentally counted as one long violation. Alternatively some missions may use cumulative board pressure—this is separate mode and not alpha default.

When a body merges or is served, delete its danger counter and apply a short spawn grace to the new output. Never transfer a partially expired counter from a consumed object to the new glass without an explicit rule. Do not let the Fx animation hide an already-active danger condition; HUD warning follows physics state.

## Terminal state evaluation order

The order of win/loss checks matters if a merge both completes an order and puts a result in the danger area. Proposal per fixed-step:

1. Resolve all legal merges and serving claims.
2. Process ordered semantic events and objective progress.
3. Evaluate mission win condition.
4. If won, finalize once and do not evaluate a simultaneous loss from a consumed body.
5. Otherwise evaluate danger and shot-budget loss.
6. On loss, finalize once and freeze all reward-producing actions.

This creates a consistent "successful final merge wins" rule that can be taught to players. Any alternative must be documented and tested.

## Game outcome types

```ts
type SessionEnd =
  | { kind: 'won'; stars: 1|2|3; score: number; ordersServed: number }
  | { kind: 'lost'; reason: 'danger'|'shots_exhausted'|'timed_out'|'scripted'; score: number }
  | { kind: 'abandoned'; reason: 'user_exit'|'save_error'|'restart' };
```

Alpha wins when five customer orders completed or when mission config says a score target. Keep the exact win objective visible on-screen. A shot-limited mode is permitted only when configured. Timed-out and scripted reasons are future extension fields; do not show them as playable mechanics until implemented.

## Difficulty pressure without unfairness

Add difficulty through board shape, starting objects, number of target drinks, spawn sequence, allowed actions and customer requests—not hidden changes in momentum every 30 seconds. A player should understand why they lost. Underlying physics presets are fixed for a mission and displayed in relevant help/tooltips for special boards.

## Accessibility and communication

- Warning must have color **and** icon/text/pulse independent of color.
- Reduced-motion mode minimizes flashing; danger indicator remains clear.
- A countdown/progress indicator may show remaining grace; avoid spurious millisecond precision in UI if gameplay is stepped.
- Loss screen should state cause and offer `Retry`, `Map` and optional `How to improve` tips. No forced purchase.
- Pause stops danger countdown and active-time objectives.

## Recovery rules and edge cases

- Shooter briefly below line at spawn: exempt.
- A collision pushes an active drink across line for 20 steps, then back: warning clears, no loss.
- A drink rests across line 51 steps: loss unless final customer objective resolves first in same simulation step.
- A merge result appears across line: placement correction and output grace begin consistently; no instant failure.
- A fixed decorative object overlaps line: does not count.
- A sleeping glass intrudes: counts, because danger is spatial, not speed-dependent.
- Hidden tab: paused, counters do not continue.
- `NaN`/invalid pose: fail safely with diagnostic and controlled session recovery; no phantom win/reward.

## Acceptance

Create reproducible fixtures: just-inside line, just-outside line, crossing in/out within grace, steady overflow, overflow during merge, simultaneous win/loss, sleep in danger, and two-body alternating intrusion. Assert exact terminal event count = 1 and no hidden-time loss after visibility changes.
