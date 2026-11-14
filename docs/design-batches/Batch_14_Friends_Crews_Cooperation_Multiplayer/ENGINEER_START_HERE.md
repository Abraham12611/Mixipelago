# Engineer Start Here — Batch 14

**Purpose:** turn a documentation batch into small, integrated PRs without overstating release readiness.

## Required context
- `Batch 01 / docs/12_SOCIAL_AND_LEADERBOARDS_OVERVIEW.md`
- `Batch 13 / docs/00_INDEX_AND_README.md`
- `Batch 08 / docs/21_21_SEASONAL_RANKED_AND_FRIEND_REWARD_HANDOFF.md`

## Non-negotiable contracts
1. Batch 02 alone owns fixed-step Rapier physics, collision/merge arbitration, and immutable simulation outcome semantics. No new feature writes physical contacts or awards rewards from visual effects.
2. Batch 03 owns the eight-tier alpha ladder and newly merged drink auto-serving to oldest compatible active order; Batch 04 owns mission goals, stars and win/loss state.
3. Batch 05 owns campaign graph visibility/unlocks; Batch 06 owns wallet and financial ledger; Batch 07 owns XP/skills; Batch 08 owns reward/collectible entitlements; Batch 09 owns customer/relationship facts while shop reputation settlement remains under Batch 06.
4. Client previews and unverified sessions are not currency, XP, competitive score, badge provenance, or trusted activity evidence. All durable grants derive from unique verified receipts.
5. Ranked play freezes the physics/scoring/content/seed profile and disables non-normalized world, shop, skill, story, social and cosmetic advantages.
6. Every stage is a proposal, not a claim of implementation. Manual browser and gameplay acceptance belongs to the owner. Engineers open PRs and do not self-merge.

## Recommended delivery order
1. Release privacy settings, block/report and friend graph
2. Add certified asynchronous challenge over Batch 13 verified runs
3. Add crew membership/permissions and one verified project
4. Test moderation, fairness, replay and recovery under concurrency
5. Prove authoritative live match server before any real-time UI launch

## Initial parallel workstreams
| Workstream | Scope | Dependency |
|---|---|---|
| Domain/contracts | pure transitions, schemas, golden fixtures | Batches 01–09 source contracts |
| Backend | trusted persistence, auth, idempotency, API | accepted domain contract |
| Frontend | feature-gated responsive views and errors | read model and approved art |
| Content | candidate definitions, content validation and authoring | catalog schema and editorial policy |
| QA/reliability | property tests, concurrency/load, rollback rehearsal | backend and test fixtures |

## Proposed GitHub issue cut
- **B14-01** — Social promise and feature sequencing: define scope, contract, golden fixture, tests and review owner.
- **B14-02** — Identity, visibility and default privacy: define scope, contract, golden fixture, tests and review owner.
- **B14-03** — Friend request lifecycle and uniqueness: define scope, contract, golden fixture, tests and review owner.
- **B14-04** — Invitations, share links and referral safety: define scope, contract, golden fixture, tests and review owner.
- **B14-05** — Blocking, reporting and safety center: define scope, contract, golden fixture, tests and review owner.
- **B14-06** — Asynchronous challenges and ghost runs: define scope, contract, golden fixture, tests and review owner.
- **B14-07** — Ghost visualization and input privacy: define scope, contract, golden fixture, tests and review owner.
- **B14-08** — Friend leaderboards and filtered ranking: define scope, contract, golden fixture, tests and review owner.
- **B14-09** — Crew creation, naming and membership: define scope, contract, golden fixture, tests and review owner.
- **B14-10** — Crew roles, permissions and governance: define scope, contract, golden fixture, tests and review owner.
- **B14-11** — Crew projects and cooperative milestones: define scope, contract, golden fixture, tests and review owner.
- **B14-12** — Contribution caps, membership changes and rewards: define scope, contract, golden fixture, tests and review owner.
- **B14-13** — Cooperative island building later: define scope, contract, golden fixture, tests and review owner.
- **B14-14** — Gifts and generosity safeguards: define scope, contract, golden fixture, tests and review owner.
- **B14-15** — Social notification inbox and consent: define scope, contract, golden fixture, tests and review owner.
- **B14-16** — Social UI app map and responsive layout: define scope, contract, golden fixture, tests and review owner.
- **B14-17** — Real-time multiplayer design boundary: define scope, contract, golden fixture, tests and review owner.
- **B14-18** — Matchmaking, latency and region policy: define scope, contract, golden fixture, tests and review owner.

## Pull request acceptance
- Separate branch and PR per domain; DO NOT self-merge. Review dependent contracts and wait for coordinator/owner approval.
- Include migration forward/backward behavior, feature flag status, config hashes, typed error states and test output.
- UI PRs include accessible mobile + desktop screens, disabled/error/empty/loading examples, and owner-directed manual acceptance instructions.
- Never connect unverified local preview evidence to trusted coins, XP, owned items, shop state, rank or social prizes.
- Prefer one end-to-end vertical slice to fifteen disconnected demo screens; no production claim until exercised against the actual service.

## First useful milestone
Release privacy settings, block/report and friend graph → Add certified asynchronous challenge over Batch 13 verified runs.

## Risks and unresolved policies
Batch 13 rankings and verified replays; Batch 06 wallet; Batch 08 rewards; Batch 09 guest personalities; Batch 12 festival co-op; Batch 02 physics server certification.

## Explicit deferred scope
Candidate v0.7.0 friends + asynchronous ghost challenges; v0.7.1 crew projects; v0.8.0+ real-time matches only after authoritative simulation, reconnect and moderation tests.
