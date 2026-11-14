# Engineer kickoff — Batch 21: Native Mobile, Performance, Scaling & Release Engineering

## Initial task and team rules

This pack is design-only. It can be used for atomic engineering tickets, not as proof that systems are already deployed. Have each engineer read [the index](docs/00_INDEX_AND_README.md), [the blueprint](docs/90_IMPLEMENTATION_BLUEPRINT.md), [the backlog](docs/91_ENGINEERING_ISSUE_BACKLOG.md) and the relevant detailed chapter before taking a ticket.

**Ownership:** iOS/Android packaging, device-specific behavior, CI/CD, store submission, performance optimization and version compatibility.

**Dependencies:** Batch 01 Next.js/Phaser/Rapier; Batch 15 UI; Batch 16 assets; Batch 17 audio; Batch 18 backend; Batch 19 security; Batch 20 digital goods and privacy.

**Alpha preservation:** Two visible scripted orders; newly merged matching drink auto-serves the oldest eligible order before a further chain reaction. The baseline drink chain is eight tiers, with tier 8 terminal. Alpha coins are local previews and never convertible to trusted currency. v0.1.0 remains a browser-first playable target, not a proven deployment.

## First shippable slice

1. Freeze the typed schema and one pure rule fixture using `examples/catalog/catalog.draft.json` and `tools/validate_batch21.py`.
2. Build Platform capability adapter and release manifest with test isolation.
3. Integrate Capacitor app shell, build matrix, deep-link safety and store artifacts and implement web fallback, silent/offline training, native unsupported banner.
4. Prove duplicate/retry/stale/unauthorized cases and show output without granting trusted rewards by UI.
5. Obtain owner-directed manual UI/art/audio/gameplay signoff before release and deployment. Developers **never self-merge** their PRs; protected `main` and production promotion require owner approval.

**Gate:** `NATIVE_APP_RELEASE_ENABLED` must start OFF for advanced/unverified features. No fake paid buttons, fabricated score, invented inventory or skipped account authorization.
