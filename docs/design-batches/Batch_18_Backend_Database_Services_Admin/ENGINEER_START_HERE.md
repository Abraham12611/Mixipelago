# Engineer kickoff — Batch 18: Backend, Database, Game Services & Admin Studio

## Initial task and team rules

This pack is design-only. It can be used for atomic engineering tickets, not as proof that systems are already deployed. Have each engineer read [the index](docs/00_INDEX_AND_README.md), [the blueprint](docs/90_IMPLEMENTATION_BLUEPRINT.md), [the backlog](docs/91_ENGINEERING_ISSUE_BACKLOG.md) and the relevant detailed chapter before taking a ticket.

**Ownership:** Accounts, server-verified state, database writes, domain API routes, content publishing, admin controls and durable event delivery.

**Dependencies:** Batches 02–04 physics/missions, 05 campaign, 06 ledger, 07 XP, 08 entitlements, 09 guests, 10 world, 11 stories, 12 events, 13 rankings, 14 social and 15 UI.

**Alpha preservation:** Two visible scripted orders; newly merged matching drink auto-serves the oldest eligible order before a further chain reaction. The baseline drink chain is eight tiers, with tier 8 terminal. Alpha coins are local previews and never convertible to trusted currency. v0.1.0 remains a browser-first playable target, not a proven deployment.

## First shippable slice

1. Freeze the typed schema and one pure rule fixture using `examples/catalog/catalog.draft.json` and `tools/validate_batch18.py`.
2. Build Server-owned entitlement and session receipt with test isolation.
3. Integrate Typed API, Postgres migrations, outbox consumers and read projections and implement local preview with explicit unverified labels.
4. Prove duplicate/retry/stale/unauthorized cases and show output without granting trusted rewards by UI.
5. Obtain owner-directed manual UI/art/audio/gameplay signoff before release and deployment. Developers **never self-merge** their PRs; protected `main` and production promotion require owner approval.

**Gate:** `TRUSTED_BACKEND_ENABLED` must start OFF for advanced/unverified features. No fake paid buttons, fabricated score, invented inventory or skipped account authorization.
