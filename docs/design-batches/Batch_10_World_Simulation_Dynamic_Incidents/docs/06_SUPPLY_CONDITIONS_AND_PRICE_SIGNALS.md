# 06 — Supply conditions and price signals

**Batch 10/21 · Design + engineering specification · 2026-11-14 · Proposed, not implemented.**

## Intent and player-facing result
Introduce meaningful market flavor without undermining starter shop affordability.

## Required behavior and invariants
1. Offer supplier shortfalls and discounts as informational or optional challenge modifiers first.
2. Price changes reference Batch 06 published economy catalog policy, not an untrusted client world variable.
3. Prevent purchase mid-flight policy switching: quote cost/version and settle atomically.

## Cross-domain contract

**Ownership:** World conditions, forecast snapshots, incident eligibility, individual incident lifecycle and player-world chronicle.
**Handoffs:** Batch 05 map, Batch 06 wallet/insurance/shops, Batch 09 customer demand, Batch 12 live calendar, Batch 04 gameplay mode rules.

| Interface | Requirement |
|---|---|
| State authority | worldSnapshotId, islandId, authoritative UTC or verified incident receipt |
| Input contract | world.condition_published / incident.offer_created |
| Transition and output | persisted world/incident state and optional downstream command |
| Audit/versioning | catalogHash, effect receipt and operator kill switch |

The owning service must validate published content IDs and the authenticated actor before a persistent mutation. Every new semantic event includes `eventId`, `schemaVersion`, `sourceId`, `rulesHash`/`catalogHash` where applicable, and correlation metadata. Consumer retries must be idempotent. Avoid undocumented direct writes between domain tables.

## Exceptional states, recovery and fairness
A shortage cannot make mandatory tier-one drinks unavailable or make an island impossible.

If required content is unpublished, a feature flag is off, or an external service becomes unavailable, provide an explicit disabled or read-only fallback. Never fabricate a successful economy award, verified score, social action or quest completion in the interface. Existing durable ownership must survive a content sunset.

## Testable acceptance
Price quote stale on condition change; fallback supplier available at capped price.

Tests must also cover unauthorized actor, duplicate event, stale content version, concurrent request, reload, offline/error recovery and accessibility as appropriate. Manual UI/gameplay feel tests are directed to the owner; unit and integration tests are the engineering team’s responsibility.

## Implementation handoff
1. Freeze the public TypeScript/JSON contract and the feature gate; add a minimal golden fixture.
2. Implement the pure rule or state transition before UI wiring; prove idempotence and safe migration.
3. Add read projection and an accessible view; integrate only with existing service authority.
4. Add telemetry, documented rollback, API error states and a PR description covering dependent batches.

**First-release rule:** Preview weather overlays after the first campaign (candidate v0.6.0); authored opt-in incidents and recovery (v0.6.1+); shop-economic world effects only after audited server-ledger integration (v0.7+).

**Batch-wide invariant:** World state is global only when explicitly authored; individual incident choices remain player-owned. Worker schedules are authoritative UTC; puzzle active-time is a different clock. Financial settlement always routes to Batch 06. Recovery options are mandatory for setbacks.

## Decisions requiring review
Do not treat numerical values, character/world concepts, scheduling dates or content examples as owner-approved production policy. Mark unresolved choices in the implementation PR, and pin released rule revisions before grant or rank settlement.
