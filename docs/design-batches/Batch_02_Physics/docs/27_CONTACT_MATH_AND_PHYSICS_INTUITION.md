# 27 — Contact Mathematics and Collision Intuition (Engineering Reference)

## Objective

This file explains what the rigid-body solver is approximately trying to do so engineers can debug surprising contact behavior. **It is not an instruction to replace Rapier with a hand-written impulse solver.** Use equations to reason about expected direction and scale; use actual Rapier fixtures for numerical acceptance.

## Positions, relative motion and contact normal

For circles A and B with center positions `pA`, `pB` and radii `rA`, `rB`:

```
d = pB - pA
centerDistance = sqrt(d.x² + d.y²)
overlap = rA + rB - centerDistance
normalFromAToB = d / centerDistance     (if distance > epsilon)
relativeVelocity = vB - vA
normalRelativeSpeed = dot(relativeVelocity, normalFromAToB)
```

If `centerDistance` approximately equals `rA + rB`, surfaces touch. If smaller, they penetrate in the geometric sense and solver positional correction may occur. If `normalRelativeSpeed < 0`, bodies are approaching along the normal (for this definition of relative velocity). If >0, they are separating. Take care that reversing the normal reverses the sign convention; tests should not confuse impact and separation.

## Idealized normal impulse

In the frictionless single-contact, no-rotation approximation for approaching bodies:

```
j = -(1 + e) * dot(vB - vA, n) / (1/mA + 1/mB)
ΔvA = -(j/mA) * n
ΔvB = +(j/mB) * n
```

Where `n` points from A toward B and `e` is restitution. If bodies are separating, no negative collision impulse should be applied. With dynamic objects with rotational inertia, contact points off the center and friction, the effective mass denominator also contains angular terms. Rapier handles the more complete contact constraints.

The formula illustrates why a moving glass hitting a stationary equal-mass glass transfers some momentum. At `e≈1`, head-on equal-mass contact can exchange velocities; at lower `e`, the incoming glass retains a smaller forward component and the target moves away with lower relative speed.

## Tangential component and oblique impacts

Break relative contact velocity into normal and tangential parts:

```
vNormal = dot(vRel, n) * n
vTangent = vRel - vNormal
```

Normal impulses act along `n`; tangential friction resists sliding along the contact tangent. An off-center hit changes `n`, which causes both X and Y velocity changes even with zero contact friction. That is the source of the natural glancing deflection we want. A perfectly circular, frictionless contact centered on both bodies does not generate much torque; a stylized glass wobble can be layered purely visually.

## Rotation and torque

For an impulse `J` applied at a world-space contact offset `r` from a body's center of mass, angular impulse is the 2D scalar cross product:

```
angularImpulse = r.x * J.y - r.y * J.x
Δω = angularImpulse / I
```

`I` is the body's moment of inertia. An impulse applied precisely at center creates no angular impulse. For symmetric circles with normal impulse through the centers, naturally generated spin can be very small; tangential friction or asymmetric geometry increases it. The drink's visual tilt should be governed by an animation spring independent of the body's actual yaw to avoid rotating the cocktail upright artwork upside down.

## Damping and glide duration

Linear damping continuously reduces speed, even when an object has no collisions. Exact numerical integration is engine-dependent; don't use an analytically exact exponential formula as a fixed test expectation without checking the library's damping implementation. An intuitive approximation for visualization is `speed(t) ≈ speed0 * exp(-d*t)`, but Rapier's implementation has its own update rule. At very small `d`, motion lasts a long time; a zero-damping body on a frictionless plane might continue indefinitely. Sleep thresholds and low-speed settle behavior create a practical end to movement.

For owner presets, compare **actual travel distance and time-to-settle under the implemented fixed-step loop**, not theoretical approximation alone. Keep per-tier physics identical in alpha to simplify learning.

## Conservation and game feel

Collision resolution roughly preserves momentum while restitution controls kinetic energy loss. But a **merge** is not an ordinary rigid-body collision: we deliberately remove two bodies and create one new body. Output position and velocity are game rules. Mass-weighted average velocity is a reasonable intuitive baseline, but it does not literally conserve the momentum of a fusion if the output has the same alpha mass as a single input. If we wanted strict momentum conservation, output mass would need to reflect both inputs and velocities adjusted accordingly; that changes gameplay difficulty and is intentionally not our alpha policy.

## Recommended visual tests

1. Equal-mass head-on impact at moderate speed: near-symmetric response.
2. 25%-radius lateral offset: small diagonal deflection.
3. 50%-radius offset: stronger diagonal response.
4. Nearly tangent: graze or miss based on actual circle geometry.
5. Very high speed near narrow gap: CCD reduces tunneling.
6. Wall at 45°: reflection includes changed normal velocity, tangent mostly retained if low friction.
7. Slow contact: collision may be practically silent; still eligible to merge if same tier.
8. Contact while one body sleeping: body wakes if contacted; validity independent of sleep.

## Solver/implementation caveats

Physics solver may include penetration correction, velocity iterations, warm starting, contact persistence, sleeping, friction-combine rules and CCD substeps. It is normal for a measured result not to match an ideal one-dimensional formula exactly. Never add ad-hoc "fix" impulses until verifying that collider sizes, units, timestep, launch impulse and restitution are correct. A visual sprite that seems to hit but doesn't collide is usually a **visual footprint mismatch**, not proof the solver is broken.

## References

- Rapier colliders and coefficient rules: https://rapier.rs/docs/user_guides/javascript/colliders/
- Rigid body impulses: https://rapier.rs/docs/user_guides/javascript/rigid_body_forces_and_impulses/
- Advanced contact graph: https://rapier.rs/docs/user_guides/javascript/advanced_collision_detection_js/
- Integration parameters: https://rapier.rs/docs/user_guides/javascript/integration_parameters/
