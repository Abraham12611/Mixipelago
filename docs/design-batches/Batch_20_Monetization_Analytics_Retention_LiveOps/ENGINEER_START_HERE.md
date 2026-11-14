# Engineer kickoff — Batch 20: Monetization, Analytics, Retention & Live Operations

## Initial task and team rules

This pack is design-only. It can be used for atomic engineering tickets, not as proof that systems are already deployed. Have each engineer read [the index](docs/00_INDEX_AND_README.md), [the blueprint](docs/90_IMPLEMENTATION_BLUEPRINT.md), [the backlog](docs/91_ENGINEERING_ISSUE_BACKLOG.md) and the relevant detailed chapter before taking a ticket.

**Ownership:** Optional monetization policy, financial reporting, privacy-approved analytics, product experiments, retention measurement and operational rollouts.

**Dependencies:** Batch 06 coins and upgrades; Batch 07 progression; Batch 08 items and seasonal rewards; Batch 12 events; Batch 13 rankings; Batch 18 backend; Batch 19 security; Batch 21 platform stores.

**Alpha preservation:** Two visible scripted orders; newly merged matching drink auto-serves the oldest eligible order before a further chain reaction. The baseline drink chain is eight tiers, with tier 8 terminal. Alpha coins are local previews and never convertible to trusted currency. v0.1.0 remains a browser-first playable target, not a proven deployment.

## First shippable slice

1. Freeze the typed schema and one pure rule fixture using `examples/catalog/catalog.draft.json` and `tools/validate_batch20.py`.
2. Build Versioned SKU/analytics catalog with test isolation.
3. Integrate Verified receipts, disclosed storefront, consented telemetry and experiment safety and implement commerce-disabled safe mode; existing ownership retained.
4. Prove duplicate/retry/stale/unauthorized cases and show output without granting trusted rewards by UI.
5. Obtain owner-directed manual UI/art/audio/gameplay signoff before release and deployment. Developers **never self-merge** their PRs; protected `main` and production promotion require owner approval.

**Gate:** `COMMERCE_ENABLED` must start OFF for advanced/unverified features. No fake paid buttons, fabricated score, invented inventory or skipped account authorization.
