# 05 — Canonical Skill Tree Graph and Prerequisite DSL

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Graph structure
A catalog contains branches and skill nodes. Each node has immutable `skillId`, localized display metadata, effect IDs, maximum rank, points per rank, minimum player level, prerequisites and mode tags. A branch is taxonomy, not entitlement. Edges represent prerequisites, not physics interactions.

## Gate semantics
A rank purchase is valid only if ALL apply: player owns enough unallocated points; requested rank equals `currentRank + 1`; published catalog marks the node enabled for the environment; account level is sufficient; required node ranks and explicit shop/campaign prerequisites are satisfied; branch requirements are met; active loadout constraints remain valid after purchase.

## Example prerequisite DSL
```json
{"all":[{"skill_rank_at_least":{"id":"hp_warm_welcome","rank":1}},{"player_level_at_least":4}]}
```
The evaluator supports only `all`, `any`, `not` (only on boolean feature flags, not point-spending), `skill_rank_at_least`, `player_level_at_least`, `campaign_completed`, `shop_prestige_at_least`, and `feature_enabled` when the relevant domain owns the published evidence. Do not allow arbitrary JS/script strings in authored catalogs. The included v0.4.0 sample uses simple rank and level gates.

## Authoring and validation
- Node IDs and effect IDs are case-stable. Graph must be a directed acyclic graph; cycles, missing node references, impossible rank requirements and unreachable enabled nodes reject publishing.
- A skill cannot require a future-only disabled node when it itself is enabled.
- Required total points and current cap must be considered: a chain requiring 25 points cannot be enabled at a level cap that awards 19.
- A node can be visible but locked; a hidden node requires a spoiler policy and must not be a mandatory main-path prerequisite.

## UI projections
Return reason codes (`LEVEL_TOO_LOW`, `PREREQUISITE_MISSING`, `POINTS_INSUFFICIENT`, `MODE_DISABLED`, `NOT_PUBLISHED`) and server-calculated next-rank cost; avoid a client duplicating the gating logic as authority. The graph layout should be cosmetic and adapt to mobile, including screen-reader list navigation.

## Expanding the tree safely
Publish catalog vN+1 with a compatibility report: removed/renamed nodes, changed costs, changed effect caps, and current player builds at risk. Existing entitlements remain addressable through prior catalog revisions. A removal requires either conversion rule or point refund and owner-approved rollout.
