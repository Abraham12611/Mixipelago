# 36 — Terminology, Source References and Technical Links

## Glossary
**Archipelago:** network of thematic playable islands. **Island:** content and art boundary with entry anchor. **District/Chapter:** pacing unit inside an island. **Route:** visible path between nodes. **Node:** selectable marker, not necessarily a physics mission. **Mission:** versioned Batch 4 simulation definition. **Graph:** immutable manifest of nodes, edges and unlocks. **Prerequisite:** predicate that grants eligibility; distinct from visual path. **Fog/Discovery:** visibility condition; distinct from eligibility. **Projection:** derived player-specific view of graph. **Gateway:** authored transition between islands. **Checkpoint:** chapter progress indicator. **Receipt:** trusted record of a completed server action. **Local preview:** untrusted device-only alpha save. **Content hash:** digest of immutable gameplay/graph data. **Active pointer:** published graph version selected for new sessions. **Golden replay:** recorded input sequence proven to win under pinned physics/content rules.

## Internal source documents consulted
- Batch 1 `docs/09_PROGRESSION_OVERVIEW.md`, `11_WORLDS_AND_EVENTS_OVERVIEW.md`, `16_RELEASE_ROADMAP.md`.
- Batch 2 `docs/07_MERGE_ARBITRATION_AND_CHAIN_REACTIONS.md`, `17_REPLAY_DETERMINISM_AND_TRUST.md`.
- Batch 3 `docs/03_ALPHA_EIGHT_TIER_DRINK_BIBLE.md`, `20_VERSIONING_MIGRATIONS_AND_COMPATIBILITY.md`.
- Batch 4 `docs/15_MISSION_SCHEMA_AND_VERSIONING.md`, `22_REWARDS_PROGRESS_AND_ECONOMY_HANDOFF.md`, `26_CONTENT_STUDIO_LEVEL_EDITOR.md`, `34_RELEASE_PHASES_AND_GATES.md`, `35_ADRS_AND_INTEGRATION_DECISIONS.md`.

## External technical references (reviewed 2026-11-14)
- Phaser documentation: https://docs.phaser.io/ (scene/camera, display objects, input and tilemap runtime; test exact Phaser release APIs).
- Tiled editor official documentation: https://doc.mapeditor.org/en/stable/manual/export-generic/ (JSON export can be used as an optional art-layout source; it does not replace custom campaign graph schema).
- Tiled JSON specification: https://github.com/mapeditor/tiled/blob/master/docs/reference/json-map-format.rst
- Supabase Row Level Security: https://supabase.com/docs/guides/database/postgres/row-level-security (separate grants and policies; keep secrets server-side).
- Rapier docs: https://rapier.rs/docs/user_guides/javascript/getting_started_js/ (used for gameplay physics, not map navigation).
- MDN Pointer Events: https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events (touch/mouse pointer abstractions).
- MDN Page Visibility: https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API (suspend/resume behavior).

## Source and approximation policy
External docs explain platform capabilities, not Mixipelago-specific rules. Examples in this batch are engineering proposals, not proof of shipped code, licensed art, playable mission design, finished map visuals or production economy. Freeze exact dependencies after an engine prototype validates them.
