# 27 — Performance Budgets, Map Streaming and Offline Delivery

## Why campaign performance is different
The map may have hundreds of decorative sprites but near-zero moving rigid bodies. CPU pressure comes from graph projection, UI and scene management; GPU/memory pressure comes from large terrain textures. Do not create thousands of inactive Phaser objects for distant missions.

## Load phases
1. Fetch lightweight current graph header, island selection and manifest hashes.
2. Load minimum assets for visible map viewport and selection card.
3. Render reachable nodes while remaining island imagery streams.
4. Prefetch adjacent chunks and currently recommended mission assets.
5. Defer other islands and high-resolution decorations until travel.

## Budgets (starting targets, require measurement)
Map interaction should reach useful state quickly on mid-range mobile; aim for 60 FPS while panning, with smooth 30 FPS on low-tier fallback. Keep graph metadata comfortably small (e.g., thousands of node records are fine), and avoid huge single decoded atlases. Track peak texture memory and largest chunk—not just downloaded bytes.

## Implementation hints
Spatial index or chunk-grid lookup for visible nodes; memoize eligibility projection by `(graphHash, progressRevision)`; update only markers whose state changed. Use fixed-resolution map background tiles where possible, WebP/AVIF with fallback; atlas common icons and avoid duplicate texture loads.

## Scene lifecycle
When leaving map for gameplay, release nonessential high-resolution map textures if memory constrained. Keep graph metadata and a small thumbnail cached for immediate return. On app resume, check context loss and reload textures safely without resetting campaign state.

## Offline behavior
A service worker/PWA can cache static graph + artwork for previously visited islands. Offline local-preview campaign can launch compatible cached missions; server-verified rewards and chests require connectivity unless a future signed offline entitlement protocol is explicitly designed. Display offline limitations clearly.

## Testing matrix
Safari iOS low-memory background/resume, Android Chrome midrange, desktop Chrome/Safari, browser zoom, large DPR, slow 3G-like simulation, cache eviction, CDN 404, corrupt atlas, context loss, orientation switching, rapid repeated island transitions.
