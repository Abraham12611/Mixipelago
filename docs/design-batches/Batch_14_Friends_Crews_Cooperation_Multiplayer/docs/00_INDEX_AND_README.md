# Batch 14 — Friends, Crews, Cooperation & Multiplayer

**Status:** design and engineering pack · 2026-11-14 · not an implemented feature.

## Product promise
Welcoming, privacy-conscious social play that starts with safe asynchronous challenges and only adds real-time competition after authoritative networking is proven.

## Source-of-truth boundaries
- Batch 02 alone owns fixed-step Rapier physics, collision/merge arbitration, and immutable simulation outcome semantics. No new feature writes physical contacts or awards rewards from visual effects.
- Batch 03 owns the eight-tier alpha ladder and newly merged drink auto-serving to oldest compatible active order; Batch 04 owns mission goals, stars and win/loss state.
- Batch 05 owns campaign graph visibility/unlocks; Batch 06 owns wallet and financial ledger; Batch 07 owns XP/skills; Batch 08 owns reward/collectible entitlements; Batch 09 owns customer/relationship facts while shop reputation settlement remains under Batch 06.
- Client previews and unverified sessions are not currency, XP, competitive score, badge provenance, or trusted activity evidence. All durable grants derive from unique verified receipts.
- Ranked play freezes the physics/scoring/content/seed profile and disables non-normalized world, shop, skill, story, social and cosmetic advantages.
- Every stage is a proposal, not a claim of implementation. Manual browser and gameplay acceptance belongs to the owner. Engineers open PRs and do not self-merge.

**This batch specifically owns:** Friend relationships, crew membership and governance, social challenges, contributions, invitations and multiplayer session orchestration.

**External integrations:** Batch 13 rankings and verified replays; Batch 06 wallet; Batch 08 rewards; Batch 09 guest personalities; Batch 12 festival co-op; Batch 02 physics server certification.

## Documents and reading order
- [01 — Social promise and feature sequencing](01_SOCIAL_PROMISE_AND_FEATURE_SEQUENCING.md)
- [02 — Identity, visibility and default privacy](02_IDENTITY_VISIBILITY_AND_DEFAULT_PRIVACY.md)
- [03 — Friend request lifecycle and uniqueness](03_FRIEND_REQUEST_LIFECYCLE_AND_UNIQUENESS.md)
- [04 — Invitations, share links and referral safety](04_INVITATIONS_SHARE_LINKS_AND_REFERRAL_SAFETY.md)
- [05 — Blocking, reporting and safety center](05_BLOCKING_REPORTING_AND_SAFETY_CENTER.md)
- [06 — Asynchronous challenges and ghost runs](06_ASYNCHRONOUS_CHALLENGES_AND_GHOST_RUNS.md)
- [07 — Ghost visualization and input privacy](07_GHOST_VISUALIZATION_AND_INPUT_PRIVACY.md)
- [08 — Friend leaderboards and filtered ranking](08_FRIEND_LEADERBOARDS_AND_FILTERED_RANKING.md)
- [09 — Crew creation, naming and membership](09_CREW_CREATION_NAMING_AND_MEMBERSHIP.md)
- [10 — Crew roles, permissions and governance](10_CREW_ROLES_PERMISSIONS_AND_GOVERNANCE.md)
- [11 — Crew projects and cooperative milestones](11_CREW_PROJECTS_AND_COOPERATIVE_MILESTONES.md)
- [12 — Contribution caps, membership changes and rewards](12_CONTRIBUTION_CAPS_MEMBERSHIP_CHANGES_AND_REWARDS.md)
- [13 — Cooperative island building later](13_COOPERATIVE_ISLAND_BUILDING_LATER.md)
- [14 — Gifts and generosity safeguards](14_GIFTS_AND_GENEROSITY_SAFEGUARDS.md)
- [15 — Social notification inbox and consent](15_SOCIAL_NOTIFICATION_INBOX_AND_CONSENT.md)
- [16 — Social UI app map and responsive layout](16_SOCIAL_UI_APP_MAP_AND_RESPONSIVE_LAYOUT.md)
- [17 — Real-time multiplayer design boundary](17_REAL_TIME_MULTIPLAYER_DESIGN_BOUNDARY.md)
- [18 — Matchmaking, latency and region policy](18_MATCHMAKING_LATENCY_AND_REGION_POLICY.md)
- [19 — Real-time session lifecycle and pause semantics](19_REAL_TIME_SESSION_LIFECYCLE_AND_PAUSE_SEMANTICS.md)
- [20 — Transport, snapshot and reconciliation](20_TRANSPORT_SNAPSHOT_AND_RECONCILIATION.md)
- [21 — Spectators, replays and shared highlights](21_SPECTATORS_REPLAYS_AND_SHARED_HIGHLIGHTS.md)
- [22 — Moderation, conduct and team safety](22_MODERATION_CONDUCT_AND_TEAM_SAFETY.md)
- [23 — Social auth, API, RLS and audit](23_SOCIAL_AUTH_API_RLS_AND_AUDIT.md)
- [24 — Social data model and event contracts](24_SOCIAL_DATA_MODEL_AND_EVENT_CONTRACTS.md)
- [25 — Security, spam, abuse and cheating model](25_SECURITY_SPAM_ABUSE_AND_CHEATING_MODEL.md)
- [26 — QA and load-testing scenarios](26_QA_AND_LOAD_TESTING_SCENARIOS.md)
- [27 — Analytics and privacy-preserving health metrics](27_ANALYTICS_AND_PRIVACY_PRESERVING_HEALTH_METRICS.md)
- [28 — Phased releases, workstreams and gates](28_PHASED_RELEASES_WORKSTREAMS_AND_GATES.md)
- [29 — Architecture decisions and traceability](29_ARCHITECTURE_DECISIONS_AND_TRACEABILITY.md)

## Supporting machine-readable files
- `../examples/catalog/catalog.draft.json` — feature-gated sample definitions, never production-approved.
- `../examples/schemas/catalog.schema.json` — strict JSON schema for the sample catalog.
- `../examples/tests/pure-rule-vectors.json` — expected pure-rule behavior.
- `../examples/tests/invalid-case-mutations.json` — intentionally invalid content mutation cases.
- `../examples/contracts/api-examples.json` — endpoint and event shapes; not deployed routes.
- `../examples/contracts/domain-reference.ts` — typed rule reference; not integrated runtime code.
- `../examples/sql/schema_draft.sql` — illustrative PostgreSQL design, NOT an approved migration.
- `../tools/validate_batch14.py` — local static validator (requires `jsonschema`).

## Target release policy
Candidate v0.7.0 friends + asynchronous ghost challenges; v0.7.1 crew projects; v0.8.0+ real-time matches only after authoritative simulation, reconnect and moderation tests.

## Engineer order
1. Release privacy settings, block/report and friend graph
2. Add certified asynchronous challenge over Batch 13 verified runs
3. Add crew membership/permissions and one verified project
4. Test moderation, fairness, replay and recovery under concurrency
5. Prove authoritative live match server before any real-time UI launch

## Acceptance not implied
Schema, fixture and documentation validation do not prove actual game physics solvability, performance, user delight, secure production APIs, compliance or manual UI approval. Those are separate implementation gates.

## Companion document references
- `Batch 01 / docs/12_SOCIAL_AND_LEADERBOARDS_OVERVIEW.md`
- `Batch 13 / docs/00_INDEX_AND_README.md`
- `Batch 08 / docs/21_21_SEASONAL_RANKED_AND_FRIEND_REWARD_HANDOFF.md`
