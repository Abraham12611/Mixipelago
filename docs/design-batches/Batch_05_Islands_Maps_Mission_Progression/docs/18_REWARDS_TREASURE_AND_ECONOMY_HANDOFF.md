# 18 — Rewards, Treasure Claims and Economy Integration

## Keep source concepts separate
- **Session score**: gameplay performance, computed by Batch 4.
- **Stars**: mission-quality rating, stored monotonically.
- **Preview coins**: client-local alpha demo values; **not spendable trusted currency**.
- **First-clear reward**: future idempotent server-authoritative grant.
- **Treasure chest**: world-map claim location with explicit entitlement.
- **Collectible cosmetic**: inventory ownership (Batch 8 later).

## Reward policy (future trusted play)
Each campaign node declares `rewardPolicyId`, not a hardcoded coin delta in the map renderer. `first_clear` is once per eligible player/mission; replay reward is explicitly zero by default pending Batch 6 economy design. Treasure claim is once per claim identity; season/event variants must use scoped claim keys.

## Treasure interaction flow
Treasure is visible/revealed → player selects → server validates unlock and unclaimed state → locks claim key → writes entitlement/ledger → returns reward receipt → animation plays. On network retry, replay same receipt, no second grant. In `v0.2.x` preview mode, a chest may only grant a **non-monetary preview badge or tutorial decoration**.

## Economy-safe design
Don't let client map JSON specify arbitrary spendable coin credits. The backend maps approved reward-policy IDs to bounded server values. Display rewards may be cached public metadata, but settlement uses validated server config. No unlimited coins for replaying entry mission; no extra reward from repeatedly toggling mission clear flags.

## Island rewards
Gateway travel is not a financial grant in itself. Island completion can unlock a cosmetic badge, theme or preview shop location. Later first-clear/resource rewards require a transaction, idempotent event, source version and rollback/audit policy.

## Edge cases
A treasure chest gets removed from a new map but was already claimed: retain receipt and cosmetic in inventory. Player starts claim then loses network: retry with same idempotency key. Two devices simultaneously claim: exactly one ledger entry. Replaying mission for higher stars updates stars without retriggering first clear reward.

## Analytics
Track claim shown/opened/claimed/rejected and reason, not secret reward payloads before eligibility. Calculate actual economic sinks/sources only from ledger events after trusted economy exists.
