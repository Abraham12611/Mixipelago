# 13 — Island Art, Landmarks, Visual Layers and Asset Production

## Art direction
Use Mixipelago's tropical casual-game mood but give each island distinct landmarks and a consistent material language. Avoid copying Merge Shooter screen compositions: invent bespoke piers, markets, colored cliffs, docks and architectural motifs. Prioritize geographic readability over particle density; a visually beautiful map that hides mission targets fails as navigation.

## Layer stack
`distant atmosphere → water/background → terrain → architecture → environmental props → mission edges → node markers → foreground framing → weather overlay (later) → DOM UI`. Each layer has a parallax factor or a fixed camera relationship; the *interactive node coordinate system* remains stable even when a cloud layer pans differently.

## Asset categories
- Island base/background chunks (pre-rendered illustrated 2.5D PNG/WebP/AVIF).
- Tile/scene props (boats, trees, market stalls, cafes, islands, cliffs, bridges).
- Landmarks with states `unrestored`, `restored`, `prestige` (future shops integration).
- Marker sprites (`available`, `locked`, `clear-1`, `clear-2`, `clear-3`, `treasure`, `gateway`, `secret`).
- Edge sprites/geometry (curved highlighted paths, dashed exploration routes, fog masks).
- Effect sprites/atlases (unlock pulse, sparkle, route lighting, milestone celebration).
- UI icons in actual vector where appropriate; localized text in React rather than baked into artwork.

## Production approach
Illustration concepts can originate from FLORA; selected 3D props from Tripo/Meshy and be normalized in Blender. Render with a fixed orthographic/isometric camera and locked palette so assets share scale and lighting. Capture source prompts, licenses, reference IDs, artist edits, versions and generated derivative paths in the asset manifest.

## Responsive scene design
Don't bake text, click targets, or node IDs into a giant background image. A single landscape image scaled to portrait often hides important areas. Compose map chunks with separate foreground/landmark layers. Define authored safe zones for labels and routes; inspect at mobile aspect ratios.

## Optimization
Use scene-specific bundles, atlases for repeated nodes, and only load nearby high-resolution chunks. Enforce texture budget and decode-memory checks; compressed download size is not the same as GPU memory. Favor WebGL compatibility and test texture dimensions and fallback formats on iOS Safari and Android browsers.

## Art acceptance
At typical mobile zoom, primary path and currently playable mission must be instantly recognizable. A player with reduced motion or color-vision differences must still distinguish states. Owners approve visual presentation and manual UI behavior; engineering tests verify asset manifests, missing references and draw performance.
