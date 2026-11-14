# 21 — Gameplay Telemetry, Recipe Analytics and Controlled Experiments

## Why analytics matters

We cannot balance thousands of drinks and missions by intuition alone. Event instrumentation should reveal whether users understand tiers, find order auto-serving intuitive, hit frustrating dead ends, or enjoy novelty. Analytics should help us fix the game, not implement manipulative retention tactics.

## Minimal event taxonomy

| Event | Properties | Purpose |
|---|---|---|
| `session_started` | mission ID/version, catalog hash, device class | denominator for all metrics |
| `shot_accepted` | step, spawn tier, control type, power band | input behavior |
| `shot_rejected` | reason, step, device class | control friction |
| `drink_collision` (sampled) | tier pair, relative speed bucket, angle bucket | physics tuning |
| `drink_merged` | output tier, chain depth, recipe ID, version | progression/action use |
| `order_progressed` | requested tier, remaining quantity | serving clarity |
| `order_fulfilled` | tier, preview coin reward, session | mission pacing |
| `session_finished` | win/loss, score, duration, shots, difficulty | balancing |
| `tier_first_seen_local` | tier, catalog version | discovery pacing |
| `recipe_hint_viewed` (future) | discovery ID, hint tier | research engagement |
| `recipe_discovered` (future) | source, rule ID, feature exposure | discovery funnel |
| `collection_opened` (future) | collection set/version | album engagement |

## Event volume and cost controls

Physical contacts can occur hundreds of times per second. Don't upload every contact in production. Aggregate or sample collision stats locally per session, upload bounded summary histograms if privacy/latency constraints allow. Keep full event traces in developer debug export or opt-in test sessions. No personally sensitive contact data needed.

## Suggested funnels

1. App loaded -> tutorial started -> first valid launch -> first merge -> first order fulfilled -> mission won.
2. Mission unlocked -> mission started -> mission won -> next mission launched.
3. Recipe clue seen -> journal opened -> explicit research attempted -> discovery earned (future).
4. Collection update -> album opened -> next meaningful milestone viewed (future).

Segment by device class, control mode, content version, browser and performance tier. Do not assume low completion = too hard if mobile touch input has a bug.

## Metric definitions

`firstMergeConversion = uniqueSessionsWithMerge / uniqueStartedSessions`; `orderServedBeforeExit = sessionsWithFulfilledOrder / completedOrAbandonedSessions`; `deadBoardRate = terminal losses by board pressure / started sessions`; `tierReachRate(n) = sessionsWithOutputTierN / startedSessions`. Track both player-first attempts and all attempts, with mission version pinned.

## Experiments

Alpha experiments: pointer drag distance/visual guide, next-preview size, order transfer animation length, launch cooldown, result sound hierarchy. Later: recipe hint granularity and optional discovery UI. Avoid concurrent experiments that change physics and scoring such that results become hard to compare. Maintain a holdout and version map; never mix experimental scoring results into the same leaderboard season.

## Privacy and retention

Use pseudonymous run IDs; collect coarse geography only for opted-in local ranking later, not for drink analytics. Respect consent requirements and data deletion. Avoid recording raw input coordinates outside essential debug/test needs. Document data retention; replay traces should not reveal personal identities by default.

## Monitoring gates

Watch crash/freezes, high-latency event queue, asset failures, impossible missions, duplicate reward alerts, score inflation, sharp changes in tier reach rates and tutorial abandonment. Any change should have a rollback feature flag or versioned content fallback.
