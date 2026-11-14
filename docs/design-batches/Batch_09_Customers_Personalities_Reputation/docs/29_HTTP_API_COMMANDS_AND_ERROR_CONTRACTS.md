# 29 — HTTP API, Commands, Read Models and Error Semantics

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## API principles
Use the existing Fastify application and Supabase PostgreSQL data authority. All mutation commands require validated identity and an idempotency key or stable source reference. Do not expose an endpoint allowing the browser to write `satisfaction`, `reputation`, `loyalty`, VIP probability or arbitrary reward amounts.

## Proposed read endpoints
| Method | Path | Notes |
|---|---|---|
| GET | `/v1/customers/catalog?locale=en` | Public published and allowed customer art/meta only |
| GET | `/v1/customers/encounters/current?shopId=` | Player-scoped reserved encounter, if feature enabled |
| GET | `/v1/customers/journal?cursor=` | Owned, unlocked recurring guests only |
| GET | `/v1/customers/journal/:customerId` | Auth + visibility checks |
| GET | `/v1/shops/:shopId/reputation` | Trusted reputation projection, source receipt summary |
| GET | `/v1/customers/policies/:version` | Public policy and fairness explanation |

## Proposed internal commands
`reserveEligibleEncounter(player, shop, mission, entitlementKey)`; `consumeVerifiedServiceReceipt(verifiedResultReceiptId)`; `deriveSatisfactionObservation(receipt, policy)`; `applyReputationDelta(verifiedObservation)`; `advanceGuestRelationship(verifiedEncounter)`. These are backend domain calls, **not public client endpoints**. Optional `POST /v1/customers/journal/preferences` changes only player display preferences, not customer game traits.

## Error contract
`UNAUTHENTICATED`, `SHOP_NOT_OWNED`, `ENCOUNTER_NOT_ELIGIBLE`, `POOL_NOT_PUBLISHED`, `CONTENT_VERSION_MISMATCH`, `ALREADY_RESERVED`, `RECEIPT_UNVERIFIED`, `IDEMPOTENCY_CONFLICT`, `FEATURE_DISABLED`, `RATE_LIMITED`, `REVISION_CONFLICT`, `SERVICE_UNAVAILABLE`. Return structured code, correlation ID and retryability flag. Failed mutation cannot return success.

## Caching
Read-only public catalog by hash can use CDN caching. Current encounter, journal, and reputation responses are authenticated private, `Cache-Control: private, no-store` for sensitive projections. Strictly derive player ID on the server from the session token.
