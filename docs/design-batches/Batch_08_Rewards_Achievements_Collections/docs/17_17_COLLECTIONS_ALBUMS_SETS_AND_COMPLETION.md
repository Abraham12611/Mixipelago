# 17 — Collections, Albums, Editions and Completion

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Album data model
A collection consists of a stable `albumId`, `edition`, named chapters or pages, ordered eligible item IDs, visibility, availability window, completion rule and milestone reward references. Each unique eligible item contributes at most once to a distinct-count album, regardless of how many duplicate copies are acquired.

## Proposed album examples
- **First Sips**: illustrated cards for the eight alpha drink tiers, unlocked when **verified** tier discoveries become supported; concept art slots do not imply proven discovery state.
- **Coconut Cove Keepsakes**: coastal decorations and first-town souvenirs from campaign treasures/achievements.
- **Island Postcards**: optional discovery rewards when published islands/landmarks become available.

## Completion formula
`uniqueEligibleOwned / totalPublishedEligible` under a **pinned album edition**. Draft or hidden unpublished items do not inflate the denominator; optional secret item counts must be disclosed as a mystery count without blocking necessary mainline completion. A completed album edition remains completed if later content is added to a new edition.

## Unlock and display states
Unseen → hinted/visible → acquired → optionally displayed. A player may acquire an item from several sources but only one unique-item entry for collection count. Duplicate physical copies may be inventoried only when explicit stackability is intended and they are not used as progress substitutes.

## Collection reward proof
Achievement service derives collection completion from trusted inventory ownership and the published album snapshot; it creates a one-time entitlement. The inventory service must never directly grant its own collection-completion reward recursively without a depth/lineage guard.

## UX
Album grid has accessible item names, silhouette for undiscovered pieces, filters by owned/unowned and page, item-source hints, and count progress. On mobile, avoid forcing horizontal scroll for the core completion denominator. Desktop may show a shelf/gallery view.
