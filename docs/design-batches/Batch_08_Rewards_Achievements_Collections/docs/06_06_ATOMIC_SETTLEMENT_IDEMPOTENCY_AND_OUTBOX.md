# 06 — Atomic Settlement, Receipts and Idempotency

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Ownership boundaries
Batch 8 maintains reward entitlement and award receipt state. Batch 6 owns wallet and coin ledger entries. Batch 7 owns XP/skill grants. Batch 8 inventory owns collectible/cosmetic ownership and uniqueness. The settlement coordinator invokes trusted internal domain commands; browsers never invoke privileged grant functions.

## Single-database baseline
If all domains share PostgreSQL, use one server transaction for claim key reservation, entitlement lock, ownership writes, wallet ledger writes, XP grant source row and outbox event. Package boundaries still remain explicit. If services later split, replace the transaction with an idempotent saga and durable `pending` records; never pretend a distributed operation is atomic.

## Claim fingerprint
Compute a canonical hash from actor, entitlement, action, catalog version and expected reward stage. Reserve `(player_id, client_request_id)` with fingerprint. If already completed, fetch original receipt; if same key with different fingerprint, reject. Canonical source grant uniqueness prevents double credit even if a new client request ID is used.

## Example SQL ordering (conceptual)
`BEGIN; SELECT entitlement FOR UPDATE; INSERT claim_requests ON CONFLICT; CHECK ownership; INSERT unique award lines; INSERT wallet ledger / inventory row / XP source; UPDATE entitlement claimed; INSERT outbox; COMMIT;`

## Partial failure and retries
A failed worker after commit can resend notification but cannot replay the grant because of unique source keys and consumer inbox dedup. Outbox consumer uses `(event_id, consumer_name)` uniqueness. If an inventory write fails before commit, roll back entire claim; show recoverable error. Compensation requires an audited operator adjustment, not deletion of a receipt.

## Finance audit
Reconcile sum of grant receipts with wallet ledger and inventory entitlements; verify claimed entitlements have all promised lines; alarm on orphans, negative wallet values or mismatched claimed quantity. Reconciliation results must be viewable in the admin console without exposing PII broadly.
