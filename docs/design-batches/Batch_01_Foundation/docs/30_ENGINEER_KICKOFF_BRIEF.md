# 30 — Copy/Paste Brief for Engineering Team

> Use this as a handoff message to engineers working in parallel. Replace repository URLs, roles, and infrastructure details only after they are actually established.

## Engineering kickoff message

We are building **Mixipelago**, an original web-first casual puzzle game: launch illustrated drinks across an almost frictionless tabletop, use believable angle-dependent physics, merge matching tiers, serve customer orders, earn score/preview coins, and complete rounds. Our first milestone is **v0.1.0 playable alpha in roughly 72 hours**, with v0.1.1 polish in the first week if possible. Later versions add islands, shop economy, skills, leaderboards, events and mobile apps.

**Read in this order:** `00_README.md`, `01_VISION_AND_SCOPE.md`, `02_PRD_AND_ACCEPTANCE.md`, `04_GAMEPLAY_AND_PHYSICS.md`, `06_TECH_STACK_AND_ARCHITECTURE.md`, `16_RELEASE_ROADMAP.md`, `17_WORKSTREAMS_AND_ISSUES.md`, and your owned module document. Technical and product docs are the source of truth; use generated images as art inspiration only.

**Stack:** Next.js/React + TypeScript for web UI; Phaser 4 for rendering/input; Rapier 2D WASM for simulation; pure TypeScript reducers for orders/score; local versioned save for alpha. Backend economy/accounts/leaderboards are later, not a launch blocker. All physical gliding and merge actions execute locally without network round trips.

**P0:** game loads on mobile/desktop, aim/launch, low-friction collisions and deflections, same-tier merge and chain merge, nonmatching collision, two customers/order completion, basic scoring and preview coins, win/fail/retry, next drink, pause, sound/mute, local save, responsive UI, one published production URL and tests.

**Do not implement in v0.1.0:** login walls, paid items, real trusted wallet, global leaderboards, detailed islands, incidents, crews, insurance, persistent simulation server or complex 3D meshes. Additional future features must not push out core mechanics.

**PR rules:** short-lived branch per atomic issue, PR to `develop`, tests and contract notes, no self-merging. Coordinator reviews/merges to `develop`; **main requires explicit product-owner approval**. Messages for coordinator belong in PR/issue comments. **All manual UI tests and subjective game-feel tests must be directed to the owner** with clear test steps and preview URL.

**Integration contract:** do not import Phaser from server-side Next code; React never drives physics frame updates; physics events pass through shared typed contracts; merge resolver ensures exactly-once consumption; no client-side coins presented as trusted backend currency. Shared schema changes require coordinated review.

**Success:** a real player can open the web URL on phone or desktop, launch a glass, witness believable deflection with a different drink, merge two matching glasses, serve a customer, finish/retry a round, hear satisfying audio and return with saved preferences.

## Example issue assignment message

```
Issue: MX-007 Merge Resolver
Owner: Physics engineer
Read: docs/04_GAMEPLAY_AND_PHYSICS.md and docs/28_INTEGRATION_CONTRACTS.md
Inputs: collision pair events, drink objects, tier catalog, fixed sim step
Outputs: exactly-once drink_merged / drink_spawned events
Acceptance: same-tier pair merges; diff-tier does not; triple collision never double-consumes; tier 8 cap; chain merging safe; tests provided
Dependencies: MX-003 physics world, MX-004 contracts, MX-006 collision
PR destination: develop; do not merge yourself
Manual UI tests: submit steps for owner, don't self-approve visual/game feel
```

## Escalations

If someone discovers conflicts around camera coordinates, aim gesture, auto-serving semantics, danger line behavior, Rapier event order, save schema or trusted economy: stop local incompatible work and raise an ADR/coordination issue immediately. Do not invent contradictory conventions.
