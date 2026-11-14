# 02 — Drink Identity, Catalog Taxonomy and Versioned Presentation

## Definitions

- **Drink definition:** a durable logical object (`drinkId`) with a name, tier, family, gameplay tags and immutable identity.
- **Tier:** a positive progression rank within a given recipe/evolution context; alpha tiers are 1–8.
- **Family:** a thematic group (`core`, later `berry`, `herbal`, `festival`), not automatically a gameplay compatibility key.
- **Recipe:** a rule transforming a defined set of inputs into an output under explicit conditions.
- **Variant/skin:** a presentational appearance of one logical drink; may be collectible but must not quietly change alpha merge eligibility.
- **Ingredient:** a resource or recipe descriptor, not a tabletop physics object unless future content explicitly declares it as such.
- **Rarity:** collection/acquisition classification; independent from `tier` and separate from score.
- **Manifest:** versioned, validated catalog and asset references loaded at session start.

## Identity contract

`drinkId` is lowercase kebab-case, namespaced by catalog where necessary (`core:citrus-shot` in composite contexts). IDs must never be recycled. An `assetId` is a separate opaque string such as `drink.core.t1.board.v1` and can be updated independently. Localization uses key `drink.core.citrus-shot.name`, not raw name comparisons.

`familyId` is relevant to future discovery and collection sets, but alpha eligibility is **same tier in the single core chain**. In the future, `recipeCompatibilityKey` will be explicit. Two tier-3 drinks from distinct recipe families should **not** merge unless the published recipe manifest permits it. Never infer compatibility solely from shared numerical tier once multiple families exist.

## Object model boundaries

A *catalog entry* knows nothing of Rapier collider handles. A *simulation instance* contains `objectId`, `drinkId`, `tier`, `status`, position/velocity, catalog hash and a transient physics-handle mapping. An *owned collectible* belongs to a player profile with acquisition evidence. A *customer order line* requests a canonical target; presentation may show a familiar localized name.

Required key separations:

| Persisted thing | Primary key | Mutability |
|---|---|---|
| Definition | `drinkId`, catalog version | Immutable within published version |
| Presentation mapping | `assetId`, art revision | Replaceable with manifest update |
| Physics instance | `objectId` scoped to session | Ephemeral, never a wallet item |
| Discovery unlock | `playerId + discoveryId` | Durable grant, idempotent |
| Collection entry | `playerId + collectionEntryId` | Durable, reversible only by audited operation |
| Recipe | `recipeId + recipeVersion` | Published copy immutable |

## Taxonomy fields for content authoring

Suggested fields: name, short name, slug, locale keys, description, collection tags, ingredient imagery, island origin, family, tier, base score, eligibility traits, unlock requirements, discoverability, adult-beverage safety classification, asset bundle, accessibility silhouette, FX sound IDs, artist/licensing attribution, publication state, schema version and audit metadata.

Do **not** overload `tags` to implement rules. Rules must be explicit and validated; tags are for filtering/search/curation.

## Art variant rules

- Every drink has a fixed collision footprint calibrated to its displayed table size; decorative garnish may extend outside the collider but must not obscure aiming or cause perception errors.
- Cosmetic skins share physics radius, mass and merge behavior with their canonical logical tier unless a separately advertised mechanic overrides this in a future mode.
- Animated drink artwork may include idle glint, travel skew, hit wobble, merge gather, reveal, order-serving and selected/locked variants; animation files are optional if procedural effects cover the behavior.
- The name and silhouette must remain distinct in motion at mobile game resolution, not only in a full-size art board.

## Data invariants

Reject duplicate IDs, bad slugs, missing asset IDs, ambiguous localization keys, unsupported image sizes, non-finite score, tier discontinuity in a linear ladder, dangling recipe output, and draft entries referenced by published missions. Mark a retired definition as non-spawnable for new runs while keeping it available to interpret pinned historical replays.

## Future extensibility

One world can host multiple catalog families; their graph may have different lengths, unlocks and special recipes. Store `familyId`, `drinkId` and `recipeId` rather than introducing a global `tier` that falsely assumes cross-family identity. A migration is required before turning on multi-family live gameplay; see 04 and 20.
