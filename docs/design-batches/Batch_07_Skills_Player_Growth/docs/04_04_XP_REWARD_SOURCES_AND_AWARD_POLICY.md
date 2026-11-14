# 04 — XP Sources, Verification and Reward Receipts

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Initial approved source categories (design candidates)
| Source | Timing | XP | Repeatability | Validation |
|---|---|---:|---|---|
| First clear of published campaign mission | mission result settlement | Published mission XP (e.g., 80–180) | Once per mission revision policy | Server-verified result + first-clear receipt |
| First completion of optional tutorial milestone | named step | 50 | Once per milestone | Versioned tutorial milestone |
| First verified island chapter completion | chapter unlock | 150 | Once per chapter | Graph prerequisites + result state |
| Special quest reward (later) | quest claim | Authored amount | Per quest run with limits | Quest server verification |
| Replayed mission | after first clear | **0** in v0.4.0 | No repeat XP | No grant |
| Raw glass merge | client physics | **0** | Never XP | Cosmetic / session scoring only |
| Untrusted preview coin balance | local alpha | **0** | Never converted | Ignore |
| Cosmetic purchase / ad view | store or UI | **0** | Never | Avoid purchased character advantage |

## First clear algorithm
1. Verify auth, session proof, mission publication and result acceptance.
2. Within a database transaction, insert `xp_grants(source_type, source_id, policy_version)` with a unique idempotency key scoped to player and source entitlement.
3. If grant already exists, return the prior grant, no new XP.
4. Atomically update `xp_total`, recompute level (possibly several levels if a single reward crosses thresholds), and insert each attained-level milestone.
5. Grant skill points for each new level via a unique `(player_id, level)` record.
6. Commit and emit an outbox event; UI receives trusted projection.

**Important:** an already-cleared mission may be replayed for score/stars, but first-clear XP remains once per defined entitlement. A mission's content version alone does not automatically enable farming the same first-clear payout.

## Daily cap and engagement
Do not force daily logins for essential XP. If repeat-clear XP is introduced, design bounded session-aware caps and rest bonuses separately with published fairness policy; avoid punishing low-session-frequency players. No XP from merely opening the app.

## Reward retry semantics
An API retry with identical idempotency key returns the same ledger receipt. A retry with the same key but a materially different request hash produces a conflict. A second device may concurrently settle the same source; the uniqueness constraint still wins. Never trust a client-submitted `xpAmount`.
