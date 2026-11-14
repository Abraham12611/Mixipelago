# 21 — Loss States, Retries, Recovery, Hints and Player Protection

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Loss taxonomy
`danger`: a non-exempt active body footprint intrudes danger zone for >= grace steps.
`shots_exhausted`: goal unmet after final committed shot has had bounded time to resolve.
`timed_out`: active-time ticks reach zero with goal unmet, after same-tick win check.
`scripted`: explicit event fails a declared mission condition (future); never use as generic catchall.
`invalid_content` or `engine_error`: system failure, NOT player loss; preserve record and offer safe retry/report.

## Recovery principles
Loss explanation is specific, nonjudgmental and actionable. Buttons: Retry, Map/Exit, Help/How It Works, optional Watch Replay when available. No forced ads, purchase gates, or irreversible currency penalty for failing a first-level puzzle. A failed session never auto-debits the user's trusted wallet in alpha.

## Hints
Tier 1: textual onboarding prompt (“Drag toward an identical glass”). Tier 2: contextual highlight pointing at viable compatible pair. Tier 3: optional post-loss aim suggestion. Later hints may show predicted direction or board clearing move; all hints should explain whether they count as booster/assist and whether ranked eligibility changes.

## Rescue feature guardrails
Free retry always available in early campaign; one optional free recovery tool could be designed in later phases. If a booster purchases extra shots or clears the board, it must have published rules, be priced by trusted economy, and generally disqualify standardized ranking unless everyone receives same allowance.

## Termination and restart
On session end: freeze input, stop reducers, emit one `session_won`/`session_lost`, snapshot stats and show UI after effects; never let an async FX promise trigger an extra award. Restart creates distinct `sessionId`, resets RNG according to retry policy (`same_seed` for authored puzzles, re-roll only when explicitly allowed), cancels prior event subscriptions and discards pending boosters.

## Unwinnable state handling
A solver might prove no remaining resources for requested tier. If locally provable, offer “No available path—retry?” rather than forcing player to keep shooting forever. But avoid falsely declaring unwinnable from heuristic failure; language must reflect certainty.

## Error recovery
On WebGL/context loss, save safe state if possible and prompt recovery. If physics snapshot unavailable/incompatible, restart same version and seed rather than silently continuing a corrupted round. Preserve prior completed mission records but do not mint new coins.

## Acceptance
Clear reason codes, no popup over gameplay until terminalization, pause doesn't burn shot/time, retries don't duplicate state, page reload matches documented support, and both desktop and mobile have accessible help/exit affordances.
