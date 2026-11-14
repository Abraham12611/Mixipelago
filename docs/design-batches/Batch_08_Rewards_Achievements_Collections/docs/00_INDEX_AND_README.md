# Batch 8 — Rewards, Achievements & Collections

**Status:** Engineering specification and authoring pack · 2026-11-14 · Proposed, not implemented.

This batch connects the previously defined merge game, mission rules, campaign unlocks, trusted wallet, and entrepreneurial XP to verified achievements, reward entitlements, collections and cosmetic ownership. It does **not** supersede those domains' authority.

## Previous contracts that remain binding

- **Batch 2:** fixed-step physics and deterministic merge arbitration; no client raw-contact event issues durable rewards.
- **Batch 3:** eight-tier drink ladder, tier 8 terminal, new matching output auto-serves the oldest pending order before further chain reactions.
- **Batch 4:** mission result, stars, scoring, trusted run verification and the two-order Coconut Cove baseline.
- **Batch 5:** published campaign graph, map treasure eligibility, stars/progression and claim identity.
- **Batch 6:** spendable coin wallet, ledger, shop purchases and source idempotency. Alpha preview coins are never convertible.
- **Batch 7:** trusted first-clear XP, level milestones and skill points; no XP from simply opening the app, ad views, raw merges or client preview currency.

## Chapter index

- [01 — Vision, Player Promise and Scope](01_01_PRODUCT_VISION_SCOPE_AND_GOALS.md)
- [02 — Rewards Taxonomy and Authority Matrix](02_02_REWARD_TAXONOMY_AND_SOURCE_OF_TRUTH.md)
- [03 — Reward Sources, Verification and Policy Precedence](03_03_REWARD_SOURCES_ELIGIBILITY_AND_PRIORITY.md)
- [04 — Entitlement State Machine and Recovery](04_04_ENTITLEMENT_LIFECYCLE_AND_CLAIM_STATES.md)
- [05 — Reward Policy Resolver, Budgets and Caps](05_05_REWARD_POLICY_ENGINE_AND_BUDGETS.md)
- [06 — Atomic Settlement, Receipts and Idempotency](06_06_ATOMIC_SETTLEMENT_IDEMPOTENCY_AND_OUTBOX.md)
- [07 — Achievements: Definitions, Evidence and Rule DSL](07_07_ACHIEVEMENT_DEFINITION_GRAPH_AND_DSL.md)
- [08 — Counters, Projections and Replay-safe Evaluation](08_08_ACHIEVEMENT_COUNTERS_STREAM_PROCESSING_AND_REBUILD.md)
- [09 — Achievement Categories and Example Catalog](09_09_ACHIEVEMENT_CATEGORIES_AND_BADGE_PROGRAMS.md)
- [10 — Trophies, Titles, Tier Badges and Display](10_10_TROPHIES_TIERS_TITLES_AND_DISPLAY.md)
- [11 — Optional Daily Rewards and UTC Windows](11_11_DAILY_REWARDS_GIFTS_AND_RESET_WINDOWS.md)
- [12 — Weekly Challenges, Activity Rewards and Task Boards](12_12_WEEKLY_CHALLENGES_AND_ACTIVITY_REWARDS.md)
- [13 — Streaks, Rest Days and Ethical Engagement](13_13_STREAKS_REST_AND_ANTI_COMPULSION_POLICY.md)
- [14 — Milestones, First Clears and Chapter Rewards](14_14_MILESTONES_CHAPTERS_AND_ONETIME_REWARDS.md)
- [15 — Map Treasures, Chests and Hidden Rewards](15_15_TREASURE_CHESTS_MAP_REWARDS_AND_SECRETS.md)
- [16 — Randomized Rewards, Odds, Guarantees and Safety](16_16_REWARD_CHEST_ODDS_DISCLOSURE_AND_SAFETY.md)
- [17 — Collections, Albums, Editions and Completion](17_17_COLLECTIONS_ALBUMS_SETS_AND_COMPLETION.md)
- [18 — Collectible Catalog, Rarity and Provenance](18_18_COLLECTIBLE_RARITY_EDITIONING_AND_PROVENANCE.md)
- [19 — Cosmetics, Ownership, Equipment and Showrooms](19_19_COSMETICS_OWNERSHIP_EQUIPPING_AND_SHOWROOMS.md)
- [20 — Prestige, Trophy Rooms and Long-term Vanity](20_20_PRESTIGE_GALLERIES_AND_VANITY_PROGRESSION.md)
- [21 — Seasonal, Ranked and Social Reward Contracts](21_21_SEASONAL_RANKED_AND_FRIEND_REWARD_HANDOFF.md)
- [22 — Events, Live Operations and Retired Content](22_22_EVENT_INTEGRATIONS_ROTATIONS_AND_LEGACY_CONTENT.md)
- [23 — Mobile UX: Rewards Inbox, Achievements and Albums](23_23_MOBILE_REWARDS_ACHIEVEMENTS_AND_ALBUM_UX.md)
- [24 — Desktop UX: Gallery, Comparison and Navigation](24_24_DESKTOP_UI_TROPHY_SHOWROOM_AND_NAVIGATION.md)
- [25 — Game Feel: Reward Presentation, SFX and Animation](25_25_PRESENTATION_SFX_VFX_AND_CELEBRATION_HIERARCHY.md)
- [26 — Onboarding, Progressive Disclosure and Failure Recovery](26_26_ONBOARDING_EDUCATION_AND_RECOVERY_PATHS.md)
- [27 — Accessibility, Localization, Privacy and Player Protection](27_27_ACCESSIBILITY_LOCALIZATION_PRIVACY_AND_YOUTH.md)
- [28 — Content Studio: Authoring, Review and Publication](28_28_CONTENT_STUDIO_AUTHORING_VALIDATION_AND_ROLLOUT.md)
- [29 — PostgreSQL Schema, RLS, Indexes and Migration](29_29_POSTGRESQL_SCHEMA_RLS_AND_MIGRATION.md)
- [30 — HTTP APIs, Idempotency and Error Codes](30_30_HTTP_API_COMMANDS_RESPONSES_AND_ERRORS.md)
- [31 — TypeScript Package Boundaries and Events](31_31_TYPESCRIPT_PACKAGES_EVENTS_AND_ISSUER_HANDOFF.md)
- [32 — Security, Fraud and Abuse Threat Model](32_32_SECURITY_ABUSE_ANTICHEAT_AND_THREAT_MODEL.md)
- [33 — Balancing, Economy Impact and Fairness Simulation](33_33_BALANCING_ECONOMY_FAIRNESS_AND_SIMULATIONS.md)
- [34 — Telemetry, Experiments, Reconciliation and Operations](34_34_ANALYTICS_EXPERIMENTATION_AND_RECONCILIATION.md)
- [35 — Performance, Offline Preview and Cross-device Sync](35_35_PERFORMANCE_OFFLINE_CACHE_AND_SYNC.md)
- [36 — Versioning, Migration, Rollback and Integrity Preservation](36_36_MIGRATIONS_CONTENT_VERSIONING_AND_ROLLBACK.md)
- [37 — QA Matrix, Property Tests and Acceptance](37_37_QA_SECURITY_PROPERTY_AND_MANUAL_TESTS.md)
- [38 — Incremental Release Plan and Feature Gates](38_38_RELEASE_SLICES_FEATURE_GATES_AND_DEPENDENCIES.md)
- [39 — Parallel Engineering Workstreams and Issue Backlog](39_39_PARALLEL_ENGINEERING_WORKSTREAMS_AND_ISSUES.md)
- [40 — Architecture Decisions, Conflicts and Owner Decisions](40_40_ADRS_CONFLICTS_OPEN_QUESTIONS_AND_DECISIONS.md)
- [41 — End-to-End Journeys and Failure Case Stories](41_41_END_TO_END_USER_JOURNEYS_AND_EDGE_CASES.md)
- [42 — Glossary, References and Non-goals](42_42_GLOSSARY_REFERENCE_LINKS_AND_LIMITS.md)
- [43 — Requirement Traceability, Acceptance and Definition of Done](43_43_REQUIREMENT_TRACEABILITY_AND_DEFINITION_OF_DONE.md)
- [44 — Engineer Kickoff, Build Order and Contract Freeze](44_44_ENGINEER_KICKOFF_FIRST_SHIPPABLE_SLICE.md)

## Machine-readable support

- `../examples/catalog/reward-catalog.draft.json`: candidate achievements, reward policies, items, albums and chest examples (all draft).
- `../examples/schemas/reward-catalog.schema.json`: JSON Schema for draft authoring.
- `../examples/tests/reward-rule-vectors.json`: expected eligibility, uniqueness, progress and settlement logic.
- `../examples/contracts/reward-api-examples.json`: future API requests/responses.
- `../examples/contracts/reward-rules-reference.ts`: pure reference functions.
- `../examples/sql/rewards_schema_draft.sql`: **illustrative only**, not a production migration.
- `../tools/validate_batch8.py`: static validator and pure fixture checks.

## Engineer reading order

`01–08 → 14–19 → 23–31 → 32–44`. If implementing only the early slice, read 02–08, 14, 29–31, 37–39 and 44. Future seasonal/randomized programs must stay disabled until their producer and compliance requirements are satisfied.

## Release guardrails

The smallest useful release is one **verified** achievement → one claimable badge → one inventory ownership → one equip projection. No full chest system or calendar task board is needed for the first slice. Manual UI/gameplay tests are directed to the owner.
