# Engineer Start Here — Batch 15

**Purpose:** turn a documentation batch into small, integrated PRs without overstating release readiness.

## Required context
- `Batch 01 / docs/03_SITEMAP_AND_UX.md`
- `Batch 01 / docs/28_INTEGRATION_CONTRACTS.md`
- `Batch 02 / docs/18_PERFORMANCE_MOBILE_AND_ACCESSIBILITY.md`

## Non-negotiable contracts
1. Batch 02 alone owns fixed-step Rapier physics, collision/merge arbitration, and immutable simulation outcome semantics. No new feature writes physical contacts or awards rewards from visual effects.
2. Batch 03 owns the eight-tier alpha ladder and newly merged drink auto-serving to oldest compatible active order; Batch 04 owns mission goals, stars and win/loss state.
3. Batch 05 owns campaign graph visibility/unlocks; Batch 06 owns wallet and financial ledger; Batch 07 owns XP/skills; Batch 08 owns reward/collectible entitlements; Batch 09 owns customer/relationship facts while shop reputation settlement remains under Batch 06.
4. Client previews and unverified sessions are not currency, XP, competitive score, badge provenance, or trusted activity evidence. All durable grants derive from unique verified receipts.
5. Ranked play freezes the physics/scoring/content/seed profile and disables non-normalized world, shop, skill, story, social and cosmetic advantages.
6. Every stage is a proposal, not a claim of implementation. Manual browser and gameplay acceptance belongs to the owner. Engineers open PRs and do not self-merge.

## Recommended delivery order
1. Establish tokens, text hierarchy and component contract
2. Ship title/play/help/settings/pause/results with Phaser boundary
3. Build responsive map, shop, progression and collection slices with their gates
4. Add leaderboard/events/social pages only with real backend projections
5. Maintain accessibility, screen snapshots and owner manual approval with every slice

## Initial parallel workstreams
| Workstream | Scope | Dependency |
|---|---|---|
| Domain/contracts | pure transitions, schemas, golden fixtures | Batches 01–09 source contracts |
| Backend | trusted persistence, auth, idempotency, API | accepted domain contract |
| Frontend | feature-gated responsive views and errors | read model and approved art |
| Content | candidate definitions, content validation and authoring | catalog schema and editorial policy |
| QA/reliability | property tests, concurrency/load, rollback rehearsal | backend and test fixtures |

## Proposed GitHub issue cut
- **B15-01** — Experience principles and non-goals: define scope, contract, golden fixture, tests and review owner.
- **B15-02** — Information architecture and navigation map: define scope, contract, golden fixture, tests and review owner.
- **B15-03** — Design tokens and semantic color: define scope, contract, golden fixture, tests and review owner.
- **B15-04** — Typography, density and hierarchy: define scope, contract, golden fixture, tests and review owner.
- **B15-05** — Layout grid, breakpoints and safe areas: define scope, contract, golden fixture, tests and review owner.
- **B15-06** — GameShell, React and Phaser boundary: define scope, contract, golden fixture, tests and review owner.
- **B15-07** — Title screen and first launch: define scope, contract, golden fixture, tests and review owner.
- **B15-08** — Gameplay HUD and board framing: define scope, contract, golden fixture, tests and review owner.
- **B15-09** — Order cards, queue and serving feedback: define scope, contract, golden fixture, tests and review owner.
- **B15-10** — Aiming, gestures and pointer affordances: define scope, contract, golden fixture, tests and review owner.
- **B15-11** — Gameplay overlays, pause and results: define scope, contract, golden fixture, tests and review owner.
- **B15-12** — Map, islands and mission selection: define scope, contract, golden fixture, tests and review owner.
- **B15-13** — Shop hub, upgrades and economy trust: define scope, contract, golden fixture, tests and review owner.
- **B15-14** — Skills and player growth interfaces: define scope, contract, golden fixture, tests and review owner.
- **B15-15** — Rewards, albums and cosmetic inventory: define scope, contract, golden fixture, tests and review owner.
- **B15-16** — Customers, portraits and shop reputation: define scope, contract, golden fixture, tests and review owner.
- **B15-17** — World conditions, story and event screens: define scope, contract, golden fixture, tests and review owner.
- **B15-18** — Leaderboards, rankings and competition UX: define scope, contract, golden fixture, tests and review owner.

## Pull request acceptance
- Separate branch and PR per domain; DO NOT self-merge. Review dependent contracts and wait for coordinator/owner approval.
- Include migration forward/backward behavior, feature flag status, config hashes, typed error states and test output.
- UI PRs include accessible mobile + desktop screens, disabled/error/empty/loading examples, and owner-directed manual acceptance instructions.
- Never connect unverified local preview evidence to trusted coins, XP, owned items, shop state, rank or social prizes.
- Prefer one end-to-end vertical slice to fifteen disconnected demo screens; no production claim until exercised against the actual service.

## First useful milestone
Establish tokens, text hierarchy and component contract → Ship title/play/help/settings/pause/results with Phaser boundary.

## Risks and unresolved policies
Batch 01 React/Phaser boundary; Batch 02 board; Batch 03 drinks; Batch 04 missions; Batch 05 map; Batches 06–14 screens and projections; Batch 16 art production.

## Explicit deferred scope
Foundational tokens, responsive gameplay shell and core routes affect v0.1.x immediately; campaign/shop/profile views rollout with their systems; social, events and live interfaces are feature-gated until owned backends work.
