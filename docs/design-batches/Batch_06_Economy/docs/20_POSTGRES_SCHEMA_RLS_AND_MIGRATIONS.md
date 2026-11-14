# 20 — PostgreSQL Schema, RLS and Migration Strategy

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Architecture
Use Supabase PostgreSQL as durable store with Fastify for trusted mutations. SQL row-level security protects any exposed player projections; direct browser writes to wallets, ledger, upgrades, purchases, reward policy catalog and shop entitlements are denied. Service role secrets stay server-side. Consult `examples/sql/economy_schema_draft.sql` for a deliberately non-production schema sketch.

## Core tables
`economy_catalog_versions`, `reward_policies`, `wallets`, `wallet_ledger`, `economy_commands`, `shops`, `upgrade_catalog`, `owned_shop_upgrades`, `inventory_entitlements`, `shop_equipped_cosmetics`, `purchase_receipts`, `economic_outbox`, `shop_reputation_events`.

## Constraints and indexes
Unique wallet per `(player_id,currency)`, unique source key in ledger per eligible grant, unique `(player_id,request_key)` command, unique `(shop_id,upgrade_id,level)` entitlement, check `balance >= 0`, check positive upgrade prices, foreign keys for ownership and upgrade catalog. Index player transaction feed, active shop and pending outbox events.

## Migration
1. Create draft catalog tables and readonly queries behind a gate.
2. Create wallet/ledger and command journal; seed zero balances only for verified auth identities.
3. Introduce first-clear reward settlement for verified session receipts (do not backfill arbitrary local preview totals).
4. Introduce purchase transaction; enable one upgrade at a time after QA.
5. Backfill a separate client-facing projection from authenticated durable state.

## Rollback and audit
Do not drop ledger on rollback. Disable new commands, retain wallets and ownership, and repair via forward-only migration or compensating entries. Backup and rehearse rollback on staging data.
