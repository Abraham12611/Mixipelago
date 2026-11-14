# 02 — Progression Layers and Shared Vocabulary

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Distinct progress bars; never collapse them
| Layer | Scope | Earned by | Unlocks | Source of truth |
|---|---|---|---|---|
| Entrepreneur level | Player profile | Verified first clears and designated quests | Eligibility, points, titles | Server XP ledger |
| Skill points | Player profile | Defined level milestone rewards | Permanent skill ranks | Trusted allocation ledger |
| Skill rank | Player build | Spending earned points | Passive and active effects | Allocation projection |
| Skill loadout | Player profile / mode | Equipping owned skills | Selected active utilities | Validated loadout row |
| Drink mastery | Recipe x player | Verified usage/discovery challenges | Badges and optional utility | Recipe mastery ledger (later) |
| Island completion | Mission x player | Verified mission result | Map paths and treasures | Campaign graph results |
| Shop prestige | Shop x player | Verified purchases/actions | VIP and cosmetic availability | Batch 6 shop aggregate |
| Competitive rank | Season x mode | Validated standardized score | Rank cosmetics, rewards | Ranking service |
| Collection | Player x item | Explicit first acquisition | Album milestones | Inventory/collection ledger |

## Name policy
- `playerLevel` is a durable account-associated RPG level. `missionId` and `nodeId` identify puzzles and world graph positions; never reuse `levelId` ambiguously.
- `XP` is not a spendable wallet unit. The `xp_total` aggregate monotonically increases; only skill points are allocated.
- `talent` and `skill` are synonyms in player-facing language; use `skill` in APIs. `rank` is within a node, whereas `level` is the player's RPG level.
- `specialization` is a player-facing profile archetype computed from investment, not an exclusive irreversible class.
- `effect` is a typed, source-attributed modifier; `modifier` is its evaluated numeric contribution; `perk` is marketing copy, not an API type.

## Example profile display
`Entrepreneur Lv. 7 • 6 / 6 points earned • 4 allocated • 2 available • Hospitality focus • 280 / 400 XP to next level` is a read-only projection. XP thresholds, totals and invested points are validated server-side; client calculates only local progress UI from trusted responses.

## Separation of player, shop, and mission stats
Skill `hp_golden_guestlist` is attached to a player; VIP Seating is attached to the active owned shop. The Customer Director receives both sources with explicit provenance. A regional tournament receives neither unless rules allow a fixed standardized build. A shop transfer or location switch changes shop stats, not player talents.

## Event taxonomy
`xp_awarded`, `player_level_changed`, `skill_points_granted`, `skill_rank_allocated`, `skill_loadout_changed`, `skills_respecced`, `effective_modifiers_computed` (internal), `mastery_progressed` (later). All events need a stable ID, actor, source receipt/version, and idempotency key where they trigger persistent value.
