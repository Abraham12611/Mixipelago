# 10 — Order Pricing, Revenue and Reward Formulas

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Keep pricing terminology precise
`orderCoinReward` is the authored payout for a successfully fulfilled customer in eligible game modes. `shopIncome` is a later aggregate projection, not a live per-collision wallet delta. `sales` can be a display metric without being spendable currency unless settled.

## Prototype formula
`eligibleOrderCoins = baseOrderCoins × difficultyFactor × boundedShopFactor` evaluated in integer arithmetic at authoritative result settlement, with caps and tie-breaking documented. Example only: base 12, difficulty x1.25, shop x1.10, final `floor(12×125×110/10000)=16` coins. The base alpha order score stays as Batch 3: `orderCoinReward × 10`; don't retroactively alter historical scores because payouts change.

## Revenue caps
For first alpha-to-economy rollout, do not enable arbitrary replay farming. Server policies can limit per-run order income, per-day repeat awards and bonuses. Reward calculation includes verified run ID and rule/content hashes; generate exactly one receipt.

## Special contracts
Future VIP, delivery, catering and event orders may use separate payout schedules and customer constraints. They should be separate authored policies, not a magic coin multiplier applied to every mission. Transparency requires the displayed reward to match the settlement rules for that mission version.

## Tuning metrics
Record realized median coins per completed mission, failed mission cost (zero in baseline), replay income, upgrade affordability and high/low skill stratification. Flag any player cohort that cannot afford its next required goal despite reasonable play.
