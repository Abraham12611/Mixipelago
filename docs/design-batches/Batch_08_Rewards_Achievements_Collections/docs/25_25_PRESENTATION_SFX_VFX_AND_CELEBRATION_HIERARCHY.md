# 25 — Game Feel: Reward Presentation, SFX and Animation

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Celebration tiers
- Quiet: progress +1, counter update, subtle icon tick.
- Small: standard badge unlocked; 500–900 ms nonblocking toast.
- Medium: chapter completion; panel with reward preview and dismissible animation.
- Rare: album completion or seasonal gold medal; staged animation, custom SFX, static fallback and skip control.

## Source of truth vs animation
Only animate *committed* acquisition as granted. A provisional preview may animate with `Preview` label and never display trusted wallet balance. If delivery is pending, use a reserved/pending visual distinct from the claimed animation.

## SFX style
Light glass harmonics and gentle seaside chimes; full album completion can layer tropical percussion and a short fanfare. Do not play 15 separate sounds for 15 batched achievement tiers—use aggregation. Audio Director handles concurrency, voice priority, user settings and mobile audio unlock.

## Reduced-motion and low-end mode
Replace confetti and bounce transforms with fade/state updates; provide a static trophy reveal. Never require waiting through an animation to interact, and no long particle effect over active gameplay.

## Instrumentation
Track UI notification delivery separately from trusted award receipt. If game is backgrounded, queue summary rather than launching a missed animation when the tab returns.
