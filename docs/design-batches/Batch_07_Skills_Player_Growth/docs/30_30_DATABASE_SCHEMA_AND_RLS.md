# 30 — PostgreSQL Tables, RLS and Trusted Persistence

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Proposed tables
`player_progression(player_id PK, xp_total BIGINT, player_level INT, earned_points INT, allocated_points INT, revision BIGINT, xp_policy_version TEXT, updated_at)`; `xp_grants(id, player_id, source_type, source_id, policy_version, amount, idempotency_key, request_hash, created_at)`; `level_milestones(player_id, level, points_granted, created_at)`; `skill_allocations(player_id, skill_id, rank, catalog_version, revision, updated_at)`; `skill_allocation_events(id, player_id, skill_id, previous_rank, new_rank, points_delta, request_id, catalog_version, occurred_at)`; `skill_respec_operations(id, player_id, old_revision, new_revision, refunded_points, request_id)`; `player_loadouts(player_id, mode_family, slots JSONB, revision)`.

## Constraints
- Strong positive/negative check constraints; level ≥1; `0 <= allocated_points <= earned_points`; one allocation per `(player, skill)`.
- Unique XP entitlement `(player_id, source_type, source_id, policy_version)`; but a policy version bump must not itself convert one first-clear into repeat payout.
- Unique `(player_id, level)` milestone; unique per-player request IDs; foreign keys to authenticated player identity and published catalog catalog references.
- Double write protection with serializable transaction or row locks. **All dependent reward grants occur transactionally**; events publish via outbox after commit.

## RLS and authorization
Players may SELECT only their progression, grants, and visible allocations; public profile view has sanitized projection. No direct client INSERT/UPDATE/DELETE into wallet/XPs/skills tables. Backend transaction functions run with minimum necessary privileges and verify caller identity + ownership.

## Account migration
Guest-to-account upgrade must reattach ownership safely with unique receipt IDs and no duplicate grants. Older `previewCoins` or local `previewXp` are never imported as trusted value. On account merge, conflicting progression requires explicit authoritative reconciliation rather than summing two arbitrary local states.

## Indexes
Index XP grants by `(player_id, created_at DESC)` and allocations by player; unique idempotency keys. A background migration backfills projections from trusted sources only. The included SQL file is **illustrative DDL**, not a production-reviewed migration.
