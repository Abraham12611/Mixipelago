# Engineer Start Here — Batch 12

**Purpose:** turn a documentation batch into small, integrated PRs without overstating release readiness.

## Required context
- `Batch 01 / docs/19_ANALYTICS_AND_LIVEOPS.md`
- `Batch 08 / docs/06_06_ATOMIC_SETTLEMENT_IDEMPOTENCY_AND_OUTBOX.md`
- `Batch 10 / docs/00_INDEX_AND_README.md`

## Non-negotiable contracts
1. Batch 02 alone owns fixed-step Rapier physics, collision/merge arbitration, and immutable simulation outcome semantics. No new feature writes physical contacts or awards rewards from visual effects.
2. Batch 03 owns the eight-tier alpha ladder and newly merged drink auto-serving to oldest compatible active order; Batch 04 owns mission goals, stars and win/loss state.
3. Batch 05 owns campaign graph visibility/unlocks; Batch 06 owns wallet and financial ledger; Batch 07 owns XP/skills; Batch 08 owns reward/collectible entitlements; Batch 09 owns customer/relationship facts while shop reputation settlement remains under Batch 06.
4. Client previews and unverified sessions are not currency, XP, competitive score, badge provenance, or trusted activity evidence. All durable grants derive from unique verified receipts.
5. Ranked play freezes the physics/scoring/content/seed profile and disables non-normalized world, shop, skill, story, social and cosmetic advantages.
6. Every stage is a proposal, not a claim of implementation. Manual browser and gameplay acceptance belongs to the owner. Engineers open PRs and do not self-merge.

## Recommended delivery order
1. Publish event read model and UTC clock fixtures
2. Build event hub, single activity and limited calendar
3. Wire verified contribution to existing mission result
4. Grant one owned cosmetic via Batch 08 trusted entitlement
5. Add archive, cancellation operations and community goals later

## Initial parallel workstreams
| Workstream | Scope | Dependency |
|---|---|---|
| Domain/contracts | pure transitions, schemas, golden fixtures | Batches 01–09 source contracts |
| Backend | trusted persistence, auth, idempotency, API | accepted domain contract |
| Frontend | feature-gated responsive views and errors | read model and approved art |
| Content | candidate definitions, content validation and authoring | catalog schema and editorial policy |
| QA/reliability | property tests, concurrency/load, rollback rehearsal | backend and test fixtures |

## Proposed GitHub issue cut
- **B12-01** — Event product scope and fairness principles: define scope, contract, golden fixture, tests and review owner.
- **B12-02** — Event calendar, UTC windows and time zones: define scope, contract, golden fixture, tests and review owner.
- **B12-03** — Event types and capability matrix: define scope, contract, golden fixture, tests and review owner.
- **B12-04** — Event state machine and publication lifecycle: define scope, contract, golden fixture, tests and review owner.
- **B12-05** — Festival worlds and cosmetic transformations: define scope, contract, golden fixture, tests and review owner.
- **B12-06** — Festival service mission rules: define scope, contract, golden fixture, tests and review owner.
- **B12-07** — Community goals and aggregate milestones: define scope, contract, golden fixture, tests and review owner.
- **B12-08** — Seasonal quests and event task boards: define scope, contract, golden fixture, tests and review owner.
- **B12-09** — Seasonal collectibles and souvenirs: define scope, contract, golden fixture, tests and review owner.
- **B12-10** — Limited-time economy and reward budgets: define scope, contract, golden fixture, tests and review owner.
- **B12-11** — Weather, dynamic incidents and event coordination: define scope, contract, golden fixture, tests and review owner.
- **B12-12** — Story scenes, guests and named event characters: define scope, contract, golden fixture, tests and review owner.
- **B12-13** — Tournaments and ranked event boundaries: define scope, contract, golden fixture, tests and review owner.
- **B12-14** — Crews, friends and cooperative event scopes: define scope, contract, golden fixture, tests and review owner.
- **B12-15** — Event registration, eligibility and opt-in: define scope, contract, golden fixture, tests and review owner.
- **B12-16** — Notification, reminder and attention policy: define scope, contract, golden fixture, tests and review owner.
- **B12-17** — Live event hub UX and navigation: define scope, contract, golden fixture, tests and review owner.
- **B12-18** — Event art, audio and asset streaming: define scope, contract, golden fixture, tests and review owner.

## Pull request acceptance
- Separate branch and PR per domain; DO NOT self-merge. Review dependent contracts and wait for coordinator/owner approval.
- Include migration forward/backward behavior, feature flag status, config hashes, typed error states and test output.
- UI PRs include accessible mobile + desktop screens, disabled/error/empty/loading examples, and owner-directed manual acceptance instructions.
- Never connect unverified local preview evidence to trusted coins, XP, owned items, shop state, rank or social prizes.
- Prefer one end-to-end vertical slice to fifteen disconnected demo screens; no production claim until exercised against the actual service.

## First useful milestone
Publish event read model and UTC clock fixtures → Build event hub, single activity and limited calendar.

## Risks and unresolved policies
Batch 10 weather and world conditions; Batch 11 story quests; Batch 04 missions; Batch 06/08 rewards; Batch 13 tournament rankings; Batch 14 crews.

## Explicit deferred scope
Candidate first opt-in festival and a single authored event mission after campaign and trusted rewards (v0.6.2); calendar rotation, community goals and seasonal live programs staged later.
