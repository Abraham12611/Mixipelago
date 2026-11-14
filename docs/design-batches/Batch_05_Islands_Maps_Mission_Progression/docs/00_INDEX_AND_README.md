# Batch 5 — Islands, Maps & Mission Progression

**Design packet 5/21.** An implementation-ready specification for a versioned archipelago graph, not a claim that game features have been shipped. This pack connects Batches 1–4 to Mixipelago's first campaign and lays out safe expansion to hundreds of missions per island.

## Required prior context

- Batch 1 progression overview and release plan.
- Batch 2 gameplay physics and event rules.
- Batch 3 eight-tier drinks, serving priority and save compatibility.
- Batch 4 mission v1 schema, stars, mode rules and gameplay-result contract.

**Non-negotiable:** `coconut-cove-001` remains a two-order Classic Service fixture; newly merged output auto-serves oldest matching order before chain continuation; tier 8 is terminal; local preview coins are not trusted; manual UI testing is owner-directed.

## Specification chapters

- [01 — World Map & Campaign Progression: Product Vision and Scope](01_PRODUCT_VISION_AND_SCOPE.md)
- [02 — World Atlas, Island Hierarchy and Expansion Blueprint](02_WORLD_ATLAS_AND_ISLAND_BLUEPRINT.md)
- [03 — Canonical World Graph Model and Invariants](03_GRAPH_DOMAIN_MODEL_AND_INVARIANTS.md)
- [04 — Node Types, Edge Semantics and Route Design](04_NODE_TYPES_EDGES_AND_ROUTE_DESIGN.md)
- [05 — Unlock Rule DSL, Evaluation Order and Explainability](05_UNLOCK_RULE_DSL_AND_EVALUATOR.md)
- [06 — Visibility, Fog of War, Secrets and Discovery](06_FOG_VISIBILITY_DISCOVERY_AND_SECRET_PATHS.md)
- [07 — Completion, Stars, Mastery, Replays and Best Results](07_STARS_MASTERY_RESULTS_AND_REPLAYS.md)
- [08 — Branches, Optional Routes, Checkpoints and Gateways](08_BRANCHING_PATHS_SIDEQUESTS_AND_GATEWAYS.md)
- [09 — Island Unlocks, Travel, and Progression Rescue Policies](09_GATE_RULES_ISLAND_TRAVEL_AND_RESCUE.md)
- [10 — Mobile Map UX, Information Architecture and Interaction States](10_MOBILE_MAP_UX_INFORMATION_ARCHITECTURE.md)
- [11 — Desktop and Tablet Map UX](11_DESKTOP_TABLET_MAP_UX.md)
- [12 — Map Camera, Pan/Zoom, Hit Testing and Coordinates](12_CAMERA_PAN_ZOOM_AND_HIT_TESTING.md)
- [13 — Island Art, Landmarks, Visual Layers and Asset Production](13_WORLD_ART_LAYOUT_AND_ASSET_PIPELINE.md)
- [14 — Map Runtime, Phaser Scene Composition and React Shell](14_MAP_RUNTIME_AND_SCENE_ARCHITECTURE.md)
- [15 — Immutable Content Manifests, Hashes, Publication and Rollback](15_CONTENT_MANIFESTS_HASHES_AND_ROLLOUT.md)
- [16 — Local Campaign Saves, Migration and Offline Preview](16_ALPHA_LOCAL_SAVE_AND_MIGRATION.md)
- [17 — Trusted Campaign Persistence, Database Schema and Security](17_BACKEND_PROGRESS_SCHEMA_AND_SECURITY.md)
- [18 — Rewards, Treasure Claims and Economy Integration](18_REWARDS_TREASURE_AND_ECONOMY_HANDOFF.md)
- [19 — Chapter Pacing, Mission Density and Difficulty Planning](19_CHAPTER_PACING_AND_MISSION_DENSITY.md)
- [20 — Island Biomes and Mission Theme Integration (Overview)](20_BIOMES_WORLD_MODIFIERS_OVERVIEW.md)
- [21 — Map Secrets, Treasure, Landmarks and Collectibles](21_SECRETS_CHESTS_LANDMARKS_AND_COLLECTIONS.md)
- [22 — Onboarding, Recommendations, Breadcrumbs and Player Guidance](22_ONBOARDING_RECOMMENDATIONS_AND_WAYFINDING.md)
- [23 — Internal Campaign Graph Editor and Content Studio Workflow](23_CONTENT_STUDIO_GRAPH_EDITOR.md)
- [24 — Graph Validation, Dead-End Analysis and Mission Feasibility](24_GRAPH_CONTENT_VALIDATION_AND_SOLVABILITY.md)
- [25 — Campaign Analytics, Funnels, Difficulty Signals and Experiments](25_ANALYTICS_RETENTION_AND_EXPERIMENTS.md)
- [26 — Accessibility, Localization and Motion Comfort](26_ACCESSIBILITY_LOCALIZATION_AND_REDUCED_MOTION.md)
- [27 — Performance Budgets, Map Streaming and Offline Delivery](27_PERFORMANCE_STREAMING_AND_OFFLINE_CACHE.md)
- [28 — Integration Contracts With Earlier and Future Batches](28_CROSS_SYSTEM_INTEGRATION_BOUNDARIES.md)
- [29 — TypeScript Domain Types, Public API and Campaign Events](29_TYPESCRIPT_API_AND_EVENT_CONTRACTS.md)
- [30 — Campaign QA Matrix, Golden Fixtures and Owner Manual Checks](30_QA_TEST_MATRIX_AND_GOLDEN_FIXTURES.md)
- [31 — Engineering Implementation Blueprint](31_IMPLEMENTATION_BLUEPRINT_AND_PSEUDOCODE.md)
- [32 — Phased Release Strategy and Feature Gates](32_RELEASE_SLICES_PHASES_AND_GATES.md)
- [33 — Parallel Engineering Workstreams and Proposed Issue Backlog](33_PARALLEL_ENGINEERING_WORKSTREAMS_AND_ISSUES.md)
- [34 — Architecture Decision Records, Precedent and Open Questions](34_ADRS_DECISIONS_AND_COMPATIBILITY.md)
- [35 — Risk Register, Abuse Cases and Failure Recovery](35_RISK_REGISTER_AND_FAILURE_MODES.md)
- [36 — Terminology, Source References and Technical Links](36_GLOSSARY_AND_REFERENCES.md)
- [37 — Requirements Traceability and Definition of Done](37_REQUIREMENT_TRACEABILITY_AND_DEFINITION_OF_DONE.md)
- [38 — Example End-to-End Player Journeys](38_EXAMPLE_USER_JOURNEYS_AND_FAILURE_STORIES.md)
- [39 — Engineer Kickoff: Build Order, Integration Rules and First Review](39_ENGINEER_KICKOFF_AND_PRIORITY_GUIDE.md)

## Machine-readable fixtures

- `../examples/worlds/coconut-cove-starter.staged.json` — two-node **staged** candidate graph referencing unchanged Batch 4 missions, not a deployed/verified campaign.
- `../examples/worlds/coconut-cove-26-node-concept.draft.json` — **26 conceptual nodes** including nonplayable draft placeholders; no implication that 26 puzzles exist.
- `../examples/schemas/campaign-graph.schema.json` — recursive typed unlock DSL and graph JSON schema.
- `../examples/tests/unlock-rule-vectors.json` — pure gate evaluation examples.
- `../examples/tests/*.json` — intentionally invalid fixtures for validator rejection.
- `../examples/missions/coconut-cove-001.json`, `-002.json` — copied byte-for-byte from Batch 4.
- `../examples/contracts/campaign-event-examples.json` — example local-preview semantic events.
- `../examples/assets/map-assets-manifest.draft.json` — placeholder *keys*, not real production assets.
- `../tools/validate_batch5.py` — static validator; requires Python `jsonschema`.

Run `python tools/validate_batch5.py` from the batch root. Validation does NOT prove physical mission solvability, real reward integrity, runtime UI behavior or owner design approval.

## Recommended engineering order

1. Contracts + pure evaluator + schema validator.
2. Integrate Batch 4 result adapter and local-preview star progression.
3. Two-node functional map/list UI, then Phaser map canvas and pan/zoom.
4. Add carefully authored + proven missions, responsive art and streaming.
5. Add branches, gateway, secrets/treasures and trusted account progression behind independent gates.

See `ENGINEER_START_HERE.md` for owner/reviewer/merging rules.
