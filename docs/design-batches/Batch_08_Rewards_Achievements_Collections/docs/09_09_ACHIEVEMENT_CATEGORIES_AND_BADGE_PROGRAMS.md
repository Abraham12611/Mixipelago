# 09 — Achievement Categories and Example Catalog

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Initial achievement families
| Family | Illustrative achievements | Evidence |
|---|---|---|
| First Steps | First verified order, first verified mission | Trusted session receipt |
| Mix Craft | Achieve tier 5 or complete a chain combo | Verified session summary |
| Campaign | Clear chapter, reach a gateway, three-star milestones | Campaign projection |
| Service | Serve 10/50/200 orders | Deduplicated order IDs |
| Business | Buy first shop upgrade, install display decor | Batch 6 purchase receipt |
| Discovery | Reveal an optional trail, find authored treasure | Batch 5 durable discovery evidence |
| Collection | Collect five unique drink cards, complete themed album | Inventory unique item ownership |
| Competition | Place in league, earn seasonal medal | Future verified ranking results |
| Social | Complete crew milestone | Future verified crew service |

## Proposed starter program
For first trusted achievement slice, publish only a small set: `first-service`, `first-mission`, `first-shop-upgrade`, `three-star-aspirant`, `five-unique-items`, and `cove-trailblazer` when matching trusted upstream features exist. The sample catalog contains 14 candidates, but most remain `draft`.

## Avoid counterfeit achievements
Do not award a business achievement for clicking an unimplemented shop button. Do not award tier-8 craft from mere client physics logs. The playable alpha may show provisional local ribbons only, unmistakably labeled as preview.

## Metadata
Each badge needs accessible name, rarity label only if derived from actual incidence, source facts, progress denominator where appropriate, time scope, reward disclosure, and a distinct color-blind-safe shape. Achievement notification settings should be optional.

## Retired and revised programs
Do not silently delete a previously earned achievement if a node is retired. Retired definitions remain readable as legacy; new claims use new epochs. Editing copy/icons may be nonbreaking, but threshold or entitlement changes require a versioned migration and parity tests.
