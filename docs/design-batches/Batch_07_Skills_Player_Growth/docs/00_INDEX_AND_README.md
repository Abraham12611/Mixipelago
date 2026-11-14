# Batch 7 — Skills, Specializations and Player Growth

**Status:** engineering design specification only · November 14, 2026 · Not implemented or deployed.

## Required earlier contracts
- Batch 2: fixed-step physics and exactly-once merge events; no implicit physics-altering talents.
- Batch 3: one eight-tier drink chain and auto-serve oldest eligible customer before further chain reactions.
- Batch 4: verified mission results and scoring; no client-level XP grants.
- Batch 5: published mission graph and separate node unlock/reward-claim identities.
- Batch 6: trusted wallet, modifier engine, capped customer probabilities, idempotent finance operations.

**v0.4.0** is a proposal for the first trusted XP and skill allocation release; it does not modify v0.1.x playable alpha.

## Chapters (41)

- [01 — Product Scope, Player Fantasy and Design Tenets](01_01_PRODUCT_SCOPE_AND_PLAYER_PROMISE.md)
- [02 — Progression Layers and Shared Vocabulary](02_02_PROGRESSION_LAYERS_AND_TERMINOLOGY.md)
- [03 — Entrepreneur XP Curve, Levels, Caps and Pacing](03_03_XP_LEVEL_CURVE_AND_CAPS.md)
- [04 — XP Sources, Verification and Reward Receipts](04_04_XP_REWARD_SOURCES_AND_AWARD_POLICY.md)
- [05 — Canonical Skill Tree Graph and Prerequisite DSL](05_05_SKILL_TREE_GRAPH_AND_PRECONDITIONS.md)
- [06 — Specializations, Build Archetypes and Hybrid Play](06_06_SIX_SPECIALIZATIONS_AND_BUILD_IDENTITIES.md)
- [07 — Master Mixologist Skill Branch: Design and Constraints](07_07_MIXOLOGIST_BRANCH.md)
- [08 — Hospitality Skill Branch: Guests, Tips and Loyalty](08_08_HOSPITALITY_BRANCH.md)
- [09 — Business Mogul Skill Branch: Efficiency and Investment](09_09_MOGUL_BRANCH.md)
- [10 — Explorer Skill Branch: Routes, Secrets and Discovery](10_10_EXPLORER_BRANCH.md)
- [11 — Risk Strategist Skill Branch: Preparedness and Recovery](11_11_RISK_BRANCH.md)
- [12 — Puzzle Specialist Skill Branch: Planning and Boosters](12_12_PUZZLE_BRANCH.md)
- [13 — Active Skills, Passive Skills and Loadout Constraints](13_13_ACTIVE_PASSIVE_AND_LOADOUT_POLICY.md)
- [14 — Typed Modifier Engine: Sources, Projections and Ownership](14_14_TYPED_EFFECT_ENGINE_AND_INTEGRATION.md)
- [15 — Modifier Stacking, Caps, Rounding and Conflict Resolution](15_15_STACKING_CAPS_AND_NUMERIC_RULES.md)
- [16 — Skill Allocation: Eligibility, Validation and Transactions](16_16_SKILL_PURCHASE_RULES_AND_PREREQUISITES.md)
- [17 — Skill Point Budget, Milestones and Anti-Farming](17_17_POINTS_MILESTONES_AND_REWARD_RULES.md)
- [18 — Respec, Refunds, Previewing Builds and Undo](18_18_RESPEC_AND_BUILD_EXPERIMENTATION.md)
- [19 — Drink Mastery and Craft Proficiency (Later Feature)](19_19_DRINK_MASTERY_AND_RECIPE_EXPERTISE.md)
- [20 — Player Identity, Reputation and Shop Effects](20_20_PLAYER_REPUTATION_AND_SHOP_HANDOFF.md)
- [21 — Campaign and Island Integration](21_21_CAMPAIGN_UNLOCKS_AND_PLAYER_LEVEL_GATES.md)
- [22 — Normalized Competition, Skills and Leaderboard Integrity](22_22_RANKED_NORMALIZATION_AND_ANTICHEAT.md)
- [23 — Hospitality Modifiers and the Customer Director](23_23_CUSTOMER_DIRECTOR_EFFECTS_AND_FAIR_SPAWNING.md)
- [24 — Mobile UI: Skill Tree, Level-Up and Builds](24_24_MOBILE_UI_SKILL_TREE_AND_PROFILE.md)
- [25 — Desktop UI: Skill Tree, Comparison and Planning](25_25_DESKTOP_UI_SKILL_TREE_AND_BUILD_PLANNER.md)
- [26 — Tutorial, First Point and Progressive Disclosure](26_26_FIRST_SKILL_ONBOARDING_AND_EDUCATION.md)
- [27 — Accessibility, Localization and Player Trust](27_27_ACCESSIBILITY_LOCALIZATION_AND_PLAYER_TRUST.md)
- [28 — Skill Economy Telemetry, Balance and Experiments](28_28_BALANCE_TELEMETRY_AND_EXPERIMENTS.md)
- [29 — Content Studio: Author, Validate, Preview and Publish Skills](29_29_SKILL_CONTENT_STUDIO_AND_PUBLICATION.md)
- [30 — PostgreSQL Tables, RLS and Trusted Persistence](30_30_DATABASE_SCHEMA_AND_RLS.md)
- [31 — API Contracts, Idempotent Commands and Domain Events](31_31_API_CONTRACTS_DOMAIN_EVENTS_AND_ERRORS.md)
- [32 — TypeScript Packages, Effect Resolver and Integration Order](32_32_TYPESCRIPT_PACKAGE_AND_SERVICE_BLUEPRINT.md)
- [33 — Feature Flags, Catalog Migration, Compatibility and Rollback](33_33_VERSION_MIGRATION_COMPATIBILITY_AND_FLAGS.md)
- [34 — Threat Model, Abuse Cases and Security Controls](34_34_SECURITY_THREAT_MODEL_AND_EXPLOIT_GUARDS.md)
- [35 — QA Matrix, Fixtures, Property Tests and Manual Acceptance](35_35_QA_TEST_MATRIX_AND_PROPERTY_TESTS.md)
- [36 — Release Roadmap: First Skill Slice Through Full Tree](36_36_RELEASE_SLICES_AND_FEATURE_GATES.md)
- [37 — Parallel Engineering Workstreams and Issue Backlog](37_37_ENGINEERING_WORKSTREAMS_AND_GITHUB_ISSUES.md)
- [38 — Architecture Decisions, Risks, Open Questions and Glossary](38_38_ARCHITECTURE_DECISIONS_GLOSSARY_AND_RISKS.md)
- [39 — Requirement Traceability, Acceptance Gates and Definition of Done](39_39_REQUIREMENT_TRACEABILITY_AND_DEFINITION_OF_DONE.md)
- [40 — End-to-End Player Journeys and Failure Recovery](40_40_END_TO_END_PLAYER_JOURNEYS.md)
- [41 — Engineer Kickoff, Build Order and Handoff Rules](41_41_ENGINEER_KICKOFF_AND_FIRST_SHIPPABLE_SLICE.md)

## Machine-readable examples
- `../examples/catalog/skills-catalog.draft.json`: 30 candidate skills, 6 branches, 6 pilot nodes and 24 gated drafts.
- `../examples/catalog/entrepreneur-xp-policy.draft.json`: integer level thresholds and point milestone policy.
- `../examples/schemas/skill-catalog.schema.json`: JSON syntax contract.
- `../examples/tests/`: XP, skill, caps, normalization and respec vectors.
- `../examples/contracts/`: proposed API payloads and pure TypeScript formulas.
- `../examples/sql/progression_schema_draft.sql`: draft only, not a deployable production migration.
- `../tools/validate_batch7.py`: static validator, no physics/browser integration.

## Reading order for engineers
01–06 → assigned branch chapter 07–12 → effects 13–18 → domain handoffs 19–23 → UX 24–27 → backend 30–34 → QA/release 35–41.

**Release gates:** only trusted verified first-clear XP may create points; ranking must use a normalized competitive profile; all manual UI/gameplay tests go through the owner.
