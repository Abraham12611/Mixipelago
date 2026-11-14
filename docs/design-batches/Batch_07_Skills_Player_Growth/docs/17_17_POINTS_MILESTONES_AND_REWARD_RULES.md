# 17 — Skill Point Budget, Milestones and Anti-Farming

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## First release candidate
- Level 1 = 0 points; levels 2–20 yield one point each, maximum **19** earned points at cap.
- Spending a skill point is not spending currency. There is **no coins-to-skill-points conversion** and no real-money sale of points.
- Future milestone grants (island quests, special achievements) are separate entitlements and must be explicitly approved; by default only level-up supplies points.
- A skill rank's cost is a nonnegative positive integer defined by its catalog. Default rank cost is one point; rare higher ranks may cost two later. More than one rank cannot be bought in one unvalidated client batch.

## Invariants
`earnedPoints = sum(distinct milestone grants)`; `allocatedPoints = sum(current catalog costs for active rank allocations)` **unless grandfathered cost locks apply**; `availablePoints = earnedPoints - allocatedPoints - reservedPoints >= 0`. When catalog point costs change, reconcile through migration receipts, not by letting negative points appear.

## Edge cases
- Player leveling up by 3 levels from one verified grant must receive 3 independent level milestone records and associated points, exactly once each.
- Max-level XP attempts do not overflow or secretly mint points.
- Respec refunds point allocations; it does not retract the earned-milestone ledger.
- Two respecs racing each other should not double refund.
- Account restore on another device rehydrates the server projection, not a local accumulation.

## Antifarming rule
Mission replay rewards and XP follow Batch 4 and the trusted Batch 6 verified receipt policy. In v0.4.0 there is no repeat XP and no raw-merge XP. Players cannot farm by manually changing a mission or catalog hash.
