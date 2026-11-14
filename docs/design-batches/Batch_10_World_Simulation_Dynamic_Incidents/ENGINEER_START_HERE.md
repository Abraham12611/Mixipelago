# Engineer Start Here — Batch 10

**Purpose:** turn a documentation batch into small, integrated PRs without overstating release readiness.

## Required context
- `Batch 01 / docs/11_WORLDS_AND_EVENTS_OVERVIEW.md`
- `Batch 05 / docs/15_CONTENT_MANIFESTS_HASHES_AND_ROLLOUT.md`
- `Batch 06 / docs/05_LEDGER_TRANSACTION_IDEMPOTENCY.md`

## Non-negotiable contracts
1. Batch 02 alone owns fixed-step Rapier physics, collision/merge arbitration, and immutable simulation outcome semantics. No new feature writes physical contacts or awards rewards from visual effects.
2. Batch 03 owns the eight-tier alpha ladder and newly merged drink auto-serving to oldest compatible active order; Batch 04 owns mission goals, stars and win/loss state.
3. Batch 05 owns campaign graph visibility/unlocks; Batch 06 owns wallet and financial ledger; Batch 07 owns XP/skills; Batch 08 owns reward/collectible entitlements; Batch 09 owns customer/relationship facts while shop reputation settlement remains under Batch 06.
4. Client previews and unverified sessions are not currency, XP, competitive score, badge provenance, or trusted activity evidence. All durable grants derive from unique verified receipts.
5. Ranked play freezes the physics/scoring/content/seed profile and disables non-normalized world, shop, skill, story, social and cosmetic advantages.
6. Every stage is a proposal, not a claim of implementation. Manual browser and gameplay acceptance belongs to the owner. Engineers open PRs and do not self-merge.

## Recommended delivery order
1. Define immutable world condition read model and kill switch
2. Render harmless condition overlay on map, with reduced motion
3. Introduce authored opt-in offers and idempotent incident choice receipts
4. Integrate verified mission/world consequences through Batch 06 domain
5. Enable operator dashboards, audit, recovery and rollback

## Initial parallel workstreams
| Workstream | Scope | Dependency |
|---|---|---|
| Domain/contracts | pure transitions, schemas, golden fixtures | Batches 01–09 source contracts |
| Backend | trusted persistence, auth, idempotency, API | accepted domain contract |
| Frontend | feature-gated responsive views and errors | read model and approved art |
| Content | candidate definitions, content validation and authoring | catalog schema and editorial policy |
| QA/reliability | property tests, concurrency/load, rollback rehearsal | backend and test fixtures |

## Proposed GitHub issue cut
- **B10-01** — Product promise, scope and boundaries: define scope, contract, golden fixture, tests and review owner.
- **B10-02** — World time, clocks, schedules and freeze points: define scope, contract, golden fixture, tests and review owner.
- **B10-03** — Island biomes and geographic conditions: define scope, contract, golden fixture, tests and review owner.
- **B10-04** — Weather state, forecast and transitions: define scope, contract, golden fixture, tests and review owner.
- **B10-05** — Tourism, crowds and visitor demand: define scope, contract, golden fixture, tests and review owner.
- **B10-06** — Supply conditions and price signals: define scope, contract, golden fixture, tests and review owner.
- **B10-07** — Incident classification and severity: define scope, contract, golden fixture, tests and review owner.
- **B10-08** — Incident finite-state machine: define scope, contract, golden fixture, tests and review owner.
- **B10-09** — Event Director eligibility and cooldown: define scope, contract, golden fixture, tests and review owner.
- **B10-10** — Probability, seed, caps and fairness: define scope, contract, golden fixture, tests and review owner.
- **B10-11** — Shop fire and emergency scenario: define scope, contract, golden fixture, tests and review owner.
- **B10-12** — Repair, resilience and recovery flows: define scope, contract, golden fixture, tests and review owner.
- **B10-13** — Insurance, liability and financial authority: define scope, contract, golden fixture, tests and review owner.
- **B10-14** — Positive world opportunities: define scope, contract, golden fixture, tests and review owner.
- **B10-15** — Dynamic challenge and rescue missions: define scope, contract, golden fixture, tests and review owner.
- **B10-16** — Cross-system world handoffs: define scope, contract, golden fixture, tests and review owner.
- **B10-17** — Offline, missed windows and anti-punishment: define scope, contract, golden fixture, tests and review owner.
- **B10-18** — World map, HUD and incident choice UX: define scope, contract, golden fixture, tests and review owner.

## Pull request acceptance
- Separate branch and PR per domain; DO NOT self-merge. Review dependent contracts and wait for coordinator/owner approval.
- Include migration forward/backward behavior, feature flag status, config hashes, typed error states and test output.
- UI PRs include accessible mobile + desktop screens, disabled/error/empty/loading examples, and owner-directed manual acceptance instructions.
- Never connect unverified local preview evidence to trusted coins, XP, owned items, shop state, rank or social prizes.
- Prefer one end-to-end vertical slice to fifteen disconnected demo screens; no production claim until exercised against the actual service.

## First useful milestone
Define immutable world condition read model and kill switch → Render harmless condition overlay on map, with reduced motion.

## Risks and unresolved policies
Batch 05 map, Batch 06 wallet/insurance/shops, Batch 09 customer demand, Batch 12 live calendar, Batch 04 gameplay mode rules.

## Explicit deferred scope
Preview weather overlays after the first campaign (candidate v0.6.0); authored opt-in incidents and recovery (v0.6.1+); shop-economic world effects only after audited server-ledger integration (v0.7+).
