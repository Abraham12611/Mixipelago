# 01 — World Map & Campaign Progression: Product Vision and Scope

**Batch:** 5 of 21 · **Status:** implementation proposal, not shipped features · **Companion:** Batches 1–4. This batch specifies *how* a player travels from individual puzzles to a connected archipelago campaign; it intentionally does not fully design stories, economic disasters, characters, or multiplayer.

## Experience promise
A player should enter the map and instantly understand **where they are, what they can play next, why a route is locked, what clearing the next mission gives them, and how far they have come**. The archipelago is both a navigation surface and a visual record of achievement. The island art, shops and discovered landmarks should gradually respond to progress while the map itself remains easy to use on a small phone.

## Non-goals for the 72-hour alpha
Do not delay `v0.1.0` for a map, account system, 100 missions, stories or cinematic island scenes. The alpha remains a single playable Classic Service mission. `v0.1.1/0.1.2` can introduce a tiny mission picker if the core game already works. A navigable Coconut Cove campaign graph belongs in the `v0.2.x` family.

## Product goals
- Provide a first-time user an obvious **Next Mission** action and an optional map browsing experience.
- Support branching paths, replay, mastery, hidden discoveries, rewards and island transitions with one consistent unlock evaluator.
- Build a content pipeline in which artists create map scenes and designers connect mission nodes **without modifying the physics engine**.
- Keep map navigation snappy and usable with keyboard, mouse, touch, text labels and reduced motion.
- Support hundreds of missions per island by streaming scene art and indexing graph metadata, rather than rendering every sprite at once.
- Preserve historical wins and active-session compatibility across content patches and rollbacks.

## Primary player journeys
1. **First clear:** finish `coconut-cove-001` → win summary → progress saved as preview-local → next mission unlocks → new node highlighted.
2. **Branch discovery:** encounter a fork → inspect mission cards → choose either route → return to the fork later.
3. **Replay:** revisit cleared mission → improve stars/score → see new best without losing earlier achievements.
4. **Island transfer:** satisfy gateway requirements → see destination preview → confirm travel → stream a new island map.
5. **Hidden content:** meet an authored discovery condition → reveal a hidden path and explain the discovery.
6. **Blocked content:** tap a lock → view exact unmet requirement and a navigable route to satisfy it.

## Guardrails
Mission outcome and map completion are distinct state machines. A cosmetic island renovation is not a prerequisite unless explicitly authored as one. Event expiry must never permanently strand campaign players. Paid purchases cannot bypass otherwise mandatory puzzle learning gates. All manual UI/gameplay approval goes through the owner; engineers automate logic and prepare evidence.

## Definition of successful Batch 5 implementation
A small but genuine campaign is playable end to end; prerequisites are visible and correct; no graph dead ends, duplicated grants or progress regressions occur; mobile/desktop navigation feels native; and content publishers can safely expand the archipelago without shipping application code for every new mission.
