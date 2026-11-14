# 28 — References, Glossary and Readiness Notes

## Earlier canonical project docs

- Batch 1 `05_DRINKS_CUSTOMERS_SCORING.md` — initial tier chain, customer order rules and scoring.
- Batch 1 `26_CONTENT_AND_CONFIG_EXAMPLES.md` — original catalog and first mission examples.
- Batch 1 `07_DATA_MODEL.md` — preview local data vs trusted wallet.
- Batch 2 `07_MERGE_ARBITRATION_AND_CHAIN_REACTIONS.md` — authoritative contact resolution algorithm.
- Batch 2 `08_SPAWN_NEXT_QUEUE_AND_GAME_DIRECTOR.md` — deterministic launch queue.
- Batch 2 `11_TYPES_COMMANDS_AND_EVENT_CONTRACTS.md` — current event envelopes and simulation types.
- Batch 2 `16_DIFFICULTY_AND_GAMEPLAY_BALANCING.md` — level skill/pressure metrics.
- Batch 2 `29_BATCH1_INTEGRATION_NOTES.md` — explicitly preserved rules across batches.

## External technical references (verified source links)

- Phaser 4 guide: https://phaser.io/oss/docs/ (rendering/scenes/loaders/animation)
- Rapier JavaScript colliders: https://rapier.rs/docs/user_guides/javascript/colliders/ (solid and sensor colliders, friction, event flags)
- Rapier collision events: https://rapier.rs/docs/user_guides/javascript/advanced_collision_detection_js/ (started/stopped contact event semantics)
- Rapier rigid bodies: https://rapier.rs/docs/user_guides/javascript/rigid_bodies/
- Supabase documentation: https://supabase.com/docs (PostgreSQL, auth, authorization)
- Zod documentation: https://zod.dev/ (runtime validation; verify exact version APIs when coding)
- JSON Schema: https://json-schema.org/ (authoring-time schemas)

These docs are technical references, not sources for our game design decisions. Confirm installed package versions during implementation.

## Glossary

| Term | Precise Mixipelago meaning |
|---|---|
| Drink tier | Progression rank in the alpha eight-item chain |
| Drink ID | Durable logical identity, not localized name |
| Drink instance | One physical object in one session |
| Output drink | New object generated after a committed merge |
| Recipe | Versioned explicit transform rule |
| Recipe family | Thematic and/or ruleset group; not automatically compatible across families |
| Collision candidate | Pair of colliders reported for possible contact |
| Merge arbiter | Deterministically claims unique eligible pairs |
| Chain root | Originating merge/shot that caused descendant merges |
| Serve claim | Exclusive reservation of new output for matching active order |
| Next queue | Seeded logical spawn sequence, not physical bodies |
| Preview coins | Client-local illustrative alpha rewards, not trusted value |
| Catalog hash | Immutable identity of published drink definitions |
| Rules version | Version of resolver/scoring/serving gameplay behavior |
| Collection entry | Durable player achievement/ownership fact, after validation |
| Mastery | Later verified progression with a drink/family |
| Feature gate | Explicit server/config switch keeping deferred behavior off |
| Golden fixture | Known deterministic initial state, commands and expected events |

## Unverified design items

Recipe families beyond `core`, rarity names, ingredient sources, first discovery story, milestone XP, advanced crafting odds and event reward values are **proposals**. They are not claims about the original Merge Shooter product and not signed off by the Mixipelago owner. All other advanced-system docs must link to an accepted ADR before implementing behavior.
