# Mixipelago — Batch 2: Physics, Shooting & Merging

**Document baseline:** 2026-11-14  
**Purpose:** Implementation-grade technical and product specification for the tactile tabletop merging puzzle.  
**Status:** Proposed engineering specification, pending owner feel-test and prototype validation. No source code is implied to exist.  
**Dependency:** Mixipelago Batch 1, especially `docs/04_GAMEPLAY_AND_PHYSICS.md`, `docs/05_DRINKS_CUSTOMERS_SCORING.md`, `docs/06_TECH_STACK_AND_ARCHITECTURE.md`, `docs/21_DECISIONS_RISKS_AND_OPEN_QUESTIONS.md`, and `docs/28_INTEGRATION_CONTRACTS.md`.  
**Release intent:** Minimal playable **v0.1.0** in ~72 hours with parallel work; v0.1.1 first-week polish; advanced variants only in later releases.

## Read in this order

1. [00_INDEX.md](docs/00_INDEX.md) — authoritative document map, scope and decision status.
2. [01_CORE_EXPERIENCE_AND_PLAYER_FEEL.md](docs/01_CORE_EXPERIENCE_AND_PLAYER_FEEL.md) — what feels right and why.
3. [02_WORLD_COORDINATES_BOARD_AND_CAMERA.md](docs/02_WORLD_COORDINATES_BOARD_AND_CAMERA.md) — mathematically consistent board and controls.
4. [03_RAPIER_PHYSICS_CONFIGURATION.md](docs/03_RAPIER_PHYSICS_CONFIGURATION.md) — precise physical setup and safe tuning.
5. [04_LAUNCH_AIM_INPUT.md](docs/04_LAUNCH_AIM_INPUT.md) — touch/mouse/keyboard/gamepad interactions.
6. [05_FIXED_STEP_SIMULATION_LIFECYCLE.md](docs/05_FIXED_STEP_SIMULATION_LIFECYCLE.md) — clock, pause, body lifecycle.
7. [06_COLLISION_CONTACT_AND_MATERIALS.md](docs/06_COLLISION_CONTACT_AND_MATERIALS.md) — collision mechanics for same/different drinks.
8. [07_MERGE_ARBITRATION_AND_CHAIN_REACTIONS.md](docs/07_MERGE_ARBITRATION_AND_CHAIN_REACTIONS.md) — exactly-once merging.
9. [08_SPAWN_NEXT_QUEUE_AND_GAME_DIRECTOR.md](docs/08_SPAWN_NEXT_QUEUE_AND_GAME_DIRECTOR.md) — next shot, preview, pacing.
10. [09_BOARD_PRESSURE_DANGER_AND_TERMINAL_STATES.md](docs/09_BOARD_PRESSURE_DANGER_AND_TERMINAL_STATES.md) — predictable win/loss.
11. [10_SIMULATION_STATE_MACHINES.md](docs/10_SIMULATION_STATE_MACHINES.md) — state invariants and transitions.
12. [11_TYPES_COMMANDS_AND_EVENT_CONTRACTS.md](docs/11_TYPES_COMMANDS_AND_EVENT_CONTRACTS.md) — shared TypeScript boundaries.
13. [12_IMPLEMENTATION_BLUEPRINT_AND_PSEUDOCODE.md](docs/12_IMPLEMENTATION_BLUEPRINT_AND_PSEUDOCODE.md) — engineering skeleton.
14. [13_PRESENTATION_ANIMATION_AND_VISUAL_FEEDBACK.md](docs/13_PRESENTATION_ANIMATION_AND_VISUAL_FEEDBACK.md) — 2.5D animation without breaking physics.
15. [14_SFX_HAPTICS_AND_IMPACT_FEEDBACK.md](docs/14_SFX_HAPTICS_AND_IMPACT_FEEDBACK.md) — tactile sounds and silence rules.
16. [15_PHYSICS_LAB_AND_TUNING.md](docs/15_PHYSICS_LAB_AND_TUNING.md) — test harness and preset comparison.
17. [16_DIFFICULTY_AND_GAMEPLAY_BALANCING.md](docs/16_DIFFICULTY_AND_GAMEPLAY_BALANCING.md) — tunable difficulty, fair challenge.
18. [17_REPLAY_DETERMINISM_AND_TRUST.md](docs/17_REPLAY_DETERMINISM_AND_TRUST.md) — snapshots, input logs, future rank verification.
19. [18_PERFORMANCE_MOBILE_AND_ACCESSIBILITY.md](docs/18_PERFORMANCE_MOBILE_AND_ACCESSIBILITY.md) — device budgets, lifecycle, input accessibility.
20. [19_QA_MATRIX_AND_AUTOMATED_TESTS.md](docs/19_QA_MATRIX_AND_AUTOMATED_TESTS.md) — exhaustive fixtures and regression gates.
21. [20_EDGE_CASES_AND_RECOVERY.md](docs/20_EDGE_CASES_AND_RECOVERY.md) — overlapping bodies, browser interruption and errors.
22. [21_IMPLEMENTATION_WORKSTREAMS_AND_RELEASES.md](docs/21_IMPLEMENTATION_WORKSTREAMS_AND_RELEASES.md) — parallel tasks, version-by-version scope.
23. [22_ADRS_RISKS_AND_OPEN_DECISIONS.md](docs/22_ADRS_RISKS_AND_OPEN_DECISIONS.md) — decisions, owner approvals, fallback strategies.
24. [23_TECHNICAL_REFERENCES_AND_GLOSSARY.md](docs/23_TECHNICAL_REFERENCES_AND_GLOSSARY.md) — official docs and terms.
25. [24_TRACEABILITY_AND_DEFINITION_OF_DONE.md](docs/24_TRACEABILITY_AND_DEFINITION_OF_DONE.md) — requirements mapped to tests.
26. [25_EXAMPLE_CONFIGS_AND_TEST_FIXTURES.md](docs/25_EXAMPLE_CONFIGS_AND_TEST_FIXTURES.md) — sample JSON/configs and scenario definitions.
27. [26_ENGINEER_KICKOFF_AND_FIRST_72_HOURS.md](docs/26_ENGINEER_KICKOFF_AND_FIRST_72_HOURS.md) — concise operational handoff.
28. [27_CONTACT_MATH_AND_PHYSICS_INTUITION.md](docs/27_CONTACT_MATH_AND_PHYSICS_INTUITION.md) — collision equations and correct solver intuition.
29. [28_SCENARIO_ATLAS_AND_DEBUG_PLAYBOOK.md](docs/28_SCENARIO_ATLAS_AND_DEBUG_PLAYBOOK.md) — player-visible scenarios linked to debug procedures.
30. [29_BATCH1_INTEGRATION_NOTES.md](docs/29_BATCH1_INTEGRATION_NOTES.md) — precise changes to carry back to the original handoff after approval.

## Guardrails

- **No copying another game's source art, characters, branding, code or hidden implementation.** User-provided screenshots are visual inspiration and behavioral hypotheses only.
- **No paid economy or public rankings in v0.1.0.** Coins are local preview values and cannot be imported as real wallet value without an explicit migration strategy.
- **No automatic manual UI testing by agents.** The product owner performs manual interface/game-feel testing; engineers run automated tests and provide recordings/repro steps for the owner's approval.
- **All integration APIs are proposed until compiled against the pinned package versions.** `examples/` are illustrative, not a standalone shipped game.
- **Do not treat numeric tuning defaults as observations from Merge Shooter or validated values.** They are Mixipelago design hypotheses.

## Deliverables

An engineer reading this pack should be able to build a fixed-step Rapier simulation, transform pointer input into accurate aim commands, spawn and launch drink bodies, handle collisions and chain merges without duplicate consumption, integrate Phaser sprites and audio, connect a deterministic session reducer, expose a physics laboratory, and run automated headless tests and a browser alpha.
