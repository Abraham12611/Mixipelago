# 11 — Desktop and Tablet Map UX

## Desktop composition
Make the map a readable, immersive center stage rather than a vertically stretched mobile view. Recommend a landscape map area with left island/district navigation, central pan/zoom canvas and optional right mission details panel. Keep game-level HUD and account controls outside the visual terrain so they remain stable across camera movements.

## Input conventions
- Mouse wheel zooms within map only when focused/hovered, bounded to avoid page-scroll hijacking; modifier or explicit zoom controls as needed.
- Left-click node selects; click and drag empty terrain pans. Space+drag is an optional power-user pan affordance.
- Keyboard: Tab through visible available/locked nodes; Enter opens node, Escape closes. Arrow-key directional focus can be added, but not at the cost of standard tab sequence.
- Trackpad gesture behavior must be tested on Mac and Windows; never assume wheel deltas have consistent scaling.
- Tablet landscape uses hybrid layout: map left or center; detail drawer overlays when width is constrained.

## Mission inspection
Desktop node hover can show a short tooltip (name, mode, stars) but hover is not required to reveal essential information. Clicking opens detail with objectives, requirements and rewards. The active mission stays visually prominent without distracting continuous particles.

## Browsing and wayfinding
Provide district filters, `Find Next`, a zoom-to-island button, optional quick jump list, and a breadcrumb like `Archipelago / Coconut Cove / Palm Boardwalk`. Recenter action should respect the player's existing zoom level when possible. The URL may encode selected island/node using shareable, non-sensitive IDs; private reward/unlock state is loaded from authorized session.

## Layout states
`loading`, `ready`, `offline_cached`, `empty_published`, `preview_only`, `node_selected`, `requirements_open`, `travel_confirm`, `download_failed`, `content_mismatch`. Handle all explicitly with non-blocking navigation and retry.

## Visual density rules
At wide view, show district silhouettes, progress badges and large landmarks; at medium view, show route nodes; at close view, show titles and fine decorative details. Collision/hit targets should be derived from the same camera transform used to render nodes. Keep decorative labels from hiding actionable nodes.

## Reuse policy
React components for cards, breadcrumbs, settings and progress should be shared with mobile; scene camera and component placement adapt independently. The map background itself can be Phaser-rendered while cards and accessibility list remain DOM-based. No physics bodies are needed in the world map scene.
