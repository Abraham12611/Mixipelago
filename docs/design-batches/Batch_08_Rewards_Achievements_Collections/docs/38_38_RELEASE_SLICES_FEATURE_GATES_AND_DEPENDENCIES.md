# 38 — Incremental Release Plan and Feature Gates

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Deliver progressively
| Candidate release | Slice | Dependencies | Ship gate |
|---|---|---|---|
| v0.1.0 | Local preview mission-result ribbons only | Batches 2–4 | No trusted payout, clear preview label |
| v0.2.x | Map/treasure UI and preview completion stamps | Batch 5 | Only published, authored nodes |
| v0.3.x | Trusted one-time first-clear/treasure reward receipt | Batch 6 ledger + verified runs | No duplicate credit on retries |
| v0.4.1 candidate | First verified achievement badges/inventory and inbox | Batch 7 identity/progression + Batch 6 trust | One 3–6 item end-to-end slice |
| v0.4.2+ | Albums and equipped profile cosmetics | Inventory + UI + content studio | Item uniqueness and owned-only equip |
| v0.5+ | Optional weekly rewards and collections | Verified event tasks | Economic cap and fairness signoff |
| Future | Seasonal medals, crew rewards, high-trust ranked prizes | Batches 12–14 | Finalized source + anti-cheat review |
| Future | Mystery chests, paid chance items (if pursued) | Compliance review | Published odds, no competitive power |

`v0.4.1` is a candidate roadmap revision, not a promise. Minor vs patch versioning can be adjusted through ADR; in a pre-1.0 project, patch releases may still include gated capability slices if defined release policy permits it.

## First production vertical slice
One verified published mission → mission receipt → achievement evidence → achievement unlock → claimable cosmetic badge → claim once → inventory owned → equip on profile → durable reload → two-device retry. Another candidate is one authored Coconut Cove map treasure. Do **not** implement 14 achievement programs at once.

## Gates
`ACHIEVEMENTS_READ_ENABLED`, `ACHIEVEMENT_CLAIMS_ENABLED`, `COLLECTION_ALBUMS_ENABLED`, `COSMETIC_EQUIP_ENABLED`, `DAILY_REWARD_ENABLED`, `MYSTERY_CHEST_ENABLED` default off in production until dependencies are proven. Gates must be server-authoritative for grant-capable operations; hiding a client button does not enforce security.

## Rollback
Disable new writes, preserve claimed receipts and inventory, retain read-only history, reconcile outstanding entitlements, publish corrective version if needed. Never re-enable preview coins as spendable balances.
