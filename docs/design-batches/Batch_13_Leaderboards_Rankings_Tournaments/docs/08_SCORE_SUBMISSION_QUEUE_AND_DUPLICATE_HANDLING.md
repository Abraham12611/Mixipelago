# 08 — Score submission, queue and duplicate handling

**Batch 13/21 · Design + engineering specification · 2026-11-14 · Proposed, not implemented.**

## Intent and player-facing result
Separate intake from asynchronous verification.

## Required behavior and invariants
1. POST submit queues verification; return pending receipt and stable runId; never block user indefinitely on live worker.
2. Unique (player,competition,runId) prevents double entries and idempotency key mismatches conflict.
3. Outbox publishes verified/rejected and materializer recomputes best eligible row.

## Cross-domain contract

**Ownership:** Score submission/proof validation, ranking materialization, season freeze, divisions and tournament adjudication.
**Handoffs:** Batch 02 physics/replay; Batch 04 scoring and missions; Batch 06 rewards; Batch 07 normalized skills; Batch 08 prize entitlements; Batch 14 friends and crews.

| Interface | Requirement |
|---|---|
| State authority | competitionEdition, certified replay hash and verified result |
| Input contract | score.verified / season.frozen |
| Transition and output | rank projection and prize eligibility |
| Audit/versioning | signed replay verdict, comparator version and frozen ledger |

The owning service must validate published content IDs and the authenticated actor before a persistent mutation. Every new semantic event includes `eventId`, `schemaVersion`, `sourceId`, `rulesHash`/`catalogHash` where applicable, and correlation metadata. Consumer retries must be idempotent. Avoid undocumented direct writes between domain tables.

## Exceptional states, recovery and fairness
Do not substitute unchecked client score on verification timeout.

If required content is unpublished, a feature flag is off, or an external service becomes unavailable, provide an explicit disabled or read-only fallback. Never fabricate a successful economy award, verified score, social action or quest completion in the interface. Existing durable ownership must survive a content sunset.

## Testable acceptance
Submission retry after HTTP timeout yields same pending/verified status.

Tests must also cover unauthorized actor, duplicate event, stale content version, concurrent request, reload, offline/error recovery and accessibility as appropriate. Manual UI/gameplay feel tests are directed to the owner; unit and integration tests are the engineering team’s responsibility.

## Implementation handoff
1. Freeze the public TypeScript/JSON contract and the feature gate; add a minimal golden fixture.
2. Implement the pure rule or state transition before UI wiring; prove idempotence and safe migration.
3. Add read projection and an accessible view; integrate only with existing service authority.
4. Add telemetry, documented rollback, API error states and a PR description covering dependent batches.

**First-release rule:** One normalized weekly global challenge after verified server replay (candidate v0.5.0); historical seasons/divisions v0.5.1+; tournaments and opt-in regional boards after safeguards.

**Batch-wide invariant:** Only a verified competition profile enters ranked standings. The official comparator is score descending, shots ascending, activeTicks ascending, verifiedAt ascending, then playerId ascending. Redis is cache; PostgreSQL and replay receipts are authoritative.

## Decisions requiring review
Do not treat numerical values, character/world concepts, scheduling dates or content examples as owner-approved production policy. Mark unresolved choices in the implementation PR, and pin released rule revisions before grant or rank settlement.
