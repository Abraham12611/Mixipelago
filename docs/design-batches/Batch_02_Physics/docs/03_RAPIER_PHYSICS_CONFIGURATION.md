# 03 — Rapier 2D Physics Setup, Parameters, and Material Semantics

## Decision

Use `@dimforge/rapier2d-compat` as a **proposed v0.1.0** implementation for bundler simplicity, evaluated against the pinned WASM build. For future ranked verification, evaluate `@dimforge/rapier2d-deterministic-compat` (or its supported equivalent) and assess size/performance tradeoffs; the exact build flavor becomes part of the replay version contract. Phaser 4 owns rendering/input, not these bodies. Simulation gravity is `(0,0)`. We simulate a glass's tabletop footprint (circle), not fluid or full glassware. One world is created per session and disposed on exit; no Rapier world or handle escapes to React state.

## Step system

- `STEP_HZ = 60`, `dt = 1 / 60`. Set Rapier's world timestep to the same constant (`world.timestep` in supported APIs, or version-equivalent parameter). Never set `dt = frameElapsed`.
- The accumulator advances 0–5 fixed steps per rendered frame; when the tab is hidden, pause and clear accumulated time.
- CCD is enabled for launched high-speed drinks; a whole-scene CCD policy can be tuned later. Confirm CCD behavior at fixed stepping against rails and tightly packed bodies.
- Prefer default Rapier solver iteration count initially. Increase only if stacked-contact instability is actually measured; extra iterations cost CPU.
- Do not invent Rapier API signatures. The compatibility wrapper is tested and version-pinned in the implementation spike.

## Configuration manifest (hypotheses, not measurements)

| Key | Proposed alpha default | Allowed lab range | Description / warning |
|---|---:|---:|---|
| `stepHz` | 60 | 60 or 120 for experiments | Fixed simulation steps per second |
| `worldWidth` | 10 | 8–14 | Logical playable width |
| `worldHeight` | 15 | 12–18 | Logical playable height |
| `drinkRadius` | 0.34 | 0.25–0.55 | Circle collider footprint |
| `drinkDensity` | 1.0 | 0.5–3.0 | Positive mass derived from collider density; don't combine ambiguous mass setters |
| `linearDamping` | 0.12 | 0.02–0.65 | Global drag proxy / slows glide |
| `angularDamping` | 0.65 | 0.1–2.0 | Suppresses indefinite spin |
| `friction` | 0.06 | 0–0.5 | Tangential contact resistance, not tabletop drag |
| `restitution` | 0.38 | 0–0.85 | Contact elasticity/bounce |
| `launchImpulse` | 4.5 | 2–9 | Magnitude in engine-world units, not pixels |
| `maxSpeed` | 10 | 6–20 | Optional cap to prevent runaway state |
| `dangerLineY` | 12.8 | configured per board | Lower gameplay pressure threshold |
| `dangerGraceMs` | 850 | 400–1500 | Time spent violating line before loss |
| `mergeFxMs` | 180 | 100–350 | *Presentation* delay; physics consequences are immediate after safe boundary |
| `minAimDragWorld` | 0.25 | 0.1–0.5 | Dead-zone guard against accidental tap |
| `launchCooldownSteps` | 24 | 0–90 | Prevent immediate spam; may be superseded by settle criterion |
| `settleSpeed` | 0.08 | 0.02–0.2 | Candidate idle threshold, only if used |

**Important:** The arbitrary demo value `drinkDensity=1` is not a real kilogram statement; world units are designer-scaled. Document dimensions and tune coherently so collision solver tolerances stay in a reasonable range. A top-down board should use sensible physical scales rather than pixel-as-meter assumptions.

## Distinguish drag, friction, restitution

- **Linear damping** reduces motion between collisions even with no physical tabletop collider. It creates the impression of smooth ice that *eventually* stops. Rapier's damping integrator is its own internal model; avoid claiming an exact `e^-kt` analytic law unless validated.
- **Collider friction** resists relative tangential slip **during contact** (e.g., glancing blows between glasses or wall slides). A zero-friction contact still exchanges normal momentum.
- **Restitution** controls the normal bounce after impact. `0` is inelastic; `1` approximately elastic under suitable conditions.
- **Friction/restitution combine rules** affect pairs with different materials. For the alpha use the *same* glass coefficients and explicit rules. If later surfaces have variants, define combining policy in material manifest; do not depend on a default that changes unnoticed during upgrades.
- **Linear/angular damping are independent**. Rotational artistry can be done in sprites even if actual circle torque is weak.

Official background: https://rapier.rs/docs/user_guides/javascript/colliders/ , https://rapier.rs/docs/user_guides/javascript/rigid_bodies/ , https://rapier.rs/docs/user_guides/javascript/integration_parameters/ .

## Body creation blueprint

```ts
// Illustrative; verify against pinned @dimforge/rapier2d-compat declarations.
const desc = RAPIER.RigidBodyDesc.dynamic()
  .setTranslation(spawn.x, spawn.y)
  .setLinearDamping(config.linearDamping)
  .setAngularDamping(config.angularDamping)
  .setCcdEnabled(config.enableCcd);
const body = world.createRigidBody(desc);
const shape = RAPIER.ColliderDesc.ball(config.drinkRadius)
  .setDensity(config.drinkDensity)
  .setRestitution(config.restitution)
  .setFriction(config.friction)
  .setActiveEvents(RAPIER.ActiveEvents.COLLISION_EVENTS);
const collider = world.createCollider(shape, body);
body.applyImpulse({x: aim.x*impulse, y: aim.y*impulse}, true);
```

Note: launch body creation and impulse application **must happen at the fixed-step command boundary**, not in an asynchronous render callback. The collider's intended radius corresponds to the drink *base* footprint. The visual glass can be larger without a larger collider.

## Walls and launch boundary

Side and top rails are static Rapier colliders, defined in world coordinates, with a tuned restitution separate from glass-to-glass material. The lower playfield has a visual dashed danger line; it is *not* a collision wall in v0.1.0. Spawn position is protected during initial shot arming and should not count as overflow until the drink has entered the playable zone.

Walls should not be so thin that fast bodies tunnel; use sufficient static collider thickness, CCD on moving drinks and automated high-speed tests. The target should never be physically impossible: allow a newly spawned result to fit within bounds by applying a bounded placement correction or re-evaluating the merge anchor.

## Mass policy and item tiers

Alpha uses equal radii and densities for all eight tiers. This makes shot outcomes legible and prevents higher-tier drinks from pushing lower-tier ones in unexpected ways. Tier-dependent masses/radii are **experiments** only; they require rebalancing spawn counts, collision chains, crowding and replay baselines. If tier-8 art is visually 2× taller, the foot collider remains the alpha radius.

## Safe solver practices

Do not teleport dynamic bodies directly into other active colliders while effects are playing. When spawning a merged result, place at a resolved midpoint, choose a legal non-overlapping position deterministically, and clamp inherited velocities. Do not set zero mass. Never mutate bodies while iterating the collision queue; stage operations and commit safely after draining contact events.

## Benchmark requirements

For 1, 10, 20, 35, 50 active glasses, measure median, p95 and worst-case simulation step time on desktop and representative Android/iOS devices; measure overlapping-pair count and memory. Track active bodies and accumulated contacts. Do not enable expensive contact-force events on every object unless impact sounds need measured impulses; compare with relative-speed approximation.

## References and known nuance

Rapier's WebAssembly/JavaScript build documents cross-platform determinism under **identical conditions and ordering**. Our *application* replay still needs canonical inputs, seeded PRNG, identical object insertion order, and stable code/config; browser-generated input and non-deterministic JS math can break those conditions. See `17` for precise threat model.
