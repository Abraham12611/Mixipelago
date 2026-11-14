# 29 — Runtime Performance, Device Classes and Capacity Budgets

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Target baseline
Aim 60 FPS on supported mid-tier browsers, with consistent feel at 30 FPS rendering fallback. Physics fixed 60 Hz independent of frame rendering, bounded catch-up after tab suspension. Exact budgets must be measured on real target devices, not assumed from desktop Chrome.

## Indicative initial budgets
- v0.1 board `maxActiveDrinks`=18 on first mission; stress test 35 and 60 in lab.
- Target fixed physics step under ~2 ms median and ~4 ms p95 on representative mid-range phone as an initial engineering hypothesis, not a performance guarantee.
- Keep on-screen opaque panels minimal and canvas clear. Use pooled sprites/particles; no per-collision React setState flood.
- Asset budget: tier sprites in atlases, no 4K background per level, lazy-load future maps and music, cap GPU texture memory empirically.
- App should remain functional with sound disabled, reduced particles, DPR cap and no bloom on low-end hardware.

## Frame pipeline
Input collection → fixed-step simulation accumulator → event snapshot → batched UI/view model update at appropriate rate → Phaser rendering/interpolation → audio cues. Never run postprocessing/asset decode synchronously in collision callback. Moving physics to Worker is a later performance experiment, not alpha requirement; Worker messaging introduces latency and integration cost.

## Time and background handling
`visibilitychange` pauses immediately; no 5-minute catch-up. Landscape rotation recalculates canvas transform, not physical objects. Resize updates view matrix only; existing world state and replay remain unchanged.

## Instrumentation
Collect frame time p50/p95, physics step time, active body count, collision pairs per tick, merge arbitration duration, GPU context loss, JS heap trend, retained texture count, audio voices, UI commits per second, asset download time and input-to-shot latency.

## Degradation strategy
Normal quality: full but restrained particles and soft shadows. Reduced quality: fewer particles, no expensive shader, lower DPR, static background. Emergency: simplified art and SFX off; never silently change solver Hz, collision radius, or scoring rule based on device tier.

## Stress scenarios
35 glasses colliding, 10 chained merges, 15-minute Endless simulation, resize during aim, pause/resume x100, 50 retries, low storage, throttled network, WebGL context loss, iOS Safari low-memory reload and Android Chrome overheating. Owner does manual feel evaluation; engineers automate technical regressions.
