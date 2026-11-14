# Mixipelago — Batch 4: Gameplay Modes & Level Design

**Design packet:** 4 of 21 | **Status:** implementation-ready specification with future-mode proposals | **Baseline:** Batches 1–3.

## Start here

1. Read [ENGINEER_START_HERE.md](ENGINEER_START_HERE.md) and [01 — Vision & Scope](docs/01_PRODUCT_VISION_SCOPE.md).
2. Read prior Batch 2 `07_MERGE_ARBITRATION_AND_CHAIN_REACTIONS.md` and `09_BOARD_PRESSURE_DANGER_AND_TERMINAL_STATES.md`.
3. Read prior Batch 3 `03_ALPHA_EIGHT_TIER_DRINK_BIBLE.md`, `09_CUSTOMER_ORDERS_AND_RECIPE_REQUIREMENTS.md` and `12_SCORE_REWARDS_AND_ECONOMY_INTEGRATION.md`.
4. Read chapters 02–05, then your assigned mode / workstream chapters. Use `examples/schemas/mission.schema.json` and `tools/validate_batch4.py`.
5. Treat future-mode examples as **design-only / disabled**, not shipped features or verified solvable levels.

## Non-negotiable carry-forward contract

- `coconut-cove-001` baseline fixture has **two orders, two-order win goal**, even though older general prose referenced five as a default demo.
- One eight-tier linear drink chain with names and tier scores from Batch 3. Tier8 is terminal; compatible same tiers merge, different tiers collide only.
- Newly produced matching output serves the oldest outstanding matching order **before chain continuation**.
- Winning primary objective is evaluated before same-tick danger / shot exhaustion.
- Client **preview coins** in v0.1 are nonspendable, untrusted, and not leaderboard eligible.
- Physics at fixed 60Hz; input/world geometry separate from render FPS; pinned mission, content, score, physics rules.
- Owner handles all manual UI and gameplay feel testing; PRs to main require explicit owner approval.

## Chapters (38 files)
- [01 — Gameplay Modes and Level Design: Vision and Scope](docs/01_PRODUCT_VISION_SCOPE.md)
- [02 — Mode Portfolio, Shared Engine and Experience Differentiation](docs/02_MODE_PORTFOLIO_AND_UNITY.md)
- [03 — Session Lifecycle, Clocks, Transitions and Event Ordering](docs/03_SESSION_LIFECYCLE_AND_CLOCKS.md)
- [04 — Objective DSL, Progress Evaluation and Dependency Graph](docs/04_OBJECTIVE_DSL_AND_REDUCER.md)
- [05 — Scoring, Combos, Stars, Medals and Tie-breakers](docs/05_SCORING_STARS_AND_COMBOS.md)
- [06 — Classic Service: Campaign Mode Full Specification](docs/06_CLASSIC_SERVICE_COMPLETE_SPEC.md)
- [07 — Rush Hour: Time-Pressure Mode](docs/07_RUSH_HOUR_TIMED_MODE.md)
- [08 — Precision Mix: Limited-Shot Puzzle Mode](docs/08_PRECISION_MIX_LIMITED_SHOTS.md)
- [09 — Survival Shift: Wave Survival and Board Pressure](docs/09_SURVIVAL_WAVES.md)
- [10 — Chain Reaction and Score Attack Modes](docs/10_CHAIN_REACTION_SCORE_ATTACK.md)
- [11 — VIP Service, Boss Challenges and Special Customer Contracts](docs/11_VIP_BOSS_AND_SPECIAL_CONTRACTS.md)
- [12 — Endless Lounge and Relaxed Free-Play](docs/12_ENDLESS_LOUNGE_AND_FREE_PLAY.md)
- [13 — Festival Events and Rotating Rule Sets: Overview](docs/13_FESTIVALS_EVENTS_AND_ROTATING_RULESETS.md)
- [14 — Asynchronous Ghosts, Friends Challenges and Ranked Constraints](docs/14_FRIEND_GHOST_AND_RANKED_RULESETS.md)
- [15 — Mission Definition Schema, Identity, Versioning and Compatibility](docs/15_MISSION_SCHEMA_AND_VERSIONING.md)
- [16 — Board Geometry, Obstacles, Hazards and Surface Material Variants](docs/16_BOARD_LAYOUTS_HAZARDS_AND_SURFACES.md)
- [17 — Spawn Director, RNG, Queue Fairness and Anti-Softlock Design](docs/17_SPAWNING_SEEDS_AND_FEASIBILITY.md)
- [18 — Customer Director, Order Pacing and Mode Integration](docs/18_CUSTOMER_DIRECTOR_AND_ORDER_PACING.md)
- [19 — Difficulty Curves, Mission Pacing and Quantitative Balancing](docs/19_DIFFICULTY_CURVE_AND_METRICS.md)
- [20 — Mission Solvability, Feasibility Proofs and Automated Playtesting](docs/20_SOLVABILITY_AND_LEVEL_PROOF.md)
- [21 — Loss States, Retries, Recovery, Hints and Player Protection](docs/21_FAILURE_RETRY_RECOVERY_AND_HINTS.md)
- [22 — Mode Rewards, Mission Progress and Trusted Economy Handoff](docs/22_REWARDS_PROGRESS_AND_ECONOMY_HANDOFF.md)
- [23 — Tutorial Script, Progressive Disclosure and Player Learning](docs/23_TUTORIALS_ONBOARDING_AND_GUIDANCE.md)
- [24 — Gameplay UI/UX, Responsive HUD and Screen States](docs/24_RESPONSIVE_UI_SITEMAP_AND_STATES.md)
- [25 — Mode-Specific Feedback, Animation, Audio and Emotional Pacing](docs/25_FEEDBACK_SFX_AND_PRESENTATION.md)
- [26 — Internal Level Editor, Preview, Validation and Publishing](docs/26_CONTENT_STUDIO_LEVEL_EDITOR.md)
- [27 — Mode Telemetry, Difficulty Analytics, Experiments and Privacy](docs/27_TELEMETRY_ANALYTICS_AND_EXPERIMENTS.md)
- [28 — Replay Protocol, Verification, Anti-Cheat and Trust Boundaries](docs/28_REPLAY_VALIDATION_AND_TRUST.md)
- [29 — Runtime Performance, Device Classes and Capacity Budgets](docs/29_PERFORMANCE_BUDGET_AND_CAPACITY.md)
- [30 — Gameplay Modes QA Matrix and Acceptance Requirements](docs/30_TEST_MATRIX_ACCEPTANCE_AND_EDGE_CASES.md)
- [31 — Level Designer Playbook: Author, Review, Prove and Improve](docs/31_MISSION_DESIGN_PLAYBOOK.md)
- [32 — Implementation Blueprint, Module Interfaces and Pseudocode](docs/32_TYPESCRIPT_ENGINE_IMPLEMENTATION.md)
- [33 — Parallel Engineering Workstreams, Tickets, Dependencies and Ownership](docs/33_ENGINEER_WORKSTREAMS_AND_ISSUES.md)
- [34 — Incremental Release Plan, Dependencies and Feature Gates](docs/34_RELEASE_PHASES_AND_GATES.md)
- [35 — Architecture Decisions, Conflicts with Earlier Batches and Proposed Resolutions](docs/35_ADRS_AND_INTEGRATION_DECISIONS.md)
- [36 — Risk Register, Anti-patterns and Engineering Failure Postmortems](docs/36_FAILURE_MODES_AND_RISK_REGISTER.md)
- [37 — Official Technical References, Internal Sources and Glossary](docs/37_TECH_REFERENCES_AND_GLOSSARY.md)
- [38 — Requirement Traceability, Test Evidence and Definition of Done](docs/38_TRACEABILITY_AND_DEFINITION_OF_DONE.md)

## Examples and executable validation

- `examples/missions/coconut-cove-001.json` — exact previously authored Batch 3 baseline, copied unchanged.
- `examples/missions/coconut-cove-002.json` — another Classic Service candidate.
- `examples/missions/precision-001.draft.json`, `rush-hour-001.draft.json`, `survival-001.draft.json`, `chain-001.draft.json`, `vip-001.draft.json`, `endless-001.draft.json` — **non-live future concepts**.
- `examples/schemas/mission.schema.json` — v1-compatible and v2-draft JSON Schema.
- `examples/tests/objective-rule-vectors.json` — stable expected pure reducer and terminalization cases.
- `examples/tests/README.md` — semantics and limits of these fixtures.
- `tools/validate_batch4.py` — JSON Schema + cross-field lint and pure arithmetic vector checks; **not a physics proof or browser playtest**.

## Release use

`v0.1.0` ship one actual playable service mission with automated win/loss test and owner manual approval; `v0.1.1–0.1.2` improve and expand authored service missions; `v0.2.0+` add campaign and optional Precision/Score Attack after proof; later add active timed, survival, VIP, endless and competition.

## Companion packages

Combine with Batch 1 Foundation, Batch 2 Physics, Batch 3 Drinks. Their contracts are not overridden except the documented mission-specific example precedence. See chapter 35 for conflict resolution.
