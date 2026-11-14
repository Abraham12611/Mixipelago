# 37 — Official Technical References, Internal Sources and Glossary

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Required internal source documents
**Batch1:** `docs/04_GAMEPLAY_AND_PHYSICS.md`, `05_DRINKS_CUSTOMERS_SCORING.md`, `07_DATA_MODEL.md`, `08_API_AND_EVENTS.md`, `16_RELEASE_ROADMAP.md`, `26_CONTENT_AND_CONFIG_EXAMPLES.md`.
**Batch2:** `docs/05_FIXED_STEP_SIMULATION_LIFECYCLE.md`, `07_MERGE_ARBITRATION_AND_CHAIN_REACTIONS.md`, `08_SPAWN_NEXT_QUEUE_AND_GAME_DIRECTOR.md`, `09_BOARD_PRESSURE_DANGER_AND_TERMINAL_STATES.md`, `10_SIMULATION_STATE_MACHINES.md`, `11_TYPES_COMMANDS_AND_EVENT_CONTRACTS.md`, `16_DIFFICULTY_AND_GAMEPLAY_BALANCING.md`, `17_REPLAY_DETERMINISM_AND_TRUST.md`, `19_QA_MATRIX_AND_AUTOMATED_TESTS.md`.
**Batch3:** `docs/03_ALPHA_EIGHT_TIER_DRINK_BIBLE.md`, `09_CUSTOMER_ORDERS_AND_RECIPE_REQUIREMENTS.md`, `12_SCORE_REWARDS_AND_ECONOMY_INTEGRATION.md`, `16_DIFFICULTY_AND_BALANCE_WORKBOOK.md`, `18_TYPES_EVENTS_AND_API_CONTRACTS.md`, `24_RELEASE_SLICES_AND_DEPENDENCIES.md`, `33_BATCH_1_2_INTEGRATION_AND_DELTA.md` and `examples/missions/coconut-cove-001.json`.

## Official external references (verified November 2026)
- Phaser 4 docs / input and cameras: https://phaser.io/oss/docs/ ; https://phaser.io/oss/docs/phaser/concepts/input ; https://phaser.io/oss/docs/phaser/concepts/cameras
- Phaser 4 API examples: https://labs.phaser.io/phaser4-index.html
- Rapier JavaScript determinism: https://www.rapier.rs/docs/user_guides/javascript/determinism/
- Rapier engine guide: https://rapier.rs/docs/
- Rapier integration/timing guide (select JS tab): https://rapier.rs/docs/user_guides/javascript/integration_parameters/
- JSON Schema 2020-12: https://json-schema.org/draft/2020-12
- W3C WCAG 2.2: https://www.w3.org/TR/WCAG22/

## Terms
**Active tick:** simulation step while player session is running, excluding pause.
**Campaign mission:** an authored playable node with explicit version and goals.
**Chain depth:** number of causally linked merge generations, not count of all contact events.
**Content hash:** digest of immutable mission/catalog/rules snapshot for verification.
**Danger grace:** consecutive active physics ticks of qualifying intrusion before loss.
**Golden replay:** a captured command trace that wins under pinned engine/build; source of proof, not merely a theory.
**Objective DSL:** typed, validated goal representation reduced from committed semantic events.
**Preview coins:** client-only visual tally, not a trusted wallet.
**Run seed:** deterministic PRNG input pinned at start.
**Mode policy:** limited variation in objectives, timers, waves and termination while sharing physics.
**Terminalization:** exactly-once transition from running/resolving to outcome.
**Verified result:** backend-confirmed receipt suitable for persistent currency or ranking.
