# Batch 13 — Content Manifest

**Source status:** all chapters and catalogs are design candidates, not approved production content.

## Counts
- **chapters:** 29
- **filesExcludingThisManifest:** 43
- **contentBytesExcludingThisManifest:** 142619

## Included files (SHA-256 checksum)
| Path | SHA-256 first 16 chars |
|---|---|
| `ENGINEER_START_HERE.md` | `e9a62f2a69db86fc` |
| `README.md` | `c651332c37002ada` |
| `REFERENCES.md` | `1161c0bdfbc7a28d` |
| `RELEASE_NOTES.md` | `a6da7f9e3a05638d` |
| `docs/00_INDEX_AND_README.md` | `fb1fc01a14865848` |
| `docs/01_COMPETITIVE_PRODUCT_SCOPE_AND_CATEGORY_DEFINITIONS.md` | `0f7ff5298abee181` |
| `docs/02_OFFICIAL_SCORE_AUTHORITY_AND_TRUST_STATES.md` | `7588a4c92c9298b9` |
| `docs/03_NORMALIZED_COMPETITION_PROFILE.md` | `32aa31aa9fea6c71` |
| `docs/04_RANK_METRICS_COMPARATOR_AND_TIE_BREAK.md` | `e095c0a5914a4606` |
| `docs/05_LEADERBOARD_SCOPE_AND_QUERY_MODEL.md` | `1933386c9ffd5276` |
| `docs/06_WEEKLY_SEASONS_AND_IMMUTABLE_EDITIONS.md` | `cfefe54c9b570379` |
| `docs/07_VERIFICATION_ENGINE_AND_REPLAY_PROOF.md` | `ef3ea5ccd136d916` |
| `docs/08_SCORE_SUBMISSION_QUEUE_AND_DUPLICATE_HANDLING.md` | `22965e933a6d9247` |
| `docs/09_BEST_ATTEMPT_AND_ENTRY_POLICY.md` | `0eff3ee0f27d0690` |
| `docs/10_BRACKET_TOURNAMENTS_AND_MATCHMAKING_LATER.md` | `9c52c5e56c77063d` |
| `docs/11_LEAGUES_DIVISIONS_AND_PROMOTION_RELEGATION.md` | `d9de8f657a5e51b9` |
| `docs/12_SEASON_PRIZE_POLICY_AND_COSMETIC_REWARDS.md` | `a563b2a9475a2c06` |
| `docs/13_LEADERBOARD_CACHING_AND_STORAGE_STRATEGY.md` | `92db2f0e91a4b2b4` |
| `docs/14_PAGINATION_RANK_WINDOWS_AND_PERFORMANCE.md` | `f4c468e55ea5d374` |
| `docs/15_REGIONS_PRIVACY_AND_SOCIAL_VISIBILITY.md` | `0391cca08a3e21d9` |
| `docs/16_COMPETITIVE_IDENTITY_AND_DISPLAY_NAME_MODERATION.md` | `55d8a4f12a946bcd` |
| `docs/17_CROSS_PLATFORM_AND_OFFLINE_RANKING_BEHAVIOR.md` | `32f52c3f2b4d482d` |
| `docs/18_COMPETITION_PAGE_AND_HUD_UX.md` | `c3d0119f67aa087a` |
| `docs/19_MATCH_REVIEW_AND_ANTI_CHEAT_APPEAL.md` | `24679ac64c40c034` |
| `docs/20_COMPETITIVE_FRAUD_MODEL_AND_LIMITS.md` | `bafc473131a4c93d` |
| `docs/21_MODERATION_DISPUTES_AND_TOURNAMENT_INTEGRITY.md` | `fc7b442dcd2ae433` |
| `docs/22_COMPETITION_CONTENT_AUTHORING_AND_PUBLICATION.md` | `c2fca140787c1aac` |
| `docs/23_LEADERBOARD_APIS_AND_DOMAIN_EVENT_CONTRACTS.md` | `d1b780f02bd975e0` |
| `docs/24_DATABASE_RLS_SCORE_EVENTS_AND_RETENTION.md` | `5fce62026458b7b6` |
| `docs/25_DISTRIBUTED_VERIFICATION_WORKERS_AND_RELIABILITY.md` | `562635671da2c5b9` |
| `docs/26_QA_GOLDEN_REPLAYS_AND_STRESS_TESTS.md` | `a79a188ad384b807` |
| `docs/27_TELEMETRY_UPTIME_AND_KILL_SWITCHES.md` | `9c67ad771b08b674` |
| `docs/28_RELEASE_PLAN_ISSUE_BACKLOG_AND_SIGN_OFF.md` | `a65e9f200dacb459` |
| `docs/29_ADR_REQUIREMENT_TRACEABILITY_AND_GLOSSARY.md` | `754ce688af3f6ee1` |
| `examples/catalog/catalog.draft.json` | `ce5e2f4959c1ac8f` |
| `examples/contracts/api-examples.json` | `35b7a469f36c72bb` |
| `examples/contracts/domain-reference.ts` | `a4090e2e928883bd` |
| `examples/schemas/catalog.schema.json` | `4818d9e031011730` |
| `examples/sql/schema_draft.sql` | `243e03b8bbbfeb1e` |
| `examples/tests/README.md` | `f11c05b6e2825981` |
| `examples/tests/invalid-case-mutations.json` | `ca17eddee6e1178b` |
| `examples/tests/pure-rule-vectors.json` | `459be23522420160` |
| `tools/validate_batch13.py` | `54b8357f6df75951` |

## Verification
- Run `python tools/validate_batch13.py` from package root.
- ZIP archive integrity, strict example-schema lint, invalid-fixture rejection, pure-rule tests and relative Markdown navigation checks are checked at packaging.
- These checks DO NOT certify browser UI, real physics, service authorization, multiplayer or live operation behavior.
