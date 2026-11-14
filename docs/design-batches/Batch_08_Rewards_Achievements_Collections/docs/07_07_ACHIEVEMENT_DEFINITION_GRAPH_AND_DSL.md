# 07 — Achievements: Definitions, Evidence and Rule DSL

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Domain model
A published achievement has `achievementId`, `definitionEpoch`, `category`, localized copy, icon, visibility, evaluation mode, evidence source allowlist, rule expression, optional tier thresholds, reward policy mapping, and lifetime or scoped period. Definition epochs isolate incompatible redesigns without deleting prior awards.

## Rule DSL
Use an explicit typed AST, not executable authored strings. Candidate operators:
- `count_event{eventType,verified:true,filters}`
- `distinct_count{eventType,key,filters}`
- `best_metric{metric,mode,minimum}`
- `mission_stars_at_least{missionId,stars}`
- `campaign_node_completed{nodeId}`
- `inventory_unique_items{collectionId}`
- `shop_upgrade_owned{upgradeId,minimumLevel}`
- `all`, `any`, `threshold`

`NOT` and time-relative conditions should be limited or banned where they create retroactive regressions. A definition must contain bounded complexity and be validated against allowed event fields.

## Authoritative evaluation
Raw physics notifications (e.g. local `drink_merged`) can feed real-time cosmetic toasts but cannot count as verified achievement evidence. Trusted events include verified mission results, authenticated shop purchases, valid treasure claims and inventory ownership. If later offering combo achievements, the verified session receipt must include a validated combo summary.

## Tiered achievements
For `serve_verified_orders` with thresholds `[10, 50, 200]`, the milestone is awarded at most once at each threshold; crossing 10→200 at once can award all three eligible tiers. One player may carry badge for tier 1 while tier 2 remains claimable. Distinguish `progress`, `unlocked`, `claimed`, and `equipped`.

## Visibility
`visible` displays rule/threshold; `secret` displays placeholder until unlocked; `retired` remains visible to earners as legacy; `draft` never shown. No mandatory achievement should depend on an unpublished hidden source.
