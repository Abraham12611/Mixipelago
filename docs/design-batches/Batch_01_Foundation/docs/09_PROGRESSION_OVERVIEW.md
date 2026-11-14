# 09 — Progression Systems Overview (Future Design Batch)

**Scope:** Major concepts and integration contracts only. Story trees, island missions, skill node catalogs and precise level balance will be designed in later batches.

## Progression layers

1. **Individual puzzle run:** score, orders, combo, win/fail.
2. **Mission:** star count, best score, replay, rewards.
3. **Island path:** branching unlocked mission nodes, side quests, chests.
4. **Player/entrepreneur level:** experience, milestone unlocks.
5. **Shop prestige:** individual property improvement and reputation.
6. **Drink mastery:** unlocked tiers, recipes, personal bests.
7. **Skills:** specialized bonuses, prerequisites and points.
8. **Competitive rank:** time-bounded verified seasons.
9. **Collections:** discovered cosmetic/reward assets.
10. **Island Chronicle:** historical milestones and consequential choices.

## Map organization

Long-term concept: multiple visually distinct islands, each with ~100–300 mission nodes, including main route, optional branches and locked secrets. These numbers are a creative design target, not launch commitments. Store islands/missions in a versioned directed graph (DAG where feasible) with explicit prerequisites; don't hardcode a level number as a linear index.

Mission schema: `missionId`, `islandId`, `chapterId`, `contentVersion`, `prerequisites[]`, `gameMode`, `boardPreset`, `objectives[]`, `rewards`, `unlockEffects[]`, `artThemeId`. Cycles in prerequisite graph should be rejected by content validation unless expressly supported for repeatable events.

## Mission progression rules

- At least one clear next playable mission; no unexplainable dead ends.
- Stars reflect measurable level performance (e.g., score/move efficiency), not mere luck.
- Replay rewards have safe caps to avoid infinite economic farming.
- Locked paths explain prerequisites.
- New island unlocks must be transactional and durable when backend is live.
- Event missions cannot permanently block main story if limited-time event expires.

## Player-level and skills integration

`mission_completed` earns XP → level threshold → unlockable content/skill points → skills service computes bounded modifiers → gameplay/customer/economy services consume modifiers. Crucial separation: ranked competitions normalize or disable progression advantages.

Potential skill branches (overview): Master Mixologist, Hospitality, Business Mogul, Explorer, Risk Strategist, Puzzle Specialist. Example `Golden Guestlist` increases VIP probability within limits; not a guarantee that every customer is rich.

## UX concepts

World map is navigable, with active mission highlighted. Player can zoom/pan, select node, see rewards/requirements, start. On mobile, node touch targets are large, and a "Current Mission" shortcut recenters map. Desktop gets hover/tooltips and precise controls. Large island scenes may be split into streamed/cached chunks.

## Later design deliverables required

- World graph and mission density by island.
- Levels 1–300 difficulty curve and scoring targets.
- Unlock/replay economy and reward caps.
- Full skill trees with prerequisite graph, power budgets and respec rules.
- Chronicle event ontology and UI.
- Dynamic pacing and onboarding unlock schedule.
