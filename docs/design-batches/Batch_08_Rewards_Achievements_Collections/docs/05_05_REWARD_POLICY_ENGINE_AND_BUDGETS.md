# 05 — Reward Policy Resolver, Budgets and Caps

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Purpose
One versioned resolver maps verified facts into rewards. It must be a pure evaluator for a pinned policy and server facts, with persistence performed by the settlement service. Policy JSON is content authored and validated; no arbitrary expressions, SQL, JavaScript, or unbounded eval in the CMS.

## Suggested rule fields
`policyId`, `policyVersion`, `status`, `sourceKind`, `scope`, `claimMode`, `rewards[]`, `eligibility[]`, `limit{perPlayer,perWindow,global}`, `validFrom`, `validUntil`, `competitiveEligibility`, `fallback`, `ownerApprovalRef`.

## Example policy
```json
{
  "policyId":"ach-first-service-badge", "policyVersion":1,
  "sourceKind":"achievement_milestone", "scope":"lifetime",
  "claimMode":"manual", "rewards":[{"kind":"cosmetic","itemId":"badge-first-service","quantity":1}],
  "maxGrantsPerPlayer":1, "status":"draft"
}
```

## Resolution order
Check account/auth → source proof → active published policy → eligibility → time window → scope unique constraint → per-player limits → global budget reservation → create entitlement → settle. If a globally finite grant is exhausted, return `REWARD_BUDGET_EXHAUSTED` and show a predeclared fallback if one exists; do not substitute unannounced lower value.

## Numeric policy
Store integer counts and integer currency minor units. Never use floating-point currency. Rewards with chance distributions require exact integer weights and full odds disclosure; ordinary core mission prizes should be deterministic. Coin bonuses from player skills can influence eligible policy formulas only through Batch 6's capped, versioned modifier resolver; a published first-clear amount may be pinned without modifier for consistency.

## Anti-farming
Rewards never automatically scale with number of UI opens, repeat button clicks or event delivery. Replays grant no additional first-clear resource. Exponential achievement rewards are forbidden unless independently reviewed for economic impact. Daily maximum faucet values must be simulated with the economy balance harness.
