# 03 — Coin Sources, Reward Policies and Earn Rates

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Faucet inventory
The v0.3 baseline permits **verified first-clear mission rewards** and **eligible customer order rewards** from server-validated sessions. Future sources: limited replay rewards, milestones, authored quests, seasonal payouts, crew grants and compensation. Every faucet has an origin, bound, verification type, fraud protections and analytics tag.

## Ordering and audit
1. Player completes a Batch 4 mission using a pinned mission/rules/content version.
2. Session verification produces one authoritative `mission_result_verified` receipt.
3. Reward policy resolver loads a server-approved `reward_policy_id` and computes eligible order and mission awards.
4. Economy settlement inserts a reward key, ledger entry and wallet change in one DB transaction.
5. Outbox records `economy.coins_credited.v1`; client displays receipt.
6. Retry with same key returns the original receipt; no duplicate payout.

## Proposed policy table
| Source | Alpha | v0.3 trust | Safeguard |
|---|---|---|---|
| Customer completion | local preview only | per verified session | dedupe source order IDs, per-run caps |
| Mission first clear | local preview only | once | unique player/mission/policy identity |
| Mission replay | local preview configurable | **0 by default** | bounded daily budget if later enabled |
| Star improvement | preview badge | optional once per threshold | monotonic star state |
| Treasure claim | preview badge | once per authored chest | unique `(player,treasure,season)` |
| Referral / ads | not in baseline | deferred | abuse, policy, and regulatory review |

## Balancing example (not published)
For onboarding levels 1–10, use nominal first-clear rewards of 100–250 coins depending on difficulty, and an affordable first meaningful upgrade by mission 3–5. This is a tunable economic hypothesis; test a zero-mastery player and a skilled player separately. Don't make gold shower VFX proportional to spendable currency if it misleads users.

## Fairness
Never make a mission mathematically unwinnable because the player cannot afford a booster. No hard dependency on ad watches, purchases or friends. Auto-serving older matching orders continues to own drink allocation; economy code consumes the committed order event only.
