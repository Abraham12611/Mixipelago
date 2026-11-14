# 20 — Island Biomes and Mission Theme Integration (Overview)

## Separation of concerns
Map biome affects scenery, audio, navigation and which themed mission presets are offered. It must **not** directly mutate Rapier friction or mission scoring merely because a node lives in a rainy or icy island. A mission may explicitly pin a `boardPresetId` or a future `surfaceModifierId`, validated under Batch 4.

## Example biome bundles
- Coconut Cove: sunlit sandy beach, palms, wood and coral accents; relaxed music.
- Sunset Bay: sunsets, hotels, boardwalk lanterns, tourism ambience.
- Mango Market: bright plazas, crates, colorful awnings and merchant motifs.
- Coral Kingdom: reefs, aquamarine lighting, glowing shells and watery atmosphere.
- Stormhaven: distant thunderstorms, protected docks, rain visual overlays.
- Neon Paradise: illuminated signage, nightlife music and festive skyline.
- Frostberry Peaks: snowy rock terraces, cooler palette, warm indoor venues.
- Golden Archipelago: gilded architecture and late-game spectacle.

## Mission linkage
`CampaignNode.themeOverrideId?` → `MissionDefinition.visualThemeId` resolves a compatible scene theme. The mission's real physics and spawn are always specified in immutable mission content. Theme and map renderer can read a lightweight `biomeId` to select art/music; gameplay never looks up biome geometry to guess its physics rules.

## Future special world conditions
Temporary rain, storms, wind, low tourism or festival celebrations belong in Batches 10–12. They produce explicit, versioned **event modifiers**, which can optionally unlock authored special puzzle missions. Keep them feature-gated and avoid changing player's already pinned active session.

## Quality and budget
A different color palette alone is not a new biome. Each island needs recognizable silhouettes, landmark language and sound identity. Large background imagery should be chunked and cached based on camera; do not load every future island at app startup.
