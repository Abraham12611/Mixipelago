# 35 — QA Matrix, Fixtures, Property Tests and Manual Acceptance

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Automated property tests
- XP level curve monotonic: `xp_to_next(L)>0`; cumulative thresholds strictly increase.
- For any valid XP grant, `levelAfter >= levelBefore`, points earned reflect every threshold crossed exactly once.
- Purchase never makes available points negative; rank ≤ max; no cycle in an enabled graph; every published node path is reachable under level/point cap.
- Modifier resolver deterministic for the same ordered versioned inputs; clamps within published caps.
- Respec preserves XP and earned points; changes only allocations, loadout and point availability.
- Ranked resolver output independent of personal skill rank/shop-upgrade inputs.
- Source idempotency and allocation request idempotency hold under interleaved/retried commands.

## Test matrix
| Case | Action | Expected |
|---|---|---|
| XP-01 | first verified 100XP | level 2, one earned point |
| XP-02 | same receipt twice | one XP grant, same response |
| XP-03 | first grant crosses 2 levels | 2 level milestones, 2 points |
| XP-04 | client submits local preview XP | rejected/no trust |
| SK-01 | purchase unpublished node | `NODE_UNPUBLISHED` |
| SK-02 | purchase rank 2 from rank 0 | `SKILL_RANK_SEQUENCE` |
| SK-03 | two concurrent spends with one point | one succeeds |
| SK-04 | incompatible catalog pin | `CATALOG_STALE` |
| RS-01 | respec twice same request | one refund |
| CO-01 | personal max build in ranked | identical effective profile to novice |
| CU-01 | VIP rank2 + seating | 10% candidate rate, not guaranteed arrivals |
| CU-02 | refresh customer encounter | does not re-roll |
| UI-01 | offline allocation attempt | saved draft; no confirmed grant |
| UI-02 | large text / keyboard only | full access to details and Learn |

## Manual owner test scripts
Owner manually tests first level-up celebration, first point allocation, skill detail comprehensibility, desktop graph interaction, mobile bottom sheet, respec confirmation, no-regret recovery, and standardized-ranked disclosure. Engineers provide deployed URLs, deterministic test accounts/fixtures and observed logs; do not self-certify owner play feel.

## Evidence
Record versioned test run and captured issue ID for failures; docs-only fixture validation does not count as end-to-end proof. No production launch until the owner approves manual UI and a security reviewer approves trusted transactions.
