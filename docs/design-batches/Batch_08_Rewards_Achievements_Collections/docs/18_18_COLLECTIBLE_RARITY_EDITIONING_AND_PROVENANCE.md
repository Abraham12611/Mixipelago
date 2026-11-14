# 18 — Collectible Catalog, Rarity and Provenance

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Item identity
A collectible definition contains immutable `itemId`, `itemType`, `collectionTags`, `rarityTag`, `edition`, `assetIds`, `displayNameKey`, `descriptionKey`, `acquisitionSources`, `tradability`, `stackingPolicy`, `retirementStatus`, and compatibility constraints. Backend ownership stores stable IDs rather than unverified asset URLs.

## Rarity
Rarity is a taxonomy for display and distribution intent: common, uncommon, rare, epic, legendary. It is not by itself a grant probability and should not imply resale value or a guarantee of scarcity. Show actual obtainable conditions/odds where relevant. Do not assign 'legendary' purely to force spending.

## Editioning and provenance
A player may own `cove-postcard@edition1` from a chapter-clear milestone. Provenance includes `acquiredFromSourceKind`, `sourceId`, `claimReceiptId`, and `acquiredAt`. Retired content remains in historical ownership. If item art is replaced, use an asset revision without changing ownership ID; if content meaning changes materially, publish a new edition.

## Duplicate handling
For nonstackable items, `UNIQUE(player_id, item_id)` ensures one ownership entitlement; second legitimate acquisition gets no extra item unless a published fallback policy grants something else. Never reroll an unwanted prize without a documented rule. For stackable consumables, use a source-based ledger and nonnegative quantity constraints; however, consumables are deferred.

## Trading
Player trading, marketplaces and auction houses are out of Batch 8 scope. All starter items are nontransferable. Opening tradability later requires identity, fraud, economic, moderation and legal review.
