# 14 — Narrative reward policy and integrity

**Batch 11/21 · Design + engineering specification · 2026-11-14 · Proposed, not implemented.**

## Intent and player-facing result
Ensure story rewards obey existing trust boundaries.

## Required behavior and invariants
1. Use rewardPolicyId not free-form coinAmount in client scene JSON.
2. Each quest completion emits a unique entitlement source; reward resolver delegates to Batch 06/07/08 domains.
3. Season/event quest scopes include edition identity so intentionally repeatable arcs can be allowed safely.

## Cross-domain contract

**Ownership:** Narrative definitions, dialogue choices and story flags, quest orchestration, approved rival behaviors and the player chronicle.
**Handoffs:** Batch 05 campaign, Batch 09 customers, Batch 06 shops and rewards, Batch 08 collectibles, Batch 10 incidents and Batch 12 festivals.

| Interface | Requirement |
|---|---|
| State authority | narrativeEdition, sceneId, questId, approved choice and server mission receipt |
| Input contract | story.choice_recorded / quest.evidence_verified |
| Transition and output | player narrative flags and quest state |
| Audit/versioning | scene version, source receipt and choice ledger |

The owning service must validate published content IDs and the authenticated actor before a persistent mutation. Every new semantic event includes `eventId`, `schemaVersion`, `sourceId`, `rulesHash`/`catalogHash` where applicable, and correlation metadata. Consumer retries must be idempotent. Avoid undocumented direct writes between domain tables.

## Exceptional states, recovery and fairness
Nonverified local story preview cannot grant durable cosmetics.

If required content is unpublished, a feature flag is off, or an external service becomes unavailable, provide an explicit disabled or read-only fallback. Never fabricate a successful economy award, verified score, social action or quest completion in the interface. Existing durable ownership must survive a content sunset.

## Testable acceptance
Concurrent completion events produce one permanent badge.

Tests must also cover unauthorized actor, duplicate event, stale content version, concurrent request, reload, offline/error recovery and accessibility as appropriate. Manual UI/gameplay feel tests are directed to the owner; unit and integration tests are the engineering team’s responsibility.

## Implementation handoff
1. Freeze the public TypeScript/JSON contract and the feature gate; add a minimal golden fixture.
2. Implement the pure rule or state transition before UI wiring; prove idempotence and safe migration.
3. Add read projection and an accessible view; integrate only with existing service authority.
4. Add telemetry, documented rollback, API error states and a PR description covering dependent batches.

**First-release rule:** Story introduction and one optional quest chain after basic map/player persistence (candidate v0.5.3); branching arcs and simulated rival businesses expand later behind distinct gates.

**Batch-wide invariant:** Narrative content never grants resources by itself. Quest evidence and story choices are stored independently. Mainline quests have an accessible no-spend route; prose is optional and can be skipped. Rival owners are fictional NPCs, not deceptive simulated human opponents.

## Decisions requiring review
Do not treat numerical values, character/world concepts, scheduling dates or content examples as owner-approved production policy. Mark unresolved choices in the implementation PR, and pin released rule revisions before grant or rank settlement.
