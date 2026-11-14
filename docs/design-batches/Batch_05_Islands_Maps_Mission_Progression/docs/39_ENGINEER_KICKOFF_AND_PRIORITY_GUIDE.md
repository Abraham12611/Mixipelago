# 39 — Engineer Kickoff: Build Order, Integration Rules and First Review

## Mission for the team
Produce a world-map progression system that **references** the existing playable puzzle engine instead of rewriting it. Ship incremental improvements behind `CAMPAIGN_MAP_ENABLED`; no 100-mission placeholder release.

## Required reading
Batch 4 mission schema and reward handoff; Batch 3 drink and save contracts; Batch 2 merge/contact rules; Batch 1 release strategy. Then this batch chapters 03–05, 07, 10–12, 14–17, 24, 29–32. Engineers should read domain chapters relevant to their workstream.

## First integration sprint
1. Lock game result adapter and canonical mission IDs (`coconut-cove-001` unchanged).
2. Implement graph schema, unlock evaluator and linter; prove fixtures pass.
3. Add tiny Cove map list view and two playable node cards.
4. Integrate successful game results into local campaign preview projection.
5. Add Phaser map art and camera; keep accessible list fallback.
6. Test complete path: Play → Win → Map → Unlock Next → Play; owner verifies actual UI.

## Parallel division
Domain/core: pure contracts and tests. Frontend: React cards and navigation. Rendering: Phaser map and gestures. Content: curated playable missions and island art. QA: validator, replay proof and cross-device test plan. Infrastructure: content bundle CDN, feature flag and rollback. Avoid overlapping file ownership until APIs are agreed.

## Hard stop conditions
Do not call the map production-ready if it references unbuilt missions, shows empty next actions, loses best results, crashes mobile Safari or accepts client-supplied spendable coins. Don't turn drafts into “locked” published nodes without clear future labeling.

## Deliverables per PR
Architecture change summary, schema version, tests and fixture checks, screenshots only for visual context (not proof), remaining owner manual tests, dependency notes and rollback steps. Engineers must not merge their PRs themselves; coordinator handles develop integration; main merge only with explicit owner approval.

## When to request owner decisions
Confirm initial map art direction, path density, branch placement, how much completion data can remain guest-local, and gateway milestone design. These are product choices, not reasons to postpone core graph engine work.
