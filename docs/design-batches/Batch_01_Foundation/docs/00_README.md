# Mixipelago — Engineering Pack (Batch 1)

**Working title:** Mixipelago  
**Product:** Web-first, cross-device tropical drink-shooting/merging puzzle game, with an expandable island campaign, shop economy, skills, social competition and a living-world layer.  
**Document baseline:** 2026-11-14 | **Status:** Proposed baseline for engineering kickoff; not evidence that implementation exists.  
**Primary target:** Functional web **v0.1.0 playable alpha in ~72 hours** with parallel engineers and limited, curated art. Stretch first-week polish to v0.1.1. Subsequent milestones are capacity-dependent.

## Start here (recommended reading order)

1. [01_VISION_AND_SCOPE.md](01_VISION_AND_SCOPE.md) — product identity, principles, exclusions and release philosophy.
2. [02_PRD_AND_ACCEPTANCE.md](02_PRD_AND_ACCEPTANCE.md) — user stories, requirements and explicit acceptance for v0.1.0/v0.1.1.
3. [03_SITEMAP_AND_UX.md](03_SITEMAP_AND_UX.md) — routes, mobile and desktop layouts, component behaviors.
4. [04_GAMEPLAY_AND_PHYSICS.md](04_GAMEPLAY_AND_PHYSICS.md) — precise simulation design, input, merge rules and edge cases.
5. [05_DRINKS_CUSTOMERS_SCORING.md](05_DRINKS_CUSTOMERS_SCORING.md) — drink catalog, orders, scores, goals, gameplay progression.
6. [06_TECH_STACK_AND_ARCHITECTURE.md](06_TECH_STACK_AND_ARCHITECTURE.md) — architectural decisions, package structure, data ownership.
7. [07_DATA_MODEL.md](07_DATA_MODEL.md) + [08_API_AND_EVENTS.md](08_API_AND_EVENTS.md) — persistence, contracts, events, future backend integration.
8. [16_RELEASE_ROADMAP.md](16_RELEASE_ROADMAP.md) + [17_WORKSTREAMS_AND_ISSUES.md](17_WORKSTREAMS_AND_ISSUES.md) — incremental releases and parallel team work.
9. [15_TESTING_AND_PERFORMANCE.md](15_TESTING_AND_PERFORMANCE.md) + [18_DEPLOYMENT_AND_OPERATIONS.md](18_DEPLOYMENT_AND_OPERATIONS.md) — quality and live deployments.
10. [21_DECISIONS_RISKS_AND_OPEN_QUESTIONS.md](21_DECISIONS_RISKS_AND_OPEN_QUESTIONS.md) — decisions already made versus questions to validate.

## Complete document catalog

| File | Covers | Depth |
|---|---|---|
| `00_README.md` | This index, handoff instructions | Reference |
| `01_VISION_AND_SCOPE.md` | Product identity, pillars, original vs inspired, release scope | Foundation |
| `02_PRD_AND_ACCEPTANCE.md` | PRD, personas, jobs-to-be-done, acceptance | Detailed near-term |
| `03_SITEMAP_AND_UX.md` | Information architecture, mobile/desktop, states | Detailed near-term |
| `04_GAMEPLAY_AND_PHYSICS.md` | Sliding, collision, launching, merging, determinism | Detailed near-term |
| `05_DRINKS_CUSTOMERS_SCORING.md` | First recipes, customer behavior, objectives, session flow | Detailed near-term |
| `06_TECH_STACK_AND_ARCHITECTURE.md` | Stack, modules, runtime, package boundaries | Detailed near-term |
| `07_DATA_MODEL.md` | Local save + planned Postgres schemas | Detailed near-term / outline long-term |
| `08_API_AND_EVENTS.md` | Domain events, API envelopes, idempotency, sync | Detailed near-term |
| `09_PROGRESSION_OVERVIEW.md` | Missions, islands, player progress, skill trees | Overview + contracts |
| `10_ECONOMY_AND_SHOPS_OVERVIEW.md` | Coins, upgrades, transactions, shop system | Overview + contracts |
| `11_WORLDS_AND_EVENTS_OVERVIEW.md` | Islands, incidents, weather, narrative, rival NPCs | Overview only |
| `12_SOCIAL_AND_LEADERBOARDS_OVERVIEW.md` | Friends, clubs, rankings, rewards, anti-cheat | Overview only |
| `13_ART_AUDIO_ASSET_PIPELINE.md` | Visual style, AI pipeline, music, SFX, optimization | Detailed production pipeline |
| `14_SECURITY_AND_GAME_INTEGRITY.md` | Threat model, trustworthy rewards, data access | Detailed guardrails |
| `15_TESTING_AND_PERFORMANCE.md` | Test matrices, acceptance cases, browser/device QA | Detailed near-term |
| `16_RELEASE_ROADMAP.md` | Phases, subphases, versions, release gates | Detailed |
| `17_WORKSTREAMS_AND_ISSUES.md` | Parallel engineering assignments, dependencies | Detailed |
| `18_DEPLOYMENT_AND_OPERATIONS.md` | Environments, secrets, CI/CD, rollback, incident response | Detailed |
| `19_ANALYTICS_AND_LIVEOPS.md` | KPIs, telemetry, staged rollout, experimentation | Detailed foundations |
| `20_ADMIN_AND_CONTENT_TOOLING.md` | Internal editors, versioned content, future pipeline | Overview + near-term |
| `21_DECISIONS_RISKS_AND_OPEN_QUESTIONS.md` | ADR list, tradeoffs, decision ownership | Detailed |
| `22_REFERENCE_DOCUMENTATION.md` | Official docs and research links | Reference |
| `23_ENGINEER_ONBOARDING.md` | Workstation setup, local run, branching and PR flow | Detailed |
| `24_FUTURE_SYSTEMS_OVERVIEW.md` | Deferred RPG, world, business, social, multiplayer | Overview only |
| `25_ACCESSIBILITY_PRIVACY_COMPLIANCE.md` | Accessible controls, location, youth/privacy, licensing | Foundation |
| `26_CONTENT_AND_CONFIG_EXAMPLES.md` | JSON/TypeScript content examples and validation approach | Detailed |
| `27_RELEASE_CHECKLISTS.md` | Go/no-go and definition of done | Detailed |
| `28_INTEGRATION_CONTRACTS.md` | UI/game/backend boundaries and schema versioning | Detailed |
| `29_VISUAL_REFERENCES.md` | Image references and art direction guardrails | Reference |
| `30_ENGINEER_KICKOFF_BRIEF.md` | Copy/paste team handoff and issue assignment | Actionable |
| `31_72_HOUR_EXECUTION_BOARD.md` | Hour-by-hour alpha coordination and go/no-go | Actionable |

## Release decision: deliberately narrow first alpha

`v0.1.0` ships **one polished tabletop, 8 core drink tiers, 2 active customer slots, merge/contact physics, basic scoring/coins, round-end, a simple progression teaser, desktop + mobile inputs, SFX, and local save**. No registration required. Coins in the initial local save are *preview progress*, not a trusted online economy. No global leaderboard, paid transactions, staff, insurance, weather, crews, or open-world simulation in the 72-hour release. An island map teaser may be static, clearly labeled.

`v0.1.1` polishes responsiveness, fixed-step behavior, pause/recover, art consistency, tutorial, a small curated set of mission configurations, and compatibility. Backend account/sync is staged for later unless isolated work is ahead of schedule; do **not** turn it into a release blocker.

## Documentation authority / precedence

1. The versioned, approved ADR and release scope in `21` + `16`.
2. The gameplay behavior/acceptance in `04`, `05`, `02`.
3. Shared TypeScript contracts/JSON schema stored in actual source packages once implemented.
4. Feature overview docs for future capabilities.
5. Mockup images are *visual exploration*, not functional specifications or verified real-world UI.

When conflicts occur, open a decision issue, label it `needs-design-decision`, and do not silently invent incompatible behavior. Recording a decision is better than merging contradictory implementations.

## Definition of handoff completion

A new engineer should be able to: run the app locally, identify their owned module, follow the gameplay and data contract, implement a task behind a branch/feature flag, write the required tests, open a PR, and independently understand what is excluded from the current release.

## Asset bundle

`../references/original_screenshots/` are source-game screenshots **for inspiration only**. `../references/generated_concepts/` are exploratory **Mixipelago image mockups**, not final reusable UI source layers. Review [29_VISUAL_REFERENCES.md](29_VISUAL_REFERENCES.md). Never place reference screenshots into the production game.
