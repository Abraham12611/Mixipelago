# 07 — Completion, Stars, Mastery, Replays and Best Results

## Authority boundary
Batch 4 computes session score, objective completion, shot count, active ticks and stars. Batch 5 **consumes** the resulting `MissionResult`; it never recomputes in-game collision scores or modifies the existing two-order goal of `coconut-cove-001`.

## Result fields
`missionId`, `missionVersion`, `scoreRulesVersion`, `physicsPresetHash`, `stars`, `score`, `shots`, `activeTicks`, `outcome`, `runId`, `completedAt`, `trustStatus` (`local_preview|pending|verified|rejected`). Store best stars, best score, fastest eligible result and least shots separately. A replay can improve one without improving the others.

## Star rules
- 0 = not cleared or failed; 1 = completed primary objective; 2 and 3 = optional authored conditions under Batch 4.
- For legacy v1 fixture where `rewards.stars=1`, the player gets **one star on win**, not automatically three.
- Maximum 3 display stars by campaign convention, but authored mode may use a different rating system only with explicit schema and UI support.
- If a mission is replayed with fewer stars, preserve earlier best stars. If score rules change incompatibly, best scores must be identified by their scoring profile rather than mixed together.

## Replay policy
After a clear, show `Replay` and `Next Mission`; replay must not re-run first-clear awards. Replays are valuable for skill, stars and practice. Any repeat coin grants require Batch 6 policy; default is no new durable campaign currency until approved.

## Mastery and 100% completion
Define `chapterClear` = all required mainline nodes completed; `chapterMastery` = approved optional star/secret thresholds; `islandClear` = gateway milestone passed; `islandCompletionPercent` = completed weighted public goals per versioned content snapshot. Clearly label retired content and new expansion nodes so a patch does not arbitrarily invalidate prior 100% achievements; use "Season/Edition" or snapshot-based badges when appropriate.

## Result ingest flow
`session_won` → result adapter validates mission identity and outcome → local preview store or trusted receipt processor → monotonic upsert → unlock evaluation → discovery/achievement projection → UI notification. An all-events-once guard prevents duplicate effects across retries and multi-tab writes.

## Cross-device account migration
Do not convert local preview mission clears into server-verified results simply because a user signs in. A later explicit conversion/replay/backfill policy must be designed with security. The interface may preserve local tutorial completion visually while showing that competitive verification is unavailable.

## QA assertions
Clear with 1 star then replay with 3 results in 3; replay failure leaves 3; 2 concurrent first-clear submissions do not double grant; old mission version can be replayed from archive when supported; unsupported retired version displays a safe migration/restart notice.
