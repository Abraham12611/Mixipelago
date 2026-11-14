# Mixipelago — Batch 3: Drinks, Recipes & Discovery

**Document status:** design/engineering handoff v0.3-draft, 2026-11-14. **Owner:** Mixipelago game director. **Audience:** gameplay, backend, UX, art, audio, content, QA, live-ops engineers. This is documentation, not implemented code. All numeric parameters below are proposed starting values subject to owner-led playtesting and telemetry.

## Intent

Batch 3 defines what the objects on the tabletop *are*, how drink identity maps to physical interactions, how drinks evolve, how recipes/collections/discoveries can expand that foundation, and how content enters the game safely. This is the source of truth for the **drink content domain**; Batch 2 remains source of truth for collision timing, deterministic merge arbitration, shooter queues and board state. Batch 1 remains source of truth for initial product scope and the overall application.

**Non-negotiable current rule:** alpha consists of **one eight-tier linear evolution chain**. Two *active* drinks with identical tiers 1–7 merge into one next-tier drink. Tier 8 is terminal. Order service automatically reserves an eligible newly produced drink for the oldest matching active order, before a follow-on chain merge. Only local, preview-only coins exist in v0.1.x. Do not silently introduce ingredients, branches, recipe crafting, premium rarity, perks, or server rewards in the alpha.

## Documents and reading paths

| File | Subject | Read by |
|---|---|---|
| 01_PRODUCT_VISION_SCOPE_AND_INVARIANTS.md | Direction, exclusions, invariants, non-goals | Everyone |
| 02_DRINK_IDENTITY_AND_CATALOG_TAXONOMY.md | Identifiers, display identity, variants and grouping | Gameplay, backend, art |
| 03_ALPHA_EIGHT_TIER_DRINK_BIBLE.md | Canonical names, chain, scores, visual briefs | All builders |
| 04_EVOLUTION_GRAPH_AND_RECIPE_RESOLUTION.md | Generalized recipe graph, ambiguity rules | Gameplay, backend |
| 05_INGREDIENTS_AND_PANTRY_FUTURE_DESIGN.md | Ingredient identity, inventory and supply overview | Future economy/content |
| 06_RECIPE_DISCOVERY_AND_SECRET_MECHANICS.md | Discovery UX, fairness, eligibility and proof | Game design, UX |
| 07_RARITY_COLLECTIONS_AND_ALBUMS.md | Cosmetic rarity, sets, milestones | Product, content |
| 08_DRINK_MASTERY_AND_SPECIALIZATION.md | Mastery XP, achievement tracking and caps | Progression, backend |
| 09_CUSTOMER_ORDERS_AND_RECIPE_REQUIREMENTS.md | Serving priorities, requested forms and variants | Gameplay, QA |
| 10_SPAWN_QUEUE_FAIRNESS_AND_REACHABILITY.md | Spawn tiers, PRNG, authored queues, solvability | Gameplay, content |
| 11_PHYSICS_TO_CONTENT_BOUNDARIES.md | Collision integration and invariants | Physics, gameplay |
| 12_SCORE_REWARDS_AND_ECONOMY_INTEGRATION.md | Points, coin previews and future trusted ledger | Economy, QA |
| 13_ART_ASSETS_RENDERING_AND_AUDIO.md | Art specs, FX, audio, asset IDs and optimization | Art, audio, rendering |
| 14_GAMEPLAY_UX_DESKTOP_AND_MOBILE.md | Drink HUD, recipe book, discovery and collections UI | UX, frontend |
| 15_TUTORIALS_AND_PROGRESSIVE_DISCLOSURE.md | Staged teaching, tutorial fixtures and help | Gameplay, UX |
| 16_DIFFICULTY_AND_BALANCE_WORKBOOK.md | Quantitative costs, tuning experiments | Designers, analysts |
| 17_DATA_MODEL_AND_PERSISTENCE.md | Canonical data entities, schema evolution | Backend |
| 18_TYPES_EVENTS_AND_API_CONTRACTS.md | TypeScript schema, domain events, commands | Integrators |
| 19_CONTENT_STUDIO_VALIDATION_AND_PUBLISHING.md | Catalog content pipeline, review and rollback | Tools, operations |
| 20_VERSIONING_MIGRATIONS_AND_COMPATIBILITY.md | Active-session pinning, migrations, replay | Backend, QA |
| 21_TELEMETRY_ANALYTICS_AND_EXPERIMENTS.md | Event definitions and KPIs | Analytics |
| 22_TEST_PLAN_AND_EDGE_CASES.md | Automated scenarios and property tests | QA, all engineers |
| 23_ACCESSIBILITY_LOCALIZATION_AND_POLICY.md | Labels, visuals, localization, licensing | UX, product |
| 24_RELEASE_SLICES_AND_DEPENDENCIES.md | v0.1.x → later recipe releases | Leads |
| 25_PARALLEL_WORKSTREAMS_AND_ISSUES.md | Work allocation and PR boundaries | Coordinator |
| 26_DESIGN_DECISIONS_RISKS_AND_OPEN_QUESTIONS.md | ADRs and owner approvals | Product leads |
| 27_FUTURE_SYSTEM_INTEGRATIONS_OVERVIEW.md | Islands, shops, skills, weather, PvP | Future batches |
| 28_REFERENCE_LINKS_AND_GLOSSARY.md | Canonical terminology and official docs | Everyone |
| 29_EXAMPLE_SESSIONS_AND_RECIPES.md | Worked examples and fixtures | Gameplay, QA |
| 30_ACCEPTANCE_TRACEABILITY_AND_HANDOFF.md | DoD, requirements and cross-team signoff | Coordinator |
| 31_VISUAL_ASSET_PRODUCTION_BRIEFS.md | Creative briefs, required states, naming | Art pipelines |
| 32_FORMAL_RULES_AND_PSEUDOCODE.md | Resolver, event sequence, validation code | Gameplay, reviewers |
| 33_BATCH_1_2_INTEGRATION_AND_DELTA.md | Exact compatibility notes, proposed updates | Maintainers |
| 34_ANTI_PATTERNS_AND_FAILURE_POSTMORTEMS.md | Common mistakes and mitigations | All engineers |

## Sample content

`examples/catalog/core-drinks-alpha.json` is the canonical example eight-tier drink catalog. `examples/missions/coconut-cove-001.json`, `examples/events/example-merge-session.json`, `examples/schemas/catalog.schema.json` and `examples/tests/drink-rule-vectors.json` are illustrative fixtures; schemas are examples, not silently approved production contracts. Validate all JSON after editing.

## Priority reading order

1. **Engineers implementing v0.1:** 01 → 03 → 09 → 10 → 11 → 18 → 22 → 24 → 29 → 32 → 33.
2. **Content/art team:** 02 → 03 → 13 → 14 → 15 → 19 → 31.
3. **Future recipe R&D:** 04 → 05 → 06 → 07 → 08 → 16 → 17 → 20 → 27.
4. **Coordinator:** 24 → 25 → 26 → 30 → 33.

## Definition of 'documented' vs 'built'

Specifications marked **alpha** are immediate contract targets, not proof that they exist in the repository. **Deferred** specs are design candidates; no engineer should independently enable them in production. No source repo, deployment or database has been changed by this documentation pack.

## Precedence / conflict policy

For Alpha behavior: Batch 2 deterministic session and merge rules > Batch 1 launch scope > Batch 3 future design options. If a Batch 3 feature requires altering an existing guarantee, submit an ADR, update cross-batch documents and bump rules/content versions in the same implementation PR. The game director retains final authority over manual UI/game feel tests; automated checks may be run by engineers.
