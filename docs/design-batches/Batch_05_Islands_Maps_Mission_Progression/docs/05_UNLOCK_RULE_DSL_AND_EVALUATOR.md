# 05 — Unlock Rule DSL, Evaluation Order and Explainability

## Intent
Unlocks must be deterministic, authorable, cheap to evaluate and explainable without executing code from a content file. Use a limited JSON DSL with explicit semantics and exhaustive validation. The campaign evaluator is a **pure function**, taking immutable graph, result and flag snapshots.

## Supported expression nodes (v1 proposal)
- `always`: boolean true; only for entry nodes.
- `missionCleared`: stable `missionId`, minimum stars 1 by default; result must be eligible for the current trust tier.
- `minStars`: count of *best earned* stars over a specified authored list; do not count a mission twice.
- `nodeClaimed`: one-time checkpoint/treasure entitlement; requires secure proof once backend exists.
- `flagEquals`: whitelisted monotonic campaign flag ID and expected allowed literal.
- `allOf`: every child is true. Empty children are invalid.
- `anyOf`: at least one child true. Empty children are invalid.
- `not`: **defer for published permanent prerequisites** to avoid nonmonotonic gates that lock previously open paths; may be used for presentation-only discovery with explicit review.

## Evaluation order
1. Resolve manifest and requested player's progress trust tier.
2. Reject unsupported expression version, unknown references, excessive nesting/leaf count and invalid flag namespace.
3. Build the relevant result/flag indexes once.
4. Evaluate expressions, returning `eligible`, unmet requirement objects and dependencies used.
5. Apply publication/availability gates; an unavailable mission is not startable even if dependencies are satisfied.
6. Present localized explanations with actionable deep links to missions or milestones.

## Result example
```ts
{
  nodeId: 'cove-n003',
  visibility: 'visible',
  status: 'visible_locked',
  eligibility: false,
  unmet: [{ code: 'MISSION_CLEAR_REQUIRED', missionId: 'coconut-cove-002', minStars: 1 }]
}
```
Avoid assembling raw error strings inside the evaluator. UI translates stable reason codes.

## Rule limits and attack surface
Max depth recommended 8, max leaf predicates 64; cap evaluation time. No arbitrary HTTP requests, JS expressions, SQL conditions or client time-sensitive `Date.now()` in shipped content. If a seasonal requirement is added, the server issues an explicit feature/event eligibility claim, not an untrusted browser clock.

## Graph validator
Create a dependency graph by resolving every `missionCleared`, `nodeClaimed` and nested target dependency. Run topological sort for the permanent critical route. An expression depending on its own node, or a cycle A→B→A, is a hard validation error. **AnyOf does not excuse a cycle in a required branch unless editorial proof and explicit alternative handling are defined; fail closed for initial launch.**

## Critical nuance: stars
Stars are awarded by Batch 4's star criteria and are independent from coins. A node may require a specific star count, but don't create progression choke points that require perfect precision before the player has learned it. Validate a demonstrated winning solution to any hard star gate.

## Untrusted versus trusted progress
Local alpha preview progress may unlock local campaign nodes in `v0.2.x` if offline/local campaign mode is active. It must never be accepted as a verified entitlement, wallet grant or competitive qualification. After accounts launch, server evaluates durable unlocks from authenticated, verified receipts.
