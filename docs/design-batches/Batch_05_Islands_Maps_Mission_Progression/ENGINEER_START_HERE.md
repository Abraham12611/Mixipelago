# Engineer Kickoff — Mixipelago Batch 5

## Goal

Build a smooth, trustworthy world-map progression system without changing gameplay physics, merge rules, or existing mission fixtures. Make the first public campaign small and real; expand through content revisions.

## Read first

1. `docs/00_INDEX_AND_README.md` and `docs/01_PRODUCT_VISION_AND_SCOPE.md`.
2. `docs/03_GRAPH_DOMAIN_MODEL_AND_INVARIANTS.md`, `05_UNLOCK_RULE_DSL_AND_EVALUATOR.md`, `07_STARS_MASTERY_RESULTS_AND_REPLAYS.md`.
3. `docs/14_MAP_RUNTIME_AND_SCENE_ARCHITECTURE.md`, `15_CONTENT_MANIFESTS_HASHES_AND_ROLLOUT.md`, `16_ALPHA_LOCAL_SAVE_AND_MIGRATION.md`, `24_GRAPH_CONTENT_VALIDATION_AND_SOLVABILITY.md`.
4. `docs/29_TYPESCRIPT_API_AND_EVENT_CONTRACTS.md`, `30_QA_TEST_MATRIX_AND_GOLDEN_FIXTURES.md`, `31_IMPLEMENTATION_BLUEPRINT_AND_PSEUDOCODE.md`, `32_RELEASE_SLICES_PHASES_AND_GATES.md`, `33_PARALLEL_ENGINEERING_WORKSTREAMS_AND_ISSUES.md`.

## Mandatory boundaries

- Staged graph is not released; draft 26-node map is **not 26 playable missions**.
- Gameboard runs Rapier; campaign map is a separate Phaser scene, no physical rigid body simulation needed.
- Only verified mission receipt can produce backend coin, season, or valuable claim; guest map progress remains local preview.
- All new mission definitions need Batch 4’s golden replay proof before being publicly playable.
- Feature-flag all unfinished features.
- All manual UI/game feel testing belongs to the owner. Engineers provide automated CI evidence and preview URLs.
- Engineers may open PRs but **must not merge them**; coordinator reviews merges; main requires explicit owner approval.

## Sprint 1 DoD

Pure unlock evaluator tested; first 2 mission refs work in staging; route renders, selection and Next action work; clear first mission projects second node as unlocked; mobile and desktop map QA sent to owner; no physics/score/coin regressions; graph publication remains gated until replay + owner signoff.
