# 16 — Board Geometry, Obstacles, Hazards and Surface Material Variants

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Core board contract
Physics world is independent of device pixels. Logical board uses [0,width] × [0,height]; typical alpha width 10 and height 15; danger line y=12.8; circular colliders with initial nominal radius 0.34. Phaser camera maps this to responsive display. Static boundaries are Rapier colliders; the dashed danger line is a **logical zone**, not a physical wall.

## Layout taxonomy
- `open_standard`: unobstructed tabletop; alpha baseline.
- `narrow_channel`: central divider with bank-shot alternatives; later.
- `islands`: static fixtures create multiple pockets; later.
- `split_launch`: two launch zones with independent cooldown; experimental.
- `spiral_rails`: decorative curved rails approximated by safe static segments; later.
- `movable_obstacle`: dynamic barriers or bumpers with explicit fixed-step motion; later, requires deterministic movement and accessibility test.

## Surface physics differentiation
**Important:** a low-friction look is primarily controlled by linear damping; contact friction is not the same as drag. For later missions, `surfaceZone` may define `dampingMultiplier` or `impulseModifier`, but Rapier body linear damping is set globally on a body, so per-zone changes must be driven by a deterministic zone controller at fixed tick boundaries. No frame-dependent accelerations or overlapping hidden modifiers.

| Material | Proposed visual cue | Intended decision | Status |
|---|---|---|---|
| `standard_glide` | warm wood, soft shine | baseline bounce/merge | alpha |
| `polished_ice` | pale blue reflection | longer coast | future |
| `sticky_patch` | rough mat/puddle texture | stop/redirect bodies | future |
| `bumper` | colored raised rail | bank shots | future |
| `conveyor` | arrow strip | alter object movement | far future |
| `fragile_rail` | cracked outlined section | one-time obstacle break | far future |

## Obstacle interface
Each obstacle has stable `id`, `shape` (box, capsule, circle, polyline/convex), `pose`, `materialId`, `isStatic`, `collidesWith`, `visualAssetId`, `releaseStatus`. Arbitrary user-generated SVG geometry must not become collider directly. Offline build tool validates nonpenetrating initial layout and collider stability.

## Hazards
- `danger_line`: spatial failure zone with configured grace; existing canonical behavior.
- `blocked_launcher`: body occupies shooter space; reject launch without consuming queue.
- `timed_gate`: a moving rail opened/closed on scheduled ticks; later.
- `spill_zone`: an authored slowing region; later.
- `no_merge_zone`: **not recommended initially**; violates intuitive same-tier contact rules, would require strong telegraphing.

## Rule transparency
At level preview show new materials/obstacles and their behavior. Never surprise player by silently altering collision radius or restitution mid-session. Future skill perks may affect campaign moves only within bounded, explained modifiers and not standardized ranked boards.

## Technical acceptance
Boundary dimensions same across phones; no hidden invisible physical clipping; high-speed CCD where needed; no body trapping outside reachable field; no spawn inside barrier; hazard visual animation doesn't modify physics; fallback assets preserve collision telegraphing; performance profiling with max obstacle count.
