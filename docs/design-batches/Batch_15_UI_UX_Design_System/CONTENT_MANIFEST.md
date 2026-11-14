# Batch 15 — Content Manifest

**Source status:** all chapters and catalogs are design candidates, not approved production content.

## Counts
- **chapters:** 30
- **filesExcludingThisManifest:** 44
- **contentBytesExcludingThisManifest:** 150417

## Included files (SHA-256 checksum)
| Path | SHA-256 first 16 chars |
|---|---|
| `ENGINEER_START_HERE.md` | `d002a8262af437cf` |
| `README.md` | `f055a1ab95b2eee3` |
| `REFERENCES.md` | `86780df1d23d954f` |
| `RELEASE_NOTES.md` | `8aedcd3fed09a52a` |
| `docs/00_INDEX_AND_README.md` | `800cb6c0757baa7b` |
| `docs/01_EXPERIENCE_PRINCIPLES_AND_NON_GOALS.md` | `308ecc93403c0d7e` |
| `docs/02_INFORMATION_ARCHITECTURE_AND_NAVIGATION_MAP.md` | `517c80503595f8a7` |
| `docs/03_DESIGN_TOKENS_AND_SEMANTIC_COLOR.md` | `20cb3c2acba852f3` |
| `docs/04_TYPOGRAPHY_DENSITY_AND_HIERARCHY.md` | `d69eb4cd2c77860c` |
| `docs/05_LAYOUT_GRID_BREAKPOINTS_AND_SAFE_AREAS.md` | `c1c042941b2e6301` |
| `docs/06_GAMESHELL_REACT_AND_PHASER_BOUNDARY.md` | `31e4d5b0af273caf` |
| `docs/07_TITLE_SCREEN_AND_FIRST_LAUNCH.md` | `3b5eeba2ad83eda2` |
| `docs/08_GAMEPLAY_HUD_AND_BOARD_FRAMING.md` | `9b411984229cdfdd` |
| `docs/09_ORDER_CARDS_QUEUE_AND_SERVING_FEEDBACK.md` | `caef2b581b99996a` |
| `docs/10_AIMING_GESTURES_AND_POINTER_AFFORDANCES.md` | `149d380cd75840f2` |
| `docs/11_GAMEPLAY_OVERLAYS_PAUSE_AND_RESULTS.md` | `a39c92110903f826` |
| `docs/12_MAP_ISLANDS_AND_MISSION_SELECTION.md` | `ecb72bf65687b231` |
| `docs/13_SHOP_HUB_UPGRADES_AND_ECONOMY_TRUST.md` | `76c68e24cc4e56f7` |
| `docs/14_SKILLS_AND_PLAYER_GROWTH_INTERFACES.md` | `db9135471f4ead53` |
| `docs/15_REWARDS_ALBUMS_AND_COSMETIC_INVENTORY.md` | `880037a3d4bdd237` |
| `docs/16_CUSTOMERS_PORTRAITS_AND_SHOP_REPUTATION.md` | `e4c33d57e8bede38` |
| `docs/17_WORLD_CONDITIONS_STORY_AND_EVENT_SCREENS.md` | `20f512322538d616` |
| `docs/18_LEADERBOARDS_RANKINGS_AND_COMPETITION_UX.md` | `4b71baef628b481a` |
| `docs/19_FRIENDS_CREWS_AND_SOCIAL_SAFETY_UX.md` | `1fa9e9a1e04eddf1` |
| `docs/20_SETTINGS_HELP_AND_ACCESSIBILITY_HUB.md` | `b8d4174213d554f1` |
| `docs/21_COMPONENT_LIBRARY_AND_INTERACTION_VARIANTS.md` | `4ccba0b25aba5f02` |
| `docs/22_MOTION_TRANSITIONS_GAME_FEEL_AND_FEEDBACK.md` | `08506438b5054628` |
| `docs/23_ART_HANDOFF_AND_2_5D_PRODUCTION_GRAMMAR.md` | `7b50d22423965ea8` |
| `docs/24_LOCALIZATION_TEXT_OVERFLOW_AND_CULTURE.md` | `beffe23c9e3de0e1` |
| `docs/25_ACCESSIBILITY_WCAG_AND_MOTOR_CONTROL.md` | `c7634644a4f79cd8` |
| `docs/26_LOADING_ERRORS_OFFLINE_AND_RECONNECT_STATES.md` | `554122cbdd19fafa` |
| `docs/27_FRONTEND_ARCHITECTURE_DESIGN_TOKENS_AND_QA_HARNESS.md` | `a2f3b4e95d16b3c7` |
| `docs/28_DESIGN_SYSTEM_GOVERNANCE_AND_COLLABORATION.md` | `e641e239fdc03e82` |
| `docs/29_RELEASE_SLICES_AND_IMPLEMENTATION_BACKLOG.md` | `aab2baf08f9d5d17` |
| `docs/30_REQUIREMENT_TRACEABILITY_ADR_AND_GLOSSARY.md` | `86bbd1ea3738240c` |
| `examples/catalog/catalog.draft.json` | `ffde90b01a05fb4b` |
| `examples/contracts/api-examples.json` | `3203f0d7f70c93fb` |
| `examples/contracts/domain-reference.ts` | `ff913b4e491f5ddf` |
| `examples/schemas/catalog.schema.json` | `d9ef648074a0cdaa` |
| `examples/sql/schema_draft.sql` | `43b781b97372fd75` |
| `examples/tests/README.md` | `4049458115de08ad` |
| `examples/tests/invalid-case-mutations.json` | `381be28c85228405` |
| `examples/tests/pure-rule-vectors.json` | `9a71287767f9c1ad` |
| `tools/validate_batch15.py` | `f3d530ce0d4709cc` |

## Verification
- Run `python tools/validate_batch15.py` from package root.
- ZIP archive integrity, strict example-schema lint, invalid-fixture rejection, pure-rule tests and relative Markdown navigation checks are checked at packaging.
- These checks DO NOT certify browser UI, real physics, service authorization, multiplayer or live operation behavior.
