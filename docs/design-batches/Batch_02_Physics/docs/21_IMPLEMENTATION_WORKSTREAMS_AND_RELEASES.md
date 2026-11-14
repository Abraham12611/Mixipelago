# 21 — Engineering Plan, Workstreams, Dependencies, Version-by-Version Delivery

## Delivery philosophy

**Build and release a playable foundation quickly.** The first 72-hour goal is ambitious and depends on disciplined scope, parallel engineers and curated assets. If critical physics quality or QA fails, release remains gated; do not sacrifice data integrity or smooth controls to hit a date. For this batch, docs support later sophistication but only v0.1.0 essentials are release blockers.

## v0.1.0 playable alpha: mandatory

- Phaser game scene within Next.js client-only mount.
- Rapier 2D WASM initialized with 60Hz fixed step.
- Circular dynamic glass colliders, static top/side rails, near-frictionless damping.
- One visual table; 8 tier assets (stylized placeholders acceptable if art lag).
- Mouse and touch aim-and-release, keyboard accessibility fallback.
- Fixed impulse, one preview next drink and deterministic seeded queue.
- Same-tier merge, nonmatching collision, merge conflict arbitration, basic chains.
- Automatic newly generated drink service to 2 customer orders per Batch 1.
- Basic scoring, preview coins, simple mission win/loss with danger line grace.
- Pause/retry/exit and local progress preview.
- Minimal collision/merge/win SFX and graceful audio fallback.
- Automated physics tests and owner manual browser playtest.

## v0.1.1 polish and stability

- Physics lab in a polished form with owner preset reviews.
- Improved aim preview, camera conversion on difficult viewports.
- Sound richness, visual collision wobble/merge choreography.
- Persistent checkpoint recovery/migrations and improved error screens.
- Device-specific low/medium/high quality profiles.
- Additional curated missions/telemetry; refined tutorial and accessibility.

## v0.1.2+ optional hardening

- First-hit trajectory prediction, wider test fixtures, deterministic replay hashes.
- Tier-specific decorative visual variations while keeping single collider footprint.
- Experimental materials/zones behind feature flags.
- Explicit owner approval required before changing base physics feel.

## Sub-phase roadmap with dependencies

| Stage | Owner group | Deliverable | Dependencies | Release gate |
|---|---|---|---|---|
| P0.1 | Contracts lead | shared TS/Zod contracts, IDs, physics preset | Batch 1 docs | typecheck and schema tests |
| P0.2 | Physics A | Rapier module init, world, rails, body registry, fixed clock | P0.1 | headless fixtures pass |
| P0.3 | Physics B | collision collector, merge arbiter, result spawn, chains | P0.2 | exactly-once and triplet tests |
| P0.4 | Input lead | aim controller + coordinate adapter + keyboard | P0.1/viewport contract | 20 shot stress |
| P0.5 | Rendering lead | Phaser scene, sprite view, interpolation, camera | P0.1 and physics snapshot | visually aligned bodies |
| P0.6 | Game rules lead | queue, orders, score, danger, session outcomes | P0.1 + semantic events | unit and integration passes |
| P0.7 | UI lead | responsive HUD, pause/retry/win/loss and local save | P0.1/VM contract | browser smoke |
| P0.8 | Audio/art leads | 8 drink sprites, SFX, asset manifest, fallback | asset contract | no missing-critical asset |
| P0.9 | Integration lead | connect complete shot→contact→merge→serve→result | P0.2–P0.8 | full flow E2E |
| P0.10 | QA/release | cross-browser automated checks, owner manual session | P0.9 | main approval |

## Parallel teams and ownership

**Team A Physics:** owns `packages/physics-rapier` and physics lab. **Team B Game rules:** owns `packages/game-core`, missions, score and queue. **Team C UI/input:** owns Next/React, viewport/input interface and accessibility. **Team D Renderer/FX:** owns Phaser scene, sprite integration and effects. **Team E Art/audio:** owns asset manifests, original sprites, SFX. **Team F QA/platform:** owns tests, CI and deployments. On small teams, combine roles but keep clear file ownership.

No engineer should independently edit the shared contracts without a contract PR and dependency owner approvals. Agents should open PRs to integration branch only; coordinator reviews/merges to `develop`; **main promotion only with owner approval**. Engineers must not merge their own PRs under the established team policy.

## 72-hour sequencing (example)

**Hours 0–12:** repository/package scaffold, contracts, WASM initialization spike, simple shapes colliding in headless simulation, canvas mount. **Hours 12–24:** shoot input, static rails, basic friction/CCD, sprite sync, seeded queue. **Hours 24–42:** merge arbitration, chain, score/order reducer, danger and outcome states; automated tests. **Hours 42–56:** customer UI, next preview, basic artwork/SFX, responsive layouts, integration. **Hours 56–68:** performance smoke, cross-device automated tests, preview deployment, owner manual testing. **Hours 68–72:** fix release-blocking issues, document known limitations, request explicit main approval. Tasks can overlap; numbers are planning windows rather than ETA promises.

## Definition of integration done

From browser: open mission → see current and next drink → aim and launch → different-tier physical collision visible → same-tier merge → new tier appears with FX → automatic order progress → score/reward preview → finish or fail round → retry without leaked world → save/reload preview. All on desktop and mobile preview with no blank canvas/hydration issue.

## Backlog structure / labels

Issue tags: `physics`, `input`, `game-core`, `renderer`, `ui`, `audio`, `assets`, `quality`, `contracts`, `blocked`, `requires-owner-test`, `release-blocker`, `future`. Each task: goal, file ownership, contract dependencies, acceptance assertions, test command, reference links, security/performance impact, PR target and evidence.

## Release quality gates

- `pnpm typecheck`, lint, unit/physics tests pass.
- No duplicate merge/reward bug under multi-contact fixtures.
- No unsupported physics presets in normal sessions.
- No body tunneling at max legal speed.
- Manual tester can aim from mobile and desktop as specified.
- No automatic import of local preview coins into a future trusted wallet.
- Owner approves tactile feel and explicit promotion to main.
