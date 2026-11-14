# 40 — Architecture Decisions, Conflicts and Owner Decisions

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Candidate ADRs
- ADR-8-01: Rewards orchestrator does not replace Batch 6 wallet or Batch 7 XP issuer. **Recommended: adopt.**
- ADR-8-02: Achievement definitions use typed DSL and immutable epochs, not arbitrary scripts. **Recommended: adopt.**
- ADR-8-03: All core chapter/mission prizes deterministic; randomized chests deferred. **Recommended: adopt.**
- ADR-8-04: Cosmetics owned and equipped separately; equipped cosmetic has no hidden power. **Recommended: adopt.**
- ADR-8-05: Daily participation is optional and not an essential XP source. **Recommended: adopt.**
- ADR-8-06: Existing earned edition trophies persist across map expansions. **Recommended: adopt.**

## Cross-batch conflict resolution
If Batch 7 says first-clear XP is granted automatically by verified mission, Batch 8 achievement completion must not pay it again. If Batch 5 says treasure becomes eligible, Batch 8 may create a claimable entitlement but cannot mark map node cleared itself. If Batch 6 says cosmetic ownership lives in shop inventory tables, Batch 8 may own a broader cross-context inventory facade but must reconcile to one canonical item entitlement table—not duplicate independent 'owned' flags.

## Open design decisions for owner
1. Do we want a single rewards hub or independent achievement and collection tabs at v0.4?
2. Should first achievement badge automatically appear in inventory, or require a manual claim?
3. Will collector album items represent verified drink discoveries or separate souvenir drops?
4. Should prestige trophies have purely visual rarity, or any clearly labeled shop prestige effect?
5. Do we want daily rewards at all, or use optional weekly milestone boards?
6. Do collections show secret silhouettes/counts prior to reveal?
7. What is the maximum count of simultaneously displayed trophies on mobile?

## Decisions requiring proof
Actual owner approval of UX, economy upper bounds, live entitlement reconciliation, replay proof, and content publishing security are release gates. Specifying a proposed behavior here does not override prior shipped contracts automatically.
