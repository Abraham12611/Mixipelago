# 10 — Trophies, Titles, Tier Badges and Display

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Design
A trophy is a durable expression of a verified feat, distinct from the score that produced it. Examples: `Coconut Cove Pioneer`, `Precision Prodigy`, `The Island Collector`. Titles appear on profile cards or leaderboards only where user-approved and moderation-safe. Trophy cases can be displayed in shop interiors or on the player's profile.

## Trophy structure
`itemId`, `trophySeriesId`, `tier` (bronze/silver/gold/legendary as design vocabulary), `earnedFrom`, `edition`, `earnedAt`, `displayAssetId`, `visibility`, `ownerId`, and optional `retirementStatus`. A high-tier badge should not erase earlier earned entries unless the program explicitly defines an evolving display item.

## Equip constraints
Player may display one primary title, a limited number of favorite badges, and one profile frame. Equipped state is a projection referencing owned item IDs; never trust arbitrary client asset URLs or equipment keys. Seasonal trophy editions should be distinct, not overwrite an older trophy's date.

## Fairness and clarity
Do not assign rarity from synthetic scarcity when everyone gets a badge after login. Trophy acquisition should not increase physics force, customer pay or ranked score. If a prestige monument visually attracts visitors later, that economic modifier belongs to Batch 6 and must be disclosed explicitly, never added covertly to a competitive prize.

## UX detail
Trophy detail shows name, actual completion condition, relevant season/edition, and acquisition date. Unowned secret trophies can show silhouette/hint without spoiler if authored. Avoid flashing giant reward celebrations for trivial actions; respect reduced motion.
