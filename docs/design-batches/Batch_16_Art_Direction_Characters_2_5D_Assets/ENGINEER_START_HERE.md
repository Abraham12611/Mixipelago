# Engineer kickoff — Batch 16: Art Direction, Characters & 2.5D Asset Production

## Initial task and team rules

This pack is design-only. It can be used for atomic engineering tickets, not as proof that systems are already deployed. Have each engineer read [the index](docs/00_INDEX_AND_README.md), [the blueprint](docs/90_IMPLEMENTATION_BLUEPRINT.md), [the backlog](docs/91_ENGINEERING_ISSUE_BACKLOG.md) and the relevant detailed chapter before taking a ticket.

**Ownership:** Visual content, export configurations, asset provenance and art presentation; never gameplay physics or ownership.

**Dependencies:** Batch 15 responsive UI and token system; Batch 02 collider/body config; Batch 03 drink IDs; Batch 05 island graphs; Batch 08 collectible metadata; Batch 09 fictional customer IDs.

**Alpha preservation:** Two visible scripted orders; newly merged matching drink auto-serves the oldest eligible order before a further chain reaction. The baseline drink chain is eight tiers, with tier 8 terminal. Alpha coins are local previews and never convertible to trusted currency. v0.1.0 remains a browser-first playable target, not a proven deployment.

## First shippable slice

1. Freeze the typed schema and one pure rule fixture using `examples/catalog/catalog.draft.json` and `tools/validate_batch16.py`.
2. Build Asset ID and provenance registry with test isolation.
3. Integrate Manifest validator, Blender render preset, atlas export checks and lazy Phaser loader and implement low memory texture atlas fallback, missing-art labeled cards.
4. Prove duplicate/retry/stale/unauthorized cases and show output without granting trusted rewards by UI.
5. Obtain owner-directed manual UI/art/audio/gameplay signoff before release and deployment. Developers **never self-merge** their PRs; protected `main` and production promotion require owner approval.

**Gate:** `ART_PIPELINE_ENABLED` must start OFF for advanced/unverified features. No fake paid buttons, fabricated score, invented inventory or skipped account authorization.
