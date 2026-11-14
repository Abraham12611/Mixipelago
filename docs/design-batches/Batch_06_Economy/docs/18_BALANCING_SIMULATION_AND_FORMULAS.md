# 18 — Economic Balancing, Simulation Scenarios and Formulas

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Model player cohorts
Simulate: new/struggling, median, expert, completionist, aesthetic-focused, VIP-optimizer, intermittent/returning, and high-activity farmer. Run at least 10,000 synthetic progression trajectories per candidate ruleset when practical, with seeded reproducibility. Ensure no inevitable bankruptcy or impossible unlock sequence.

## Initial metrics
`coinsEarned/hour`, `coinsSpent/hour`, `purchaseAffordabilityMissions`, `medianUnspentBalance`, `progressionBlockedRate`, `timeToFirstUtilityUpgrade`, `timeToFirstCosmetic`, `sinkCoverage`, `top1percentWealthShare` and `replayFarmingYield`.

## Example goals (hypotheses)
- First starter utility: affordable after 3–5 normal mission clears.
- First cosmetic: affordable before first optional branching path.
- At least one meaningful purchase per progression band without grind-heavy loops.
- No mandatory recurring expenses during the first island.
- Returning players with minimal balances can still complete meaningful content.

## Formula hygiene
Use integer/decimal units with consistent rounding once at settlement. An example utility discount formula: `effectivePrice = max(minPrice, floor(basePrice × (10000 - discountBps)/10000))`, with `discountBps` capped below 10000. Never compose percent multipliers without a defined stacking and rounding order.

## Simulation workflow
Generate mission completion outcomes from Batch 4 fixtures; feed trusted reward policies; select agent spending behaviors; summarize purchase outcomes and stalls; compare distributions to targets; require owner approval for changes. Couple balance rules to `economyRulesVersion` and catalog hash for reproducibility.
