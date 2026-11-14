# 33 — Batch 1/2 Integration Notes and Proposed Document Deltas

## We reviewed these exact earlier documents

Batch 1: `05_DRINKS_CUSTOMERS_SCORING.md`, `07_DATA_MODEL.md`, `26_CONTENT_AND_CONFIG_EXAMPLES.md`, `08_API_AND_EVENTS.md`, `16_RELEASE_ROADMAP.md`.
Batch 2: `07_MERGE_ARBITRATION_AND_CHAIN_REACTIONS.md`, `08_SPAWN_NEXT_QUEUE_AND_GAME_DIRECTOR.md`, `11_TYPES_COMMANDS_AND_EVENT_CONTRACTS.md`, `16_DIFFICULTY_AND_GAMEPLAY_BALANCING.md`, `29_BATCH1_INTEGRATION_NOTES.md`.

## Carried forward without change

- Alpha core catalog names and scores: Citrus Shot / Sunny Lemon / Sunset Splash / Blossom Fizz / Coral Martini / Mint Lagoon / Ocean Cloud / Crown of the Isles, scores `[10,25,60,140,320,720,1600,3500]` by output tier.
- Tier 1–7 same-tier pair evolution; tier 8 terminal.
- Auto-serve first on eligible **new output** only, deterministic oldest active order; no retroactive service of idle board items.
- Separate physical collisions from scoring, orders and SFX.
- One logical drink object per collider; new output gets fresh object ID.
- Local preview coins only for alpha; server authority later.
- Content and physics versions pinned per session, fixed-step tick and seeded spawn queue.

## Specific corrections/clarifications proposed

**1. 'DrinkTier' global typing.** Batch 2 `DrinkTier = 1..8` is correct for alpha. Future multiple families require `drinkId + familyId + recipeId`, with tier scoped to family. Do not immediately weaken type safety in alpha; add a future adapter when feature launches.

**2. Merge scoring.** Batch 1's example `tier2+tier2=>tier3` awards 60, correct because score derives from output. Tier-1 `mergeScore=10` is dormant for ordinary merges. Clarify this in future comments/tests to prevent off-by-one reward bugs.

**3. Customer serving order.** Batch 2 explicitly reserves output for serving ahead of chain, which can make naïve tutorial scripts unsolvable. First mission must contain tested scripted inputs and appropriately seeded objects. Batch 1's `firstItems:[1,1,1,1,1]` plus initial two tier-1s is a candidate, not proof of success.

**4. Recipe logic.** Existing Batch 2 arbiter has no need to know ingredients or rarity. Introduce a pure resolver interface under the arbiter in an additive way; the default alpha resolver preserves exact same-tier semantics. Do not alter contact sorting or output momentum.

**5. Data model.** Batch 1's `game_sessions` and wallet ledgers remain. Add proposed recipe and mastery entities only in later backend migrations, not mandatory day-one tables.

**6. Audio/art.** AI-made art and pre-rendered 3D sprites are presentation-layer concerns. Asset filenames and artistic variants must not be collision/recipe IDs.

**7. Events.** Batch 2 events can eventually include `outputDrinkId`, `recipeId`, `catalogHash`, but require schema version/adapters before editing existing event payload semantics. Replays and score verifier must use matching versions.

## Source code change workflow

Implement domain contracts first, obtain PR review, run golden session fixtures, update earlier relevant docs *in same PR* as behavior changes, bump content/rules/save version appropriately, and seek owner signoff. Do not edit an approved document to imply a feature is already built just because a design file exists.

## Unresolved owner approvals

Accept/reject new recipe graph features, future off-board pantry crafting, mastery utility, collection reward policy and rarity labels. These are not prerequisites for shipping linear alpha.
