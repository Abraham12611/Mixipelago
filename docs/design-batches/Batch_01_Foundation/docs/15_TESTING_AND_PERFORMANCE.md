# 15 — QA, Performance, Physics and Browser Test Plan

**Policy for this project:** Automated tests may run in CI; all manual UI testing and subjective playfeel verification must be directed to the product owner/user. Engineers should prepare steps, URLs, test data and expected results; do not claim manual sign-off on the owner's behalf.

## Test pyramids

1. Unit: `game-core` reducers, scoring, orders, config validation, local save migrations.
2. Physics: stepping, collision pairs, spawn bounds, merge single-consumption, chain merges, sleeping/danger boundary.
3. Integration: renderer/physics event bridge, input command mapping, persistence.
4. Browser automation: load, Play, aim/release, order completion, results, pause, refresh, settings.
5. Performance: frame time, memory, asset load, frame drop and context loss.
6. Manual owner tests: visual fidelity, "feels like ice" movement, real touch usability, audio polish.

## P0 automated tests

| ID | Test | Expected |
|---|---|---|
| T-001 | Start session | ready state, valid seed, two orders |
| T-002 | Aim min threshold | no shot consumed if drag canceled |
| T-003 | Same tier collision | exactly one next-tier spawn |
| T-004 | Different tier collision | no merge, both still exist |
| T-005 | Simultaneous triple overlap | no object consumed twice |
| T-006 | Chain merge | valid next merge; bounded events |
| T-007 | Top tier contact | no tier overflow |
| T-008 | Orders | oldest eligible order progresses exactly once |
| T-009 | Round win | all future mutations blocked after terminal state |
| T-010 | Danger boundary | warning/grace, no false instant loss |
| T-011 | Pause/resume | no skipped physics steps/reward repeats |
| T-012 | Storage migration | invalid JSON → recoverable default; supported versions migrate |
| T-013 | Unit consistency | screen-to-world coordinates correct after resize |
| T-014 | Cleanup | destroy scene removes listeners/audio/physics bodies |
| T-015 | Sound muted | no audible SFX when disabled |

## Physics laboratory test scenarios

Head-on same mass, head-on different mass, glancing near miss, 30°/45° side-impact, two-wall rebound, pileup of 8–20 bodies, high-speed impact with CCD, repeated contact under low damping, merge during other contact, collision at board edge, off-axis launcher near side wall. Record reference trajectories/positions and flag regressions by tolerance rather than fragile pixel snapshots.

## Responsive browser/device matrix

**Mandatory owner/manual QA:** iPhone Safari recent version; Android Chrome on mid-range and lower-power device; desktop Chrome and Safari, keyboard/mouse. Additional: Firefox desktop, Edge desktop, tablets and landscape phone orientation.

Representative CSS viewport targets: 320×568, 360×800, 390×844, 430×932, 768×1024, 1366×768, 1920×1080. Test DPR 1/2/3 under explicit memory cap. Simulate notches/safe-area and accessibility text scaling.

## Performance budgets (targets not guarantees)

- Goal 60 FPS on targeted midrange phones; minimum stable 30 FPS fallback.
- Physics fixed 60 Hz; avoid dynamic-step dependence.
- 95th percentile render frame cost ideally <16.7ms on target 60Hz device; test repeated sessions.
- Initial compressed playable assets target ~5–8 MB pending real measurement; avoid unnecessary preloading of later islands.
- Monitor total textures and heap; don't assume a universal per-tab mobile RAM limit.
- Zero unbounded sprites, listeners, audio sources or textures over 20 consecutive retries.
- Page hidden must pause; context restore should rehydrate or show controlled reload.

Use browser performance profiler, WebGL diagnostics, Playwright traces, Sentry metrics when connected. Track shot-to-visible-motion latency in addition to FPS.

## Instrumentation

Store FPS p50/p95, physics step duration, active rigid bodies, texture count/bytes estimate, scene load, input lag, audio voices, errors. Sample rather than log every body contact in production. Include build/version and browser family in bug reports without collecting unnecessary personal data.

## Owner manual test script — v0.1.0

1. Open staging URL on phone and desktop; verify title and Play.
2. Drag from launch area and release; see a glass glide.
3. Strike matching glass and observe merge and score once.
4. Strike different glass at an angle; check credible physical deflection.
5. Serve customer; see coin reward and new goal.
6. Intentionally crowd danger line; check grace + understandable fail.
7. Win a mission; check end result and replay.
8. Mute SFX and music separately, refresh; preference retained.
9. Change orientation/resize desktop while in game; UI remains functional.
10. Hide tab/reopen; no physics catch-up explosion.
11. Restart repeatedly, check for freezes or significant slowdown.

Provide checklist and instructions to the user for sign-off; no silent engineer-only manual "approved" status.

## Go/no-go criteria

All P0 tests green, no reproducible duplicate merge/reward, no blank canvas, owner completes main flow on at least one iOS and one Android device or documents unavailable testing risk, production build reachable and rollback tested. Failures block alpha unless user explicitly accepts release risk with written decision.
