# 29 — PostgreSQL Schema, RLS, Indexes and Migration

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Core entities (proposed)
- `reward_catalog_versions` / `reward_policies`: immutable publishing snapshot and policy metadata.
- `achievement_definitions`, `achievement_evidence`, `player_achievement_progress`, `player_achievement_awards`.
- `reward_entitlements`, `reward_claim_commands`, `reward_claim_receipts`, `reward_claim_lines`.
- `collectible_catalog`, `album_editions`, `album_items`, `player_inventory_entitlements`.
- `player_equipped_cosmetics`, `reward_consumer_inbox`, `reward_outbox_events`.

## Uniqueness
One claim stage per player/source/scope, unique claim command `(player_id,client_request_id)`, immutable source-based line `(player_id,source_kind,source_id,policy_id,reward_index)`, unique nonstackable inventory `(player_id,item_id)`, and unique achievement tier `(player_id,achievement_id,definition_epoch,tier_id)`. Use FK ownership and index `player_id,status,created_at` for inbox pages.

## RLS and privileges
Public/authenticated clients may read only their own approved projections; no direct insert/update to grant/receipt/claim status, wallets or source proof. Catalog reads use published view only. Service role remains backend-only. Admin override APIs must require explicit RBAC and audit.

## Migration order
1. Publish read-only catalog tables and draft schema validation.
2. Create player claim/entitlement tables and unique constraints.
3. Integrate verified fact inbox and achievement projections.
4. Connect inventory entitlements and approved claim routing to Batch 6/7.
5. Enable a small set of claims behind cohort gate and monitor reconciliation.

## Rolling back
Use additive schema migrations; do not erase spent coins or legitimately owned cosmetics. Disable grant triggers, keep records, and repair with a forward migration or compensating receipt. Test re-running migrations and restoring snapshots in staging before live release.

## Draft DDL
See `examples/sql/rewards_schema_draft.sql`: illustrative, **not** a production-safe migration; no RLS policies or exhaustive foreign keys are claimed until backend implementation review.
