# 44 — Engineer Kickoff, Build Order and Contract Freeze

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Required reading
Batch 4 reward handoff → Batch 5 treasure handoff → Batch 6 ledger/idempotency → Batch 7 XP authority → Batch 8 chapters 02–08, 17, 29–31, 37–39. The pack is design/specification only; **nothing here asserts that a game or backend is currently deployed**.

## Contract-first sequence
1. Agree on canonical source receipt identity, policy version, entitlement key and exact owner of wallet/XP/inventory tables.
2. Implement catalog + schema validator and pure achievement DSL with golden fixtures.
3. Add authenticated event inbox, projections and entitlement state machine.
4. Wire one nonspendable cosmetic badge to one verified first-clear event, including exactly-once claim and inventory ownership.
5. Expose read-only reward inbox and a minimal claim UI on desktop/mobile.
6. Prove duplicate/retry/race cases in PostgreSQL and authorization/RLS tests.
7. Add a single collection with 3–5 real collectible sources and an album completion reward.
8. Ship behind server feature gates and owner manual acceptance; expand rewards only after monitoring.

## Implementation invariants
Alpha preview coin balances are untrusted and cannot convert to wallet assets. XP from verified first clears is Batch 7's responsibility. Rank prizes are deferred until Batch 13 verified snapshots. No client `unlock_achievement` command. All monetary and durable item grants require source proof, a frozen award policy, and idempotent settlement.

## Engineers and approval
Code owners enforce PR boundaries and test evidence. Engineers do not merge their own PRs. Core gameplay/visual manual tests go through the product owner. New releases preserve existing data and include a rollback plan.

## Definition of first good demo
A player wins a real verified mission, receives a legitimate nonmonetary badge entitlement, claims it once, sees it in inventory, equips it, and can reload or switch devices without duplication. If the backend validation is not ready, the user-facing demo must be clearly marked preview-only and must not pretend it is the trusted feature.
