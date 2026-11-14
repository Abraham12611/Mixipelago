# 29 — Architecture decisions and traceability

**Batch 14/21 · Design + engineering specification · 2026-11-14 · Proposed, not implemented.**

## Intent and player-facing result
Record unresolved choices before engineers code them.

## Required behavior and invariants
1. Decide live match turn model, privacy defaults, maximum crew size, age-aware social behavior, gift limitations and regional service strategy.
2. Trace each social command to actor authorization, RLS, unique constraints, UI statuses and rollback.
3. Explicitly identify any new service dependency or paid infrastructure.

## Cross-domain contract

**Ownership:** Friend relationships, crew membership and governance, social challenges, contributions, invitations and multiplayer session orchestration.
**Handoffs:** Batch 13 rankings and verified replays; Batch 06 wallet; Batch 08 rewards; Batch 09 guest personalities; Batch 12 festival co-op; Batch 02 physics server certification.

| Interface | Requirement |
|---|---|
| State authority | authenticated actor, canonical friend pair / crew / match id |
| Input contract | social.friend_accepted / crew.contribution_verified |
| Transition and output | authorized social state or server-owned match result |
| Audit/versioning | request id, actor, revision and moderation trail |

The owning service must validate published content IDs and the authenticated actor before a persistent mutation. Every new semantic event includes `eventId`, `schemaVersion`, `sourceId`, `rulesHash`/`catalogHash` where applicable, and correlation metadata. Consumer retries must be idempotent. Avoid undocumented direct writes between domain tables.

## Exceptional states, recovery and fairness
Social never overrides ranking score or campaign unlocks directly.

If required content is unpublished, a feature flag is off, or an external service becomes unavailable, provide an explicit disabled or read-only fallback. Never fabricate a successful economy award, verified score, social action or quest completion in the interface. Existing durable ownership must survive a content sunset.

## Testable acceptance
Feature gate has independent kill switch and saved-state migration plan.

Tests must also cover unauthorized actor, duplicate event, stale content version, concurrent request, reload, offline/error recovery and accessibility as appropriate. Manual UI/gameplay feel tests are directed to the owner; unit and integration tests are the engineering team’s responsibility.

## Implementation handoff
1. Freeze the public TypeScript/JSON contract and the feature gate; add a minimal golden fixture.
2. Implement the pure rule or state transition before UI wiring; prove idempotence and safe migration.
3. Add read projection and an accessible view; integrate only with existing service authority.
4. Add telemetry, documented rollback, API error states and a PR description covering dependent batches.

**First-release rule:** Candidate v0.7.0 friends + asynchronous ghost challenges; v0.7.1 crew projects; v0.8.0+ real-time matches only after authoritative simulation, reconnect and moderation tests.

**Batch-wide invariant:** Friend consent, blocking and privacy protections are product primitives. A real-time client cannot authoritatively determine match score, collision or winner. In early releases there are no unrestricted public DMs or player-to-player coin trades.

## Decisions requiring review
Do not treat numerical values, character/world concepts, scheduling dates or content examples as owner-approved production policy. Mark unresolved choices in the implementation PR, and pin released rule revisions before grant or rank settlement.
