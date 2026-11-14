# 24 — Graph Validation, Dead-End Analysis and Mission Feasibility

## Static checks
JSON schema validates types and bounds. Semantic checker ensures unique IDs, known islands/chapter IDs, valid edges, supported unlock rules, acyclic dependency graph, referenced published mission versions and resolvable content asset IDs. The mainline must have at least one entry and a viable path to chapter goal or a deliberate end-of-published-content marker.

## Reachability is not merely graph traversal
Drawing an edge A→B does not mean B is achievable; conditions may demand three stars on an impossible mission. Compute conservative optimistic reachable states using authored rules, then require simulation proof/human validation for high-star prerequisites and gateway missions. Static checker reports `UNKNOWN_SOLVABILITY` rather than declaring success.

## Dependency cycles
For every unlock expression, map `missionCleared` to its corresponding node ID(s); add prerequisite dependencies. A cycle in published permanent unlocks is an error. Multiple `anyOf` branches still need analysis; conservative rules may reject suspicious cycles even if one path hypothetically escapes.

## Publication barriers
- No published node links to a `draft` mission.
- No critical path relies only on secret, time-limited, disabled-shop or future-feature content.
- Every lock has at least one human-readable requirement code.
- Every branch rejoin has satisfiable prerequisites.
- No node auto-claims a reward merely because a line animation played.
- Compatibility report explains what changed for users with old completed nodes.

## Automated graph sampling
Generate sample player-progress profiles: none cleared; only mainline; optional branch A; branch B; all 1-stars; all 3-stars; old-content receipts; partially revealed secrets; impossible locked branch. Assert projection and next mission selection for each. A property-based test can generate DAGs and verify that adding a monotonic clear never locks previously available nodes.

## Runtime safety
Even published content can fail due to networking or a bad artifact. Runtime must detect an unsupported mission ref and show `Unavailable — try updating` rather than attempt launching. Keep last-known-good graph manifest in cache for safe rollback.

## Tools
`tools/validate_batch5.py` handles structural and selected semantic checks for example graphs. It does **not** prove real physical solvability, render aesthetics, reward accounting or browser responsiveness. The engineering CI must integrate Batch 4's headless golden-replay tests separately.
