# 21 — Achievements, Souvenirs, Collectibles and Journal Integration

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## In-world collecting
A recurring guest may gift a named souvenir, postcard, photo frame or badge. These are collectible cosmetic ownerships under **Batch 8**, not ad hoc item flags stored in the customer reducer. `CustomerSouvenirEligible` is an evidence event, not an entitlement by itself.

## Example flow
Guest earns loyalty tier `regular` through verified encounters -> Batch 9 emits unique eligible milestone -> Batch 8 achievement/claim engine creates entitlement -> player claims `coral-postcard` -> inventory row and catalog version are persisted -> collection album updates. If the claim service retries, no duplicate item or coin is minted.

## Separation
Batch 9 owns relationship threshold calculations, Batch 8 owns item catalog, claim eligibility/equipment/provenance, Batch 6 owns coins, Batch 7 owns XP. Do not give player reputation as a cosmetic auto-grant without a rule-published receipt. Seasonal guest editions should retain provenance and not invalidate historic collections on content retirement.

## Content safety
Collectible images should not include copyrighted IP or likeness of a real celebrity without permission. Character reactions and gift dialog must be family-friendly. No real money mystery prizes or undisclosed randomized reward odds are introduced here.

## Test focus
Milestone reached twice -> one entitlement; account sync delayed -> pending state; invalid retired collectible -> stable fallback; discarded preview session cannot grant souvenir; trophy reward from a ranked event needs the trusted future leaderboard receipt, not a local social screenshot.
