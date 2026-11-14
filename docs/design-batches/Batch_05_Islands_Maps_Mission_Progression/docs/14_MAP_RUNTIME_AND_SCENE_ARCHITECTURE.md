# 14 — Map Runtime, Phaser Scene Composition and React Shell

## High-level architecture
`CampaignService` returns authorized map projection and a content manifest; `WorldMapScene` renders terrain, edges and nodes; `MapInputController` translates touch/mouse; `ReactMapShell` renders HUD/cards/navigation; `GameRouter` transitions to the separate gameplay scene. There is **no** need for physics simulation in the map itself.

## Proposed modules
```
packages/campaign-core/
  graph.ts  unlock-evaluator.ts  projection.ts  next-mission.ts
packages/map-renderer/
  world-map-scene.ts  map-camera.ts  chunk-manager.ts
  node-renderer.ts  edge-renderer.ts  hit-test.ts
apps/web/components/campaign/
  map-hud.tsx  mission-sheet.tsx  requirements.tsx
  island-select.tsx  accessible-node-list.tsx
```

## Scene lifecycle
`bootstrap → loadGraphMetadata → deriveNodeProjection → streamVisibleAssets → ready`. On node selection, React consumes a serializable `SelectedNodeViewModel`, not a direct Phaser display-object reference. On `Play`, router validates supported mission + player eligibility, loads pinned mission bundle, and swaps to the gameplay runtime.

## State synchronization
Maintain one campaign store as immutable values; avoid making Phaser scene mutable state the source of truth for which nodes are unlocked. Scene subscribes to projection changes and reconciles marker appearances. UI can update optimistically in local preview mode; server-authoritative mode must reconcile after a valid receipt.

## Network loss
If a published map manifest is already cached, display it and local-progress badges with offline labeling. If player has no trusted eligibility proof for a valuable unlock, disable claims and show retry. A failed visual chunk request must not delete graph state or blank the entire app.

## Deep links
`/map?island=coconut-cove&node=cove-n002` can open a selection when permitted. Unsupported/hidden node IDs should resolve to a neutral island map and a generic notice, not leak hidden content or reveal private player state. Preserve scroll/camera only in client state.

## Map version handling
Resolve node rendering from `mapLayoutVersion`, gate evaluation from `graphVersion`, and mission runtime from `missionVersion`; never equate them. A layout-only hotfix changes marker positions but not player unlocks. A gate change needs graph revision and compatibility review.

## Failure containment
A map crash must not corrupt a pinned in-progress puzzle. Keep session snapshot isolated. Component error boundary allows reloading the map or switching to accessible node-list mode.
