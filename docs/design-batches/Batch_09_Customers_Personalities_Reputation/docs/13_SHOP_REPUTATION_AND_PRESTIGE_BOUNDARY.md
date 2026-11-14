# 13 — Shop Reputation, Prestige and Business Integrity

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Ownership and separation
Batch 6 owns the authoritative `ShopReputation` projection and all shop economics. Batch 9 supplies verified customer satisfaction evidence; it does **not** directly debit or credit the wallet. `reputation` measures reliable service trust, `prestige` measures aesthetic/status investment, `playerLevel` is Batch 7 XP, and `score` is Batch 4 session performance. Keep these separate in schema and UI.

## Candidate update policy
Calculate one authorized customer observation per eligible encounter; resolve `repDelta` under a versioned policy, aggregate and cap per verified run, then submit to the Batch 6 reputation service with a stable source ID. Materialized reputation is bounded `0..10000` (candidate). Each delta stores `before`, `after`, source run, policy hash, and `createdAt`. Negative results in ordinary loss must be gentle and avoid trapping new players.

## Example
Current shop rep `5200`, verified eligible completed run containing one satisfied encounter `7800` -> candidate delta `+28` (floor((7800−5000)/100)); projected rep `5228`. Repeating same result receipt returns original observation and **does not add another +28**. Existing 0.3 economy behavior remains unchanged until this feature is gated on.

## Effects and visibility
Reputation may unlock authored customer pools or cosmetic titles in a later release. It does not retroactively change pending orders, completed score or first-clear coins. Financial effects must be defined by Batch 6 approved modifier snapshots and capped, not inferred from cosmetic tier or reputation icon.

## Player protection
There must be a bounded recovery path from low reputation. Never have a negative customer event automatically launch an unaffordable repair, forced paid action, or permanent mission lock. Validate anti-farming and degradation fairness through cross-skill simulations.
