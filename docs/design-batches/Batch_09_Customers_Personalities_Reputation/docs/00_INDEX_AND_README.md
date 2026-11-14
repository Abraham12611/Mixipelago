# Batch 9 — Customers, Personalities & Reputation

**Status:** engineering specification only · 2026-11-14 · Proposed, not implemented or deployed. **Documentation batch 9 of 21.**

## Scope and compatibility

- Keep Batch 2 Rapier collision/merge semantics unchanged; guest art has no physics authority.
- Keep Batch 3 oldest-first automatic service of *newly merged outputs*; no board-drink retroactive service.
- Keep Batch 4 `coconut-cove-001` at **two scripted customer orders, two-order win**, fixed-stage 60Hz gameplay and terminal win priority.
- Batch 5 owns published mission graph and unlock state. Batch 6 owns trusted coins, shop reputation and economic effects; Batch 7 owns XP, skill modifiers and standardized ranked profiles; Batch 8 owns achievement/collectible entitlements.
- All new customer trust systems are future gated; there is **no legitimate route from local preview coins or NPC animations to durable rewards**.

## Full chapter index (45 chapters)

- [01 — Product Vision, Scope and Player Promise](01_PRODUCT_VISION_SCOPE_AND_PLAYER_PROMISE.md)
- [02 — Core Domain, Identities and Sources of Truth](02_DOMAIN_GLOSSARY_AND_AUTHORITY_MATRIX.md)
- [03 — Customer Definition, Instance, Encounter and Lifecycle](03_CUSTOMER_IDENTITY_AND_LIFECYCLE.md)
- [04 — Customer Segments, Archetypes and Fictional Roles](04_SEGMENTS_ARCHETYPES_AND_CHARACTER_ROLES.md)
- [05 — Personality Traits, Expressions and Behavioral Policies](05_PERSONALITY_TRAITS_AND_BEHAVIOR_MODEL.md)
- [06 — Taste Profiles, Favorite Drinks and Recipe Compatibility](06_PREFERENCES_TASTE_PROFILES_AND_RECIPES.md)
- [07 — Customer Director: Eligibility, Deterministic Selection and Reservations](07_CUSTOMER_DIRECTOR_ELIGIBILITY_AND_SELECTION.md)
- [08 — Order Generation, Difficulty Fairness and Spawn Integration](08_ORDER_FAIRNESS_FEASIBILITY_AND_SPAWN_CONTROL.md)
- [09 — Service Lifecycle, Event Ordering and Exactly-once Fulfillment](09_SERVICE_PIPELINE_AND_ORDER_EVENTS.md)
- [10 — Satisfaction Model, Deterministic Scoring and Feedback](10_SATISFACTION_MODEL_AND_FEEDBACK.md)
- [11 — Customer Patience, Deadlines and Pause Semantics](11_PATIENCE_TIMERS_AND_ACTIVE_SESSION_CLOCK.md)
- [12 — Recurring Visitors, Loyalty, Affinity and Return Journeys](12_RECURRING_GUESTS_AND_LOYALTY.md)
- [13 — Shop Reputation, Prestige and Business Integrity](13_SHOP_REPUTATION_AND_PRESTIGE_BOUNDARY.md)
- [14 — Customer Reviews, Complaints and Service Recovery](14_REVIEWS_COMPLAINTS_AND_SERVICE_RECOVERY.md)
- [15 — VIP Guests, Premium Encounters and Transparent Risk](15_VIP_GUESTS_ELIGIBILITY_AND_CHALLENGES.md)
- [16 — Critics, Special Guests and Quest Integration](16_CRITICS_SPECIAL_GUESTS_AND_NARRATIVE_HANDOFF.md)
- [17 — Groups, Families and Multi-line Orders](17_GROUP_CUSTOMERS_BUNDLES_AND_PARTY_REQUESTS.md)
- [18 — Island Regions, Visitor Pools and Cultural Presentation](18_ISLAND_BIOMES_AND_REGIONAL_VISITORS.md)
- [19 — Skill Tree Integration, Modifier Precedence and Caps](19_SKILL_MODIFIERS_AND_CUSTOMER_EFFECT_CAPS.md)
- [20 — Customer Rewards, Tips, Coins and Economic Source Boundaries](20_ECONOMY_TIPS_REWARDS_AND_SETTLEMENT_HANDOFF.md)
- [21 — Achievements, Souvenirs, Collectibles and Journal Integration](21_ACHIEVEMENTS_COLLECTIONS_AND_CUSTOMER_SOUVENIRS.md)
- [22 — Future World Events, Weather, Incidents and Rivals: Interface Overview](22_DYNAMIC_EVENTS_WEATHER_INCIDENTS_AND_RIVALS_HANDOFF.md)
- [23 — Gameplay Customer HUD: Mobile, Tablet and Desktop](23_CUSTOMER_HUD_MOBILE_AND_DESKTOP_UX.md)
- [24 — Guest Journal, Loyalty and Shop Reputation Screens](24_GUEST_JOURNAL_RELATIONSHIPS_AND_REPUTATION_UX.md)
- [25 — Character Art, Portraits, 2.5D States and Asset Pipeline](25_CHARACTER_ART_PORTRAITS_AND_STATE_ASSETS.md)
- [26 — Dialogue System, Voice, Sound Effects and Localization](26_DIALOGUE_VOICE_SFX_AND_LOCALIZATION_PRODUCTION.md)
- [27 — Accessibility, Inclusive Design, Privacy and Player Protection](27_ACCESSIBILITY_PRIVACY_YOUTH_AND_CONTENT_STANDARDS.md)
- [28 — Customer Catalog IDs, Versioning, Publication and Migration](28_CONTENT_CATALOGS_VERSIONING_AND_PUBLISHING.md)
- [29 — HTTP API, Commands, Read Models and Error Semantics](29_HTTP_API_COMMANDS_AND_ERROR_CONTRACTS.md)
- [30 — PostgreSQL Data Model, RLS and Forward-only Migration](30_POSTGRES_SCHEMA_RLS_AND_MIGRATION_DRAFT.md)
- [31 — TypeScript Modules, Event Contracts and Reducer Blueprint](31_TYPESCRIPT_PACKAGES_EVENTS_AND_REDUCERS.md)
- [32 — Seeded RNG, Replay Verification and Deterministic Sampling](32_SEEDED_RNG_REPLAY_AND_VERSIONED_ENCOUNTERS.md)
- [33 — Threat Model, Abuse Prevention and Security Controls](33_SECURITY_PRIVACY_ANTICHEAT_AND_ABUSE.md)
- [34 — Analytics, Feedback Loops and Experimentation](34_ANALYTICS_EXPERIMENTS_AND_METRICS.md)
- [35 — Customer Balance Models, Probability Simulations and Fairness](35_BALANCING_SIMULATION_AND_FAIRNESS.md)
- [36 — Customer Content Studio: Authoring and Publish Gates](36_CONTENT_STUDIO_AUTHORING_REVIEW_AND_DEPLOY.md)
- [37 — QA Matrix: Unit, Integration, Property, Browser and Security](37_QA_TEST_MATRIX_PROPERTY_AND_INTEGRATION.md)
- [38 — Performance, Asset Streaming, Offline Preview and Sync](38_PERFORMANCE_CACHING_OFFLINE_AND_SYNC.md)
- [39 — Incremental Releases, Feature Flags and Rollback Plans](39_RELEASE_PHASES_FEATURE_GATES_AND_ROLLBACK.md)
- [40 — Parallel Engineering Workstreams and Proposed Issues](40_ENGINEERING_WORKSTREAMS_ISSUE_BACKLOG.md)
- [41 — Architecture Decisions, Trade-offs and Open Questions](41_ADRS_DECISIONS_RISKS_AND_OWNER_QUESTIONS.md)
- [42 — Representative Player Journeys and Failure Recoveries](42_END_TO_END_PLAYER_JOURNEYS_AND_RECOVERY.md)
- [43 — Requirement Traceability, Acceptance Evidence and Definition of Done](43_TRACEABILITY_ACCEPTANCE_AND_DEFINITION_OF_DONE.md)
- [44 — Engineering Kickoff and First Shippable Customer Slice](44_ENGINEER_KICKOFF_AND_FIRST_SHIPPABLE_SLICE.md)
- [45 — Glossary, Internal References, Technical Links and Non-goals](45_GLOSSARY_INTERNAL_REFERENCES_AND_NON_GOALS.md)

## Supporting artifacts

- `../examples/catalog/customer-catalog.draft.json`: 14 fictional customer definitions, 7 segments, 6 pools, candidate policy and OFF feature gates.
- `../examples/catalog/dialogue-briefs.draft.json`: sample original dialogue.
- `../examples/schemas/customer-catalog.schema.json`: strict draft schema and release guardrails.
- `../examples/contracts/customer-events-and-api-examples.json`: server and read-model event examples.
- `../examples/contracts/example-encounters.draft.json`: scripted / dynamic / VIP encounter examples.
- `../examples/contracts/customer-rules-reference.ts`: candidate pure integer math and weighted sampling.
- `../examples/tests/customer-rule-vectors.json`: positive rule fixtures.
- `../examples/sql/customer_schema_draft.sql`: **ILLUSTRATIVE ONLY**, not a production migration.
- `../tools/validate_batch9.py`: Python static validator; requires `jsonschema`.

Run `python tools/validate_batch9.py` from the batch root. Static validation does **not** prove mission physical solvability, real settlement integrity, UI performance, or manual gameplay acceptance.

## Engineering reading order

01–10 and 13 for core domain; 07–09 and 31–33 for implementation; 23–29 for UI/content; 30 and 34–39 for persistence/ops/QA; 40–45 for team handoff. Earlier Batch 3/4 contracts take precedence for order semantics; any change requires an approved ADR.

## Proposed release slices

- v0.1.x: scripted customer cards, accessible order feedback, two original portraits and short serving reactions only.
- v0.4.2: **candidate** verified service observations and read-only reputation after Batch 6 authority exists.
- v0.4.3+: guest journal and one recurring visitor behind gates.
- v0.5.x+ / later: VIP/critic, optional deadlines, group guests, event-driven demand.

Manual interface/gameplay testing is directed to the project owner. Engineers open PRs, do not merge their own code, and obtain owner approval for releases to main.
