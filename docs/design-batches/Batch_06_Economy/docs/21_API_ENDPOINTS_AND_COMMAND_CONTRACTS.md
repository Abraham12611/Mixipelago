# 21 — HTTP API, Error Codes and Command Contracts

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## API conventions
Authentication by validated session, `Idempotency-Key` required for mutations, `Content-Version` optional for optimistic expectation, structured error codes and no trusted price/identity coming from request body. Command envelope includes `requestId`, `shopId`, `upgradeId`, optional `expectedCatalogVersion`; server derives player ID, price and eligibility.

## Proposed endpoints
| Method | Path | Returns |
|---|---|---|
| GET | `/v1/economy/wallet` | balance, revision and currency |
| GET | `/v1/economy/transactions?cursor=` | paginated ledger feed |
| GET | `/v1/shops` | owned shops and summary projections |
| GET | `/v1/shops/:id` | shop assets, installed upgrades, stats |
| GET | `/v1/shops/:id/upgrades` | eligible catalog and prices |
| POST | `/v1/shops/:id/upgrades/purchase` | purchase receipt and new balance |
| POST | `/v1/shops/:id/cosmetics/equip` | equipped cosmetic projection |
| GET | `/v1/economy/reward-receipts/:id` | authoritative receipt status |

## Error codes
`UNAUTHENTICATED`, `SHOP_NOT_OWNED`, `INSUFFICIENT_COINS`, `UPGRADE_ALREADY_OWNED`, `UPGRADE_PREREQUISITE_UNMET`, `ECONOMY_CATALOG_STALE`, `IDEMPOTENCY_CONFLICT`, `FEATURE_DISABLED`, `REWARD_PENDING_VERIFICATION`, `RATE_LIMITED`, `SERVICE_UNAVAILABLE`.

## Write example
`POST /v1/shops/s_123/upgrades/purchase` with `{ "upgradeId":"hibiscus-planters" }`, header `Idempotency-Key: UUID`. Response `{ receiptId, wallet:{ balance, revision }, ownedUpgrade:{ upgradeId,level }, display:{ priceCharged } }`. On retry return same receipt and balance-at-commit plus latest wallet revision separately if needed; document response semantics to avoid user confusion.

## Auth/cache
Wallet endpoints `Cache-Control: private, no-store`; public upgrade catalog cache by version hash; all mutations rate-limited and instrumented. A stale cached UI must display correct server price before confirmation.
