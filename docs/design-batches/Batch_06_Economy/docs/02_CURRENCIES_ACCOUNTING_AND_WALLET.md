# 02 — Currencies, Wallets and Accounting Units

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Currency taxonomy
`COINS` is the first spendable **soft currency**. A `previewCoins` number in local alpha save is a distinct diagnostic value, not a `COINS` wallet balance. `XP`, `stars`, `score`, `reputation`, `mastery` and optional future `gems` are not synonyms or convertible by default. Avoid adding premium currency until monetization is designed.

| Unit | Produced by | Consumed by | Authority |
|---|---|---|---|
| Score | deterministic gameplay events | ranking comparison only | versioned session result |
| Stars | threshold result from eligible mission | graph unlock checks | verified mission record |
| Preview coins | alpha order & mission summaries | nothing trusted | browser-only save |
| COINS | verified reward policies, bounded quests | shop purchases and selected service fees | server wallet ledger |
| XP | eligible mission progress | level calculation, not spending | server progression |
| Shop reputation | customer/service outcomes | unlock thresholds | shop projection |
| Future premium unit | separate legal/commerce design | clearly labeled non-ranked purchases | server payment/entitlement |

## Wallet rules
One wallet per `(player_id,currency)` in v0.3. All delta amounts are integer *minor units*; avoid floating point money math. A nonnegative balance must be maintained under concurrent writes. Clients only receive `balance`, `revision`, `updatedAt`, and limited transaction history. An admin correction always creates a compensating ledger entry with reason and actor id.

## Reward states
`PENDING_VALIDATION` → `ELIGIBLE` → `GRANTED`, or `REJECTED` with a stable code. An animation must wait for trusted settlement before announcing persistent receipt; an optimistic preview can say **Pending verification**.

## Invariant examples
A mission first-clear grant unique key is `first-clear:{player}:{mission}:{rewardPolicyVersion}` with a documented migration strategy. Replay payouts, if introduced, use different keys scoped to verified run and daily cap. Never convert the player's local preview coins into trusted funds after login.
