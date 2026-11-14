# 13 — Drink Art, Rendering, Animation and Audio Asset Specification

## Desired aesthetic

Mixipelago art is polished, buoyant 2.5D tropical stylization: colorful but not crowded, dimensional glass shapes, consistent light source, clear item silhouettes, understated shadows, and restrained flourishes on premium-tier drinks. Screenshots of Merge Shooter are *genre references*, not content to duplicate. All original drink forms, naming, branding and textures must be independently produced and rights-cleared.

## Production asset layers

| Layer | Asset/rendering method | Requirements |
|---|---|---|
| Board glass sprite | Pre-rendered transparent WebP/PNG or atlas texture | Identical camera/light perspective for all tiers |
| HUD/order miniature | Separate crop or dedicated icon | Sharp at 32–48 CSS px |
| Contact shadow | Shared sprite/ellipse shader | Align with physics footprint, not garnish extent |
| Drink liquid | Baked artwork for alpha | Optional subtle procedural shimmer later |
| Travel tilt/wobble | Renderer transform only | Never changes collider shape |
| Merge flash | Particle/sprite sequence | Under ~250ms primary flash; skippable/reduced motion |
| Recipe discovery reveal | Card and silhouette layers | Future; supports skip and localization |
| Collection showcase | High-res layered render | Deferred until album launches |

## Art brief for eight tiers

Refer to 03. Tier silhouette progression should be legible through geometry: squat tumbler → tall lemon glass → layered tumbler → floral soda → coupe → green frosty margarita → taller blue foam drink → ornate tall crowned signature. Don't build all drinks as the same glass with a color swap. Avoid dense toppings that cover neighbors or misleading perspective sizes.

## File and manifest conventions

Example asset ID: `drink.core.t03.board.v001`; path `assets/drinks/core/t03/board@2x.webp`. Provide 1x/2x resolutions; avoid making every 4K art asset part of the initial gameplay bundle. Asset manifest maps logical ID -> file URL, dimensions, optical center, collider anchor (normalized), pixel density, checksum, content license and source brief.

A physical collider is defined in world units and rendered with separately calibrated pixels-per-world-unit. A garnish may protrude beyond its physical base; shadow and collision debug circle must align with the portion on the table that appears to contact other glasses.

## AI-assisted workflow

Create style bible and strict reusable reference before generation; optionally use FLORA for concept/state variations and Tripo/Meshy/Blender for consistent model renderings. Batch-check: camera angle, palette, border thickness, shadow direction, level of detail, transparency, anatomy of glass rim, unwanted text/watermarks, licensed provenance, consistent anchor and scale. Approve *individual assets* rather than automatically treating a generated mockup as production-ready.

A robust approach for multi-state variations is to render a **single 3D glass** to multiple controlled frames so its shape and label never mutate across states. Use shader/transform effects for hover and click where possible; generate separate images only if artwork changes materially.

## Audio event mapping

`launch` -> soft whoosh/glass slide; `contact` -> speed-sensitive clink with throttling; `merge` -> tier-specific watery pop+chime; `chain_depth_2+` -> musical escalation; `order_served` -> quick tick/swish; `order_fulfilled` -> reward sting; `tier_first_created` -> optional discovery accent only if valid/eligible.

Audio Director gets event ID and volume/intensity, not a mutable wallet reference. Prioritize major feedback over continuous clinks; cap simultaneous voices and apply pitch variation in bounded ranges, independent from PRNG gameplay. Respect muted tab, autoplay restrictions, music/SFX separation, reduced effects, and performance quality presets.

## Optimization

Use scene-specific atlases rather than one monolithic texture; prioritize WebP/AVIF where supported with PNG fallback as needed; pack with transparent padding to avoid texture bleeding. Asset loader prefetches the eight gameplay tier icons and only the visible customer portraits. Offscreen island/album art should load on navigation. Validate memory on actual low-end phones, not only desktop DevTools emulation.

## Definition of done

Eight approved silhouettes, manifest entries, fallback sprites, calibrated anchors, mini icons, start/impact/merge assets, reduced-motion behavior, mobile performance budgets, audio volume hierarchy, and a repeatable source-to-export production script. Each entry has an owner and licensing note. Future deep dive belongs to Batches 16–17.
