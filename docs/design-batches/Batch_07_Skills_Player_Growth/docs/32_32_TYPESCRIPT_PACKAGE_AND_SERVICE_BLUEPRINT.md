# 32 — TypeScript Packages, Effect Resolver and Integration Order

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Recommended packages
`packages/progression-contracts`: Zod/TypeScript public DTOs, event schema, stable error IDs; `packages/progression-rules`: XP threshold pure functions, prerequisite DSL evaluator, refund math; `packages/skills-catalog`: validated definitions; `apps/game-api/src/modules/progression`: DB command handlers and query projections; `apps/web/src/features/skills`: React tree/list and profile pages. Use existing monorepo conventions if present; do not create duplicate workspaces.

## Pure functions
`xpRequiredForLevel(level): bigint`, `levelFromTotalXp(xp, levelCap): number`, `validateSkillGraph(catalog): Issue[]`, `checkSkillPurchase(catalog, profile, nodeId, requestedRank, context): Decision`, `resolveEffects(catalog, allocations, shop, mode): ModifierBreakdown`, `previewRespec(build, catalog): RespecPreview`.

## Boundary adapter example
```ts
const result = await missionService.verifyAndSettle(sessionReceipt);
if (result.accepted && result.firstClearEntitlement) {
  await progressionService.awardXp({
    verifiedEntitlementId: result.firstClearEntitlement.id,
    policyVersion: result.rewardPolicyVersion,
    requestId: `first-clear:${result.firstClearEntitlement.id}`,
  });
}
```
The progression service loads the trusted XP amount from published policy; the browser does not submit it. A real implementation uses a durable outbox or shared transaction boundary so missed callbacks cannot permanently lose XP.

## Session pinning
Calculate eligible modifiers at session start and include `skillCatalogVersion` / `allocationRevision` only where mode accepts them. Mid-session rank purchases do not modify an in-progress physics simulation or score. Reconnect validates the pinned snapshot rather than hot-swapping abilities.

## UI state discipline
Render read models from server; optimistic preview is allowed only with pending markers. Never show a committed level-up/point spend before backend acknowledgment. Errors restore previous allocation and preserve user input.
