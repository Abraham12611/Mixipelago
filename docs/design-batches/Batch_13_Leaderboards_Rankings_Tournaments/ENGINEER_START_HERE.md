# Engineer Start Here — Batch 13

**Purpose:** turn a documentation batch into small, integrated PRs without overstating release readiness.

## Required context
- `Batch 01 / docs/12_SOCIAL_AND_LEADERBOARDS_OVERVIEW.md`
- `Batch 04 / docs/28_REPLAY_VALIDATION_AND_TRUST.md`
- `Batch 07 / docs/22_22_RANKED_NORMALIZATION_AND_ANTICHEAT.md`

## Non-negotiable contracts
1. Batch 02 alone owns fixed-step Rapier physics, collision/merge arbitration, and immutable simulation outcome semantics. No new feature writes physical contacts or awards rewards from visual effects.
2. Batch 03 owns the eight-tier alpha ladder and newly merged drink auto-serving to oldest compatible active order; Batch 04 owns mission goals, stars and win/loss state.
3. Batch 05 owns campaign graph visibility/unlocks; Batch 06 owns wallet and financial ledger; Batch 07 owns XP/skills; Batch 08 owns reward/collectible entitlements; Batch 09 owns customer/relationship facts while shop reputation settlement remains under Batch 06.
4. Client previews and unverified sessions are not currency, XP, competitive score, badge provenance, or trusted activity evidence. All durable grants derive from unique verified receipts.
5. Ranked play freezes the physics/scoring/content/seed profile and disables non-normalized world, shop, skill, story, social and cosmetic advantages.
6. Every stage is a proposal, not a claim of implementation. Manual browser and gameplay acceptance belongs to the owner. Engineers open PRs and do not self-merge.

## Recommended delivery order
1. Certify replay worker and normalized profile first
2. Add verified score submit/decision states
3. Materialize one public weekly board and around-me query
4. Freeze season and settle cosmetic prizes via Batch 08
5. Add filters/divisions/tournament only after privacy and moderation

## Initial parallel workstreams
| Workstream | Scope | Dependency |
|---|---|---|
| Domain/contracts | pure transitions, schemas, golden fixtures | Batches 01–09 source contracts |
| Backend | trusted persistence, auth, idempotency, API | accepted domain contract |
| Frontend | feature-gated responsive views and errors | read model and approved art |
| Content | candidate definitions, content validation and authoring | catalog schema and editorial policy |
| QA/reliability | property tests, concurrency/load, rollback rehearsal | backend and test fixtures |

## Proposed GitHub issue cut
- **B13-01** — Competitive product scope and category definitions: define scope, contract, golden fixture, tests and review owner.
- **B13-02** — Official score authority and trust states: define scope, contract, golden fixture, tests and review owner.
- **B13-03** — Normalized competition profile: define scope, contract, golden fixture, tests and review owner.
- **B13-04** — Rank metrics, comparator and tie-break: define scope, contract, golden fixture, tests and review owner.
- **B13-05** — Leaderboard scope and query model: define scope, contract, golden fixture, tests and review owner.
- **B13-06** — Weekly seasons and immutable editions: define scope, contract, golden fixture, tests and review owner.
- **B13-07** — Verification engine and replay proof: define scope, contract, golden fixture, tests and review owner.
- **B13-08** — Score submission, queue and duplicate handling: define scope, contract, golden fixture, tests and review owner.
- **B13-09** — Best attempt and entry policy: define scope, contract, golden fixture, tests and review owner.
- **B13-10** — Bracket tournaments and matchmaking later: define scope, contract, golden fixture, tests and review owner.
- **B13-11** — Leagues, divisions and promotion/relegation: define scope, contract, golden fixture, tests and review owner.
- **B13-12** — Season prize policy and cosmetic rewards: define scope, contract, golden fixture, tests and review owner.
- **B13-13** — Leaderboard caching and storage strategy: define scope, contract, golden fixture, tests and review owner.
- **B13-14** — Pagination, rank windows and performance: define scope, contract, golden fixture, tests and review owner.
- **B13-15** — Regions, privacy and social visibility: define scope, contract, golden fixture, tests and review owner.
- **B13-16** — Competitive identity and display-name moderation: define scope, contract, golden fixture, tests and review owner.
- **B13-17** — Cross-platform and offline ranking behavior: define scope, contract, golden fixture, tests and review owner.
- **B13-18** — Competition page and HUD UX: define scope, contract, golden fixture, tests and review owner.

## Pull request acceptance
- Separate branch and PR per domain; DO NOT self-merge. Review dependent contracts and wait for coordinator/owner approval.
- Include migration forward/backward behavior, feature flag status, config hashes, typed error states and test output.
- UI PRs include accessible mobile + desktop screens, disabled/error/empty/loading examples, and owner-directed manual acceptance instructions.
- Never connect unverified local preview evidence to trusted coins, XP, owned items, shop state, rank or social prizes.
- Prefer one end-to-end vertical slice to fifteen disconnected demo screens; no production claim until exercised against the actual service.

## First useful milestone
Certify replay worker and normalized profile first → Add verified score submit/decision states.

## Risks and unresolved policies
Batch 02 physics/replay; Batch 04 scoring and missions; Batch 06 rewards; Batch 07 normalized skills; Batch 08 prize entitlements; Batch 14 friends and crews.

## Explicit deferred scope
One normalized weekly global challenge after verified server replay (candidate v0.5.0); historical seasons/divisions v0.5.1+; tournaments and opt-in regional boards after safeguards.
