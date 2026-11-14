# Batch 13 — Leaderboards, Rankings & Tournaments

**Status:** design and engineering pack · 2026-11-14 · not an implemented feature.

## Product promise
Competition that measures actual drink-shooting skill under equivalent rules, with clear tie-breaking, privacy controls, verifiable scores and trustworthy rewards.

## Source-of-truth boundaries
- Batch 02 alone owns fixed-step Rapier physics, collision/merge arbitration, and immutable simulation outcome semantics. No new feature writes physical contacts or awards rewards from visual effects.
- Batch 03 owns the eight-tier alpha ladder and newly merged drink auto-serving to oldest compatible active order; Batch 04 owns mission goals, stars and win/loss state.
- Batch 05 owns campaign graph visibility/unlocks; Batch 06 owns wallet and financial ledger; Batch 07 owns XP/skills; Batch 08 owns reward/collectible entitlements; Batch 09 owns customer/relationship facts while shop reputation settlement remains under Batch 06.
- Client previews and unverified sessions are not currency, XP, competitive score, badge provenance, or trusted activity evidence. All durable grants derive from unique verified receipts.
- Ranked play freezes the physics/scoring/content/seed profile and disables non-normalized world, shop, skill, story, social and cosmetic advantages.
- Every stage is a proposal, not a claim of implementation. Manual browser and gameplay acceptance belongs to the owner. Engineers open PRs and do not self-merge.

**This batch specifically owns:** Score submission/proof validation, ranking materialization, season freeze, divisions and tournament adjudication.

**External integrations:** Batch 02 physics/replay; Batch 04 scoring and missions; Batch 06 rewards; Batch 07 normalized skills; Batch 08 prize entitlements; Batch 14 friends and crews.

## Documents and reading order
- [01 — Competitive product scope and category definitions](01_COMPETITIVE_PRODUCT_SCOPE_AND_CATEGORY_DEFINITIONS.md)
- [02 — Official score authority and trust states](02_OFFICIAL_SCORE_AUTHORITY_AND_TRUST_STATES.md)
- [03 — Normalized competition profile](03_NORMALIZED_COMPETITION_PROFILE.md)
- [04 — Rank metrics, comparator and tie-break](04_RANK_METRICS_COMPARATOR_AND_TIE_BREAK.md)
- [05 — Leaderboard scope and query model](05_LEADERBOARD_SCOPE_AND_QUERY_MODEL.md)
- [06 — Weekly seasons and immutable editions](06_WEEKLY_SEASONS_AND_IMMUTABLE_EDITIONS.md)
- [07 — Verification engine and replay proof](07_VERIFICATION_ENGINE_AND_REPLAY_PROOF.md)
- [08 — Score submission, queue and duplicate handling](08_SCORE_SUBMISSION_QUEUE_AND_DUPLICATE_HANDLING.md)
- [09 — Best attempt and entry policy](09_BEST_ATTEMPT_AND_ENTRY_POLICY.md)
- [10 — Bracket tournaments and matchmaking later](10_BRACKET_TOURNAMENTS_AND_MATCHMAKING_LATER.md)
- [11 — Leagues, divisions and promotion/relegation](11_LEAGUES_DIVISIONS_AND_PROMOTION_RELEGATION.md)
- [12 — Season prize policy and cosmetic rewards](12_SEASON_PRIZE_POLICY_AND_COSMETIC_REWARDS.md)
- [13 — Leaderboard caching and storage strategy](13_LEADERBOARD_CACHING_AND_STORAGE_STRATEGY.md)
- [14 — Pagination, rank windows and performance](14_PAGINATION_RANK_WINDOWS_AND_PERFORMANCE.md)
- [15 — Regions, privacy and social visibility](15_REGIONS_PRIVACY_AND_SOCIAL_VISIBILITY.md)
- [16 — Competitive identity and display-name moderation](16_COMPETITIVE_IDENTITY_AND_DISPLAY_NAME_MODERATION.md)
- [17 — Cross-platform and offline ranking behavior](17_CROSS_PLATFORM_AND_OFFLINE_RANKING_BEHAVIOR.md)
- [18 — Competition page and HUD UX](18_COMPETITION_PAGE_AND_HUD_UX.md)
- [19 — Match review and anti-cheat appeal](19_MATCH_REVIEW_AND_ANTI_CHEAT_APPEAL.md)
- [20 — Competitive fraud model and limits](20_COMPETITIVE_FRAUD_MODEL_AND_LIMITS.md)
- [21 — Moderation, disputes and tournament integrity](21_MODERATION_DISPUTES_AND_TOURNAMENT_INTEGRITY.md)
- [22 — Competition content authoring and publication](22_COMPETITION_CONTENT_AUTHORING_AND_PUBLICATION.md)
- [23 — Leaderboard APIs and domain event contracts](23_LEADERBOARD_APIS_AND_DOMAIN_EVENT_CONTRACTS.md)
- [24 — Database, RLS, score events and retention](24_DATABASE_RLS_SCORE_EVENTS_AND_RETENTION.md)
- [25 — Distributed verification workers and reliability](25_DISTRIBUTED_VERIFICATION_WORKERS_AND_RELIABILITY.md)
- [26 — QA, golden replays and stress tests](26_QA_GOLDEN_REPLAYS_AND_STRESS_TESTS.md)
- [27 — Telemetry, uptime and kill switches](27_TELEMETRY_UPTIME_AND_KILL_SWITCHES.md)
- [28 — Release plan, issue backlog and sign-off](28_RELEASE_PLAN_ISSUE_BACKLOG_AND_SIGN_OFF.md)
- [29 — ADR, requirement traceability and glossary](29_ADR_REQUIREMENT_TRACEABILITY_AND_GLOSSARY.md)

## Supporting machine-readable files
- `../examples/catalog/catalog.draft.json` — feature-gated sample definitions, never production-approved.
- `../examples/schemas/catalog.schema.json` — strict JSON schema for the sample catalog.
- `../examples/tests/pure-rule-vectors.json` — expected pure-rule behavior.
- `../examples/tests/invalid-case-mutations.json` — intentionally invalid content mutation cases.
- `../examples/contracts/api-examples.json` — endpoint and event shapes; not deployed routes.
- `../examples/contracts/domain-reference.ts` — typed rule reference; not integrated runtime code.
- `../examples/sql/schema_draft.sql` — illustrative PostgreSQL design, NOT an approved migration.
- `../tools/validate_batch13.py` — local static validator (requires `jsonschema`).

## Target release policy
One normalized weekly global challenge after verified server replay (candidate v0.5.0); historical seasons/divisions v0.5.1+; tournaments and opt-in regional boards after safeguards.

## Engineer order
1. Certify replay worker and normalized profile first
2. Add verified score submit/decision states
3. Materialize one public weekly board and around-me query
4. Freeze season and settle cosmetic prizes via Batch 08
5. Add filters/divisions/tournament only after privacy and moderation

## Acceptance not implied
Schema, fixture and documentation validation do not prove actual game physics solvability, performance, user delight, secure production APIs, compliance or manual UI approval. Those are separate implementation gates.

## Companion document references
- `Batch 01 / docs/12_SOCIAL_AND_LEADERBOARDS_OVERVIEW.md`
- `Batch 04 / docs/28_REPLAY_VALIDATION_AND_TRUST.md`
- `Batch 07 / docs/22_22_RANKED_NORMALIZATION_AND_ANTICHEAT.md`
