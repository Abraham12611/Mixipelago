# 26 — Economy QA, Security, Load and Regression Matrix

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Mandatory test matrix
| Test | Expected result |
|---|---|
| Same claim posted twice | exactly one credit; same receipt returned |
| Two purchases with balance sufficient for one | at most one commits |
| Wrong price submitted by client | ignored/rejected; server catalog used |
| Request ID reused with changed payload | `IDEMPOTENCY_CONFLICT` |
| Locked shop upgrade | no debit or ownership |
| Two simultaneous first-clear results | exactly one first-clear payout |
| Wallet query for another player | denied |
| Client preview coin save imported on login | no trusted balance change |
| Worker retries outbox event | no repeated credit or entitlement |
| Purchase response lost after commit | retry retrieves successful receipt |
| Catalog changed during purchase | consistent snapshot, or explicit stale response |
| Negative grant/overflow amount | rejected, never underflow/overflow |
| Cosmetic purchased | UI visual changes; no gameplay stat mutation |
| Ranked session with VIP perks | standardized competitive profile |
| Offline shop purchase | clearly unavailable; no false success |
| 0-coin player | core mission remains accessible |
| Duplicate ledger projection | reconciliation detects and alerts |
| Mission replay | no first-clear refarming |
| Graph chest unclaimed retry | same claim receipt and value |
| RLS unauthorized direct write | denied |

## Testing layers
Unit: pure effects, prices, policy, caps and prerequisite resolver. Integration: Postgres transactions, parallel writes, RLS, auth, migrations. Contract: API schema and errors. E2E: shop UI pending/error states. Property-based: balance nonnegative and ledger sum invariant. Performance: request p95, lock hold duration, job lag, high-player transaction burst.

## Manual approval
All manual interface/play-feel tests go to owner. QA automation is required before review, and the team must not claim manual approval was performed by an engineer.
