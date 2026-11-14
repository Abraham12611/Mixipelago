# 31 — TypeScript Package Boundaries and Events

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Recommended packages
`@mixipelago/reward-contracts`, `reward-rules` (pure evaluation), `achievement-projections`, `reward-settlement`, `inventory-domain`, `collection-projections`, `reward-ui`. Reuse existing Batch 6 economy ledger package and Batch 7 XP service; do not fork them.

## Trusted event envelope
`eventId`, `schemaVersion`, `type`, `playerId`, `sourceKind`, `sourceId`, `occurredAt`, `verifiedAt`, `producer`, `contentVersion`, `correlationId`. Event types: `achievement.progressed.v1`, `achievement.unlocked.v1`, `reward.entitlement_created.v1`, `reward.claim_started.v1`, `reward.claim_settled.v1`, `inventory.item_granted.v1`, `collection.milestone_unlocked.v1`.

## Service commands
`deriveAchievements(verifiedFact, rulesSnapshot)`, `createEntitlement(playerId,source,policyId)`, `claimEntitlement(playerId,entitlementId,requestId)`, `equipOwnedCosmetic(playerId,slot,itemId,expectedRevision)`, `projectCollection(playerId,albumEdition)`.

## Event processing semantics
At-least-once delivery is expected; consumer inbox dedups by event ID. Side effects may be delivered out of order; source verification and ownership checks must converge. Keep original event time and verified time separate. No endless recursive `inventory.item_granted → achievement → inventory.item_granted ...`; enforce event ancestry depth and source-stage uniqueness.

## Adapter seams
- Batch 4: verified mission results and order facts; no score recomputation.
- Batch 5: graph node unlock/treasure visibility and durable completion.
- Batch 6: `issueCoinGrantFromVerifiedEntitlement` and shop equipment; transaction-safe.
- Batch 7: `issueXpGrantFromVerifiedEntitlement` only for separately approved XP sources; first-clear XP must not be paid twice.
- Future Batches 12–14: finalized event/season/social source receipts.

## Sample reference code
See `examples/contracts/reward-rules-reference.ts`. It is pedagogical pure logic, not an authenticated production service.
