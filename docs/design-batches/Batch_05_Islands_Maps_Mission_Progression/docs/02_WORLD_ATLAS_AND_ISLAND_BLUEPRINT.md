# 02 — World Atlas, Island Hierarchy and Expansion Blueprint

## Geographic hierarchy
`World → Archipelago → Island → District/Chapter → Route → Node`. **Island**, **chapter**, **route**, **node** and **mission** have independent IDs; never infer them from level number or display label. The map may show two geographically separated sections of the same island via separate chunks. A route is visual and navigational; prerequisites remain explicit and can cross routes.

## Conceptual world atlas (working titles)
| Island | Fantasy and purpose | Potential expansion range | First exposure |
|---|---|---:|---|
| Coconut Cove | Beach stand and foundational puzzle learning | 100–150 missions | First campaign region |
| Sunset Bay | Tourist districts and premium service | 120–180 | After Cove gateway |
| Mango Market | Commerce, routes and customer variety | 150–200 | Later |
| Coral Kingdom | Reefs and secret recipe exploration | 150–220 | Later |
| Stormhaven | Weather modifiers and resilience | 140–200 | Later |
| Neon Paradise | Night-time venues and tournament atmosphere | 180–250 | Later |
| Frostberry Peaks | Mountain drinks and temperature mechanics | 150–200 | Later |
| Golden Archipelago | Prestige, mastery and advanced optional content | 200–300 | Late game |
These ranges are world-building targets, **not an obligation to author 1,500 levels immediately**. The initial `v0.2.0` design target is 20–40 curated Coconut Cove nodes after sufficient mission content has been authored and solved.

## Island definition fields
An island has `islandId`, stable `slug`, `displayNameKey`, `themeId`, `musicSetId`, `worldBounds`, `districts`, `initialFocusNodeId`, `gatewayRules`, map chunks, asset bundle IDs, `contentVersion` and `status` (`draft|staged|published|retired`). Optional future references: shop plots, customer pools, event hooks, lore chapters, collectibles. The map loader ignores disabled optional systems.

## District anatomy
A district has a landmark and a learning promise. Example Coconut Cove districts: **First Steps Pier** teaches aim and first merge; **Palm Boardwalk** teaches orders and replay; **Reef Lookout** introduces forks, bank shots and hidden discoveries; **Harbor Gate** culminates in a gateway challenge. Every district should have a visible entry and exit, an obvious main route and at most a small number of newly introduced mechanics.

## Island expansion discipline
Use one island renderer, one graph evaluator, one map-control design and one mission engine. New islands should be mostly *content*: a set of map chunks, graph nodes/edges, decorations, themed audio, curated missions and configured encounters. Engineers should add a new island with data and assets, not a new hardcoded React route for every location.

## Geography versus mission order
Geographic proximity must not imply an unlock dependency. For instance, a scenic path can cross behind a mountain without giving access. Art expresses the graph; the graph is authoritative. Nodes may move visually during an art refresh, but stable IDs, prerequisites and completion receipts must not change unintentionally.

## Release posture
The full archipelago is a future content architecture. Initially show only authored, published and reachable content; future islands can be marketed with clearly labeled previews but must not masquerade as playable missions.
