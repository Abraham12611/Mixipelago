# 16 — Randomized Rewards, Odds, Guarantees and Safety

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Product policy
Mixipelago's baseline rewards are **deterministic**. Mystery chests are deferred until the game's economy and security are proven. No paid random chance for competitive power, and no core campaign progression locked behind uncertain prize rolls. If random rewards are ever monetized, obtain jurisdiction/platform legal review and disclose probabilities before purchase.

## Candidate random algorithm
Server pins a distribution (integer weights totaling a fixed denominator, e.g. 10,000), validates eligibility/pity constraints if any, rolls with cryptographically secure randomness, stores the outcome against a unique source receipt and then settles. Retries return the *same* outcome; they never roll again.

## Example policy
Three purely cosmetic options with weights `[7000, 2500, 500]` imply 70%, 25%, 5%. This is a **demonstration**, not the proposed paid reward distribution. Total must equal 10000. If duplicate protection rerolls, published *effective* probabilities must account for it; better to use explicit fallback tokens or grant a duplicate-safe cosmetic shard, if those exist.

## Pity and guarantees
If introduced, pity guarantees must be authored, independently testable, and disclosed to users; the pity counter is server-owned with atomic claim settlement. Do not let clients adjust seeds, weights, pity counts or sample repeatedly without consuming one entitlement.

## Compliance questions
Review age rating, gambling-lookalike UX, chance-asset pricing, regional restrictions, consumer protection, refund flows, data practices, and App Store/Play Store rules with specialist input before shipping paid randomness.

## Fallback decision
If the complexity or ethical cost outweighs retention benefit, do not implement mystery rewards; theme visually distinct fixed chests instead.
