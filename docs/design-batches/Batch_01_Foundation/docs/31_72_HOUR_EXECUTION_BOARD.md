# 31 — 72-Hour Release Execution Board

This is an aggressive **best-case coordination plan**, not a guarantee. The day-based gates are actionable checkpoints for a team with prepared development access and several parallel contributors. No work should proceed to production if P0 quality gates fail.

## Day 1 — Prove the core (hours 0–24)

**0–4h — Interfaces and project start**
- [ ] Coordinator creates repo, protected branches, issue labels and issue board.
- [ ] Workstream E creates Next/Phaser scaffold, CI, preview environment.
- [ ] Workstreams A/C approve game events, physics units, schema and ownership.
- [ ] Workstream D makes 8 placeholder tier sprites, one board, original icons.

**4–12h — Simulation and input**
- [ ] Rapier runs fixed step with zero gravity.
- [ ] Dynamic circular colliders, static bounds, low damping and restitution tuned.
- [ ] Mouse/touch aim transforms world/screen coordinates and fires shot.
- [ ] Quick visual debugger shows collider rings and velocity.

**12–24h — Collisions and merges**
- [ ] Collision events collected with active event flags.
- [ ] Same-tier merging, off-center nonmerge collision and top-tier handling.
- [ ] Triple contact dedupe, body removal timing and chain merge tests.
- [ ] Integration merges small PRs into `develop` after CI.

**Day-1 exit:** Glasses launch, glide, bounce and merge in a minimal interactive board on a preview URL. If not, prioritize physics over new features.

## Day 2 — Make it a game (hours 24–48)

**24–36h — Session and orders**
- [ ] Tier catalog, seeded spawn queue, two customer cards, auto-serve.
- [ ] Score, preview coins, round goals and danger line fail conditions.
- [ ] Session state machine, terminal state and safe retry.

**30–44h — Look, feel and save (parallel)**
- [ ] Mobile portrait and desktop landscape UI; player can play with no scroll collision.
- [ ] Original drink art and background (placeholders allowed).
- [ ] Launch/collision/merge/order/win SFX and separate mute settings.
- [ ] Local versioned save (tutorial flag, settings, best score, preview coins).
- [ ] Pause on visibility change; cleanup without leaked listeners.

**44–48h — Integration test**
- [ ] End-to-end Play → shoot → merge → serve → result → retry.
- [ ] Profile basic browser performance and initial download.

**Day-2 exit:** A full loop exists, not a collection of screenshots or disjoint mockups.

## Day 3 — Public alpha hardening (hours 48–72)

**48–60h — Fix P0**
- [ ] Run collision edge cases and unit tests.
- [ ] Repair mobile pointer cancel, viewports and safe-area issues.
- [ ] Validate correct state after rapid retry, pause and refresh.
- [ ] Verify loading/error fallback and no hidden fake features.

**60–66h — Owner manual UI round**
- [ ] Provide staging link and step-by-step owner test script (docs/15).
- [ ] Collect owner feedback on glass glide/deflections, readability, audio and response.
- [ ] Fix owner-confirmed blockers, rerun automated QA.

**66–72h — Release**
- [ ] Coordinator performs final merge review.
- [ ] Owner explicitly approves `main` promotion.
- [ ] Tag `v0.1.0`, produce release notes and known limitations.
- [ ] Deploy live URL, verify smoke checks, set telemetry, prepare rollback.

**Day-3 exit:** working browser game with proven core mechanic. If no approval/gate, keep release candidate on staging and ship once corrected.

## Week 1 after alpha — v0.1.1

- [ ] Turn strongest physics-lab values into approved preset.
- [ ] Improve tutorial, sound mix, particles and type scale.
- [ ] Add 3–10 authored/tested mission configs if game is stable.
- [ ] Improve asset compression, low-power graphics settings, error recovery.
- [ ] Compare phone/desktop session experience and fix biggest friction.
- [ ] Optional Capacitor smoke spike only after web quality acceptable.

## If resource-constrained

**Solo/2-person fallback:** Days 1–3 focus only on one board, no customers until physics correct; week 1 add customer loop and responsive UI. Do not claim public v0.1.0 functionality not actually complete. Quality wins over invented timeline.

## Progress reporting template

```
Timestamp:
Milestone (A0/A1/A2/A3):
PRs open / merged to develop:
P0 acceptance passed/total:
Current blocker:
Risk to 72-hour gate:
Next decision needed from owner:
Preview URL:
Owner manual test checklist link:
```
