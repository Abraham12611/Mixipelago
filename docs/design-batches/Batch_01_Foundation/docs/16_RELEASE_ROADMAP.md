# 16 — Phases, Subphases, Versioning and Release Roadmap

## Release language

Use Semantic Versioning as a *project convention*: `0.MINOR.PATCH` while product is pre-1.0. In strict SemVer, pre-1.0 APIs may change; we still maintain migration and save compatibility where practical. `v0.1.0` is **playable public alpha**, `v0.1.1` is stabilization/polish, `v0.2.0` is a progression feature wave. Do not confuse an internal prototype with a shipped release.

## Intended cadence

Goal: first web alpha in ~72 hours **if team is parallel and assets/deploy credentials are ready**; extend to one week for first stable loop. Thereafter deploy small changes frequently, use feature flags and publish release notes. Dates are aspirational, conditional on release gates.

## Phase A — 72-hour playable public alpha (v0.1.0)

### A0. Environment & parallel foundation (hours 0–6)

- Create monorepo, Next shell, Phaser client-only wrapper, Rapier loader, lint/test/build, Vercel preview.
- Lock initial engine package versions and smoke-test deployment.
- Define shared `GameCommand`, `GameEvent`, tier/config schema and asset manifest.
- Establish asset placeholders, UI token library and simple camera scaling.
- QA baseline: game boots on Chrome/Safari, canvas available, no SSR crash.

### A1. Physics and input core (hours 6–24)

- World rectangle/walls, circular glass collider, zero gravity, damping, restitution, CCD.
- Touch/mouse aim, shot impulse, trajectory preview, spawn queue, camera transform.
- Merge resolver with safe pair arbitration, result creation, visual sync.
- Debug physics lab with tuning, reference collision scenarios.
- Gate: angled nonmatching collisions and same-tier merges working, tests pass.

### A2. Minimal game loop (hours 20–42; parallel)

- 8 tiers, simple drink art; 2 orders, score, demo coins, next preview.
- Win/fail/round restart, basic goal and danger line; seeded first round.
- React UI for desktop/mobile; audio director and 5–8 SFX.
- Local save v1; pause and hidden tab behavior.
- Gate: play → merge → serve → win/fail → retry without refresh.

### A3. Release hardening (hours 42–72)

- Real mobile browser checks prepared for owner, QA fixes, collision test suite.
- Asset optimization, error boundary, loading states, accessibility basics.
- Check browser memory and time-to-interaction; verify no double-award.
- Deploy production, release notes, analytics essential events, feedback channel.
- **No feature creep:** omit accounts/map/social/shop if core physics isn't stable.

## Phase B — First-week quality update (v0.1.1, optional v0.1.2 fixes)

### B1 Gameplay

Fine-tune physics from real feedback, improve shot guidance and chain-reaction visuals, add 3–10 authored missions and basic tutorial.

### B2 UX

Polish desktop/mobile layout, safe-area behavior, gamepad/keyboard fallback if feasible, settings and reduced-motion modes.

### B3 Infrastructure

Automate tests, add bundle size check, make asset manifest and CDN deploy robust, preserve local save on updates.

### B4 Alpha feedback loop

Instrument replay/retry/failure funnel; triage usability complaints and prioritize top crash/performance issues. Native build spike optional—not blocking web release.

## Phase C — Island campaign (v0.2.0 family)

C1 mission data schema/content validator; C2 first island map with ~20–40 curated nodes initially, expandable to hundreds; C3 unlock/stars/progression; C4 authored special puzzles; C5 map polish and content loader. Do not generate hundreds of repetitive levels prematurely.

## Phase D — Trusted economy & shop (v0.3.0 family)

D1 account/auth + migration path (may ship earlier as foundational patch); D2 server ledger/reward grants and score/session validation; D3 one shop; D4 functional/cosmetic upgrade purchases; D5 economy balancing/telemetry. **Do not permit client-authoritative shop transactions.**

## Phase E — Player identity & skills (v0.4.0 family)

E1 persistent profiles/cross-device save; E2 skill infrastructure/modifier registry; E3 starter branch and respec rules; E4 collectible/achievements; E5 account deletion/privacy controls. Account sync may precede this milestone if required by v0.3 trusted economy—order based on technical dependencies, not label.

## Phase F — Competitive & social (v0.5.0 family)

F1 verified score submissions; F2 weekly standardized challenge; F3 global and opt-in regional boards; F4 seasonal reward worker; F5 friends and private challenges. Crews/live multiplayer deferred.

## Phase G — Live-world growth (v0.6.0+)

Additional islands/recipes, VIP customers, branches of skills, incidents, shops/franchises, festivals, crew objectives, Chronicle, native app store packaging. Plan separate content batches for detailed specifications.

## Milestone dependency gates

```
Physics engine ─┬─> Playable loop ─> Mission framework ─> Island campaigns
                └─> Session event schema ─> Validation ─> Economy + ranking
User identity ─────────────────────────────────> Trusted economy/social
Asset system ──> Alpha scenes ────────────────> New islands + native bundles
```

## Version examples

- `v0.1.0`: initial alpha.
- `v0.1.1`: fix touch-cancel bug and tune glide movement.
- `v0.1.2`: save migration repair, minor sound mix.
- `v0.2.0`: island map and new mission classes.
- `v0.2.1`: mission unlock edge-case fix.
- `v0.3.0`: trusted economy/store (after auth/security prerequisites).

## Feature rollout and rollback

All future systems behind OFF-by-default release flags. New content manifests can be rolled back to last-known-good version; avoid mutable asset URL reuse. Postgres migrations forward-compatible during deployment. Each release gets `CHANGELOG.md`, smoke checklist, version stamp and rollback owner. Never promise functionality on the UI before backend is ready.

## Scope arbitration rule

If 72-hour goal slips: cut future features and decoration, **not core physics correctness, mobile input, session terminal states or deployment quality**. Aim for a *smaller finished game*, not a giant partly functional dashboard.
