# Batch 16 — Art Direction, Characters & 2.5D Asset Production

**Status:** Detailed engineering design pack; not an implemented/deployed feature. **Prepared:** 2026-11-14.
**Owner:** Visual / Art Pipeline. **Candidate release:** v0.1.x foundational, extended with island/shop releases. **Advanced gate:** `ART_PIPELINE_ENABLED` default OFF.

## Critical earlier rules
Two visible scripted orders; newly merged matching drink auto-serves the oldest eligible order before a further chain reaction. The baseline drink chain is eight tiers, with tier 8 terminal. Alpha coins are local previews and never convertible to trusted currency. v0.1.0 remains a browser-first playable target, not a proven deployment.

## Source-of-truth responsibilities
Visual content, export configurations, asset provenance and art presentation; never gameplay physics or ownership.
Batch 15 responsive UI and token system; Batch 02 collider/body config; Batch 03 drink IDs; Batch 05 island graphs; Batch 08 collectible metadata; Batch 09 fictional customer IDs.

## Specification chapters
- [01 — Product vision, visual goals and first-ship boundaries](./01_PRODUCT_VISION_VISUAL_GOALS_AND_FIRST_SHIP_BOUNDARIES.md)
- [02 — Visual grammar, shapes, silhouettes and material families](./02_VISUAL_GRAMMAR_SHAPES_SILHOUETTES_AND_MATERIAL_FAMILIES.md)
- [03 — Palette, lighting, reflections and tropical atmosphere](./03_PALETTE_LIGHTING_REFLECTIONS_AND_TROPICAL_ATMOSPHERE.md)
- [04 — Camera, perspective, anchors and world scaling](./04_CAMERA_PERSPECTIVE_ANCHORS_AND_WORLD_SCALING.md)
- [05 — Eight-tier alpha drink artwork bible](./05_EIGHT_TIER_ALPHA_DRINK_ARTWORK_BIBLE.md)
- [06 — Drink glass geometry, liquid and garnish rules](./06_DRINK_GLASS_GEOMETRY_LIQUID_AND_GARNISH_RULES.md)
- [07 — Future recipe variants, rarity skins and themed drinks](./07_FUTURE_RECIPE_VARIANTS_RARITY_SKINS_AND_THEMED_DRINKS.md)
- [08 — Customer portraits, body proportions and expressive faces](./08_CUSTOMER_PORTRAITS_BODY_PROPORTIONS_AND_EXPRESSIVE_FACES.md)
- [09 — NPC animation pose library and lip-sync exclusions](./09_NPC_ANIMATION_POSE_LIBRARY_AND_LIP_SYNC_EXCLUSIONS.md)
- [10 — Island atlas and map landmark art](./10_ISLAND_ATLAS_AND_MAP_LANDMARK_ART.md)
- [11 — Buildings, kiosks, bars and shop upgrade visuals](./11_BUILDINGS_KIOSKS_BARS_AND_SHOP_UPGRADE_VISUALS.md)
- [12 — Furniture, props, hazards and interactive affordances](./12_FURNITURE_PROPS_HAZARDS_AND_INTERACTIVE_AFFORDANCES.md)
- [13 — Backgrounds, compositing and layered parallax](./13_BACKGROUNDS_COMPOSITING_AND_LAYERED_PARALLAX.md)
- [14 — UI art production and Batch 15 token mapping](./14_UI_ART_PRODUCTION_AND_BATCH_15_TOKEN_MAPPING.md)
- [15 — Badges, rarity framing and collection illustration](./15_BADGES_RARITY_FRAMING_AND_COLLECTION_ILLUSTRATION.md)
- [16 — Weather, seasons and environment visual states](./16_WEATHER_SEASONS_AND_ENVIRONMENT_VISUAL_STATES.md)
- [17 — Animation states and frame budgets](./17_ANIMATION_STATES_AND_FRAME_BUDGETS.md)
- [18 — Merge, glint, liquid slosh and particle FX](./18_MERGE_GLINT_LIQUID_SLOSH_AND_PARTICLE_FX.md)
- [19 — Blender master scenes and 3D source hygiene](./19_BLENDER_MASTER_SCENES_AND_3D_SOURCE_HYGIENE.md)
- [20 — AI-assisted concept generation and human review](./20_AI_ASSISTED_CONCEPT_GENERATION_AND_HUMAN_REVIEW.md)
- [21 — Licensing, attribution, releases and provenance ledger](./21_LICENSING_ATTRIBUTION_RELEASES_AND_PROVENANCE_LEDGER.md)
- [22 — Asset IDs, versioning, hashing and dependency graph](./22_ASSET_IDS_VERSIONING_HASHING_AND_DEPENDENCY_GRAPH.md)
- [23 — Sprite formats, atlases, compression and texture RAM](./23_SPRITE_FORMATS_ATLASES_COMPRESSION_AND_TEXTURE_RAM.md)
- [24 — Scale variants, DPR, safe areas and responsive output](./24_SCALE_VARIANTS_DPR_SAFE_AREAS_AND_RESPONSIVE_OUTPUT.md)
- [25 — Phaser loaders, texture lifetimes and fallback visuals](./25_PHASER_LOADERS_TEXTURE_LIFETIMES_AND_FALLBACK_VISUALS.md)
- [26 — Accessibility, color-blind modes and visual comfort](./26_ACCESSIBILITY_COLOR_BLIND_MODES_AND_VISUAL_COMFORT.md)
- [27 — Asset QA, golden captures and quality signoff](./27_ASSET_QA_GOLDEN_CAPTURES_AND_QUALITY_SIGNOFF.md)
- [28 — Automated asset pipeline and CI gates](./28_AUTOMATED_ASSET_PIPELINE_AND_CI_GATES.md)
- [29 — Content Studio visual review and publication](./29_CONTENT_STUDIO_VISUAL_REVIEW_AND_PUBLICATION.md)
- [30 — Engineering workstreams and release slices](./30_ENGINEERING_WORKSTREAMS_AND_RELEASE_SLICES.md)
- [31 — Decisions, risks, source references and traceability](./31_DECISIONS_RISKS_SOURCE_REFERENCES_AND_TRACEABILITY.md)

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
- `../tools/validate_batch16.py` — Python validator using `jsonschema` for full schema checks.

## Start implementation
1. Read the first six chapters and the implementation blueprint.
2. Pin content and rules versions, prove fixtures and agree on event boundaries.
3. Build a small feature-gated integration slice with accessible fallback.
4. Run negative authorization and replay tests, then owner-directed visual/audio/gameplay acceptance.
5. No engineer self-merges; owner approval required for main/production promotion.

**Next batch/dependency:** 17 — Sound, music and game feel.
