# 24 — Future Systems Register (Overview Only)

This is a feature catalog and dependency map, **not** approval for engineers to implement complex systems without future PRDs. We will produce meticulous follow-on batches per domain after a playable alpha validates game feel.

## Proposed long-term modules

| System | Player value | Technical dependencies | Detailed design deferred |
|---|---|---|---|
| Branching archipelago | Explore 100s of paths/missions per island | Mission graph, content editor, map renderer | Full island maps, mission taxonomy |
| Rich character personalities | Recurring regulars/VIPs and narrative arcs | Customer Director, NPC registry, dialogue UI | All characters, relationship curves |
| Shop expansion | Meaningful business-building | Trusted wallet, shop state, upgrade catalog | Prices, staffing, capacity formulas |
| Franchise network | Specialize several properties across islands | Shop ownership, economy simulation | Cross-shop synergy, passive income |
| Skill trees | Different player strategies | Player XP, skill graph, modifier registry | Node lists, power budgets, respec |
| Incidents and consequences | Risk/recovery narrative choices | Event director, shop economy, quest engine | Fire, insurance, loans, recovery policies |
| Island weather | New puzzle modifiers and scenery | Weather/event schedules, asset variants | Forecasting, random rules, frequencies |
| Rival businesses | Friendly competition, dynamic story | NPC businesses, reputation, events | Rival strategies, dialogue trees |
| VIP customers | Higher stakes and rewards | Customer Director, shop reputation, skills | Appearance probability and rewards |
| Rare recipes | Collection and specialized strategies | Branching recipes, item catalog | Recipe discovery tables |
| Tournaments | Skill-focused competitive goals | Verified runs, equal conditions, reward ledger | Event schedules/rank formula |
| Regional/local boards | Community competition | Opt-in coarse region, verified rankings | Geographic scopes and privacy UI |
| Friends/Crews | Shared challenges and status | Account/social graph, moderation | Invitations, governance, prizes |
| Live duels | Direct multiplayer | Server-authoritative state/real-time transport | Matchmaking/netcode/anti-cheat |
| Island Chronicle | Personal history/legacy | Event stream, milestones | Journal UI, story content |
| Seasons/live events | A world that continues evolving | Content publish, workers, reward engine | Content calendar/balance |
| Native apps | App-store presence | Capacitor, platform APIs, QA | Purchases, haptics, push, policies |

## Cross-feature design rules

1. New systems use existing `GameEvent` and durable domain event contracts; never patch Phaser scene files to award real coins.
2. Future skill modifiers need power-budget caps, clear UI and competition normalization.
3. Future events must preserve recovery routes, avoid permanently stranding broke players and be idempotent.
4. Future rankings need verified inputs/results and opt-in location scopes.
5. Every new island should mostly be authored data + art; physics engine changes require independent testing.
6. Large future systems must have kill switches and incremental launches.

## Prioritization filter

Before accepting a system for implementation, answer: Does it reinforce core merging? Is it fun to use more than once? Can we measure success? Can we ship a small version? Does it have a sound, fair economy? Can the team operate it? How will we turn it off safely?

## Suggested future documentation batches

- **Batch 2:** Full archipelago, island story bible, world graph, 100–300 mission structures.
- **Batch 3:** Economy, shop inventory, income/expense curves, progression balance and skill trees.
- **Batch 4:** Dynamic world, incidents, characters, reputation, rivals, weather and narrative.
- **Batch 5:** Social, competition, seasons, anti-cheat, local/country/global reward rules.
- **Batch 6:** Asset universe, animation/audio style guide, complete UI component and icon catalog.
- **Batch 7:** Native mobile strategy, live operations and performance at scale.
