# 14 — Milestones, First Clears and Chapter Rewards

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Milestone taxonomy
- First mission clear: Batch 4 verified result, Batch 6 owns coin payout, Batch 7 owns XP, Batch 8 may attach collectible badge.
- Star threshold: Batch 5 owns monotonic best-star state; Batch 8 uses unique `(missionId,threshold)` achievement/entitlement.
- Chapter clear and island gateway: Batch 5 evaluates required nodes; Batch 8 attaches milestone presentation and approved one-off cosmetics.
- Shop upgrade: Batch 6 purchase receipt, not clicking the upgrade card.
- High-score feat: only eligible verified runs under a pinned score-profile version, never mixed across incompatible rulesets.

## Examples
`first-service-badge` is a cosmetic once-ever entitlement on first verified order; `cove-trailblazer-title` unlocks at a published gateway; `three-star-sampler` unlocks when three distinct campaign missions reach best 3 stars. These are candidate content rules, not shipped achievements.

## Claim sequencing
Mission result verified → campaign projection committed → milestone evidence established → achievement stage written → claimable reward generated → user accepts if manual → inventory granted. Notification delivery is asynchronous; a skipped animation never blocks durable state.

## Versioning
If an island adds missions later, preserve historically earned chapter-clear edition badges. New 100% completion rewards may be `edition2` milestones rather than invalidating old claims. A gateway's historical eligibility is pinned to its published content snapshot.

## Validation
No first-clear payout on mission replay, no regression from 3 stars to 1, no achievement from draft/unpublished nodes, and no duplicate milestone award from parallel event consumers.
