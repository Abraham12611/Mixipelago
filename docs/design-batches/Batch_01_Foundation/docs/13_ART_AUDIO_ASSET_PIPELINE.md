# 13 — Visual Art, Asset Generation, Animation, Music and SFX Pipeline

## Purpose

Create a distinctive, polished, **original** Mixipelago visual/audio library. The source screenshots demonstrate a genre/style reference—bright tropical palette, dimensional drinks, readable casual UI—but do not grant permission to use source assets. Generated concept screen images are not production assets: rebuild the interface with separately authored sprites, backgrounds, icons and React controls.

## 1. Visual direction

- Style: cheerful stylized 2.5D, dimensional/glossy objects, subtle warm lighting, soft shadows, legible rounded UI, bright lagoon accents.
- Less busy than the source imagery: avoid stacked gradients, flowers, thick outlines and giant brand banners on every game panel.
- Signature shapes: smoothly rounded objects, illustrated wood and woven materials, water/glass highlights, distinctive Mixipelago iconography.
- Cohesive character lineup without relying on red-haired reference-game heroine as a direct template.
- Each island has a distinct palette/audio signature; preserve shared UI controls across worlds.
- Nonalcoholic-looking tropical juices/mocktails should be the default theme so the game remains broad-audience. If alcoholic references are ever introduced, require age/rating and regional policy review.

## 2. Source tooling and roles

| Tool | Use | Notes |
|---|---|---|
| FLORA | Concept exploration, style reference systems, layered PNG assets, bulk variations | Production assets require review/correction |
| Tripo | 3D glass/building/prop concept generation | Inspect geometry/materials and output rights |
| Meshy | Alternative 3D generation and texturing | Benchmark against Tripo for usable meshes |
| Blender | Asset cleanup, lighting, camera, turntable/pre-render sprites | Preferred consistent orthographic render setup |
| Inkscape/Figma/vector editor | True SVG icons and UI vector construction | No raster renamed as SVG |
| Krita/Photoshop/etc. | Paintover, transparency cleanup, separations | Preserve master files |
| TexturePacker/atlas builder | Sprite atlas output | Consistent sampling/padding |
| ElevenLabs | Prototype SFX, character stingers, ambient/music exploration | Verify commercial rights and content policy |
| WeLoveIndies / SFX libraries | Licensed authored sound assets | Log asset license and attribution |
| DAW (Reaper/Audacity/etc.) | Editing, mastering, looping, loudness | Deliver clean stems and short one-shots |

Official/reference sites in `22`.

## 3. Asset taxonomy

`drink/icon/tierN`; `drink/board/tierN`; `drink/effect/mergeN`; `environment/table/<theme>`; `environment/island/<slug>`; `character/customer/<id>`; `ui/button/<type>`; `ui/icon/<id>`; `fx/<event>`; `audio/sfx/<event>`; `audio/music/<island>`; `audio/ambient/<island>`.

Assets should have a stable semantic ID independent of filename. A renamed asset should not break mission content if manifest ID is constant.

## 4. Real-time rendering choice

**Default:** pre-rendered 2.5D art in PNG/WebP/AVIF where supported, delivered as atlases. Key UI needs crisp vector/CSS components. Optional real 3D object only when gameplay benefits from user-controlled camera/rotation. Keep Glass art and physics footprint separate. Do not load 3D meshes for every glass when high-quality sprites suffice.

Drink asset example: render in Blender from fixed orthographic camera, consistent color temperature and perceived scale; output base RGBA, separate shadow/shine optional, merge sparkle overlays independent. On table, positions/rotations derive from Rapier; wobble/squash can be procedural and bounded.

## 5. Interaction states

For UI controls: use base image + CSS/GSAP or Phaser transform for hover, pressed, focus, disabled, awarded; render unique images only where substantial visual change is required. For characters, use curated face/pose states (idle, delighted, waiting) and keep silhouettes stable. Avoid generative AI producing unrelated shapes across animation frames.

## 6. Asset manifest example

```json
{
  "manifestVersion": "2026-11-14-alpha1",
  "items": {
    "drink.tier3.board": {
      "url": "/assets/drinks/tier3.9abc.webp",
      "width": 256,
      "height": 320,
      "pivot": [0.5, 0.88],
      "collisionFootprintRadius": 0.34,
      "checksum": "sha256:...",
      "licenseTag": "internal-original"
    }
  }
}
```

Separate physical dimensions from pixel sprite size. Every production asset must have `assetId`, creator/tool, source, usage rights, version, checksum, dimensions, target scene, and review status.

## 7. Initial v0.1 asset budget

- 8 original recognizable drink sprites (+ thumbnail variants from same masters).
- 1 tabletop background + simple side/background decor, 1 title background.
- 2–3 original customer portraits or silhouettes; can reuse stylized cards for alpha.
- ~8 foundational UI icons (play, pause, sound, score, coins, next, retry, settings).
- 2–3 small FX sprite sets (launch puff, collision glint, merge sparkle).
- 1 ambient loop + 1 music loop, 5–8 SFX: click, launch, clink, merge, order complete, win, lose, invalid.

Ship optimized placeholders if asset production threatens 72-hour build. Physics quality outranks visual flourish.

## 8. Texture and download budgets

Budget per scene and measure real RAM. Pack atlases at 1024 or 2048 texture dimensions as hardware allows; avoid 4K atlas on low-end devices without testing. Source PNG remains as original, deliver WebP/AVIF for standalone assets, atlases in supported format; KTX2/Basis if GPU compressed pipeline tested. 2048² RGBA can consume ~16MiB uncompressed even if file downloads compactly; account for mipmaps and duplicate copies. Texture unload when changing scenes; preload only current and likely next mission.

Aiming for initial compressed playable assets <~5–8MB is a *target*, not automatic gate without device measurement. Audio streams decode memory differently; measure peak. Cache versioned assets with hashed filenames and safe invalidation.

## 9. Sound system design

**AudioDirector** subscribes to game events, routes to effects/music/ambience buses with independent volume and mute, schedules combo layers and limits concurrent voices. Collision volume/pitch varies modestly with relative impact speed; avoid playing 40 clinks at once. Music fades between title, active play, win and other scenes; loop points checked manually. Respect `prefers-reduced-motion`, but audio needs independent mute.

Illustrative event mapping:

| Event | Sound | Visual |
|---|---|---|
| aim_begin | subtle UI tick (optional) | trajectory line |
| shot_fired | soft whoosh/splash | elastic launch motion |
| body_contact | velocity-weighted glass clink | tiny sparkle, bounded wobble |
| drink_merged | watery pop + ascending chime | scale/sparkles |
| combo_advanced | harmonized ascending stinger | colored ribbon/score |
| order_fulfilled | positive chord/coin | customer reaction, coin float |
| session_won | brief theme flourish | result overlay |
| session_lost | gentle falling cue | retry prompt, no punitive sound |

## 10. Production acceptance criteria

- Correct transparency, no visible white fringe; original subject; consistent camera and light.
- All assets have tracked licensing and provenance; AI outputs reviewed for prohibited similarities.
- Retina/high-DPI displays remain crisp at target size without uncontrolled texture growth.
- Audio is loop-safe, normalized, no harsh clipping; legal license verified.
- Character icon remains recognizable at 48 px; drink tiers distinguishable by more than hue alone.
- Full scene still readable with effects set to Low.
