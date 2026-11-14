# 16 — Skill Allocation: Eligibility, Validation and Transactions

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Command: allocate one rank
`POST /v1/progression/skills/{skillId}/allocate` consumes exactly one server-owned request ID, desired rank, and optional observed allocation revision. Client never sends the point price, new point balance, skill effect, unlock claim or XP total.

## Transaction algorithm
1. Authenticate player and rate-limit.
2. Acquire the player progression allocation lock (single DB transaction; row lock or conditional revision update).
3. Resolve published catalog and active release gate. Reject if unsupported or build is in a migration-required state.
4. Assert `requestedRank === currentRank+1`, not greater than max; check level/minimum rank prerequisites and eligible mode.
5. Compute cost from catalog, confirm available skill-point balance (`earned - allocated - reserved`); no overdraft.
6. Insert allocation event with unique `(playerId,idempotencyKey)` and immutable policy/source hashes.
7. Update rank projection, available points, allocation revision, cached effect invalidation and outbox event in the same transaction.
8. Return the trusted updated profile and explanation. A replay returns the original receipt.

## Concurrent allocation examples
If a player has one remaining point and two devices concurrently buy different skills, only one succeeds. The loser receives `INSUFFICIENT_POINTS` or `STALE_REVISION`; the UI reloads the profile. Both cannot create valid competing ledger entries.

## Node lock UX
Locked nodes remain inspectable with explicit requirement copy. For example, `Requires Hospitality: Guest Book rank 1; Player Level 5`. Unknown or unreleased nodes should not appear as purchasable. Avoid irreversible confirmations for free point previews; show precise effects before finalizing a trusted allocation.

## Auditability
Allocation events are immutable, although respecs create compensating refunds and new allocation state. Never retroactively change a previous purchase receipt when a skill description or tuning value changes.
