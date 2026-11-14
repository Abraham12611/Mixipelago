# 10 — Mobile Map UX, Information Architecture and Interaction States

## Experience priorities
Mobile is a first-class map, not desktop shrunk vertically. Portrait experience should emphasize a vertically navigable district near the current mission, with enough nearby context to understand the path. The user must always find the current recommended node quickly and should never need precise multi-finger gestures to progress.

## Screen anatomy
1. **Top HUD:** small island title/level, preview-only coin label where relevant, settings/profile entry, network/sync state when applicable.
2. **Main map canvas:** illustrated terrain, accessible node targets, route connections, compact landmark labels; camera controlled by player.
3. **Contextual node card:** mission title, mode label, objective summary, best stars, rewards, requirements, `Play` or `See Requirements`.
4. **Floating `Next` action:** recenter to recommended available mission; persists even when user zooms far away.
5. **Bottom navigation:** Map, Shop, Events, Leaderboard slots appear only when respective features exist; disabled future screens must be clearly labeled, not dead links.

## Primary touch gestures
Single-finger drag pans the map unless the gesture starts on a node and has not exceeded movement threshold. Tap a node opens detail; tap outside closes detail. Two-finger pinch zooms around gesture centroid; double-tap can optionally zoom, but no required function may rely on double-tap. Releasing a pan should stop predictably; inertia is a visual preference and respects reduced-motion.

## Touch targets and overlays
Aim for practical 44–48 CSS px target boxes at standard zoom even if the illustration's visible circle is smaller. Nodes must be hit-tested in screen space, with overlapping targets deconflicted by current context and z-order. Bottom sheets should not cover the selected node; camera can pan the node into remaining visible area. Respect `env(safe-area-inset-*)` on notched screens.

## Node cards
An available mission card shows `Mission 12`, player-understandable name, gameplay mode, clear objective, stars, one primary `Play` button, optional `Replay` on cleared nodes and optional `Back to Map`. Locked state shows **exact** missing prerequisite with a `Go to Requirement` action. Secret nodes must not leak names before reveal. Unpublished nodes should not have a functioning Play button.

## Motion and progression celebration
After a clear: animate the filled stars and path opening once, but store unlock first. If the animation is interrupted by browser backgrounding, reopening the map shows correct stable state. Reduced motion uses fade and direct state changes without camera swoops.

## Accessibility fallback
Provide an accessible DOM mission list/route navigator, keyboard tab focus and screen-reader labels (`Mission 12, available, Classic Service, best two stars`). Phaser canvas alone does not guarantee accessible navigation. Include an option to switch from map to list mode.

## Manual user acceptance scenarios
Owner tests on narrow Android portrait, iPhone Safari with safe area, landscape phone, small tablet: pan vs tap disambiguation, zoom, tooltip overlap, orientation changes, locked requirement clarity, returning from gameplay, and map state restored after tab suspension.
