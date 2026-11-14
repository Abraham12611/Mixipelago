# 25 — Mode-Specific Feedback, Animation, Audio and Emotional Pacing

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Feedback ownership
A presentation director subscribes to committed semantic events and makes cosmetic choices; it never increments scores or commits merges. Individual effects are cancelable at session end and bound to object IDs; no stale React animation is allowed to award progress.

## Shared event feedback
`shot_fired`: short launch swish; slight glass tilt; no score.
`body_contact_started`: speed-dependent clink with rate limit; nonmerge collisions audible but understated.
`drink_merged`: squash/stretch, liquid splash, sparkle, tier-up chime. Stronger tier = richer sound/FX without hiding the next player decision.
`order_fulfilled`: brief customer delight, tick/check icon, coin sparkle, one score bubble from reducer.
`combo_advanced`: escalating but capped note/chime harmony, clear multiplier label.
`danger_warning`: pulsing dashed line, icon and optional low alarm sound; reduced-motion static alternative.
`session_won`: short bright flourish, then result overlay. `session_lost`: gentle feedback with readable reason, not humiliating effects.

## Mode-specific feel
Service celebrates each customer with light feedback. Precision emphasizes clean aim and final-shot suspense. Rush Hour music can intensify near countdown zero without increasing physics tick. Chain Challenge escalates musical scale by chain depth. Survival shifts ambience at wave boundaries. Endless uses quiet low-interruption loops. VIP can give bespoke dialogue in later batches.

## Input and audio performance
Mobile browser audio unlocks on first user gesture; muted devices have equivalent visual cues. Limit simultaneous clink voices, normalize SFX loudness, avoid clipping during 5+ merges, and pre-decode core audio in scene preloader. Prefer short compressed audio for repeat SFX, stream or lazy-load music. Do not call generative AI at runtime for sound output.

## 2.5D asset integration
The body has an invisible collider; glass sprite follows interpolated physics pose. Liquid slosh, soft shadows and reflections are shader/sprite animations. They must not move collider center, radius or score data. A heavy visual tilt must not mislead players about hitbox size.

## Acceptance
Effects can be disabled completely without changing game outcome or event sequence. Rapid 10-merge chain does not crash low-end mobile, stale effects end on restart, reduced motion works, score presentation matches reducer, volume preferences persist. Sound and assets must have commercial distribution rights recorded.
