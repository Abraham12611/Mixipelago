# 10 — Explorer Skill Branch: Routes, Secrets and Discovery

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Promise
Exploration increases a player's *awareness* of optional opportunities, not access to content that isn't authored, published, or permitted.

## Proposed nodes
- `ex_compass_rose`: highlight the nearest already-unlocked mission branch on the map; never modify unlock state.
- `ex_treasure_sense`: show a gentle indicator when a **published and currently eligible** treasure clue exists in the region.
- `ex_cartographer`: add a filtered map journal for discovered landmarks.
- `ex_shortcut_scout`: reveal an optional alternate route hint only once the campaign graph author marks the hint visible.
- `ex_atlas_keeper`: unlock archive layouts and journey map cosmetics after completing a published exploration milestone.

## Boundaries
A hidden mandatory node violates Batch 5 graph invariants; no skill can reveal a database-secret field meant to stay unavailable. The map API returns only authorization-filtered hints. Offline clients may show cached known paths, but cannot claim newly discovered rewards until trusted sync.

## Side-effect ordering
`hint_revealed` is cosmetic/player-specific discovery state; `node_unlocked` is campaign state. They are separate event types and transactions. A talent tooltip must not call the unlock endpoint as a shortcut. Treasure rewards remain one-time claims with their own ledger keys.
