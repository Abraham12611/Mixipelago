# 31 — Engineering Implementation Blueprint

## Recommended build order
**A.** Extract a shared campaign domain package and compile schemas/types. **B.** Implement pure unlock and projection functions with fixtures. **C.** Integrate local-preview mission result reducer. **D.** Render simple node-line map using Phaser or Canvas, no fancy art. **E.** Add DOM node cards, Next/Replay actions, touch/mouse camera. **F.** Add themed map chunks and route animations. **G.** Add optional secret/treasure and gateway nodes only once validated. **H.** Add auth/server receipts in later trusted economy work.

## Modules and ownership
`campaign-core`: gate DSL, graph/topology, derived node projection, progress reducer and recommendation, unit tests. `map-renderer`: camera, hit targets, scene layers, chunks, node/edge sprites. `web-app`: route, map shell, cards, menus and accessible list. `content`: island JSON, validation schema and publication manifest. `backend`: verified receipt integration later.

## Pseudocode for successful mission return
```ts
async function onMissionEnded(result: MissionResult) {
  if (result.outcome !== 'won') return showResults(result);
  const current = loadPreviewProgress(); // preview mode only
  const updated = upsertMonotonicBest(current, result);
  persistValidatedPreviewState(updated);
  const newProjection = deriveProjection(activeGraph, updated);
  return showResultsWithUnlockedNodes(result, newProjection.delta);
}
```
Production server mode replaces local update with receipt confirmation; never trust client `won` for durable rewards.

## Node launch pseudocode
```ts
function requestStartNode(nodeId: string) {
  const node = graph.indexById.get(nodeId);
  const vm = projection.byNodeId.get(nodeId);
  if (!node || node.status !== 'published' || node.type !== 'mission') return unavailable();
  if (!vm?.eligible || !vm.visible) return showRequirements(vm);
  if (!node.mission || !runtimeSupports(node.mission)) return updateRequired();
  return router.openGame(node.mission); // gameplay locks mission/hash at start
}
```
No map-renderer bypass. Router/backend revalidate as appropriate.

## Integration tasks
Use an additive adapter for Batch 4's existing MissionResult; never change its score rules just to fit a map. Keep `coconut-cove-001` as a 2-order mission; `coconut-cove-002` as authored. Shared normalized events can drive score UI, progression reducer and celebrations without DOM game engine coupling.

## Shipping discipline
Feature flags hide incomplete nodes. Every PR lists new schema versions and migration effects. Graph content additions must be accompanied by validator output and a published-mission reference. Visual changes must not alter eligibility. Manual UI testing is directed to owner. Only coordinator merges approved PRs; main requires explicit owner approval.
