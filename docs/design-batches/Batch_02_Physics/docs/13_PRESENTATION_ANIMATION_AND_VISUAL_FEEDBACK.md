# 13 — 2.5D Glass Presentation, VFX and Interaction States

## Production approach

Use consistent high-quality **pre-rendered 3D-looking 2D sprites** for drinks, shadows, UI elements and splash effects. FLORA/image generation can create concepts; Tripo/Meshy + Blender can produce repeatable glass geometry and render views. Do not load a full 3D renderer for every glass unless a later benchmark proves the benefit. Images need stable pivots, collision footprints and color treatment across all tiers.

## Visual layers per glass

1. `contactShadow` — soft ellipse anchored at physics center with tiny offset; remains near table, not rotated with artwork.
2. `spriteBase` — drink/ice/garnish art; anchored at bottom-center/foot.
3. `highlight` — small specular/shine overlay, optional.
4. `liquidWobble` — cosmetic sway/scale/overlay; decoupled from physics rotation.
5. `selectionGlow` — only during active aim/hover or targeted help states.
6. `mergeFx` — particles/bright silhouette/intermediate gathering animation.
7. `statusIndicator` — reserved for order, danger warning, queued result, or tutorial.

Avoid applying physics angle directly to tall glass artwork if it makes the drink appear to lie on its side. Instead map small angular impulses to restrained horizontal wobble (suggest ±4–8 degrees maximum) with a spring decay, and perhaps subtle liquid slosh. The real body's circular angle may be recorded for replay but visual yaw/tilt may be intentionally bounded. This should be declared so simulation and image aren't misleading.

## Interaction states

| State | Visual treatment | Trigger | Must not affect |
|---|---|---|---|
| Idle | soft contact shadow, occasional gentle shine | stable active drink | physics body |
| Aiming | preview ray, subtle shooter halo | input aiming | score/queue |
| Launched | brief trail, body follows Rapier | accepted launch | velocity independently |
| Contact light | tiny glass jiggle, small SFX | collision below medium threshold | merge eligibility |
| Contact heavy | slightly stronger wobble and impact sparkle | higher relative speed | collision resolution |
| Merging | both inputs gather to anchor, scale/fade, next-tier flash | committed merge event | extra rewards |
| Chain merge | scaled glow/chime on depth 2+ | connected merge ancestry | order mutation |
| Auto-served | result briefly highlights, arcs to customer bubble | server/session rule says served | serving twice |
| Danger | dashed line pulse and object outline | rule-level warning | physical collision |
| Pause | board freeze + overlay | session pause | step index |
| Victory | celebratory FX, summary | terminal win | further gameplay mutation |

## Merge FX choreography (proposal)

`0ms`: merge already committed logically; input sprite transforms become render-only ghost instances. `0–70ms`: both ghost sprites move a small distance toward anchor and shrink; `70–120ms`: a quick luminous splash and particle burst; `120–180ms`: upgraded sprite scales from 0.6 to 1.08 to 1.0 with highlight; auto-serve indicator appears afterward if applicable. These are suggested durations, not tested values. Prefer that physical result is active in simulation immediately or after an explicit rule-based arming window; never hide an active collider in an unexpected place for a long animation.

## Chain FX choreography

Depth 1 = standard soft pop; depth 2 = secondary sparkle and rising musical accent; depth 3–4 = stronger glow/score label but still readable; depth 5+ = rare hero moment, small slow-motion **presentation-only** effect if it doesn't change game physics/timers. Avoid 3-second mandatory interrupt sequences on frequent combos.

## Asset packaging

Each item has stable IDs: `drink.t1.default`, `drink.t1.highlight`, `fx.merge.base`, `fx.merge.combo2`, `shadow.drink.base`. Export correct premultiplied/nonpremultiplied alpha setting for Phaser; maintain a transparent export. Sprite atlas packing should avoid edge bleed with sufficient padding/extrusion. Use source resolutions sufficient for a high-DPI screen but avoid massive GPU memory. Prefer atlas sets per island/level and lazy load variants.

## Particle system

Small VFX: 4–12 particles for contact, 10–28 for ordinary merge, 25–45 for a large chain; these are proposed limits. Reuse emitters or pooled particles. Disable nonessential particles on low-quality mode and reduced-motion. FX always anchored in *world* coordinates, transformed by same camera as drink, not absolute DOM pixels.

## Visual quality and readability

- Preserve distinct silhouettes and color separation between adjacent drink tiers.
- Avoid red/green-only differentiation; garnish shape and glass form identify tier.
- Keep launch target/next tier visible at all times.
- Avoid customers/score popups obscuring active collisions.
- Keep score/status text as crisp DOM/React when that improves accessibility.
- Shadows and sparkles shouldn't resemble additional draggable drinks.

## Performance considerations

Preload only current mission drink chain, background and active FX. Defer remote islands. Keep all sprite texture dimensions known and inspect decoded memory cost. Compress static backgrounds appropriately; use GPU-compressed textures only when actual deployment pipeline and target devices support them. Pool FX instances; do not allocate hundreds of new display objects during each chain. Profile shader/filter costs on mobile Safari.

## Test/approval

Compare visuals with and without FX to ensure physics trajectory is identical. Verify no invisible collider after sprite disposal. Owner manual test confirms impact visually communicates contact angle and strength without inducing sickness or obscuring gameplay. Screenshots are design reference, not a source to crop into production assets.
