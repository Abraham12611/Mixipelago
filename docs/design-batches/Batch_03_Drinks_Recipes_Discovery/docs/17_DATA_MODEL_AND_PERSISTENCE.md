# 17 — Data Model: Drink Content, Unlocks, Mastery and Player Collections

## Content storage policy

v0.1.x stores an eight-tier catalog as versioned JSON in repository with a content hash; no production database is required just to render these eight definitions. Published server phase stores immutable catalog/recipe versions and generated manifests. PostgreSQL records are authoritative only for player-owned unlocks, trusted scores and inventory.

## Canonical logical entities

| Entity | Fields (suggested) | Constraints |
|---|---|---|
| `drink_catalog_versions` | id, version, hash, schema_version, published_at, status | immutable after publish |
| `drink_definitions` | catalog_version_id, drink_id, family_id, tier, next_drink_id, score, locale_keys, metadata | unique `(catalog_version_id,drink_id)` |
| `drink_asset_mappings` | catalog_version_id, drink_id, role, asset_id, variant | referenced asset manifest must exist |
| `recipes` | recipe_id, recipe_version, output_drink_id, context, priority, mode | unique immutable version |
| `recipe_inputs` | recipe_id, input_drink_id/ingredient_id, quantity | exact multiset; positive counts |
| `ingredients` | ingredient_id, type, localized_key, manifest | immutable ID, non-negative weights |
| `recipe_discoveries` | player_id, discovery_id, source, evidence_id, discovered_at | unique `(player_id,discovery_id)` |
| `collection_progress` | player_id, collection_id, entry_id, source_run_id, awarded_at | unique grant evidence |
| `drink_mastery_events` | event_id, player_id, run_id, drink_id, activity, delta_xp, validated_at | idempotent source event |
| `drink_mastery_summaries` | player_id, drink_id, xp, level, best_chain | aggregate recalculable |
| `ingredient_inventory` | player_id, ingredient_id, quantity, version | nonnegative quantity |
| `ingredient_ledger` | id, player_id, ingredient_id, delta, reason, idempotency_key | immutable audit trail |

Don't create all these tables for v0.1; a future integration migration will create only required tables when trusted features ship. Use `jsonb` for appropriate content metadata, but keep ownership, unique keys and financial constraints relational.

## Local alpha save

Compatible with Batch 1 `mixipelago:save:v1`: tutorial completion, unlocked mission IDs, best score and preview coins. Optional `highestTierSeen` is **local only**, explicitly nontrusted; must validate tier within known alpha catalog. Do not add permanent owned skin/recipe state to this save as though it were backend-authoritative.

## RLS and API boundaries

Read-only published catalog may be public. Player unlocks and inventory require authenticated ownership policies. A player must not issue direct table writes that mint inventory, mastery or collection grants; use trusted server commands/RPCs with validation. Public profile queries expose only opted-in cosmetic showcase and aggregate public stats, never email, precise location or unpublished recipe clues.

## Migrations

IDs persist across revisions. A drink rename changes only localization. Asset update changes mapping version. A recipe rule change changes published recipe and rules version, so old replays use pinned definitions. Retirement marks spawn eligibility false in newer catalogs; prior verified ownership remains. Moving an entry between collections needs explicit set-version migration and reward dedupe. Player inventory adjustments use compensating ledger entries, not destructive editing of past transactions.

## Indexes and concurrency

Indexes on `(player_id,drink_id)`, `(player_id,collection_id)`, `source_run_id`, and idempotency keys. For unlock processing, transaction inserts an event with unique ID, then updates aggregates under safe conflict handling. Concurrent request duplicates must result in one grant. Replay evidence retention has explicit policy independent from personal account deletion requests.

## Data validation

Use shared Zod schemas in API for content and command validation; database CHECKs for nonnegative quantities and valid status, and foreign keys for owned items. JSON schema can lint authoring fixtures. A catalog publish transaction should fail when an active mission references a deleted/unpublished drink ID.
