# 30 — HTTP APIs, Idempotency and Error Codes

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Read endpoints
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/v1/rewards/inbox?status=&cursor=` | Current own entitlements; paginated |
| GET | `/v1/rewards/receipts/:receiptId` | Read own settlement receipt |
| GET | `/v1/achievements/catalog?edition=` | Public, published definitions |
| GET | `/v1/achievements/me?cursor=` | Verified progress/unlocks |
| GET | `/v1/collections/albums` | Visible albums and edition metadata |
| GET | `/v1/collections/me/:albumId` | Own item list and completion |
| GET | `/v1/inventory/me?cursor=` | Owned items with equipment state |

## Write endpoints
- `POST /v1/rewards/entitlements/:id/claim` with `Idempotency-Key: UUID` and optional `expectedRevision`.
- `POST /v1/rewards/choices/:entitlementId/select` accepts an allowed `optionId`; selected outcome is final within grant receipt.
- `PUT /v1/inventory/equipment/:slot` with `{itemId,expectedRevision}` and idempotency key.
- No public endpoint `grantCoins`, `grantXp`, `unlockAchievement`, `issueEntitlement`, or `setInventoryQuantity`.

## Example response
```json
{"receiptId":"rr_123","status":"claimed","entitlementId":"re_123","lines":[{"kind":"cosmetic","itemId":"badge-first-service","quantity":1}],"claimedAt":"2026-11-14T12:00:00Z","revision":8}
```

## Error codes
`UNAUTHENTICATED`, `ENTITLEMENT_NOT_FOUND`, `NOT_ELIGIBLE`, `CLAIM_ALREADY_COMPLETE`, `EXPIRED`, `CATALOG_STALE`, `REWARD_SOURCE_UNVERIFIED`, `POLICY_DISABLED`, `ITEM_ALREADY_OWNED`, `CHOICE_INVALID`, `IDEMPOTENCY_CONFLICT`, `REVISION_CONFLICT`, `SETTLEMENT_PENDING`, `RATE_LIMITED`, `SERVICE_UNAVAILABLE`.

## Request ownership and caching
Actor identity comes from session auth, not request body. Wallet/claim/inventory reads are `private, no-store` as necessary; public published catalog may cache by content hash. All mutation routes require auth, authorization, actor-scoped idempotency and telemetry with no PII in logs.
