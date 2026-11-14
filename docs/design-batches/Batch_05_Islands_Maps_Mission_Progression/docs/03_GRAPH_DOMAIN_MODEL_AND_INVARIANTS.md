# 03 — Canonical World Graph Model and Invariants

## Domain separation
- **`MissionDefinition` (Batch 4):** simulation payload: board, spawn, orders, goal, mode and rewards. Immutable by `(missionId, missionVersion, contentHash)` once published.
- **`CampaignNode`:** the place a player selects on the world map; references a versioned mission **only if type `mission`**. A treasure or gateway node is not a physics mission.
- **`CampaignEdge`:** a visible connection between nodes, optionally expressing travel presentation; not by itself proof of availability.
- **`UnlockExpression`:** pure, bounded rule-language evaluated against player progress and approved world flags.
- **`CampaignSnapshot`:** derived state of node visibility, unlock eligibility and completed landmarks; can be recalculated from canonical results.
- **`PlayerMissionResult`:** monotonic best stats and provenance of verified versus local-preview outcomes.

## Keys and cardinality
`worldId` and `islandId` globally stable kebab IDs. `nodeId` globally unique (suggest `cove-n001` rather than numeric `1`); `missionId` already uses `coconut-cove-001`. One mission can be referenced from multiple locations *only with explicit editorial approval* (repeatable tutorials/event cards); by default reject accidental duplicates. Each node belongs to one island and one authored chapter; edges may cross islands only when `kind='gateway'`.

## A directed unlock graph, not a level array
The prerequisite dependency graph should be acyclic for permanent campaign unlocks. Visual edges may be bidirectional for browsing and may form loops if artistically useful; **dependency cycles are forbidden**. Model alternative path logic through `anyOf`, not reciprocal dependencies. Repeatable events use a separate repeat/scheduling model.

## Core invariants
1. Every published mission node points to an existing, supported, published `MissionDefinition` at a precise version or immutable release pointer.
2. Every published island has an entry node and at least one currently achievable forward path to a defined milestone. No published required node is permanently unreachable.
3. Every referenced node exists and every cross-island edge is typed and approved.
4. Unmet requirements are explainable in a localized UI; no arbitrary code predicates.
5. Mission results never downgrade: `bestStars = max`, `bestScore = max`, best shots/time tracked with explicit semantics.
6. First-clear grants are idempotent; reward policies are separate from whether a node appears complete.
7. Content changes are immutable publication revisions; active runs continue with their pinned mission hashes.
8. Draft placeholders are excluded from player-facing playable route calculation.
9. No timed event is a hard prerequisite for permanent mainline completion unless an evergreen fallback exists.
10. Client rendering cannot grant access, stars, coins, collectibles or backend flags.

## Pure state computation
`deriveNodeState(node, playerProgress, manifest)` produces a `{visibility, status, requirementExplanations, selectedAction}` view model. Do not persist the rendered status string as the authoritative truth. Use functional tests with mocked progress. Server progression must independently validate any client-supplied node ID.

## Where rules live
Campaign logic belongs in `packages/campaign-core`; mission execution in `packages/game-core`; asset layout in map content; trusted progression in backend domain services. Share discriminated types but not privileged database access.
