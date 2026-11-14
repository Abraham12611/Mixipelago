# 05 — Trusted Ledger, Transaction Semantics and Idempotency

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Authoritative write algorithm
The backend receives a command such as `purchase_upgrade(shopId, upgradeId, requestId)`; it authenticates the player, resolves the authoritative catalog version and price, verifies shop ownership, prerequisite, stock, feature gate and remaining balance, then atomically debits wallet, records ledger entry, grants ownership and appends an outbox event.

Pseudo-SQL order: begin → reserve idempotency key → lock wallet row (`SELECT ... FOR UPDATE`) → validate current catalog and owned upgrades → insert purchase receipt → update wallet with `balance >= price` condition → append negative ledger line → upsert ownership → outbox → commit. Two duplicate commands return the same purchase receipt. Concurrency tests must prove last-coin races cannot double-spend.

## Durable records
- `wallets`: balance, revision, immutable owner and currency.
- `wallet_ledger`: each immutable change, signed delta, before/after snapshots for diagnosis, source receipt, actor/reason, catalog/rules version and created time.
- `economy_commands`: request id, fingerprint, status and original result; same id with different body is a conflict.
- `purchases`: shop/upgrade, resolved cost, content version, transaction references.
- `outbox_events`: transactions to publish at least once to downstream projections.

## Idempotency and race invariants
Unique `(player_id, currency, source_kind, source_id)` for credit grants; unique `(player_id, idempotency_key)` for commands. `Idempotency-Key` must be an opaque client-generated UUID for retry, scoped to authenticated actor. Replay receipts are read-only. A gateway timeout after commit must recover the committed result.

## Reconciliation
Hourly/daily job compares wallet materialized balances to ledger rollups; alert on discrepancy, negative balances or orphaned purchases. Rebuild projections from ledger if necessary. Never delete historical entries to hide errors. PII-free financial aggregates can be retained longer than raw telemetry.
