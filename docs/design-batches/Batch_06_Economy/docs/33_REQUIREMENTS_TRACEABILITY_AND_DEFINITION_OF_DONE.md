# 33 — Requirement Traceability and Definition of Done

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Traceability
| ID | Requirement | Evidence |
|---|---|---|
| ECON-001 | Earn only from verified sources | receipt tests + DB query |
| ECON-002 | Same grant cannot duplicate | concurrency fixture |
| ECON-003 | Purchases atomic | transaction integration suite |
| ECON-004 | Client cannot set price | tamper tests |
| ECON-005 | Negative balances impossible | DB constraint/property suite |
| ECON-006 | Shop upgrade effect is true and explained | modifier unit test + owner UI acceptance |
| ECON-007 | Cosmetic purchase changes art only | renderer snapshot + stat check |
| ECON-008 | Ranked standardized | competitive mode fixture |
| ECON-009 | Zero-coins player can progress | simulated journey |
| ECON-010 | Safe rollback/reconciliation | staging drill logs |
| ECON-011 | Prior batches unchanged | cross-batch regression |
| ECON-012 | Accessibility and localization | automated checks + owner review |

## Release acceptance
Production wallet & purchases cannot be enabled with a broken reconciliation job, failing concurrency suite, missing security tests, unapproved UI, or inconsistent ledger balance. At least one functional shop upgrade must have an actually working effect and explanation; no dummy paid buttons. Art assets must be properly licensed and associated with correct shop slots.

## Documentation-only validation
Example JSON/SQL and formulas can be linted in this pack. That is not equivalent to executed PostgreSQL migrations, load tests, user-play testing, or deployment verification. Engineering work must supply runtime evidence separately.
