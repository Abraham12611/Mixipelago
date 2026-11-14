# Batch 11 — Content Manifest

**Source status:** all chapters and catalogs are design candidates, not approved production content.

## Counts
- **chapters:** 28
- **filesExcludingThisManifest:** 42
- **contentBytesExcludingThisManifest:** 139987

## Included files (SHA-256 checksum)
| Path | SHA-256 first 16 chars |
|---|---|
| `ENGINEER_START_HERE.md` | `c78afbefba3e0882` |
| `README.md` | `6bf565d32c98b9a0` |
| `REFERENCES.md` | `2403749cb317949e` |
| `RELEASE_NOTES.md` | `9ad138573366eb3d` |
| `docs/00_INDEX_AND_README.md` | `bafcb5125720a54d` |
| `docs/01_NARRATIVE_DIRECTION_AND_OPTIONAL_STORY_PROMISE.md` | `7fc5873f8c1ff455` |
| `docs/02_NARRATIVE_WORLD_BIBLE_AND_CANON_HIERARCHY.md` | `3ae43056995742c8` |
| `docs/03_STORY_ACTS_EPISODES_AND_CAMPAIGN_BEATS.md` | `9d96dcb675b4d6ac` |
| `docs/04_CHARACTER_REGISTRY_AND_PERSISTENT_ROLES.md` | `b952e8d4fad2032f` |
| `docs/05_QUEST_TAXONOMY_AND_PROGRESSION_OBJECTIVES.md` | `7f7f4a8a346c98d4` |
| `docs/06_QUEST_DSL_AND_PREREQUISITES.md` | `3229b46a5e876582` |
| `docs/07_DIALOGUE_GRAPH_AND_CONVERSATIONAL_UI.md` | `e82bc20f860931ab` |
| `docs/08_CHOICES_CONSEQUENCES_AND_REVERSIBILITY.md` | `be3bcef61a5c68f4` |
| `docs/09_RELATIONSHIP_AND_AFFINITY_FLAGS.md` | `e11a75d39e2a3a40` |
| `docs/10_RECURRING_RIVAL_OWNERS_AND_BUSINESSES.md` | `6af4d131b21c9db8` |
| `docs/11_RIVAL_CHALLENGE_SYSTEM_AND_SCORING_FAIRNESS.md` | `c4daeb3f1f243e08` |
| `docs/12_NPC_SCHEDULE_PRESENCE_AND_RETURN_APPEARANCES.md` | `3c6db9d3fa2a514d` |
| `docs/13_QUESTS_LINKED_TO_MISSIONS_SHOPS_AND_ISLANDS.md` | `415b9f667b276983` |
| `docs/14_NARRATIVE_REWARD_POLICY_AND_INTEGRITY.md` | `8b0fef863ae11801` |
| `docs/15_STORY_HISTORY_CHRONICLE_AND_RECAP.md` | `ee7a5ed5f0826d7c` |
| `docs/16_BRANCHING_RECONVERGENCE_AND_SAVE_MIGRATION.md` | `c4674909b60f96a7` |
| `docs/17_NARRATIVE_WORLD_AND_DYNAMIC_INCIDENTS.md` | `0183aa668b8a181a` |
| `docs/18_FESTIVAL_STORYTELLING_AND_CALENDAR_COORDINATION.md` | `001dc45ef308f05d` |
| `docs/19_NARRATIVE_UI_TRANSITIONS_AND_ACCESSIBILITY.md` | `3806e69f143e039f` |
| `docs/20_CHARACTER_ART_VOICE_AND_LOCALIZATION_PIPELINE.md` | `fb49a4e0c45f40dd` |
| `docs/21_CONTENT_STUDIO_FOR_STORY_AND_QUEST_AUTHORS.md` | `aa41d99fbc0f36f4` |
| `docs/22_STORY_DOMAIN_API_EVENTS_AND_TYPESCRIPT.md` | `e898061428e82e70` |
| `docs/23_STORY_SCHEMA_RLS_RETENTION_AND_MIGRATIONS.md` | `23d408ae6033c49f` |
| `docs/24_SECURITY_CONTENT_MODERATION_AND_ABUSE.md` | `c2abcd608ef55e0b` |
| `docs/25_QA_STORYLINE_CONSISTENCY_AND_REPLAY.md` | `0db8a2ba780892a8` |
| `docs/26_NARRATIVE_ANALYTICS_AND_AUTHOR_FEEDBACK.md` | `47e8a4dd954d1b69` |
| `docs/27_RELEASE_SLICES_DEPENDENCIES_AND_PARALLEL_TICKETS.md` | `47a4f76960daa779` |
| `docs/28_ADR_TRACEABILITY_GLOSSARY_AND_OWNER_DECISIONS.md` | `e4c0d8c6d9b7ae45` |
| `examples/catalog/catalog.draft.json` | `0711a528c1e19a99` |
| `examples/contracts/api-examples.json` | `44e7e8bd297a96f7` |
| `examples/contracts/domain-reference.ts` | `40315bddf6d8050f` |
| `examples/schemas/catalog.schema.json` | `8a414c0ade15eed8` |
| `examples/sql/schema_draft.sql` | `c4a4fac43f6a45eb` |
| `examples/tests/README.md` | `15dfa94387b05f5e` |
| `examples/tests/invalid-case-mutations.json` | `b4f3661f209d63fb` |
| `examples/tests/pure-rule-vectors.json` | `db855b5a78b1cf87` |
| `tools/validate_batch11.py` | `8a0a59147ff706ca` |

## Verification
- Run `python tools/validate_batch11.py` from package root.
- ZIP archive integrity, strict example-schema lint, invalid-fixture rejection, pure-rule tests and relative Markdown navigation checks are checked at packaging.
- These checks DO NOT certify browser UI, real physics, service authorization, multiplayer or live operation behavior.
