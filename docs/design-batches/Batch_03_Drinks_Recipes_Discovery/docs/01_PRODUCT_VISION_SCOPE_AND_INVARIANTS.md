# 01 — Product Vision, Scope and Canonical Invariants

## Product thesis

Mixipelago is a cross-device casual game where a glass's physical movement has consequence: players aim and launch drinks on a low-friction tabletop, generate higher-tier drinks by compatible contact, satisfy customer orders, complete missions, and progressively unlock a tropical world. The drink system must be deep enough for years of content without diluting the immediate **same-tier pair-merge** skill loop.

A player should understand 'two identical items become a better one' after one successful action. A veteran should be able to optimize chain opportunities, route valuable results to orders, discover specialty recipes in supported future modes, and maintain meaningful mastery and collections.

## Decisions carried from Batches 1–2 (accepted baseline unless owner changes)

- Web-first desktop and mobile; Phaser 4 render layer, Rapier 2D simulation, TypeScript domain packages, React menus.
- Fixed-step physics at 60 Hz baseline; no merge decisions from sprites, React state, sound callbacks or wall-clock timing.
- Eight alpha tiers, exact chain and merge-output scores in document 03; no rarity/variant-specific collision behavior.
- Two active customer orders, automatic newly generated drink serving, oldest qualifying order wins; serve claim supersedes next merge eligibility.
- Next queue is seeded/versioned; no UI `Math.random()`; rejected/cancelled shots never consume queue.
- Local alpha coins are **preview-only**, never imported into a trusted wallet by default.
- IDs and prices are data-driven; content schemas and simulation versions pinned per run.
- Owner is responsible for manual gameplay and UI approvals; engineers automate tests. Main branch deployment/promotion requires explicit owner authorization according to Batch 1 coordination policy.

## Principles

**Physics remains readable.** Same collision results must correspond to the same gameplay rules. Novel recipe outcomes should be visibly explained and should not override a user's expected same-tier merge without an opt-in mode or explicit recipe selector.

**Discovery rewards curiosity, not random punishment.** Players should know when they are experimenting, receive usable hints, and never have their required mission outcome hijacked by an undocumented secret recipe.

**Catalog identities are durable.** A renamed drink retains its `drinkId`; a revised sprite gets a new asset version; a changed rule gets a new recipe/rules version. Never use display strings as persistence keys.

**Rarity does not automatically equal strength.** A rare skin or collectible can convey prestige without increasing physics power. Any later functional rarity must be separately categorized, bounded, and excluded or normalized in ranked competition.

**Content is authorable, verifiable and reversible.** All drink assets must be traceable to licenses, art briefs, image variants, collision footprints, supported locales, manifest hashes and tests.

## Release scope gates

| Capability | Alpha v0.1.0 | Polish v0.1.1–2 | Future extension |
|---|---|---|---|
| Linear 8-tier merge | Required | Refined | Permanent foundation |
| Catalog manifest & asset mapping | Required | Cache/art improvement | Full authoring/publish system |
| Auto-serving single-tier orders | Required | Animation/hints | Mixed recipe orders |
| New recipe families | Not active | Not active | Later minor release after feature gate |
| Ingredients/inventory | Not active | Not active | Later economic expansion |
| Hidden recipes | Not active | Concept UX only | Event/recipe modes |
| Mastery & collection rewards | Not active | Optional local prototype | Trusted server implementation |
| Rarity & cosmetic variants | Not active | Art variants only if approved | Profile/album and economy integration |

## Explicit non-goals of Batch 3

Full character writing, island lore, incident probabilities, economic policy, crew tournaments, PvP matchmaking and skill-tree balancing belong to later batches. This pack defines extension contracts only, and should never be used as a mandate to prematurely ship those features.

## End-to-end responsibility

`CatalogPublisher` -> immutable published catalog -> `MissionLoader` pins versions -> `SpawnDirector` chooses logical drink ID/tier -> `RapierAdapter` moves colliders -> `MergeArbiter` resolves compatible contacts -> `SessionReducer` scores/serves -> `PresentationDirector` animates and plays audio -> eventually `ValidatedSessionService` persists trusted progress. No layer may mint a server currency ledger credit based on unauthenticated client art/FX events.
