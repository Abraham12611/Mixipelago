# 04 — Entitlement State Machine and Recovery

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Canonical state model
`not_eligible → eligible → claimable → claiming → claimed` for manual claims. Automatic policies may pass directly through `eligible → claiming → claimed`. Other terminal outcomes: `expired` only if the published policy says so, `revoked` only for fraud/clear operator cause, and `failed_retryable` as a transient operational status. A failed retry is not an entitlement loss.

## Transition guards
- `eligible`: server facts satisfy published rules; do not equate a client's claim button with eligibility.
- `claimable`: entitlement row recorded with player identity, award scope, item manifest/version, evidence hash and optional expiry.
- `claiming`: claim request idempotency reserved under transaction; multiple devices converge on same receipt.
- `claimed`: every line has a durable corresponding ledger/ownership row; notification is queued once.
- `expired`: time-limited claim with published and displayed expiry; no silent expiration for permanent achievement badges.

## API behavior
`GET /v1/rewards/inbox` returns entitlement states and visible reasons. `POST /v1/rewards/entitlements/{id}/claim` requires `Idempotency-Key`, optional `expectedRevision`, and no caller-defined reward amount. Repeating the same command returns the original receipt. Same key with a different entitlement fingerprint returns `IDEMPOTENCY_CONFLICT`. Do not report success while grants are `pending`.

## Network outage path
After a successful database commit, the response may be lost. The client queries the entitlement or retries with the **same** key; server returns the prior receipt and current entitlement state. If a downstream owner is pending, render 'Claim processing' with a safe retry button or automatic polling and a support trace ID.

## Schema properties
Entitlement uniqueness by `(player_id, program_id, source_scope, source_id, reward_stage)`. Receipt records have immutable source and policy snapshots. Use monotonic timestamps and UTC for expiration; UI localizes their display only.
