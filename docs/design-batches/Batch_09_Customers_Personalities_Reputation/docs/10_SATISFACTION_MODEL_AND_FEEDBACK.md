# 10 — Satisfaction Model, Deterministic Scoring and Feedback

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Principle
Satisfaction is an **optional, bounded, derived service-quality signal**, not a new score and not an authority to award coins. Starting candidate scale: integer `0..10000` representing 0–100%. Only verified service evidence can update durable aggregates. The alpha does not calculate persistent satisfaction at all.

## Candidate formula (v0.4.2, provisional)
For an eligible verified encounter, `base=5000`, `fulfillmentBonus=+2200` for completed requested order, `missionClearBonus=+600` if the run wins, `timelinessBonus=0` in untimed Classic Service, `publishedExtraBonus` in `[0,400]`, `publishedPenalty` in `[0,1500]` for explicitly enabled advanced timed service. `satisfaction=clamp(0,10000,base+bonuses-penalties)`. In the baseline example, a clear fulfilled order yields **7800**; a fulfilled order in a lost session yields **7200** if verified policy permits such evidence. Policies must specify whether lost-run fulfillment contributes to trusted satisfaction; default recommendation is **only verified completed runs** to prevent farming.

## Derived signals
For reputation, candidate `repDelta=floor((satisfaction-5000)/100)` clamped to `[-30,+30]` per eligible encounter, then cumulative per-run cap `[-60,+60]`. A non-eligible mission contributes zero. This is a *proposed formula*, not a deployed economic effect. Positive/negative sign rules must be tested carefully, including integer division on negatives. Do not apply permanent reputation decay for inactivity.

## No hidden timers
Classic Service and beginner missions should not penalize a customer based on wall-clock time. Later patience-enabled modes use **active simulation ticks**, pause on tab backgrounding, and expose a readable timer. Any penalty requires an explicit published `customerPolicyVersion` and UI warning.

## Feedback UX
After a trusted mission, show an easy-to-understand breakdown: order fulfilled, chapter objective, optional service challenge and reputation impact. If server verification is pending, show `Pending verification`; don't celebrate a permanent reputation increase before a receipt is committed. Never weaponize low satisfaction with shaming language.
