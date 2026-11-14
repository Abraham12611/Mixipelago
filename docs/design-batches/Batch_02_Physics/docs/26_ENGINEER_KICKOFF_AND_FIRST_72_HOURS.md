# 26 — Engineer Kickoff Brief and First 72 Hours

## Copy/paste engineering directive

**Mission:** Build Mixipelago's first playable web alpha from the Batch 1 + Batch 2 specifications. Highest priority is credible low-friction glass dynamics on a tabletop, mouse/touch aiming, valid same-tier merges, believable nonmatching collisions, chain reactions, an understandable next queue and two customer slots. Do not independently implement advanced islands, business economy, ranked leaderboards, story AI, server-authoritative multiplayer or heavy 3D runtime in v0.1.0.

**Stack baseline:** TypeScript/Next.js/React for shell, Phaser 4 for real-time rendering/input, Rapier 2D WASM for rigid bodies, Zod shared contracts, Vitest/Playwright testing. Use proper package locks. The first round works with local preview progress, no real money or valuable currency. Art and sounds may begin with original curated placeholders and be replaced without changing physics rules.

**Manual-testing rule:** Every subjective/manual UI playtest must be directed to the product owner. Engineers run automated suites, instrument metrics and provide playable preview links, screenshots, recordings or reproducible checklists for the owner's feedback.

**Merge rule:** Engineers open PRs; coordinator reviews and merges to `develop`. No self-merge. Promoting to main requires the owner's explicit approval.

## Group assignments

### Engineer/Group 1 — Contracts and simulation foundations

Deliver package `domain-contracts` with `SimulationInit`, `PhysicsPreset`, `GameCommand`, `SimEvent`, `SimulationSnapshot`, plus Zod parsing and sample fixtures. Define stable ID policy and version fields. Provide unit tests and architectural boundary lint.

### Engineer/Group 2 — Rapier world and collision integration

Implement WASM init, fixed clock, walls, body registry, launch impulses, CCD and tests. `world.step(eventQueue)` outputs raw contacts; no score updates or sprite state manipulation. Implement headless fixtures for glides, head-on and angled impacts. Expose read-only snapshots.

### Engineer/Group 3 — Merge arbitration and chains

Build stable contact candidate normalization, pair dedup, claim sets, deferred mutation commit, output momentum/placement and chain ancestry. Write property-based tests for triple-contact, two disjoint pairs, spawned result and max-tier collisions. Never emit duplicate merge reward events.

### Engineer/Group 4 — Input + responsive camera

Build pointer capture, touch cancellation, world-coordinate mapping, aim cone, release-to-fire and keyboard fallback. Build desktop/mobile HUD wireframes that do not obstruct game canvas. Tests for CSS scale, orientation and dead zone.

### Engineer/Group 5 — Renderer, SFX and assets

Build Phaser scene mounted once in Next client component, eight original placeholder tiers, sprite anchors, shadows, interpolation, limited impact/merge FX, SFX and missing-asset fallback. All reactions consume semantic events, not modify physics. Create separate audio and graphics quality settings.

### Engineer/Group 6 — Game rules/integration/QA

Build deterministic queued tiers, two customer order view models, automatic serve, score preview coins, board danger and terminal reducer. Integrate shot → collision → merge → score → customer order → win/loss → retry, run E2E, owner manual preview handoff and release checklist.

## Sync and implementation checkpoints

**Checkpoint 1 (contract readiness):** public types compiled and examples accepted by dependents. **Checkpoint 2 (physics proof):** plain colored circles glide/deflect and contact events are correct. **Checkpoint 3 (gameplay proof):** exactly-once merging and one chain visible in headless/browser tests. **Checkpoint 4 (product proof):** drink artwork and HUD connected, mobile and desktop playable. **Checkpoint 5 (release gate):** QA and owner approval. Do not wait for full art to validate physics.

## Mandatory PR checklist

1. Link requirement ID(s) and doc sections.
2. State which package/files modified and why.
3. State whether public contracts or rules changed; if yes, link ADR and required owner approval.
4. Include command output for typecheck, unit/physics tests and relevant Playwright tests.
5. Include reproducible fixture/video for any visual physics behavior.
6. List target device/browser, known bugs, performance impact, rollback plan.
7. Confirm no untrusted real coin balance or ranked reward path added.
8. Never mark an unperformed manual UI test as complete; request owner testing.

## Owner's quick acceptance script

1. Open preview in desktop Chrome, load first board, launch straight at a different-tier drink, observe believable hit and movement.
2. Launch intentionally off-center into another different-tier drink; check angled deflection.
3. Launch at a same-tier target; see one result and score progress.
4. Trigger a chain with a fixture or curated setup; make sure the upgraded glass appears and no double scoring.
5. Verify next queue and two customer orders; a created matching result should serve one order automatically.
6. Let a drink enter danger briefly then be rescued; no immediate loss. Leave it across line beyond grace; see clear loss screen.
7. Retry, pause/resume, navigate away/back; no invisible running game or duplicated canvas.
8. Repeat essential shots on a real mobile browser; evaluate aim comfort, responsiveness, sound, visual clarity.
9. Compare `glide-soft`, `glide-balanced`, `glide-pinball` presets and identify favorite. Record feedback with device model and short video if possible.

## Alpha scope vetoes

Anything requiring authenticated wallet, public ranking, quests, full world map, 3D fluid simulation, character dialogue, loot boxes, random incidents, insurance or live duels is not a blocker for v0.1.0. Protect the early release from unchecked expansion. After owner playtesting, prepare v0.1.1 polish and Batch 3 drink/recipe design.

## Stop-ship defects

- Shot physics fails to initialize or canvas blank on supported mobile browser.
- Different-tier glasses pass through each other at legal speed.
- Same-tier pair can be consumed multiple times / rewards duplicate.
- Coordinate mismatch makes aimed shot consistently go elsewhere.
- Next queue advances on cancelled/denied shot.
- Data loss corrupts session or leaks preview currency into trusted economy.
- Terminal state produces conflicting outcomes or further rewards.
- Performance below viable baseline without fallback.
- Owner manual acceptance not performed or explicit main approval missing.

## Suggested next issue batch after v0.1.0

Physics lab full UI, aim-gesture alternative, better collision VFX, device quality tuning, replay hash tests, long-play memory QA, richer original SFX and first curated mission set. These are appropriate for v0.1.1/v0.1.2 as quality and capacity permit.
