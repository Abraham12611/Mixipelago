# 32 — Formal Rules, Pure Resolver and Reducer Pseudocode

## Inputs and outputs

The engine accepts `(catalog, mission, physicsPreset, seed, commands)`. Physics emits contact candidate pairs with logical drink object IDs. Resolver returns `ineligible` or `(recipeId, outputDrinkId, outputTier)`. Arbiter ensures only one claim per body per resolution step; session reducer awards score and serves orders. This is intentionally pure except for physics body management in the adapter.

## Canonical alpha recipe resolver

```ts
type Drink = Readonly<{ id: string; tier: number; familyId: string }>;
type Catalog = ReadonlyMap<string, Drink & { nextTierId: string | null }>;
type Resolution =
  | Readonly<{ kind: 'merge'; recipeId: string; outputDrinkId: string; outputTier: number }>
  | Readonly<{ kind: 'none'; reason: string }>;

export function resolveAlphaPair(aId: string, bId: string,
  catalog: Catalog): Resolution {
  const a = catalog.get(aId), b = catalog.get(bId);
  if (!a || !b) return { kind: 'none', reason: 'unknown-drink' };
  if (a.familyId !== 'core' || b.familyId !== 'core')
    return { kind: 'none', reason: 'family-not-enabled' };
  if (a.tier !== b.tier) return { kind: 'none', reason: 'different-tier' };
  if (a.tier === 8 || !a.nextTierId || a.nextTierId !== b.nextTierId)
    return { kind: 'none', reason: 'max-tier-or-mismatched-rule' };
  const output = catalog.get(a.nextTierId);
  if (!output || output.tier !== a.tier + 1)
    throw new Error('Published catalog invariant violation');
  return {
    kind: 'merge',
    recipeId: `core:tier-${a.tier}-to-${output.tier}`,
    outputDrinkId: output.id,
    outputTier: output.tier
  };
}
```

**Important:** Future family rules must not infer compatibility from `tier` alone. Explicit recipe index/map will supersede this alpha-only resolver.

## Deterministic candidate arbitration (pseudocode)

```ts
function arbitrate(step: number, contactPairs: Pair[], state: SimState) {
  const candidates = canonicalizeAndSort(contactPairs, step);
  const claimed = new Set<string>();
  const pending: MergePlan[] = [];
  for (const [idA, idB] of candidates) {
    if (claimed.has(idA) || claimed.has(idB)) continue;
    const a = state.objects.get(idA), b = state.objects.get(idB);
    if (!a || !b || !eligibleStatus(a) || !eligibleStatus(b)) continue;
    const result = resolveAlphaPair(a.drinkId, b.drinkId, state.catalog);
    if (result.kind !== 'merge') continue;
    claimed.add(idA); claimed.add(idB);
    pending.push({
      step, inputIds: [idA, idB], recipe: result,
      mergeId: `m:${state.sessionId}:${step}:${idA}:${idB}`,
      pose: deterministicAnchor(a, b), velocity: boundedMergedVelocity(a, b)
    });
  }
  return pending; // Commit after physics step, in this sorted order.
}
```

`canonicalizeAndSort` sorts pair IDs independent of Rapier's runtime collider handle order. Collision may be detected multiple times; committed merge IDs and consumed object IDs are idempotently protected.

## Session reducer serving priority

```ts
function processMergedOutput(event: DrinkMerged, session: SessionState) {
  if (session.appliedMergeIds.has(event.mergeId)) return session;
  session.appliedMergeIds.add(event.mergeId);
  session.score += mergePoints(event.outputTier, event.chainDepth);
  session.merges++;
  const order = session.activeOrders
    .filter(o => o.requestedTier === event.outputTier && o.servedCount < o.quantity)
    .sort((a,b) => a.createdAtStep - b.createdAtStep || a.id.localeCompare(b.id))[0];
  if (order) {
    session.objects.get(event.outputObjectId)!.status = 'serve_claimed';
    order.servedCount++;
    emitOnce('order_line_progressed', order.id, event.mergeId);
    if (order.servedCount === order.quantity) {
      order.status = 'fulfilled';
      session.score += order.coinReward * 10;
      session.previewCoinsEarned += order.coinReward;
      emitOnce('order_fulfilled', order.id, event.mergeId);
    }
  }
  // Evaluate win/loss before generating a replacement order.
  evaluateTerminal(session);
  if (!session.terminal && order?.status === 'fulfilled') maybeReplaceOrder(session);
  return session;
}
```

Above is illustrative, not copy-paste production code: `emitOnce` needs scoped event IDs; `sort` should use stable preallocated order keys; world mutations must run at safe boundaries; and `processMergedOutput` must not rely on mutable UI state.

## Contract invariants

- For every merge: consumed two active input object IDs, produced one new object ID, output tier is exactly +1 in alpha.
- Tier 8 has no next tier; no conditional special transform in alpha.
- In any step, one object participates in no more than one merge transaction.
- Newly produced item is auto-served before it can remerge if an eligible active order exists.
- Duplicate merge events do not change score, orders, or preview coins.
- Rejected shot never advances PRNG/queue.
- Cosmetic variant never affects logical compatibility or physical restitution.
- All outputs/rewards derive from pinned content/rules version.

## Additional formal recipe manifest validation (future)

Normalize each recipe input multiset as sorted `drinkId*count` tokens. For each `(mode, inputKey, contextSignature)` reject more than one satisfiable rule unless precedence/selector is explicit. Restrict recipe graph depth and cycles according to declared mode. When rule selection requires a player choice, capture the choice in signed/verified session command *before* the collision or crafting transaction.

## Required fixtures

Run DRK-001..018 and DRK-024..030 as applicable to alpha, with deterministic expected event lists for: one merge, no merge, max tier, simultaneous triples, chain root, auto-serve, duplicate replay and content pin. Fixture JSON supplied with this pack is illustrative and must be turned into executable unit/integration tests in source.
