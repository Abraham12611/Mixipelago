# 31 — Visual Production Briefs for Eight Core Drinks

## Global creative brief

Original Mixipelago art should be cheerful, crisp and distinct from source reference artwork. Preferred direction: rich 2.5D illustration with soft glass transparency, consistent 3/4 overhead camera, subtle contact shadows, clean rims and garnish that never hides collision centers. Premium casual-game polish with restrained highlights. Use the same key light direction and camera across every tier.

### Individual briefs

1. **Citrus Shot (t1):** stout, nearly circular amber juice tumbler with tiny citrus peel; smallest visual footprint but same collider footprint; designed to read instantly as base item.
2. **Sunny Lemon (t2):** taller golden lemon cooler, obvious lemon wheel rim and straight sides; distinct from t1 through height and citrus disk silhouette.
3. **Sunset Splash (t3):** sunset gradient red/orange layered tumbler, bright ice cubes and a curved blue straw; avoid making it a recolored t2.
4. **Blossom Fizz (t4):** pink soda with large hibiscus accent, fizzy bubbles and wider upper body; bloom must not cover other glasses.
5. **Coral Martini (t5):** red/coral wide coupe, long tapered stem and small fruit garnish; obvious silhouette in progression mini.
6. **Mint Lagoon (t6):** wide green lime/mocktail glass with mint leaves and frosty rim; high contrast against t4/t5.
7. **Ocean Cloud (t7):** tall turquoise-blue glass with rounded foamy crown and small cloud motif; soft highlights; avoid making foam look like a separate clickable object.
8. **Crown of the Isles (t8):** ornate signature goblet with restrained gold rim, tropical flower, tiny crown motif and iridescent ocean colors. Keep it elegant rather than overwhelming or too wide.

## Per-asset requirements

Every tier needs: transparent board sprite, 48px-readable HUD icon, order miniature, appropriate shadow placement/optical anchor, metadata (dimensions, author/source/license, art version), color-vision check and collision-footprint overlay screenshot. Optional only: alternate animations, showcase high-res version, seasonal skin preview.

## Asset acceptance matrix

- Recognizable in grayscale and against both wood table and light UI.
- No watermarks, illegible AI text, inconsistent garnish geometry or unintended human subjects.
- At screen-size 48px the silhouette is distinct from neighboring tiers.
- All files have consistent transparent padding, anchors and pixel-density policy.
- Sprite collider debug center aligns with perceived tabletop contact.
- Art licenses/provenance permit use in commercial web/native games.
- File sizes and atlas packing satisfy budget measured on actual target device.

## Production chain

Art director approves style tile → AI concept iterations or sketches → select one consistent glass design → generate controlled views/states from one source asset (Blender if useful) → clean pixels/alpha and color → create order/HUD crops → test in Phaser with real collisions → texture atlas and CDN manifest → owner visual approval → version stamp. Do not regenerate all tiers during each iteration without locking proportions and lighting.

## FX and audio coordination

T1–T3: small bubble/splash. T4–T6: richer sparkle + short chime. T7–T8: restrained prestige flare + special sonic accent. FX intensity is based on output tier/chain depth, but no tier changes physics behavior unless explicitly approved in a future ruleset. Respect reduced-motion and low-performance modes.
