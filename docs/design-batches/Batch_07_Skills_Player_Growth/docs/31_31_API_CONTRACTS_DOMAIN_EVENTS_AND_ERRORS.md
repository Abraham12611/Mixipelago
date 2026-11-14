# 31 — API Contracts, Idempotent Commands and Domain Events

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Read endpoints
`GET /v1/progression/me` returns server-owned XP, level, thresholds, earned/allocated/available points, active catalog hash and allocation revision. `GET /v1/skills/catalog?locale=en` returns published, authorization-filtered definitions and mode annotations. `GET /v1/skills/me` returns ranks, suspended nodes, loadout, and effect summary; never includes secret graph node content.

## Write endpoints
- `POST /v1/progression/skills/{skillId}/allocate`: body `{requestedRank, expectedRevision, clientRequestId}`; response `{receiptId, progression, allocations, effectiveFrom}`.
- `POST /v1/progression/respec/preview`: compute point refund and affected nodes; read-only.
- `POST /v1/progression/respec/commit`: `{previewToken, expectedRevision, clientRequestId}`; atomic respec.
- `PUT /v1/progression/loadout`: `{slotIds, expectedRevision, clientRequestId}`; authoritative validation.
- XP grant has **no public client API**. Trusted mission/quest service calls internal `awardXpFromVerifiedReceipt` with signed/server-owned entitlement.

## Error model
`UNAUTHENTICATED`, `CATALOG_STALE`, `NODE_UNPUBLISHED`, `SKILL_ALREADY_MAXED`, `SKILL_RANK_SEQUENCE`, `LEVEL_REQUIRED`, `PREREQUISITE_MISSING`, `INSUFFICIENT_POINTS`, `REVISION_CONFLICT`, `IDEMPOTENCY_KEY_REUSED`, `MODE_DISABLED`, `RATE_LIMITED`, `POLICY_MIGRATION_REQUIRED`, `INTERNAL_ERROR`. Never return a generic success when transaction failed.

## Events
Produce outbox records on `xp_awarded`, `level_attained`, `skill_points_granted`, `skill_rank_allocated`, `respec_completed`, `loadout_changed`. Each event includes `eventId`, `schemaVersion`, `playerId`, `sourceId`, `sourceCatalogVersion`, `occurredAt`, and correlation/request ID. Consumers must deduplicate by event ID.

## Retry and load
Client may retry a timed-out request with the same request ID; server returns original result. Throttle skill-spend commands per player and version; cache reads but never cache writes without transactional origin.
