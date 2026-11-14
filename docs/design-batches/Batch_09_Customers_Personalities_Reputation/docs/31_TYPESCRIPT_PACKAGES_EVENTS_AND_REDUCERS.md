# 31 — TypeScript Modules, Event Contracts and Reducer Blueprint

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Package architecture
Create `packages/customers` with submodules `catalog/`, `director/`, `order-bridge/`, `observations/`, `reputation/`, `relationships/` and `contracts/`. Batch 3/4 session logic remains a dependency; customers must **not** fork a second order matching engine. Use zod or JSON Schema for runtime payload validation, TypeScript discriminated unions for event types and pure functions for deterministic policy calculation.

## Core functions
```
selectEligibleCustomer(pool, snapshot, randomDrawBps)
validateOrderAgainstMission(request, publishedMission, drinkCatalog)
prepareCustomerEncounter(eligible, pinnedContext)
projectSatisfaction(verifiedOrderEvidence, policy)
computeReputationDelta(satisfaction, policy)
reduceRelationship(verifiedEncounter, priorRelationship, policy)
```
Pure functions do not call network, DB or random global state; orchestrators generate and persist seeds/receipts. Use stable integer arithmetic; any multiplier must document rounding.

## Events and schema revisions
`customer.encounter_reserved.v1`, `customer.order_presented.v1` (visual/read side), `customer.service_observed.v1`, `customer.satisfaction_derived.v1`, `customer.relationship_advanced.v1`, `shop.reputation_observed.v1`. All include `{eventId, schemaVersion, playerId?, sourceRunId?, encounterId?, contentHash, occurredAt, correlationId}` where authorized. Consumer idempotency uses event ID plus domain source uniqueness, not fragile in-memory flags.

## Business transaction
Ingest verified order receipt -> lock relevant relationship/reputation projection if enabled -> insert unique observation -> compute bounded derived values -> append event/outbox -> commit. Currency is settled through Batch 6's already authoritative issuer and must not be reissued in this transaction.

## Replay and testing
Scripted alpha sessions can omit persistent customers entirely. Pure director and observation tests can run in Vitest before API wiring. Runtime simulation must not wait on customer-network updates to advance physics ticks.
