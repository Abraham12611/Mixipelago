# Engineer Start Here — Batch 11

**Purpose:** turn a documentation batch into small, integrated PRs without overstating release readiness.

## Required context
- `Batch 01 / docs/11_WORLDS_AND_EVENTS_OVERVIEW.md`
- `Batch 05 / docs/03_GRAPH_DOMAIN_MODEL_AND_INVARIANTS.md`
- `Batch 09 / docs/00_INDEX_AND_README.md`

## Non-negotiable contracts
1. Batch 02 alone owns fixed-step Rapier physics, collision/merge arbitration, and immutable simulation outcome semantics. No new feature writes physical contacts or awards rewards from visual effects.
2. Batch 03 owns the eight-tier alpha ladder and newly merged drink auto-serving to oldest compatible active order; Batch 04 owns mission goals, stars and win/loss state.
3. Batch 05 owns campaign graph visibility/unlocks; Batch 06 owns wallet and financial ledger; Batch 07 owns XP/skills; Batch 08 owns reward/collectible entitlements; Batch 09 owns customer/relationship facts while shop reputation settlement remains under Batch 06.
4. Client previews and unverified sessions are not currency, XP, competitive score, badge provenance, or trusted activity evidence. All durable grants derive from unique verified receipts.
5. Ranked play freezes the physics/scoring/content/seed profile and disables non-normalized world, shop, skill, story, social and cosmetic advantages.
6. Every stage is a proposal, not a claim of implementation. Manual browser and gameplay acceptance belongs to the owner. Engineers open PRs and do not self-merge.

## Recommended delivery order
1. Freeze character and quest IDs and authored scene graph
2. Implement read-only dialogue and skip/Chronicle
3. Add server-verified quest flags and repeat-safe choice command
4. Integrate one verified story quest/reward handoff
5. Add optional rival challenge and localized voice later

## Initial parallel workstreams
| Workstream | Scope | Dependency |
|---|---|---|
| Domain/contracts | pure transitions, schemas, golden fixtures | Batches 01–09 source contracts |
| Backend | trusted persistence, auth, idempotency, API | accepted domain contract |
| Frontend | feature-gated responsive views and errors | read model and approved art |
| Content | candidate definitions, content validation and authoring | catalog schema and editorial policy |
| QA/reliability | property tests, concurrency/load, rollback rehearsal | backend and test fixtures |

## Proposed GitHub issue cut
- **B11-01** — Narrative direction and optional story promise: define scope, contract, golden fixture, tests and review owner.
- **B11-02** — Narrative world bible and canon hierarchy: define scope, contract, golden fixture, tests and review owner.
- **B11-03** — Story acts, episodes and campaign beats: define scope, contract, golden fixture, tests and review owner.
- **B11-04** — Character registry and persistent roles: define scope, contract, golden fixture, tests and review owner.
- **B11-05** — Quest taxonomy and progression objectives: define scope, contract, golden fixture, tests and review owner.
- **B11-06** — Quest DSL and prerequisites: define scope, contract, golden fixture, tests and review owner.
- **B11-07** — Dialogue graph and conversational UI: define scope, contract, golden fixture, tests and review owner.
- **B11-08** — Choices, consequences and reversibility: define scope, contract, golden fixture, tests and review owner.
- **B11-09** — Relationship and affinity flags: define scope, contract, golden fixture, tests and review owner.
- **B11-10** — Recurring rival owners and businesses: define scope, contract, golden fixture, tests and review owner.
- **B11-11** — Rival challenge system and scoring fairness: define scope, contract, golden fixture, tests and review owner.
- **B11-12** — NPC schedule, presence and return appearances: define scope, contract, golden fixture, tests and review owner.
- **B11-13** — Quests linked to missions, shops and islands: define scope, contract, golden fixture, tests and review owner.
- **B11-14** — Narrative reward policy and integrity: define scope, contract, golden fixture, tests and review owner.
- **B11-15** — Story history, Chronicle and recap: define scope, contract, golden fixture, tests and review owner.
- **B11-16** — Branching, reconvergence and save migration: define scope, contract, golden fixture, tests and review owner.
- **B11-17** — Narrative world and dynamic incidents: define scope, contract, golden fixture, tests and review owner.
- **B11-18** — Festival storytelling and calendar coordination: define scope, contract, golden fixture, tests and review owner.

## Pull request acceptance
- Separate branch and PR per domain; DO NOT self-merge. Review dependent contracts and wait for coordinator/owner approval.
- Include migration forward/backward behavior, feature flag status, config hashes, typed error states and test output.
- UI PRs include accessible mobile + desktop screens, disabled/error/empty/loading examples, and owner-directed manual acceptance instructions.
- Never connect unverified local preview evidence to trusted coins, XP, owned items, shop state, rank or social prizes.
- Prefer one end-to-end vertical slice to fifteen disconnected demo screens; no production claim until exercised against the actual service.

## First useful milestone
Freeze character and quest IDs and authored scene graph → Implement read-only dialogue and skip/Chronicle.

## Risks and unresolved policies
Batch 05 campaign, Batch 09 customers, Batch 06 shops and rewards, Batch 08 collectibles, Batch 10 incidents and Batch 12 festivals.

## Explicit deferred scope
Story introduction and one optional quest chain after basic map/player persistence (candidate v0.5.3); branching arcs and simulated rival businesses expand later behind distinct gates.
