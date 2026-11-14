# 11 — Islands, World Events, Incidents and Narrative (Overview)

**Status:** High-level design intent only. This batch intentionally does not write full lore, incidents, character arcs, map contents or economy simulation.

## Island framework

Suggested thematic starts: Coconut Cove (tutorial), Sunset Bay (tourism), Mango Market (trade), Coral Kingdom (rare recipes), Stormhaven (weather), Neon Paradise (nightlife), Frostberry Peaks (cold drinks), Golden Archipelago (late-game prestige). These are working names and pitches. Versioned art/map content separates region definition from mission logic.

Each island can supply: art theme, background audio, customer pools, unique rules, map subareas, shop plots, mission branches, discoveries and optional event hooks. One mission engine should support all islands.

## Incident engine (later)

`EventDefinition` describes eligibility, cooldown, rarity, choice options, costs, deadline and possible state transitions. `PlayerEventInstance` records the actual choice and result. Event Director consumes coarse, permissible state (progress, resources, active events, recovery capacity) to select an event; do not overfit punishment to players being broke.

Example **shop fire**: choices: immediate repair, special earning mission, short loan, delayed rebuild. Failure to meet a deadline should create alternative progression/recovery, never erase unlocked content. Insurance is an optional strategic investment once the economy is mature.

## Additional event categories

Positive opportunities (festival, influencer visit, new supplier), neutral changes (market demand shift, new neighbor), negative incidents (equipment outage, storm damage), rival challenges, world ceremonies, collectible discoveries, social/co-op events.

## Character and world identity

Named customers and rival owners can later have light recurring arcs, relationship flags and reputation effects. Character interactions remain concise and optional for players seeking quick puzzles. Avoid runtime generation of unmoderated financial/reward outcomes; all durable effects follow validated content rules.

## Technical integration

`world_event_started` → world state → mission catalog and UI → player choice → server transaction → economy/shops/progression → chronicle entry. Event scheduling via workers only when persistent accounts/DB are live.

## Later detail batch must cover

Map lore and geography, NPC registry, event catalog, trigger odds, fairness constraints, cooldowns, event simulation tests, recovery mechanics, seasonal world changes, illustrated story beats and moderation.
