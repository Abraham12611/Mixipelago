# 27 — ADR, requirements, glossary and source links

**Batch 12/21 · Design + engineering specification · 2026-11-14 · Proposed, not implemented.**

## Intent and player-facing result
Record open ownership and publication decisions.

## Required behavior and invariants
1. Decide initial event cadence, cutoff grace, participation caps and no-login event browsing.
2. Trace event definition → API/worker → trusted receipt → reward issuer → UI → QA fixture; no unowned step.
3. Keep design-only ideas marked disabled and review dates fixed at publish.

## Cross-domain contract

**Ownership:** Event calendar editions, schedule semantics, activity enrollment, eligibility, participation projections and event orchestration.
**Handoffs:** Batch 10 weather and world conditions; Batch 11 story quests; Batch 04 missions; Batch 06/08 rewards; Batch 13 tournament rankings; Batch 14 crews.

| Interface | Requirement |
|---|---|
| State authority | eventEditionId, serverUTC, participation and verified activity receipt |
| Input contract | event.enrolled / event.contribution_verified |
| Transition and output | bounded progress, eligibility and claim receipt |
| Audit/versioning | immutable edition hash and claim source key |

The owning service must validate published content IDs and the authenticated actor before a persistent mutation. Every new semantic event includes `eventId`, `schemaVersion`, `sourceId`, `rulesHash`/`catalogHash` where applicable, and correlation metadata. Consumer retries must be idempotent. Avoid undocumented direct writes between domain tables.

## Exceptional states, recovery and fairness
No event configuration can override Batch 04/06/08/13 authority.

If required content is unpublished, a feature flag is off, or an external service becomes unavailable, provide an explicit disabled or read-only fallback. Never fabricate a successful economy award, verified score, social action or quest completion in the interface. Existing durable ownership must survive a content sunset.

## Testable acceptance
Every event has clear edition hash, end state, rollback plan and support message.

Tests must also cover unauthorized actor, duplicate event, stale content version, concurrent request, reload, offline/error recovery and accessibility as appropriate. Manual UI/gameplay feel tests are directed to the owner; unit and integration tests are the engineering team’s responsibility.

## Implementation handoff
1. Freeze the public TypeScript/JSON contract and the feature gate; add a minimal golden fixture.
2. Implement the pure rule or state transition before UI wiring; prove idempotence and safe migration.
3. Add read projection and an accessible view; integrate only with existing service authority.
4. Add telemetry, documented rollback, API error states and a PR description covering dependent batches.

**First-release rule:** Candidate first opt-in festival and a single authored event mission after campaign and trusted rewards (v0.6.2); calendar rotation, community goals and seasonal live programs staged later.

**Batch-wide invariant:** An event edition is immutable once opened. Eligibility is server-UTC based, and rewards require verified activity receipts. Event windows, score windows, and prize claim grace are different. Community contributions are bounded and idempotent.

## Decisions requiring review
Do not treat numerical values, character/world concepts, scheduling dates or content examples as owner-approved production policy. Mark unresolved choices in the implementation PR, and pin released rule revisions before grant or rank settlement.
