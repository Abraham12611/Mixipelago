# Engineer kickoff — Batch 17: Music, Sound Effects, Animations & Game Feel

## Initial task and team rules

This pack is design-only. It can be used for atomic engineering tickets, not as proof that systems are already deployed. Have each engineer read [the index](docs/00_INDEX_AND_README.md), [the blueprint](docs/90_IMPLEMENTATION_BLUEPRINT.md), [the backlog](docs/91_ENGINEERING_ISSUE_BACKLOG.md) and the relevant detailed chapter before taking a ticket.

**Ownership:** Sound rendering, audio mixer state, cue selection, optional local haptics; no session scoring or rewards.

**Dependencies:** Batch 02 merges and fixed ticks; Batch 03 drink tier semantics; Batch 04 mission results; Batch 09 customer reactions; Batch 15 controls and reduced-motion settings; Batch 16 visual effects.

**Alpha preservation:** Two visible scripted orders; newly merged matching drink auto-serves the oldest eligible order before a further chain reaction. The baseline drink chain is eight tiers, with tier 8 terminal. Alpha coins are local previews and never convertible to trusted currency. v0.1.0 remains a browser-first playable target, not a proven deployment.

## First shippable slice

1. Freeze the typed schema and one pure rule fixture using `examples/catalog/catalog.draft.json` and `tools/validate_batch17.py`.
2. Build AudioCue catalog and mixer with test isolation.
3. Integrate Event-to-cue router, one AudioContext lifecycle manager and device interruption handlers and implement silence mode and visual-only cues.
4. Prove duplicate/retry/stale/unauthorized cases and show output without granting trusted rewards by UI.
5. Obtain owner-directed manual UI/art/audio/gameplay signoff before release and deployment. Developers **never self-merge** their PRs; protected `main` and production promotion require owner approval.

**Gate:** `AUDIO_PRESENTATION_ENABLED` must start OFF for advanced/unverified features. No fake paid buttons, fabricated score, invented inventory or skipped account authorization.
