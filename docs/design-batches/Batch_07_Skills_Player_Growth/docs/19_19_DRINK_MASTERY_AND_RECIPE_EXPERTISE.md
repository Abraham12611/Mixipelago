# 19 — Drink Mastery and Craft Proficiency (Later Feature)

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Separate from player level
Recipe-specific mastery tracks should exist only when Batch 3 recipe discovery and verified usage are enabled. Mastery does not overwrite the alpha eight-tier catalog, automatic serving order or terminal tier.

## Proposed milestone ladder
For a drink `drinkId`, verified mastery XP is accumulated through first produced/served occurrences in eligible modes, craft difficulty achievements, or curated recipe tasks. Prototype bands: Novice (0), Familiar (100), Skilled (350), Expert (900), Virtuoso (2,000). All values are tentative; use a versioned cumulative table.

## Rewards
Default rewards: journal entries, badges, frames, cosmetic drink trails, eligible recipe-lore text and celebration effects. Optional operational bonuses must be separately capped and never modify physics or ranked tier scoring.

## Verification
Mastery source events refer to validated mission receipts, not raw browser `drink_merged` events. Repetitive craft spam within one session cannot mint unlimited trusted mastery. Each unique mission challenge source can award mastery at most once unless a published repeat policy exists.

## UI and migration
Recipe Journal can show player mastery alongside tier chart. Keep hidden-recipe metadata spoiler-filtered. When the recipe tree branches in future, mastery IDs remain anchored to stable `drinkId`, not visual tier position.
