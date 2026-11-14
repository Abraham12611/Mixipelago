# 10 — Bracket tournaments and matchmaking later

**Batch 13/21 · Design + engineering specification · 2026-11-14 · Proposed, not implemented.**

## Intent and player-facing result
Outline head-to-head brackets without pretending they are built.

## Required behavior and invariants
1. Tournament definitions include entry period, seeding, quarter/semifinal/final rounds, advance conditions and disqualification/forfeit rules.
2. Asynchronous bracket matches use standardized replay challenge before synchronous network gameplay.
3. Live matches are separately owned by Batch 14 real-time service.

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
No cash prizes or betting without separate policy/legal review.

If required content is unpublished, a feature flag is off, or an external service becomes unavailable, provide an explicit disabled or read-only fallback. Never fabricate a successful economy award, verified score, social action or quest completion in the interface. Existing durable ownership must survive a content sunset.

## Testable acceptance
Two tied bracket scores resolve under published tie-break; no admin arbitrary winner.

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
