# 33 — Threat Model, Abuse Prevention and Security Controls

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Main attackers and impacts
A malicious client may replay `order_fulfilled`, forge customer satisfaction, force VIP rerolls, overwrite loyalty, claim guest collectibles, query another player's relationship journal, or inflate shop reputation to unlock better rewards. Also consider repeated concurrent requests, compromised admin catalogs and fraudulent session receipts.

## Minimum controls
- Backend verifies result receipt/signature or authoritative evidence before any durable observation.
- Unique source keys and transactional upserts prevent duplicate credit through retries and outbox redelivery.
- VIP/guest reservation is server-side, idempotent and rate-limited, with seed commitment stored before response.
- RLS/private API authorizes every player/shop relationship; browser has no direct write permission to economic/relationship state.
- Published catalogs are signed/hash-pinned, reviewed and have value/cap validations.
- No client-supplied `tipAmount`, `vipChance`, `repDelta`, `loyaltyPoints`, or `reviewScore` is accepted as truth.

## Competitive integrity
Normalized ranked missions use fixed customer/orders independent of skills, economy and guest friendship. Score comes from Batch 4; VIP/loyalty is not a new competitive score faucet. Suspicious rankings are verified against replay before awarding future seasonal benefits.

## Privacy
Guest interactions are fictional gameplay telemetry. Avoid collecting real-world player identity/demographics for segmentation. Store source IDs, not raw sensitive dialogue or precise location. Aggregate business analytics with privacy-conscious retention and deletion controls.

## Adversarial tests
Two devices race claim; repeated REST retries; malformed negative satisfaction; reused idempotency key with changed body; unauthorized player reads guest journal; invalid catalog references; admin accidentally publishes zero-eligible pool; stale signed config; account deleted during reputation rebuild.
