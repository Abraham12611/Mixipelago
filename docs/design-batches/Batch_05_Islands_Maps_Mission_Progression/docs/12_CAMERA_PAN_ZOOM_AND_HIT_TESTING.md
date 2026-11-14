# 12 — Map Camera, Pan/Zoom, Hit Testing and Coordinates

## Independent coordinate spaces
1. **Map world coordinates:** float x/y values in stable authored units for nodes, landmarks and route control points.
2. **Screen pixels:** CSS pixel sizes after device pixel ratio and viewport.
3. **Phaser camera transform:** pan, zoom, content bounds and device safe-area offset.
Do not reuse the tabletop physics board's `10×15` world as island map coordinates. No Rapier step runs for panning a static map.

## Zoom and camera policy
Use a finite `zoomMin`/`zoomMax`, e.g., 0.65–2.4 as a *design starting point*, not a forced runtime constant. Clamp camera view to authored island bounds, with a modest scenic overscroll. On short screens ensure map not obscured by the UI bottom sheet. Persist last zoom and center per island separately from recommended next node.

## Pan interaction state machine
`idle → pointerDownPending → draggingMap → inertialSettle? → idle`. A pointer down over a node is still pending until movement exceeds the configured touch threshold; this prevents accidental node activation on pans. Pinch gesture suspends node tap and calculates zoom at finger centroid. Pointer capture/release ensures no stuck drag after browser loses focus.

## Hit testing
Project every visible interactive node's world anchor into screen space and use a generous circular/rounded tap footprint. For dense overlaps, prioritize modal context, selected node, currently available node, then closest center. Provide accessible list fallback so players are not blocked by overlapping pins.

## Map chunk streaming
Compute camera-visible rectangular world bounds with padding, request overlapping chunks and their level-of-detail texture sets, and unload distant *visual* chunks after a grace period. Keep lightweight node graph metadata resident so gate evaluation doesn't depend on image loading. Prefetch adjacent chunks when moving toward edge.

## Returning from gameplay
Store `lastSelectedNodeId`, `lastMapCamera` and `lastVisitedIslandId`; when mission is completed, compute next available node and offer camera focus transition. If player rejects auto-navigation, retain their manual position. If content version changed, map anchors are re-resolved by stable IDs.

## QA
At DPR 1, 2 and 3, verify node tap accuracy, consistent zoom, no double transforms, no sudden jump on orientation change, correct pan bounds, and smooth focus after opening/closing a detail sheet. Log slow camera draw and chunk loading separately from puzzle FPS.
