# 04 — Gameplay Simulation & Physics Specification

**Priority:** P0. This is the product's critical-path engineering design.  
**Proposed engine:** Phaser 4 (render/input/scenes) + Rapier 2D WASM (rigid bodies, contacts). Test against Matter.js only if integration/performance requires an alternative. See official links in `22`.

## 1. Desired feel

- Glasses glide as though on an almost frictionless wooden tabletop (a stylized icy-smooth surface), but eventually settle.
- Collisions are responsive to approach angle, current velocity, body mass and contact geometry.
- Different-tier drinks collide physically but do **not** merge.
- Same-tier drinks merge once; new upgraded object inherits momentum or receives a carefully tuned bounded impulse.
- Shot positioning and aim matter; chain reactions create mastery.
- Visual glass appearance may be tall/2.5D while physics uses an invisible 2D footprint.
- Controls feel direct at both 30 FPS render fallback and 60 FPS render target.

## 2. Coordinate and rendering model

World: 2D horizontal plane. No planar gravity. Physics unit convention: 1 world unit = nominal table-unit; define `WORLD_WIDTH`, `WORLD_HEIGHT` from level config. Physics origin = upper-left; X right, Y down. Rendering maps world-to-canvas by an affine camera transform. **No pixel-coordinate dependencies in simulation.**

Use circular colliders initially. Glasses visually face upward, with contact point represented by collider center/footprint. Highly irregular collectibles may get a convex/compound collider in a future version only when user testing demonstrates value. Never use AI-generated alpha mask pixels as collision geometry.

Renderer position follows physics body; smooth render interpolation is allowed, but input and scoring only read authoritative simulation positions. Drop shadow can lag/stretch cosmetically; it must not modify collision state.

## 3. Recommended runtime boundaries

```
UI (React) → GameShell command → InputController (Phaser)
 → LaunchCommand → SimulationCore (Rapier + merge rules)
 → Simulation events → Phaser visual systems + AudioDirector
 → SessionReducer (orders/score/win-fail)
 → Session snapshot / results → React UI
```

- `SimulationCore` owns active bodies, collider mappings and step timing.
- `InputController` owns pointer state and converts screen coordinates to world launch direction.
- `MergeResolver` owns tier eligibility and pair deduplication.
- `GameDirector` owns spawn queue and round objectives.
- `EffectsDirector` consumes read-only presentation events.
- `SessionStore` owns latest durable local save.

## 4. Frame timing

Choose fixed simulation step: **1/60 sec**. Render as often as environment permits, interpolating between snapshots. Clamp frame delta after tab suspension and cap catch-up steps (e.g., 4–5); never fast-forward an accumulated minute of physics after the tab resumes. On `visibilitychange → hidden`, pause simulation and save a safe snapshot/result state. Resume gracefully on visibility.

Illustrative loop (API may be adapted to the engine):

```ts
const STEP = 1 / 60;
let accumulator = 0;
function update(deltaSeconds: number) {
  accumulator += Math.min(deltaSeconds, 0.1);
  let steps = 0;
  while (accumulator >= STEP && steps < 5) {
    simulation.step(STEP);
    accumulator -= STEP;
    steps++;
  }
  if (steps === 5 && accumulator >= STEP) accumulator = 0;
  renderer.interpolate(accumulator / STEP);
}
```

Rapier integration requires setting the world integration timestep appropriately; do not modify `dt` per render frame. Store simulation version and level content version on every run.

## 5. Physics parameter manifest

Start with a *tunable config*, not scattered constants. Values are starting hypotheses, not final verified game feel.

```json
{
  "physicsVersion": "alpha-1",
  "stepHz": 60,
  "gravity": [0, 0],
  "worldBounds": [0, 0, 10, 15],
  "drinkRadius": 0.34,
  "massKgLikeUnits": 1,
  "linearDamping": 0.12,
  "angularDamping": 0.65,
  "contactFriction": 0.06,
  "restitution": 0.38,
  "launchImpulse": 4.5,
  "maxLinearSpeed": 10,
  "mergeEffectDurationMs": 180,
  "collisionSoundThreshold": 0.25,
  "dangerLineY": 12.8,
  "dangerGraceMs": 850,
  "enableCcd": true
}
```

**Interpretation:** `linearDamping` approximates tabletop drag; `contactFriction` applies tangential collision resistance; `restitution` sets normal bounciness. A perfectly zero-damping system never settles naturally, so the game needs a small damping, sleep thresholds and safe board pressure mechanics.

Tune via `/dev/physics-lab` (non-production or admin-protected): sliders for launch strength, damping, restitution, friction, mass, collider radius, merge attraction, wall behavior, body count, spawn queue and fixed Hz. Export JSON presets for review.

## 6. Pointer and touch input contract

1. Touch/click begins inside launch-zone; pointer ID captured to avoid multitouch corruption.
2. Drag direction and distance compute aim vector + optional power. Design choice for v0.1: **drag from launch point toward desired destination and release**, with constant force initially. Future variable power gated behind testing.
3. Clamp angle to acceptable launch cone (e.g. no back-shot below lower boundary).
4. Show light trajectory preview while aiming; do not falsely promise a perfect collision path when objects move.
5. Cancel on pointer leaving viewport, second touch interruption, Escape, overlay activation, or distance below dead zone.
6. On valid release: consume exactly one next item, fire `shot_fired`, apply an impulse to body.
7. Disable another shot while state `launched/resolving` until short settle/cooldown rule; avoid input queuing unpredictability.
8. Convert DOM pointer to canvas/world using active scale and letterbox offsets; never use CSS pixels as world units.
9. On keyboard: optional Left/Right aim + Space/Enter launch; Escape pause.

On pointer move, `preventDefault` only on the canvas and set `touch-action: none` there; preserve page scrolling elsewhere.

## 7. Body and collider lifecycle

`drink_spawned`: allocate unique `objectId`, tier, origin, body handle, collider handle, visual sprite, session ID. Maintain both `objectId → object` and `colliderHandle → objectId`. Use object pooling for sprites but **not** reusing a still-live collider handle before physics state has finished reading collision events.

Movement: apply impulse, step world, read pose, update sprite. Inactive/sleeping bodies remain eligible for collisions and merges.

Merge: mark both inputs as `merging` in a single decision before removal. Remove colliders at a safe point **outside** event queue iteration; spawn result at mass-weighted midpoint or resolved contact center, clamp inside world, inherit bounded velocity. Emit `drink_merged`, `drink_spawned` with a causation ID. Destroy or release visuals after FX.

## 8. Merge eligibility and conflict priority

Eligibility for alpha: both objects in `active`, same tier, tier < `maxTier`, not flagged as `reserved_for_order`, and allowed by mission config. Later specialized recipes may use different compatibility rules, but alpha stays simple.

For a physics step with multiple collision pairs: normalize pair keys (`min(objectId),max(objectId)`), sort by first contact time if available then stable key, lock input objects in deterministic order, skip pairs touching already-claimed objects, resolve merges, then enqueue resulting collisions for subsequent steps. The same pair must never consume twice. Keep `mergeId` in event log.

Top-tier behavior must be explicit: v0.1 max tier does **not** merge upward; it acts as a physical object until consumed/served/cleared. Later alternate evolution trees possible.

## 9. Interaction with customer orders

For v0.1, **automatic serving** occurs when an eligible drink output matches the leftmost suitable outstanding order *and the merge result has completed its short creation phase*. Do not serve the two consumed lower-tier inputs. A served drink is removed only once; `order_progressed` and coin reward are emitted by a session reducer. This reduces input complexity for alpha. Manual tap/drag serving is a future design decision.

Keep a brief highlighted result visual before serving so users understand what they created. If multiple customers want same tier, stable priority is order created-at, then order ID. See `05`.

## 10. Collisions that do not merge

Rapier handles separation, impulses, velocity exchange and angular behavior. Body size/mass policy must be consistent. Small default circle colliders may not produce pronounced spin on frictionless impact; add restrained **visual wobble** based on impulse strength or introduce asymmetrical compound colliders if needed. Never change simulation velocity solely to imitate an animation unless deliberately designed and bounded.

The bottom dashed line is a **danger boundary**, not a literal collision wall. Evaluate when settled/drifting drink bodies remain in the danger area longer than grace period. Incoming shooter spawn is exempt from losing until it crosses the official playable line. No instant loss from a single transient overlap during a collision.

## 11. Session rules / end states

Alpha round win: complete a configured target of served orders OR specified score target, depending on level JSON. Default demo `serve 5 orders`. Loss: a non-spawned active body remains across danger boundary for > grace period or max action budget exhausted (only in missions that specify budget). Also allow `retry`, `pause`, `exit`. Do not auto-fire another drink after round end.

## 12. Runtime events

`shot_aim_started`, `shot_fired`, `body_contact_started`, `drink_merged`, `drink_spawned`, `drink_served`, `combo_advanced`, `order_progressed`, `order_fulfilled`, `score_changed`, `danger_warning`, `session_won`, `session_lost`. Every event includes `sessionId`, `sequence`, `simulationVersion`, `levelVersion`, `occurredAtStep` and typed payload. Raw contact events are generally internal and sampled only for analytics.

## 13. Tests — mandatory cases

- 0° / 30° / 45° / 90° impacts; varying mass and velocity.
- Same-tier merge, different-tier bounce, tier-max no merge.
- Triplet simultaneous contacts: each object consumed ≤1 time.
- A newly spawned result triggers legal chain merge on subsequent step.
- High-speed body against thin boundary with CCD; no tunneling.
- Drag cancel, rapid input spam, double tap, two-finger interruptions.
- 30/60 FPS rendering produce consistent collision result under same stepped simulation.
- Tab hidden/resumed after 5+ min doesn't skip forward or award twice.
- Repeated round retries release world, sprites and audio without memory growth.
- Out-of-bounds launch and missing sprite fallback handled gracefully.

## 14. Replay/determinism caveat

Record inputs with step index, RNG seed, level config hash, physics and rules versions. Rapier floating-point outcomes may differ across implementations/environments; do **not** assume identical deterministic replay across browser, WASM build, and backend without cross-platform verification. Local alpha is casual only, and local scores are **not trusted** for public rankings. For ranked modes, design validated replay or authoritative server simulation separately.

## 15. Physics acceptance gate

A tester can intuitively aim and consistently induce an angled deflection, a successful same-tier merge and a chain reaction; the sim does not shake/explode/spawn duplicates; the table feels smooth and glidy, yet sessions complete predictably; mobile touch is no worse than desktop mouse.
