# Batch 10 — Content Manifest

**Source status:** all chapters and catalogs are design candidates, not approved production content.

## Counts
- **chapters:** 29
- **filesExcludingThisManifest:** 43
- **contentBytesExcludingThisManifest:** 145939

## Included files (SHA-256 checksum)
| Path | SHA-256 first 16 chars |
|---|---|
| `ENGINEER_START_HERE.md` | `dd54ae8312ad2b05` |
| `README.md` | `ed31fb363f68cc90` |
| `REFERENCES.md` | `ea800be2737327f4` |
| `RELEASE_NOTES.md` | `9ab12d503b59a0ec` |
| `docs/00_INDEX_AND_README.md` | `5dde3c623df855de` |
| `docs/01_PRODUCT_PROMISE_SCOPE_AND_BOUNDARIES.md` | `70e33aa7e955ba0c` |
| `docs/02_WORLD_TIME_CLOCKS_SCHEDULES_AND_FREEZE_POINTS.md` | `34cd319d94c75cc2` |
| `docs/03_ISLAND_BIOMES_AND_GEOGRAPHIC_CONDITIONS.md` | `d6d66ed856e71c31` |
| `docs/04_WEATHER_STATE_FORECAST_AND_TRANSITIONS.md` | `d7e7059cf9c63f43` |
| `docs/05_TOURISM_CROWDS_AND_VISITOR_DEMAND.md` | `1888761be5e33150` |
| `docs/06_SUPPLY_CONDITIONS_AND_PRICE_SIGNALS.md` | `5d9303426547db54` |
| `docs/07_INCIDENT_CLASSIFICATION_AND_SEVERITY.md` | `131b99e4fab9dc36` |
| `docs/08_INCIDENT_FINITE_STATE_MACHINE.md` | `1f0f8c0b8f0c4d12` |
| `docs/09_EVENT_DIRECTOR_ELIGIBILITY_AND_COOLDOWN.md` | `dd05dc832950f5a4` |
| `docs/10_PROBABILITY_SEED_CAPS_AND_FAIRNESS.md` | `48655b111d8d1c44` |
| `docs/11_SHOP_FIRE_AND_EMERGENCY_SCENARIO.md` | `35c26363611ebf62` |
| `docs/12_REPAIR_RESILIENCE_AND_RECOVERY_FLOWS.md` | `6159732da322c177` |
| `docs/13_INSURANCE_LIABILITY_AND_FINANCIAL_AUTHORITY.md` | `6b4777aa43e92f54` |
| `docs/14_POSITIVE_WORLD_OPPORTUNITIES.md` | `534940623d046e39` |
| `docs/15_DYNAMIC_CHALLENGE_AND_RESCUE_MISSIONS.md` | `108100883be3a2b9` |
| `docs/16_CROSS_SYSTEM_WORLD_HANDOFFS.md` | `345911f486209118` |
| `docs/17_OFFLINE_MISSED_WINDOWS_AND_ANTI_PUNISHMENT.md` | `03f2862a9ac6214d` |
| `docs/18_WORLD_MAP_HUD_AND_INCIDENT_CHOICE_UX.md` | `2d9b44d31a4a74fd` |
| `docs/19_WORLD_ART_SOUND_AND_ANIMATION_BUDGETS.md` | `815c0c473c22bc57` |
| `docs/20_INCIDENT_CONTENT_AUTHORING_AND_MODERATION.md` | `7a61d5ce7e1ac4fc` |
| `docs/21_VERSIONING_SNAPSHOTS_AND_ROLLBACK.md` | `c18e328e609d1cef` |
| `docs/22_API_EVENTS_AND_AUTHORIZATION.md` | `5f9517122de929bc` |
| `docs/23_PERSISTENCE_RLS_AND_AUDIT_RECORDS.md` | `2006c3869bee19f7` |
| `docs/24_SCHEDULED_WORKERS_CACHING_AND_RESILIENCE.md` | `733449578f0ebdfe` |
| `docs/25_SECURITY_ABUSE_AND_FAIRNESS_REVIEW.md` | `a46332d6d41cd88e` |
| `docs/26_QA_MATRIX_AND_SIMULATION_FIXTURES.md` | `b9270e0ed14bcde3` |
| `docs/27_ANALYTICS_BALANCE_AND_OPERATIONS.md` | `0f123ff921ef4a65` |
| `docs/28_RELEASE_SLICES_TICKETS_AND_SIGN_OFF.md` | `e95f2ad41a3f80ae` |
| `docs/29_TRACEABILITY_DEFINITIONS_AND_DECISIONS.md` | `c347038fd0251f20` |
| `examples/catalog/catalog.draft.json` | `e5206133c82c619d` |
| `examples/contracts/api-examples.json` | `905163859084fc55` |
| `examples/contracts/domain-reference.ts` | `60ae8af95b0187f3` |
| `examples/schemas/catalog.schema.json` | `db3f9dc90b46507f` |
| `examples/sql/schema_draft.sql` | `272ab71062ee69fb` |
| `examples/tests/README.md` | `7ee736420756e5a2` |
| `examples/tests/invalid-case-mutations.json` | `4b6afb8ee6a0a733` |
| `examples/tests/pure-rule-vectors.json` | `d272013287c5c121` |
| `tools/validate_batch10.py` | `1938f87ad153d3dd` |

## Verification
- Run `python tools/validate_batch10.py` from package root.
- ZIP archive integrity, strict example-schema lint, invalid-fixture rejection, pure-rule tests and relative Markdown navigation checks are checked at packaging.
- These checks DO NOT certify browser UI, real physics, service authorization, multiplayer or live operation behavior.
