# Batch 17 — Music, Sound Effects, Animations & Game Feel

**Status:** Detailed engineering design pack; not an implemented/deployed feature. **Prepared:** 2026-11-14.
**Owner:** Audio / Game Feel. **Candidate release:** v0.1.x foundational audio, dynamic mix after gameplay proof. **Advanced gate:** `AUDIO_PRESENTATION_ENABLED` default OFF.

## Critical earlier rules
Two visible scripted orders; newly merged matching drink auto-serves the oldest eligible order before a further chain reaction. The baseline drink chain is eight tiers, with tier 8 terminal. Alpha coins are local previews and never convertible to trusted currency. v0.1.0 remains a browser-first playable target, not a proven deployment.

## Source-of-truth responsibilities
Sound rendering, audio mixer state, cue selection, optional local haptics; no session scoring or rewards.
Batch 02 merges and fixed ticks; Batch 03 drink tier semantics; Batch 04 mission results; Batch 09 customer reactions; Batch 15 controls and reduced-motion settings; Batch 16 visual effects.

## Specification chapters
- [01 — Audio vision and player promise](./01_AUDIO_VISION_AND_PLAYER_PROMISE.md)
- [02 — Sound category taxonomy and naming](./02_SOUND_CATEGORY_TAXONOMY_AND_NAMING.md)
- [03 — Original composition direction and island leitmotifs](./03_ORIGINAL_COMPOSITION_DIRECTION_AND_ISLAND_LEITMOTIFS.md)
- [04 — Launch, aim and gesture feedback](./04_LAUNCH_AIM_AND_GESTURE_FEEDBACK.md)
- [05 — Glass contact material response](./05_GLASS_CONTACT_MATERIAL_RESPONSE.md)
- [06 — Merge tiers, chain arcs and anticipation](./06_MERGE_TIERS_CHAIN_ARCS_AND_ANTICIPATION.md)
- [07 — Serving, customers, failure and celebration](./07_SERVING_CUSTOMERS_FAILURE_AND_CELEBRATION.md)
- [08 — UI navigation, toggles and notifications](./08_UI_NAVIGATION_TOGGLES_AND_NOTIFICATIONS.md)
- [09 — Ambient island soundscapes](./09_AMBIENT_ISLAND_SOUNDSCAPES.md)
- [10 — Dynamic soundtrack layers and musical states](./10_DYNAMIC_SOUNDTRACK_LAYERS_AND_MUSICAL_STATES.md)
- [11 — Music loops, stems, tempo and edit points](./11_MUSIC_LOOPS_STEMS_TEMPO_AND_EDIT_POINTS.md)
- [12 — Original SFX authoring and synthesis](./12_ORIGINAL_SFX_AUTHORING_AND_SYNTHESIS.md)
- [13 — Audio format matrix and download budgets](./13_AUDIO_FORMAT_MATRIX_AND_DOWNLOAD_BUDGETS.md)
- [14 — Mixer buses, volumes and ducking](./14_MIXER_BUSES_VOLUMES_AND_DUCKING.md)
- [15 — Collision rate limiting and audio voice budget](./15_COLLISION_RATE_LIMITING_AND_AUDIO_VOICE_BUDGET.md)
- [16 — Spatial audio and board position mapping](./16_SPATIAL_AUDIO_AND_BOARD_POSITION_MAPPING.md)
- [17 — Web Audio initialization and autoplay policies](./17_WEB_AUDIO_INITIALIZATION_AND_AUTOPLAY_POLICIES.md)
- [18 — Phaser and React audio ownership](./18_PHASER_AND_REACT_AUDIO_OWNERSHIP.md)
- [19 — Audio lifecycle, focus, pause, interruption and background](./19_AUDIO_LIFECYCLE_FOCUS_PAUSE_INTERRUPTION_AND_BACKGROUND.md)
- [20 — Audio preferences and accessibility](./20_AUDIO_PREFERENCES_AND_ACCESSIBILITY.md)
- [21 — Voice, character utterances and localization boundaries](./21_VOICE_CHARACTER_UTTERANCES_AND_LOCALIZATION_BOUNDARIES.md)
- [22 — Haptics and multisensory feedback contract](./22_HAPTICS_AND_MULTISENSORY_FEEDBACK_CONTRACT.md)
- [23 — Audio event schema and priority routing](./23_AUDIO_EVENT_SCHEMA_AND_PRIORITY_ROUTING.md)
- [24 — Adaptive quality and low-end fallback](./24_ADAPTIVE_QUALITY_AND_LOW_END_FALLBACK.md)
- [25 — Recording, mastering and loudness QA](./25_RECORDING_MASTERING_AND_LOUDNESS_QA.md)
- [26 — Music and sound licensing/provenance](./26_MUSIC_AND_SOUND_LICENSING_PROVENANCE.md)
- [27 — Audio Content Studio and review publishing](./27_AUDIO_CONTENT_STUDIO_AND_REVIEW_PUBLISHING.md)
- [28 — Telemetry, tuning and sensory health](./28_TELEMETRY_TUNING_AND_SENSORY_HEALTH.md)
- [29 — Audio QA matrix and device verification](./29_AUDIO_QA_MATRIX_AND_DEVICE_VERIFICATION.md)
- [30 — Workstreams, alpha deliverables and release gates](./30_WORKSTREAMS_ALPHA_DELIVERABLES_AND_RELEASE_GATES.md)
- [31 — Risks, decisions, event matrix and glossary](./31_RISKS_DECISIONS_EVENT_MATRIX_AND_GLOSSARY.md)

## Implementation and governance
- [90 — Engineering Implementation Blueprint](./90_IMPLEMENTATION_BLUEPRINT.md)
- [91 — Atomic Engineering Issue Backlog](./91_ENGINEERING_ISSUE_BACKLOG.md)
- [92 — QA and Golden Fixtures](./92_QA_GOLDEN_FIXTURES.md)
- [93 — Release Gates and Rollback](./93_RELEASE_GATES_AND_ROLLBACK.md)
- [94 — ADRs and Traceability](./94_ADRS_AND_TRACEABILITY.md)
- [95 — Official Sources and Precedence](./95_OFFICIAL_SOURCES.md)

## Machine-readable materials
- `../examples/catalog/catalog.draft.json` — candidate domain catalog; nothing enabled or production-approved.
- `../examples/schemas/catalog.schema.json` — example JSON schema.
- `../examples/tests/pure-rule-vectors.json` — expected pure behavior.
- `../examples/tests/invalid-case-mutations.json` — intentionally invalid catalog mutations.
- `../examples/contracts/reference.ts` — TypeScript reference functions.
- `../examples/contracts/api-examples.json` — sample event/HTTP envelopes.
- `../examples/sql/schema_draft.sql` — illustrative, not a deployable migration.
- `../tools/validate_batch17.py` — Python validator using `jsonschema` for full schema checks.

## Start implementation
1. Read the first six chapters and the implementation blueprint.
2. Pin content and rules versions, prove fixtures and agree on event boundaries.
3. Build a small feature-gated integration slice with accessible fallback.
4. Run negative authorization and replay tests, then owner-directed visual/audio/gameplay acceptance.
5. No engineer self-merges; owner approval required for main/production promotion.

**Next batch/dependency:** 18 — Backend and content tooling.
