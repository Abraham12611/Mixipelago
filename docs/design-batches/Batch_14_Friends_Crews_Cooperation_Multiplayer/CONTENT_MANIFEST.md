# Batch 14 — Content Manifest

**Source status:** all chapters and catalogs are design candidates, not approved production content.

## Counts
- **chapters:** 29
- **filesExcludingThisManifest:** 43
- **contentBytesExcludingThisManifest:** 142971

## Included files (SHA-256 checksum)
| Path | SHA-256 first 16 chars |
|---|---|
| `ENGINEER_START_HERE.md` | `b530653263335279` |
| `README.md` | `7125464123ffa807` |
| `REFERENCES.md` | `1bb0dae9937b4bc4` |
| `RELEASE_NOTES.md` | `86bfc92988f5ec2a` |
| `docs/00_INDEX_AND_README.md` | `c29cbfd604d8d5da` |
| `docs/01_SOCIAL_PROMISE_AND_FEATURE_SEQUENCING.md` | `2e4fd613c95e643f` |
| `docs/02_IDENTITY_VISIBILITY_AND_DEFAULT_PRIVACY.md` | `ea9909f9550c7435` |
| `docs/03_FRIEND_REQUEST_LIFECYCLE_AND_UNIQUENESS.md` | `9c01f49f129db74d` |
| `docs/04_INVITATIONS_SHARE_LINKS_AND_REFERRAL_SAFETY.md` | `ee5779f34f8a4539` |
| `docs/05_BLOCKING_REPORTING_AND_SAFETY_CENTER.md` | `e19519bdeddc42b1` |
| `docs/06_ASYNCHRONOUS_CHALLENGES_AND_GHOST_RUNS.md` | `50c6157a66c1b15c` |
| `docs/07_GHOST_VISUALIZATION_AND_INPUT_PRIVACY.md` | `f5c4f562bf8bd53b` |
| `docs/08_FRIEND_LEADERBOARDS_AND_FILTERED_RANKING.md` | `d617e17b0054524a` |
| `docs/09_CREW_CREATION_NAMING_AND_MEMBERSHIP.md` | `8c54511d16d1d0b8` |
| `docs/10_CREW_ROLES_PERMISSIONS_AND_GOVERNANCE.md` | `f375cec24bdb70ad` |
| `docs/11_CREW_PROJECTS_AND_COOPERATIVE_MILESTONES.md` | `4a2f03df886239be` |
| `docs/12_CONTRIBUTION_CAPS_MEMBERSHIP_CHANGES_AND_REWARDS.md` | `1745ec25a86e74b7` |
| `docs/13_COOPERATIVE_ISLAND_BUILDING_LATER.md` | `d120a21e181fbfc8` |
| `docs/14_GIFTS_AND_GENEROSITY_SAFEGUARDS.md` | `10598dd4df3d65d3` |
| `docs/15_SOCIAL_NOTIFICATION_INBOX_AND_CONSENT.md` | `29155eaf5bedd804` |
| `docs/16_SOCIAL_UI_APP_MAP_AND_RESPONSIVE_LAYOUT.md` | `f7d631aa9b695d2c` |
| `docs/17_REAL_TIME_MULTIPLAYER_DESIGN_BOUNDARY.md` | `7f9014d405e5cad6` |
| `docs/18_MATCHMAKING_LATENCY_AND_REGION_POLICY.md` | `e080819ed94b9399` |
| `docs/19_REAL_TIME_SESSION_LIFECYCLE_AND_PAUSE_SEMANTICS.md` | `28717e0ac844ff20` |
| `docs/20_TRANSPORT_SNAPSHOT_AND_RECONCILIATION.md` | `6c8e02a39709ef6f` |
| `docs/21_SPECTATORS_REPLAYS_AND_SHARED_HIGHLIGHTS.md` | `663a59e3ab954256` |
| `docs/22_MODERATION_CONDUCT_AND_TEAM_SAFETY.md` | `a7c42d10d347ab1c` |
| `docs/23_SOCIAL_AUTH_API_RLS_AND_AUDIT.md` | `98a7546880bb7f1e` |
| `docs/24_SOCIAL_DATA_MODEL_AND_EVENT_CONTRACTS.md` | `1261ed336dc9c3e9` |
| `docs/25_SECURITY_SPAM_ABUSE_AND_CHEATING_MODEL.md` | `968a5f8265650ea5` |
| `docs/26_QA_AND_LOAD_TESTING_SCENARIOS.md` | `bd2aa7df424a02f2` |
| `docs/27_ANALYTICS_AND_PRIVACY_PRESERVING_HEALTH_METRICS.md` | `900d8ed5c20d782b` |
| `docs/28_PHASED_RELEASES_WORKSTREAMS_AND_GATES.md` | `637b133b14b01b90` |
| `docs/29_ARCHITECTURE_DECISIONS_AND_TRACEABILITY.md` | `dd04e32e71ae473e` |
| `examples/catalog/catalog.draft.json` | `453172ec443b2925` |
| `examples/contracts/api-examples.json` | `20819f9d42d44d85` |
| `examples/contracts/domain-reference.ts` | `ed45a46de3d70134` |
| `examples/schemas/catalog.schema.json` | `0f44ed2d314ac002` |
| `examples/sql/schema_draft.sql` | `34d01c5441b58f50` |
| `examples/tests/README.md` | `a558139a9534bedb` |
| `examples/tests/invalid-case-mutations.json` | `f9e11347912a8b40` |
| `examples/tests/pure-rule-vectors.json` | `e3927898f9811c76` |
| `tools/validate_batch14.py` | `8c83ca03f01d79d7` |

## Verification
- Run `python tools/validate_batch14.py` from package root.
- ZIP archive integrity, strict example-schema lint, invalid-fixture rejection, pure-rule tests and relative Markdown navigation checks are checked at packaging.
- These checks DO NOT certify browser UI, real physics, service authorization, multiplayer or live operation behavior.
