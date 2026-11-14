# 37 — QA Matrix, Property Tests and Acceptance

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Pure rules
Verify event counters dedupe IDs, maximum-star progress monotonicity, threshold crossing, once-ever stage uniqueness, album percent by unique item, expired-window behavior, claim fingerprint, reward budget exhaustion and rejected negative quantities.

## Backend and concurrency
- 100 simultaneous claims on one entitlement produce **one** settled grant and 99 original-result replays/conflict-safe responses.
- Two devices with different idempotency keys cannot double-credit the same source.
- Shared PostgreSQL transaction rolling back one item must also roll back its paired wallet credit.
- Two distinct eligible programs produce two separately budgeted rewards without sharing the same source key improperly.
- After outbox retry, consumer applies effect once.
- Player A cannot query or claim player B's receipt/inventory/equipment.
- Stale `expectedRevision` rejects conflicting equip/update.

## UX / accessibility
Responsive reward inbox on Android Chrome and iOS Safari, keyboard navigation on desktop, 200% browser zoom, reduced motion, disabled audio, missing images, offline reconnection, cross-device same-claim status. **All manual UI and play-feel tests are directed to the project owner.** Engineers may run automation and report cases for owner verification.

## Regression against earlier batches
The core eight-tier merge chain, auto-serving oldest order, mission star rules, campaign graph unlocks, wallet/XP authority, preview-only alpha, and normalized ranked scoring must be unchanged. Ensure reward effect event cannot cause a second mission completion or untrusted score grant.

## Release evidence
Require proof of static fixture validation, migration up/down or forward repair rehearsals, Postgres concurrency tests, integration receipts, API access tests, measured economic budget, manual owner signoff and feature gate monitoring. A document-only validation is not a deployed feature certification.
