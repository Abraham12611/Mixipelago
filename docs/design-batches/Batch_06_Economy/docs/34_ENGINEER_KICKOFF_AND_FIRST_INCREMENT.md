# 34 — Engineer Kickoff and First Trusted Increment

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Immediate read order
Batch 1 economy overview → Batch 3 reward semantics → Batch 4 result verification → Batch 5 campaign claims → Batch 6 docs 01,02,03,05,06,07,17,20,21,26,27,28.

## First engineering sequence
1. Review existing repository and accept shared typed contracts, preserving gameplay semantics.
2. Build pure reward-policy and upgrade price resolvers with test vectors.
3. Implement gated DB wallet/ledger/idempotency tables plus RLS and reconciliation tests.
4. Wire verified first-clear receipt to credit settlement, gate OFF by default.
5. Add one starter shop, one working utility upgrade and one cosmetic; implement transactional purchase.
6. Build accessible responsive shop UI, pending/success/error state and clear benefits.
7. Conduct automated concurrent/replay/offline tests and stage owner-led manual UI testing.
8. Review, merge to development branch, promote only with owner approval and verified release checklist.

## Non-goals for first increment
No passive income, salaries, loans, random destructive incidents, unbounded VIP bonuses, idle farming, premium currency, auction, cross-player markets or real-money trading. Avoid building fake UI screens with nonfunctional purchase confirmations.

## Engineer PR rules
Every PR includes changed contracts, feature flags, migrations, tests, screenshots/recorded output where applicable, telemetry plan, fallback and evidence. Individual engineers must not merge their own PRs.
