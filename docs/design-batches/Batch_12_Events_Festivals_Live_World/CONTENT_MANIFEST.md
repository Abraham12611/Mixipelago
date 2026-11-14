# Batch 12 — Content Manifest

**Source status:** all chapters and catalogs are design candidates, not approved production content.

## Counts
- **chapters:** 27
- **filesExcludingThisManifest:** 41
- **contentBytesExcludingThisManifest:** 134056

## Included files (SHA-256 checksum)
| Path | SHA-256 first 16 chars |
|---|---|
| `ENGINEER_START_HERE.md` | `c7c05c0f2fe7176d` |
| `README.md` | `ca68cf937b65695f` |
| `REFERENCES.md` | `e9ea3d128a4e9a89` |
| `RELEASE_NOTES.md` | `8d43a1f2b14c743d` |
| `docs/00_INDEX_AND_README.md` | `1baa8452648f8361` |
| `docs/01_EVENT_PRODUCT_SCOPE_AND_FAIRNESS_PRINCIPLES.md` | `cf3f60e08e8d7f1a` |
| `docs/02_EVENT_CALENDAR_UTC_WINDOWS_AND_TIME_ZONES.md` | `f354e57964aafd19` |
| `docs/03_EVENT_TYPES_AND_CAPABILITY_MATRIX.md` | `17f4fb57b6011fc6` |
| `docs/04_EVENT_STATE_MACHINE_AND_PUBLICATION_LIFECYCLE.md` | `0402949df12ceb6d` |
| `docs/05_FESTIVAL_WORLDS_AND_COSMETIC_TRANSFORMATIONS.md` | `47512b1a2ff58ed5` |
| `docs/06_FESTIVAL_SERVICE_MISSION_RULES.md` | `f5abe3c9adbcdb41` |
| `docs/07_COMMUNITY_GOALS_AND_AGGREGATE_MILESTONES.md` | `b7b29e95a7471af7` |
| `docs/08_SEASONAL_QUESTS_AND_EVENT_TASK_BOARDS.md` | `79626f24f0045c1b` |
| `docs/09_SEASONAL_COLLECTIBLES_AND_SOUVENIRS.md` | `dea7497f9278db9b` |
| `docs/10_LIMITED_TIME_ECONOMY_AND_REWARD_BUDGETS.md` | `56c4d00bf3973528` |
| `docs/11_WEATHER_DYNAMIC_INCIDENTS_AND_EVENT_COORDINATION.md` | `8f6d77ebbb7ca749` |
| `docs/12_STORY_SCENES_GUESTS_AND_NAMED_EVENT_CHARACTERS.md` | `0c751accae353556` |
| `docs/13_TOURNAMENTS_AND_RANKED_EVENT_BOUNDARIES.md` | `b13ede35bd955c0c` |
| `docs/14_CREWS_FRIENDS_AND_COOPERATIVE_EVENT_SCOPES.md` | `35cae06096fb5791` |
| `docs/15_EVENT_REGISTRATION_ELIGIBILITY_AND_OPT_IN.md` | `de76a6fa6983edff` |
| `docs/16_NOTIFICATION_REMINDER_AND_ATTENTION_POLICY.md` | `2410d6b828e7e065` |
| `docs/17_LIVE_EVENT_HUB_UX_AND_NAVIGATION.md` | `c90f1c7e405b02d0` |
| `docs/18_EVENT_ART_AUDIO_AND_ASSET_STREAMING.md` | `a40bf93b0bd5fcc2` |
| `docs/19_EVENT_CONTENT_STUDIO_AND_EDITORIAL_APPROVAL.md` | `94201b567f09a5c9` |
| `docs/20_SCHEDULING_WORKERS_LEASES_AND_CACHE.md` | `e7f9d85a4bd923da` |
| `docs/21_EVENT_APIS_DOMAIN_MESSAGES_AND_AUTHORIZATION.md` | `b852b9a919c193b9` |
| `docs/22_DATABASE_PRIVACY_AND_IMMUTABLE_EVENT_EDITIONS.md` | `a3a586b7597a6960` |
| `docs/23_SECURITY_FRAUD_AND_LEGAL_COMPLIANCE_OVERVIEW.md` | `1acd5cac9affd667` |
| `docs/24_QA_SCENARIO_ATLAS_AND_SIMULATED_CALENDAR.md` | `71a4ff288a6b5a1b` |
| `docs/25_EVENT_ANALYTICS_AND_LIVE_OPERATIONS_DASHBOARD.md` | `ae6730d197eb5891` |
| `docs/26_RELEASE_SLICES_WORKSTREAMS_AND_ROLLBACK.md` | `ad001ac24659eb05` |
| `docs/27_ADR_REQUIREMENTS_GLOSSARY_AND_SOURCE_LINKS.md` | `c8c122cd1da138f8` |
| `examples/catalog/catalog.draft.json` | `142823ce4d7ab87c` |
| `examples/contracts/api-examples.json` | `9e47e276d028f6ec` |
| `examples/contracts/domain-reference.ts` | `092051e42dcb70a0` |
| `examples/schemas/catalog.schema.json` | `9b3d9c29176a9c5e` |
| `examples/sql/schema_draft.sql` | `d7b83c0f3985a5cf` |
| `examples/tests/README.md` | `738332eaaa502d4c` |
| `examples/tests/invalid-case-mutations.json` | `d1d66325604ce3a3` |
| `examples/tests/pure-rule-vectors.json` | `21951460b0b614d1` |
| `tools/validate_batch12.py` | `b9614e9c8658d70e` |

## Verification
- Run `python tools/validate_batch12.py` from package root.
- ZIP archive integrity, strict example-schema lint, invalid-fixture rejection, pure-rule tests and relative Markdown navigation checks are checked at packaging.
- These checks DO NOT certify browser UI, real physics, service authorization, multiplayer or live operation behavior.
