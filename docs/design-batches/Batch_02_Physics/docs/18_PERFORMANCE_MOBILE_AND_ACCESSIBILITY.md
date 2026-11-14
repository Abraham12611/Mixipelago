# 18 — Browser Performance, Device Profiles, and Accessible Gameplay

## Primary targets

Desktop Chrome, Firefox, Safari, Edge; Android Chrome; iOS Safari. v0.1.0 should start on supported modern browsers without a native app. Feature detection and fallback UI required if WebGL or WASM fails. Native iOS/Android wrappers via Capacitor are planned later, not a dependency for the first web release.

## Frame budgets

At 60 FPS one render frame is about 16.67ms total. At 30 FPS budget is about 33.33ms. The physics adapter has its own fixed step budget; it should generally fit comfortably within a small fraction of the frame on target mobile devices. Example targets to validate, not guarantees:

- p95 physics step ≤2ms at 20–30 active objects on midrange test phones.
- p95 render frame duration ≤16.67ms at 60Hz target, fallback to 30fps quality tier.
- No unbounded memory growth after 20 restarts/level changes.
- 1–2 MB compressed art for immediate startup is desirable, but total first playable assets may be larger; measure real performance rather than enforcing unsupported budget claims.
- No sustained main-thread stalls >100ms from image decode, shader compile, save or synchronous analytics.

Performance baselines must record device model/OS/browser, DPR, viewport, asset manifest version, scene object count and quality profile.

## Rendering profiles

`high`: larger resolution and richer particles, soft shadows, glow effects. `balanced`: limited particles and effects, capped canvas DPR. `low`: reduced texture sizes, fewer effects, static shadow where possible, no expensive filters. Quality profiles **may only change cosmetics**, not collision radius, shot force, timestep, merge rules or game time.

## Texture memory

Encoded PNG/WebP size is not a reliable estimate of decoded GPU memory. A 2048×2048 RGBA texture can occupy ~16 MiB before mipmaps and duplicate buffers. Use atlases with sensible size (typically 1024–2048 for mobile, verified by tests), discard source images after upload if safe, avoid duplicate texture caching, and load per mission/island. Test 2D sprites with WebGL, since WebGPU support/behavior differs among mobile browsers.

## Physics performance

- Fixed step accumulator with catch-up ceiling. Avoid processing raw contact event thousands of times per frame in UI.
- Keep collision footprints simple, a circle per drink plus walls. The broad-phase handles candidate pairs.
- Use sleep thresholds where appropriate but don't wait for whole table to sleep before allowing shots.
- Object pool render sprites and particles; do not cache unbounded replay snapshots.
- Contact-force events disabled unless needed; cap detailed telemetry in production.
- Dev overlay not bundled in release build unless explicitly gated.

## Worker choice

A Web Worker can isolate physics from the main thread, but transferring state to the render thread, synchronization, WASM load and Safari compatibility may increase complexity. Start with a main-thread fixed-step simulation and profile. If simulation is a bottleneck, move the entire SimulationCore to a Worker through a clearly typed message protocol with pooled transfer buffers / structured clone; do not split entity authority across threads. OffscreenCanvas is an independent option and not required for moving only math off-thread.

## Responsive input

- Correct world mapping across camera scale, letterboxing, browser zoom and dynamic DPR.
- Explicit `touch-action: none` only on game canvas, not whole document.
- Screen orientation changes cancel aim; don't move the shot origin mid-gesture.
- Larger interactive target around launch region on small phones.
- Use safe-area insets for bottom boosters and menus.
- Keyboard controls for all essential puzzle actions, including aim/firing, pause and retry; focus management after modals.

## Accessibility

- Color + icon + text for danger and order state.
- Reduce unnecessary flashing and decorative shake; provide reduced-motion mode.
- Separate mute/music/SFX sliders and text feedback for critical sound cues.
- Focus-visible controls, DOM menus with semantic buttons, clear status announcements that don't overwhelm screen readers.
- Game canvas may not be accessible to screen readers by default; expose a parallel status/controls region for current drink, aim angle, score, order target and outcome where feasible.
- For cognitive accessibility, keep first tutorial short and one goal at a time.
- Avoid countdown pressure in basic mode; design alternate low-stress modes later.

## Browser lifecycle

Hidden tab: stop physics, clear accumulator, pause audio. Page freeze/resume: reload resources if context lost, restore checkpoint if compatible. Browser back/forward: pause or confirm exit according to app shell route. WebGL context loss: show recovering overlay and rebuild textures or offer safe retry; never silently continue invisible physics for seconds while user cannot see the board. WASM initialization failure: explicit error state with retry and support diagnostics, not blank canvas.

## Device QA suite

At least: desktop mouse and keyboard, iPhone Safari on a midrange supported device, Android Chrome on midrange supported device, reduced-motion preference, narrow portrait, 120Hz display, background/resume, orientation change, low memory stress. **All manual interface testing assigned to product owner**, engineers supply automated Playwright/CI plus clear steps for owner validation.
