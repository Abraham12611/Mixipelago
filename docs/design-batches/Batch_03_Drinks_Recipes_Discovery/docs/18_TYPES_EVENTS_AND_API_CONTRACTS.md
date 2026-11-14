# 18 — TypeScript Types, Domain Commands, Events and Proposed API

## Contract package

`packages/domain-contracts` from Batch 2 remains framework-free. This batch proposes adding `DrinkCatalogV1`, `DrinkDefinitionV1`, `RecipeRuleV2` (future), `DrinkContentRef`, and `DiscoveryState`, all with runtime validation. Do not let React/Phaser/CSS import into these types.

## Alpha definitions

```ts
type AlphaTier = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8;
type DrinkDefinitionV1 = Readonly<{
  id: string; tier: AlphaTier; nameKey: string;
  nextTierId: string | null; assetId: string;
  mergeScore: number; familyId: 'core';
}>;
type DrinkCatalogV1 = Readonly<{
  schemaVersion: 1; catalogId: string;
  catalogVersion: string; tiers: readonly DrinkDefinitionV1[];
}>;
```

The app can use a `DrinkTier` alias within alpha but must resolve canonical `drinkId` when emitting long-lived events; future family migration should not make `tier=3` ambiguous. `drinkId` and `tier` must agree in the locked catalog.

## Merge event extension

```ts
type DrinkMergeEventV2 = Readonly<{
  eventId: string; sessionId: string; step: number;
  mergeId: string; inputObjectIds: readonly [string,string];
  inputDrinkIds: readonly [string,string];
  outputObjectId: string; outputDrinkId: string;
  outputTier: number; recipeId: string;
  catalogHash: string; rulesVersion: string;
  rootShotId?: string; chainDepth: number;
}>;
```

For v0.1 the `recipeId` can be `core:tier-1-to-2`, etc. This is a **proposed additive extension**, not a claim that Batch 2's existing event schema already has it. Prefer versioned adapters/aliases and do not break tests or persisted replays silently.

## Recipe resolver interface

```ts
type RuleContext = Readonly<{
  modeId: string; catalogHash: string;
  playerUnlocks?: ReadonlySet<string>;
  selectedRecipeId?: string;
}>;
type RecipeMatch =
  | {kind:'merge'; recipeId:string; outputDrinkId:string; outputTier:number}
  | {kind:'none'; reason:'different-tier'|'max-tier'|'locked'|'not-eligible'};
interface RecipeResolver {
  resolvePair(a: {drinkId:string;tier:number},
              b: {drinkId:string;tier:number},
              context: RuleContext): RecipeMatch;
}
```

Alpha implementations can ignore unlocks and special recipe selection, using a compile-time simple catalog resolver. Future recipes require approved versioned manifest and explicit modes.

## Proposed server HTTP boundaries (not alpha requirements)

`GET /v1/catalogs/:hash` fetches signed/immutable published catalog; `GET /v1/players/me/recipes` returns discovered/hidden progress; `POST /v1/recipes/research` attempts an authorized resource-consuming discovery with idempotency key; `GET /v1/players/me/mastery` fetches mastery aggregate; `POST /v1/sessions/:id/submit` submits validated run evidence. Client cannot post arbitrary mastery XP, collection ownership or currency grants.

## Semantic domain events

`drink_launched`, `drink_merged`, `order_line_progressed`, `order_fulfilled`, `mission_finished`, `drink_first_created` (future), `recipe_discovery_granted` (future), `collection_milestone_granted` (future), `mastery_xp_granted` (future). Each event contains stable schema version, unique event ID, game session identifier where applicable, logical simulation step for gameplay, catalog/rules hash, causation ID, timestamp only for server audit, and a documented owner. UI/FX subscribes without side effects on scoring.

## Error semantics

Bad catalog ID -> `catalog_unknown`; hash mismatch -> `content_version_mismatch`; retired output in new mode -> `recipe_retired`; missing unlock -> `recipe_locked`; stale command -> `command_stale`; duplicate request -> idempotent replay of same success; invalid material quantity -> `insufficient_ingredients`; persistence unavailable -> `pending_save`, not false success. HTTP status mapping chosen with backend team and codified in OpenAPI when API is implemented.

## Compatibility contract

Do not change event field semantics in place. Add version fields and translation adapters where possible; record archived content manifests for verified runs. Validate app and backend against identical schema version. Contract tests must check alpha compatibility plus future dummy recipe samples while keeping future features disabled by default.
