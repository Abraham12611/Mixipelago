# 16 — Drink Ladder Difficulty, Quantitative Balance and Content Fairness

## Quantities to model

A two-to-one merge implies exponentially increasing raw input cost. If a tier-1 object is a unit, `baseCost(n)=2^(n−1)` for producing one tier-n glass from scratch. Thus core tier 1..8 costs are `[1, 2, 4, 8, 16, 32, 64, 128]`. These costs are *theoretical lower bounds*, not minimum shots in a level seeded with existing objects or tier-2 spawns.

If a tier-3 output is consumed by an order, it no longer contributes toward a tier-4. Resource budgeting for multiple orders sums required units after accounting for free starting bodies and spawned tiers. The authoring tool must know the specific serving policy and output tier before approving mission feasibility.

## Fundamental metrics

- `shotEfficiency`: mission-relevant output base units / total spawned tier-1 equivalents.
- `mergeRate`: committed merges / accepted shots.
- `chainDepth` and `chainRoots`: measure depth and causal origin, not mere time proximity.
- `orderCompletionRate`: orders completed / total orders encountered.
- `firstAttemptWinRate`: cohort win rate on first valid run.
- `timeToFirstMerge` and `timeToFirstOrder`.
- `boardPressure`: active drink count / capacity; boundary grace usage.
- `wastedShots`: accepted shots with no near-term progress (interpret cautiously; setup shots can be strategic).

## Proposed early mission ramp

| Mission | Objective | Starting support | Teaching point | Complexity guard |
|---|---|---|---|---|
| Cove 001 | serve tier 2, then tier 3 | sparse tier-1 bodies and curated queue | basic aim and service | scripted test proves success |
| Cove 002 | two tier-2 orders | starting tier-1 pair | priority and order quantity | no timer |
| Cove 003 | serve tier 4 | helpful tier-2 seed | resource planning | generous shot allowance |
| Cove 004 | 2-link chain goal | authored aligned tiers | chain ancestry | visible expected path |
| Cove 005 | score target with board pressure | seeded mixed low tiers | space management | early rescue feedback |

Concrete values remain proposals pending owner-led playtests. Do not make claims of tested solvability until golden input traces exist.

## Sample calculations

If a mission asks for two tier-3 outputs, it needs ≥8 tier-1 equivalents without seeded bodies; if it asks for one tier-3 and one tier-4 and both are automatically served, it needs ≥12. A tier-8 in normal small-shot missions is unrealistic without seeded advanced drinks. With weighted tier-2 spawns, calculate an optimistic and conservative lower bound based on the actual finite queue, not an assumed mean.

## Difficulty director rules

Difficulty is a product of geometry, queue, order targets, collision friction, shot budget and starting state. Prefer adjusting one dimension at a time. Changing a collision preset across ordinary adjacent levels may harm skill transfer; reserve physics variations for clearly named modes. If the table becomes crowded, provide player hints or an approved recoverability mechanic; avoid opaque systems that make purchases necessary.

## Balance experiment design

A/B tests need distinct `contentVersion`/`experimentId`, consistent assignment across retries, guardrails for latency/crashes, and ethical communication if rewards change. Key candidates: first queue composition, available tier-2 spawn weight, board size, merge effect duration, order target mix and chain combo bonus. Do not A/B core scoring in active ranked seasons without rule separation.

## QA automation proposals

- Static graph cost calculator flags impossible orders under finite shot counts.
- Random board generator property tests invariants.
- Seeded scripted agents sweep 100+ curated queues to estimate soft-lock risk.
- Content QA dashboard shows first-attempt completion by cohort, device and level version.
- All 'difficult' missions need owner gameplay approval; bot solvability alone is not proof of enjoyability.

## Risks

Theoretical input cost can encourage excessive farming. Mitigate with meaningful intermediate spawns, varied objective types, clear milestones and mission rewards. Do not raise costs just to force purchases or reward addictive play cycles. Batch 4 will specify full difficulty/mode design; this is the drink-graph quantitative foundation.
