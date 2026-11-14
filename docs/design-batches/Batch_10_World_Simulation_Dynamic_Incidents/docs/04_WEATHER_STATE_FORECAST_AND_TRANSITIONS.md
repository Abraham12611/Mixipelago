# 04 — Weather state, forecast and transitions

**Batch 10/21 · Design + engineering specification · 2026-11-14 · Proposed, not implemented.**

## Intent and player-facing result
Design understandable weather instead of arbitrary unpleasant surprises.

## Required behavior and invariants
1. Model clear, breezy, showers, tropical-storm-warning and storm only where supported.
2. Forecasts are authored probability bands; do not promise literal meteorology or imply real-world weather.
3. Blend visuals/audio with reduced-motion controls; notify of a rule effect before joining a mission.

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
A forecast is informational; an unpublished random outcome cannot charge money.

If required content is unpublished, a feature flag is off, or an external service becomes unavailable, provide an explicit disabled or read-only fallback. Never fabricate a successful economy award, verified score, social action or quest completion in the interface. Existing durable ownership must survive a content sunset.

## Testable acceptance
Transition between rain and clear with muted motion; offline player sees summary, not a barrage of dialogs.

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
