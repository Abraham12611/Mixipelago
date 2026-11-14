# 12 — Merge Score, Order Rewards, Preview Coins and Future Economy

## Immediate rule

Every committed merge awards points according to the **output tier** score table in doc 03, plus an optional capped chain multiplier computed by the session reducer. Customer order fulfillment adds `coinReward × 10` to score and `coinReward` to **local preview coins** exactly once. Shooting, collisions without merges, hover effects, recipe silhouettes, and unlocking a menu screen do not award score.

## Proposed alpha function

`mergePoints = round(score[outputTier] × min(3, 1+0.25×max(0,chainDepth−1)))`. One merge of tier-2 + tier-2 -> tier-3 yields 60 base points at chain depth 1. A tier-4 output (base 140) at depth 2 yields `round(140×1.25)=175` points. Sum only unique merge IDs. Session score uses safe finite integers; define overflow behavior and cap totals explicitly.

## Preview coin sources

- Completed order: nominal `coinReward` recorded once.
- Completed mission: optional bonus `rewards.previewCoins` separate from order payouts.
- No coin grants for mere discovery in v0.1; no trusted wallet or leaderboard awards.

A session summary should distinguish `orderPreviewCoins`, `missionBonusPreviewCoins`, and `totalPreviewCoinsEarned`, so the UI is auditable. A local save may be deleted or manipulated; no local balance should be advertised as recoverable or exchanged for purchases.

## Server phase

When trusted progression launches, validated `game_sessions` and `mission_results` become sources for wallet ledger credits. Ledger fields include immutable entry IDs, player ID, currency, delta, reason, run ID, source event ID, request idempotency key and rule version. Never accept `{coins:999999}` from client as the authoritative result. Duplicate submission and retries must produce the same wallet outcome.

## Economy design constraints

Recipe mastery and collectibles should not create runaway compounding passive income. Any spendable materials, power-ups or specialty consumables must have explicit costs/availability and valid server receipts. Tier-8 is difficult to produce but should not be farmed for unlimited coins through a score loop. Mission rewards need daily/season caps where future repeated play makes farming exploitable. All financial balancing is deferred to Batch 6.

## Ranked fairness

Leaderboards should primarily rank standardized score under a versioned ruleset. Currencies, skill perks and paid skins may be displayed but should not alter ranked session scoring. If a future craftable recipe has a unique score effect, it belongs in its own ranked mode with identical unlocked options or is excluded entirely.

## Example event ordering

- `drink_merged(m1, outputTier=3)` -> merge points 60.
- `order_line_progressed(o1, sourceMergeId=m1, quantity=1)` -> order progress.
- `order_fulfilled(o1, reward=15)` -> score +150 and preview coin +15.
- `session_won` -> completion bonus +configured preview coins.
- `session_summary` -> distinct totals and best score persistence.

A UI replay of an effect must not re-invoke any reward reducer. Presentation remains read-only.

## QA

Check safe integer overflow, score from invalid tier, duplicate merge IDs, combo cap, simultaneous order progress, mission completion ordering, failed runs, local-save corruption, server retry concurrency, and leaderboard mode modifier normalization.
