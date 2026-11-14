# 06 — Collisions, Impacts, Material Rules, Walls and Contact Semantics

## Physical baseline

All eight alpha drink tiers use equal-radius circular colliders and equal densities. Every drink is a dynamic rigid body with near-zero global drag and controlled restitution. Side/top walls are static bodies. Different-tier glasses always receive normal collision response and cannot merge. Same-tier eligible glasses participate in collision detection and are consumed by the merge resolver after contact is reported.

Rapier solves collision normals, penetration correction, velocities and impulse effects. **Do not** write a custom pairwise bounce solver on top of Rapier. If visual response needs more energy, add event-driven sprite animation; never modify authoritative velocity based solely on drawn animation unless a dedicated, bounded mechanic is specified.

## Head-on impact intuition

In an ideal one-dimensional elastic collision, masses `m1,m2`, incoming velocities `u1,u2`, and restitution `e` satisfy conservation of momentum and relative normal speed. Rapier computes an iterative 2D constraint-based approximation using the contact geometry and solver settings. For equal masses and nearly elastic collisions, an incoming body can transfer much of its velocity to a resting body. With lower `e`, some normal kinetic energy is not preserved.

**Do not evaluate correctness by expecting textbook analytic values at every frame.** The solver may use contact persistence, penetration correction, damping and finite integration. Instead use qualitative rules plus numerical bounds measured from a fixed baseline fixture.

## Glancing impact

For circular footprints, contact normal lies approximately along the line connecting circle centers. A noncentral hit generates diagonal separation; the target moves away along the contact normal and shooter changes its velocity. If friction is very low, two perfectly symmetric circles have relatively little physical angular spin. If we want side-to-side rocking, the visual animation layer supplies a subtle reaction. For later asymmetric footprint objects, torque and angular velocity may emerge naturally.

## Contact event handling

Rapier `EventQueue` produces **started/stopped intersection/contact state changes** when `ActiveEvents.COLLISION_EVENTS` is enabled; it does not emit a new started event on every solver tick where two bodies stay in contact. To implement sustained overlap checks or detect a freshly spawned result already touching another body, supplement event queue with contact graph queries or a deterministic overlap probe. Distinguish:

- `contact_started`: source pair begins contact, suitable as a merge candidate.
- `contact_stopped`: source pair no longer in contact, usually not relevant to merging.
- `contact_force`: optional thresholded event useful for impact-sound magnitude; should not drive merges by itself.
- `contact_persisting`: derived from graph/fixture queries when needed, not assumed to be emitted automatically.

Drain event queue and translate collider handles immediately to stable IDs while mappings exist. Ignore fixed wall contacts for merging; they can still trigger wall impacts. Validate both objects are active and belong to the current session.

## Materials registry

| Material | Damping | Friction | Restitution | Alpha availability |
|---|---|---|---|---|
| Standard glass | 0.12 | 0.06 | 0.38 | Required |
| Wood rail | static | 0.1 | 0.28 | Required |
| Soft cushion | 0.30 | 0.3 | 0.08 | Future |
| Ice panel | 0.03 | 0.0 | 0.15 | Future |
| Rubber bumper | static | 0.2 | 0.8 | Future |
| Sticky puddle | 0.8 | 0.8 | 0.02 | Future |
| Conveyor area | force field | configurable | configurable | Future |

Damping belongs primarily to the moving body's movement model; a surface-specific damping zone needs custom state/forces or an area controller, not a magical collider-friction change in a top-down zero-gravity world. If a drink enters an ice zone, calculate its effective damping from active zone(s) in a deterministic pre-step update. Surface templates are for future missions, not alpha.

## Collision layers

Proposed categories: `DRINK=0x1`, `WALL=0x2`, `SENSOR=0x4`, `DECORATIVE=0x8`, `LAUNCH_PREVIEW=0x10`. Real drink colliders collide with drinks and walls. Sensors intersect drinks but do not generate physical response. FX particles, static background artwork, labels and shadows never collide. If a booster makes a body temporarily intangible, implement explicit filtering with state and version the mechanics.

## Collision sound from impact strength

For a collision pair, use relative speed projected along normal as a cheap approximation:

```
relativeVelocity = vA - vB
approachSpeed = max(0, -dot(relativeVelocity, normalAB))
```

Normal direction conventions matter; unit-test sign for A→B and B→A. A true contact-force event is more accurate but costs work; choose based on profiling. Apply thresholds and cooldowns to avoid audio storms. Wall collision may use different SFX sample family.

## Continuous collision detection (CCD)

Fast launched objects can tunnel through thin walls or narrowly spaced objects if the solver uses only discrete positions. Enable CCD on launched dynamic bodies and test with the maximum legal launch impulse. Use adequate rail thickness and reasonable collider sizes. CCD is not permission to run arbitrarily high speeds or fragile collision geometry.

## Merge collision priorities

A collision event by itself never grants score. It proposes candidate pairs. The `MergeResolver` validates tier equality, active state, allowed tier evolution, ownership, reservation and stable pair arbitration. Only semantic `drink_merged` triggers scoring. See `07`.

## Complex cases

- **Triple contact:** A hits B and C in one step. Only one pair can consume A; deterministic sort chooses which.
- **Wall + drink same step:** wall physics resolves normally; matching drink pair still eligible.
- **Edge-of-board merge:** choose legal result placement; don't spawn partly outside due to a weighted midpoint.
- **Resting body contacts:** sleeping does not imply ineligible; wake/resume naturally when hit.
- **Repeated overlap:** do not repeatedly merge same pair. Contact is consumed exactly once; pair locks prevent duplicate processing.
- **Fast parallel glance:** two bodies may pass without contact; don't artificially merge based on sprites visually overlapping if colliders do not touch. Adjust visuals or radius instead.
- **Two immobile packed bodies:** sustained contact query may be needed for new merge results, but prevent infinite instant cascade loops by per-step limits.

## Acceptance fixtures

Head-on 0°, offsets of approximately 25%, 50%, 90% of radius, and grazing contact near the sum of radii; varying speeds across low/medium/high; walls at 30°, 45°, and nearly tangent; five-drink cluster; a fixed sensor near danger boundary. Tests assert finite positions/velocities, no unintended penetration after solver settles, monotonic IDs, no duplicate merges and bounded speed.
