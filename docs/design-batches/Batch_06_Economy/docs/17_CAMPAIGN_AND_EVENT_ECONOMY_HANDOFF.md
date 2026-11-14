# 17 — Campaign, Mission Rewards, Treasures and Event Integration

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Source-of-truth boundaries
Batch 4 owns mission outcome and star thresholds. Batch 5 owns graph unlocks and treasure eligibility. Batch 6 owns spendable currency movement and purchases. Batch 7 owns skills and modifiers. Batch 10 owns incidents and weather, but cannot directly debit coins without an economy command.

## Result processing
Verify session → persist mission result receipt → resolve first-clear/eligible reward policies → settle ledger exactly once → emit `economy.reward_granted.v1` → rebuild player/shop projections → notify UI. A high-score replay can update best score/stars without minting a first-clear bonus.

## Treasure rewards
Treasure node has a `rewardPolicyId`, not a raw client-set coin delta. Successful claim uses `(playerId,treasureId,seasonScope)` uniqueness. In `v0.2.x` preview mode a chest may grant only a local nonmonetary badge; server wallet settlement activates with trusted economy.

## Future skills
Skill modifiers may affect eligible future reward formula within explicit caps, never the already-verified result and never standardized ranked scoring. Persist `rulesVersion` and `modifierSnapshotHash` in reward receipt.

## Failure examples
If an outbox consumer fails after wallet commit, retries must not award again. If graph updates after a mission was started, settle using pinned, eligible published content snapshot. If account sync finds local preview coins, do not convert them; show clear migration messaging.
