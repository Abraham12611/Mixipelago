# 15 — Modifier Stacking, Caps, Rounding and Conflict Resolution

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Standard evaluation order (candidate)
1. Start from published base stats for the eligible domain/mode.
2. Apply additive absolute contributions (`percentage_point_add`, `flat_add`) within named buckets.
3. Apply explicitly authorized multiplicative benefits with bounded maximum.
4. Apply hard target caps and floors; clamp invalid combinations.
5. Round money using integer coin units and an explicitly published rule (floor to whole coin for positive payouts; avoid floating arithmetic for money).
6. Return an explanation tree with source, raw contribution, final impact and whether capped/disabled.

## Proposed caps (subject to data)
| Stat | Candidate clamp | Rationale |
|---|---|---|
| `guest.vip_probability` | 0..0.20 absolute | Prevent VIP-only shops |
| `trusted.order_coin_multiplier` | 1.0..1.35 | Limit runaway compounding |
| `trusted.tip_multiplier` | 1.0..1.50 | Separate additive tips from order payouts |
| `shop.upgrade_discount` | 0..0.15 | Avoid free shops and discount arbitrage |
| `ui.next_spawn_preview_count` | 1..2 total | Preserve puzzle difficulty |
| `active_skill_slots` | 0..3 | Control cognitive overload |

## Example VIP calculation
`base 0.05 + seating 0.02 + skill rank2 0.02 + reputation 0.01 = 0.10`; cap 0.20. An exception is a designer-authored mission with fixed customers, in which the customer list is not sampled from this probability at all.

## Pitfalls
- Never multiply `1.05` from each bonus to produce unexplained exponential growth when the product means +5 percentage points.
- Reject NaN, infinity, negative values for nonnegative stats, integer overflow and configs with contradictory cap ranges.
- Do not round per component and then again at total in a way that makes transaction retries differ.
- Server invoices, score receipts and QA trace logs must use the *same version-pinned evaluator* as the preview. A browser estimate cannot authorize a purchase.

## Competitive fairness
A normalized profile is an input override, not a post-hoc subtraction. Compute competitive scores from standardized rules before submitting leaderboards; do not try to reverse purchased bonuses after a session ends.
