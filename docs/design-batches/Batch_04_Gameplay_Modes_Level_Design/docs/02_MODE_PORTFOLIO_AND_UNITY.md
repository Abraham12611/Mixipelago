# 02 — Mode Portfolio, Shared Engine and Experience Differentiation

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Mode registry
| Stable ID | Visible name | Unique decision pressure | Initial status | Future progression |
|---|---|---|---|---|
| `service` | Classic Service | Build orders efficiently without filling board | v0.1.0 | Main campaign |
| `precision` | Precision Mix | Limited launch budget, plan each collision | v0.2+ gated | Special stars/medals |
| `score_attack` | Chain Reaction / Score Attack | Plan merges and chains for score | v0.2+ gated | Time/score events |
| `rush_hour` | Rush Hour | Active-time deadline plus rotating orders | future | Festivals, missions |
| `survival` | Survival Shift | Waves and increasingly difficult board pressure | future | Endless milestones |
| `vip_service` | VIP Service | Complex high-value, deterministic client contracts | future | Rival/NPC arcs |
| `endless` | Endless Lounge | Self-paced merging, personal-best attempts | future | Relaxed mode |
| `festival` | Festival Service | Large scripted customer crowds | future | Seasonal content |
| `ghost_challenge` | Ghost / Friend Challenge | Compare equivalent seed and inputs | future | Friends/leaderboards |
| `ranked_duel` | Ranked Duel | Standardized competitive scenario | future | Batch 13–14 |

## Common invariants for all modes
Run `MissionDefinition` through the same session constructor; load version-pinned physics/catalog; select a mode plugin; spawn/step/merge through `SimulationCore`; reduce events through `SessionReducer`; pass semantic events to `ObjectiveEngine` and `ScoringEngine`; evaluate terminal outcomes; save/export signed or local session summaries. The mode may configure supported conditions, never bypass the simulation or award currency directly.

## Feature gating
A mode exists in content registry with `releaseStatus: planned|internal|beta|live|retired`, `featureFlag`, `clientMinVersion`, `serverMinVersion`, and `contentManifestHash`. The UI lists only enabled and playable modes. An unpublished future mode may appear in admin tools only, never as a fake accessible button.

## Selection UX
A player selects an island mission to enter the resolved `modeId`. A dedicated modes screen is unnecessary for v0.1. Future mode selection should explain **goal, number of shots/time, modifiers, reward type, difficulty** before launch. Replays need a pinned definition, not today's live definition.

## Decision differentiation
- Service: matching incoming requests versus preserving better chain possibilities.
- Precision: more accurate aim with limited attempts; no random unfair spawn.
- Score Attack: risk-managed setup to maximize combo multiplier.
- Rush Hour: short-term throughput and active-time management.
- Survival: solve increasingly pressured geometry with constrained cleanup opportunities.
- VIP: prioritize exact high-tier contracts versus lower-tier turnover.
- Endless: optimize self-imposed goals, no punitive deadline.

## Mode composition anti-patterns
Do not implement a mode by attaching arbitrary numeric multipliers to the same level. Do not make timed levels require the browser to remain foregrounded. Do not let passive shop perks secretly change ranked physics. Do not reuse story NPC “VIP status” as an unexplained scoring advantage. Separate themed presentation from the objective and time rules.

## Evaluation matrix
To graduate from internal→beta: prove a clear unique play pattern in owner manual tests, mission schema validity, boundary conditions, 10+ reproducible QA simulations, acceptable device performance, understandable tutorial, published rules and analytics. To graduate beta→live: demonstrate no progression blocker, no score dupe, acceptable abandon/failure signals, rollback switch and verified content integrity.
