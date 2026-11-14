# 20 — Prestige, Trophy Rooms and Long-term Vanity

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Long-term goal
A player's world should visibly remember their achievements. Shop walls, island galleries and profile cards can display earned trophies and collectible sets without introducing permanent competitive advantage.

## Example progression
- Level 1 showcase: a simple one-shelf trophy case in the starter shop.
- Later: themed display wall, island landmark plaque, animated fish tank, gilded cocktail cabinet, gallery room and season wall—these are visual proposals, not released features.
- Show the player's favorite earned medals and collections, but distinguish purchased decor from earned prestige badges.

## Display constraints
Limit active dynamic assets to device budget; show a simplified static fallback on low-memory phones. Virtualized collection lists and atlas texture management prevent dozens of simultaneous animated trophies. A single public-facing profile should not expose precise location data.

## Ownership and references
Showroom layout references `ownedItemId` and `layoutSlot`; the persisted layout never includes arbitrary serialized 3D scene code. Validate maximum object count and allowed coordinates. Shareable screenshots may use the existing renderer and must follow normal UGC and privacy review.

## Design ethics
Do not position vanity collections as necessary to keep shops competitive. A fully decorative golden roof may cost substantial earned coins, but its reward is spectacle and self-expression. When marketing a premium item, explicitly state whether it has gameplay utility.
