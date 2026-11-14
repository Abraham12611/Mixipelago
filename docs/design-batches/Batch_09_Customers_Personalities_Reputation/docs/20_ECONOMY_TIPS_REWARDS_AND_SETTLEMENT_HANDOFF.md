# 20 — Customer Rewards, Tips, Coins and Economic Source Boundaries

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Critical distinction
`orderCoinReward` is a **published mission payout unit** and the Batch 3/4 order score bonus uses it (`orderCoinReward × 10` in alpha). `tip` or `customer appreciation bonus` is a future independent reward policy. `shopRevenue` may be an aggregate metric but is not automatically a wallet credit. The interface must not promise currency based on a customer portrait alone.

## Settlement path
Verified mission result -> validated `order_fulfilled` evidence with source receipts -> Batch 6 reward-policy resolver -> wallet ledger transaction -> outbox -> client receipt. Duplicate customer event, network timeout or repeat mission cannot mint the same first-clear/order reward twice.

## Tips (deferred)
A tip, if enabled, must be capped, mode-aware and clearly described. Proposed policy: tips apply only to a verified unique eligible customer encounter, not on every cosmetic reaction; integer rounding after all multipliers; unique source tuple `(playerId, encounterId, rewardPolicyVersion)`; no unlimited tip farming by repeatedly losing/abandoning a mission.

## Economy fairness
VIP base payouts may be higher but must show corresponding challenge and expected reward. The game must remain finishable without real-money purchases, optional ads or shop upgrades. A player's cosmetic purchase does not imply extra customer tips unless an explicit approved gameplay perk exists—and standardized ranked modes ignore that perk.

## Error conditions
`REWARD_PENDING_VERIFICATION`, `POLICY_STALE`, `SOURCE_ALREADY_SETTLED`, `NOT_ELIGIBLE`, `WALLET_UNAVAILABLE`. Show a pending receipt status; do not optimistically alter trusted balance. Never directly access the service-role database key from Phaser or browser code.
