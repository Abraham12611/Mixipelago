# Engineer kickoff — Batch 19: Security, Anti-Cheat & Game Integrity

## Initial task and team rules

This pack is design-only. It can be used for atomic engineering tickets, not as proof that systems are already deployed. Have each engineer read [the index](docs/00_INDEX_AND_README.md), [the blueprint](docs/90_IMPLEMENTATION_BLUEPRINT.md), [the backlog](docs/91_ENGINEERING_ISSUE_BACKLOG.md) and the relevant detailed chapter before taking a ticket.

**Ownership:** Cross-service threat models, verification controls, misuse prevention, authorization testing, incident response and audit policy.

**Dependencies:** All Batches 01–18, especially 02 deterministic Rapier, 04 score proofs, 06 wallet, 08 rewards, 13 ranks, 14 social, 18 backend, 20 payments and 21 native bridge.

**Alpha preservation:** Two visible scripted orders; newly merged matching drink auto-serves the oldest eligible order before a further chain reaction. The baseline drink chain is eight tiers, with tier 8 terminal. Alpha coins are local previews and never convertible to trusted currency. v0.1.0 remains a browser-first playable target, not a proven deployment.

## First shippable slice

1. Freeze the typed schema and one pure rule fixture using `examples/catalog/catalog.draft.json` and `tools/validate_batch19.py`.
2. Build Threat register and negative contract fixtures with test isolation.
3. Integrate Auth/RLS matrices, replay verifier, ledger uniqueness and staged security gates and implement read-only fallback and conservative reject.
4. Prove duplicate/retry/stale/unauthorized cases and show output without granting trusted rewards by UI.
5. Obtain owner-directed manual UI/art/audio/gameplay signoff before release and deployment. Developers **never self-merge** their PRs; protected `main` and production promotion require owner approval.

**Gate:** `CERTIFIED_SESSION_VERIFICATION_ENABLED` must start OFF for advanced/unverified features. No fake paid buttons, fabricated score, invented inventory or skipped account authorization.
