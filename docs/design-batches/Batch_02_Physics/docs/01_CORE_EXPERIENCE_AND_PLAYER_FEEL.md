# 01 — Gameplay Fantasy, Player Feel, and Success Criteria

## Purpose

Mixipelago is a **skillful, nearly frictionless drink-shooting merge puzzle**. The player launches a drink across a tabletop; matching glasses merge and evolve; nonmatching glasses push, bounce, redirect, and sometimes set up chain reactions. Customers provide goals. A credible physics model makes each shot feel intentional rather than scripted.

We are not simulating liquid hydrodynamics or fragile glass destruction in the alpha. The visual fantasy is "gliding beverages on a polished magical table," not realistic bar logistics. The game can be physically plausible while deliberately bending reality to maximize clarity, excitement and control.

## The first 30 seconds

1. A short onboarding cue identifies the active drink, next drink and highlighted matching glass.
2. Player holds pointer/touch in the launch zone; an aim ray appears.
3. Player drags toward the target and releases. The glass accelerates in the selected direction.
4. On a nonmatching collision, both glass sprites deflect according to impact geometry, with restrained impact sound and wobble.
5. On a matching collision, the two glasses disappear into a clear "merge" motion and a new higher-tier glass materializes at a stable point; score increases.
6. Customer bubble reacts if the created result satisfies their request; reward/goal progress is clearly displayed.
7. The next glass becomes available after a transparent cooldown/settle rule.

## Desired tactile adjectives (for user testing)

- **Smooth:** the glass glides after launch; no frame-to-frame shudder.
- **Believable:** oblique impacts visibly deflect rather than passing through one another.
- **Readable:** even a complex chain is understandable; the player sees what merged and why.
- **Responsive:** input release and launch have very little perceptible delay.
- **Predictable:** same aim and same setup usually produce a comparable outcome; precision can be learned.
- **Alive:** distinct light taps, medium collisions, and large chains have corresponding animation and audio intensity.
- **Forgiving:** boundary warning gives a chance to recover; first levels teach before punishing.

## Anti-goals

- Excessive spin that makes cocktail artwork rotate upside down constantly.
- Fully frictionless motion that never stops and traps the player in interminable movement.
- "Magnetized" merges across visible gaps with no communicated ability.
- Large camera shakes that obscure input or make mobile aiming nauseating.
- AI-created sprite variants that change cup shape during hover/collision.
- Too many popups, confetti bursts or reward sounds for ordinary shots.
- Unpredictable random drift introduced without a visible modifier.
- Pay-to-win boosters in equal-condition ranked challenges.

## Prototype acceptance experiments

**P-01 Glide feel:** launch one glass from center in empty lane; travel should appear continuous and settle within designer-defined time; compare at 30 and 60 render FPS. Prototype hypothesis: it travels several glass diameters and slows over several seconds, but no exact distance or duration is assumed until owner testing.

**P-02 Head-on transfer:** shoot equal-mass glass into a stationary different-tier glass with near-zero lateral offset. Target should move and shooter should lose forward motion/deflect as predicted by restitution. No overlap or scene explosion.

**P-03 Glancing collision:** introduce half-radius offset; the target gains diagonal velocity and the moving glass changes direction. Player should be able to aim intentionally for such a deflection.

**P-04 Same-tier merge:** two same-tier objects collide once and become one next-tier object. New sprite should not teleport an obvious large distance; reward exactly once.

**P-05 Combo:** a new result contacts a third legal matching object and produces exactly one further-tier result. FX must distinguish first merge from chain.

**P-06 Crowded board:** twelve or more glasses stay stable, with no long-lived penetration, uncontrollable vibration, frame-time spikes or unfair terminal state.

## UX tuning framework

For every iteration, compare 3 presets: `glide-soft` (low bounce, mild drag), `glide-balanced` (moderate bounce), `glide-pinball` (higher bounce). Owner should play each blind or in randomized order and rate: gliding (1–5), predictability (1–5), satisfying collisions (1–5), chain readability (1–5), mobile aiming (1–5), and session pace (1–5). Record device, preset ID, video and notes.

## Design ethos

We will achieve quality by tuning **input → motion → contact → merge → feedback** as a complete loop. High-detail art is important, but if impact physics is poor, the result feels cheap. Conversely, physically accurate dynamics alone may feel dry; controlled animation and sound make the motion expressive.

## Exit gate

The owner can perform a head-on nonmerge collision, an intentional oblique deflection, a normal merge, and a chain merge on both mobile and desktop. No opaque or surprise behavior blocks these achievements. Manual UX tests are carried out by the owner; engineers deliver instrumented builds, automated tests and reproducible fixtures.
