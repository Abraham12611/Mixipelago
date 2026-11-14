# 39 — Incremental Releases, Feature Flags and Rollback Plans

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Release contract
Features are implemented and **tested** before being enabled. A batch of documentation is not a release. Proposed sequence must not delay the 3-day-to-1-week playable-alpha target.

| Release | Candidate slice | Dependencies | Gate |
|---|---|---|---|
| `v0.1.0` | Two scripted order avatars, reaction states and deterministic auto-service | Batches 2–4 | alpha only; no trusted reputation |
| `v0.1.1–0.1.2` | Portrait polish, sound, small-screen orders and accessibility | asset QA | owner UI signoff |
| `v0.3.x` | Existing Batch 6 wallet/shop reputation *foundation* | trusted service and auth | no new customer trust claims yet |
| `v0.4.2` | Published customer catalog + verified service observations + read-only shop reputation | verified mission receipts, Batch 6 | `CUSTOMER_REPUTATION_ENABLED` |
| `v0.4.3` | One recurring named guest, loyalty journal and milestone | Batch 8 entitlements, RLS | `CUSTOMER_RELATIONSHIPS_ENABLED` |
| `v0.5.x+` | Authored optional VIP challenge/pool, critic demo | mission proof, rewards and integrity | `CUSTOMER_VIP_ENABLED` |
| Later | Group orders, weather influence, character quests, festivals | Batches 10–12 | separate isolated gates |

## Feature flags (default OFF)
`CUSTOMER_DYNAMIC_POOLS_ENABLED`, `CUSTOMER_SATISFACTION_ENABLED`, `CUSTOMER_REPUTATION_ENABLED`, `CUSTOMER_RELATIONSHIPS_ENABLED`, `CUSTOMER_VIP_ENABLED`, `CUSTOMER_PATIENCE_ENABLED`, `CUSTOMER_GROUP_ORDERS_ENABLED`, `CUSTOMER_JOURNAL_ENABLED`.

## Rollback
Disable new encounter reservation and new trust settlement; preserve previously verified observations and entitlements. If customer catalog is faulty, pin the previous good version for new reservations. Don't rewrite the historic run's score or wallet. Cosmetic guest rendering can fall back locally without requiring a new server migration.

## Definition of done
Architecture, positive/negative tests, schema validation, idempotency/load tests, performance evidence and owner-directed manual UI QA are prerequisites to each gate. No promises of actual deployment in this documentation pack.
