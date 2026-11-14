# 04 — Node Types, Edge Semantics and Route Design

## Node types
| Type | Action | Success/reward source | Visual expression |
|---|---|---|---|
| `mission` | Open versioned Classic/other supported puzzle | Mission result receipt | Numbered/starred medallion |
| `checkpoint` | Review district progress and optionally claim authored grant | Validated checkpoint rule | Flag or small landmark |
| `treasure` | Claim one-time collection/resource | Idempotent claim | Chest / bottle capsule |
| `gateway` | Travel to another district or island | Eligibility rule + transition | Pier, boat, bridge, portal |
| `discovery` | Reveal hidden chapter/collectible | Discovery condition | Question marker / sparkle |
| `shop` | Open business view if enabled | Batch 6 shop service | Shop marker |
| `event` | Open time-bounded content if enabled | Batch 12 event service | Calendar/banner |
| `landmark` | Inspect an authored world milestone | Optional progress flag | Scenic pin |
Only `mission` is required for the first campaign milestone. Future node types must be gated until their services exist. A disabled node may be preview-only but cannot offer a nonfunctional button.

## Edge types
`route` = normal path line, `shortcut` = optional convenience, `secret` = hidden until reveal, `gateway` = explicit island change, `scenic` = decorative with no unlock meaning. Edges have unique ID, ordered `from` and `to`, control points for rendering, style ID and optional reveal condition. **Do not infer prerequisites solely from edge direction.**

## Primary versus optional routes
Each chapter has a clear critical route with a unique visible next objective. Optional side routes can reconnect, carry collectibles or provide mastery challenges. Branching should feel empowering, not like a maze: first island can introduce one gentle fork after core fundamentals. Each fork needs text explaining its identity (e.g., "Precision route" versus "Service route") rather than simply differently colored lines.

## Gate examples
- Node C unlocks after node B is cleared.
- Treasure T appears when a player has earned 3 stars on mission A; claiming T is separate.
- Alternate branch D unlocks after **either** mission B or C is cleared (`anyOf`), not both.
- Island travel G requires an authored mainline milestone and an optional presentation transition; side missions remain accessible.

## Node status vocabulary
`hidden` (not revealed), `visible_locked`, `available`, `attempted`, `cleared`, `mastered`, `retired`. `mastered` is a display state with a defined local star criterion, not an independent outcome. On older versions distinguish `legacy_cleared` if score/ratings cannot be compared under new rules.

## Density and wayfinding
Avoid placing 100 nodes on a single-screen thumbnail. Group nodes into districts or map chunks. At normal mobile zoom, the active route should show a handful of choices; at reduced zoom, aggregate distant nodes into landmark clusters and a progress badge. A **Next Mission** control is always available.

## Edge cases
If a secret edge is revealed but destination mission retires, show a retired/coming replacement state with a safe fallback. If a player completes optional D before mainline C, do not roll back; recompute `anyOf` and all downstream gates. If an island is renamed, route via stable ID and update only localized labels/assets.
