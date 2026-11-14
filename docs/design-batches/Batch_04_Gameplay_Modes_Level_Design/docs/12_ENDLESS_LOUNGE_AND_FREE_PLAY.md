# 12 — Endless Lounge and Relaxed Free-Play

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Promise
A low-pressure playground to enjoy the physics, explore combos, and experiment with drinks without strict mission failure. The experience should be suitable for short breaks and accessible play.

## Proposed rules
`mode='endless'`, no mandatory campaign completion, no active-time deadline. The danger line can be disabled with explicit on-screen explanation or retained as optional “score survival” submode. The player may end session voluntarily, receive a summary and save a personal best. No trusted coin farming or leaderboard credit from unrestricted free play unless a future normalized ruleset is introduced.

## Board maintenance
Even relaxed play needs a way to clear terminal tier-8 objects eventually. Do not silently merge tier-8 pairs into an undocumented tier-9. Options for later explicit mechanics: board reset between rounds, limited clear token earned by ordinary play, or consume tier-8 into collection counter without coins. Proposed earliest Endless beta: a clearly labeled `Reset Table` action that starts a new free-play board while keeping session high-score metadata; confirm with owner before implementation.

## Spawn policy
A bounded weighted pool, predictable next preview, seeded per-run sequence and fairness anti-streak controls. Unlimited shots mean clients can generate vast numbers of logical events; cap retained event log, active bodies and particle emissions, compact achievements safely and periodically checkpoint.

## HUD
Less clutter than campaign: score, max chain, next drink, pause/reset/end, optional self-imposed goal, sound settings. No constantly blinking countdown or punitive failures. An info panel explains that rewards are sandbox-only.

## Technical requirements
No unbounded collision body count; no runaway floating-point values; long-session memory tests; browser suspend/resume; safe end-of-session summary; no ghost award duplication. Always available as a relaxing option after onboarding if user research supports it.
