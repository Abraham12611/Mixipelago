# 03 — Canonical Alpha Eight-Tier Drink Bible

**Status:** carried forward from Batch 1. Names, score values and art treatments are *working proposals* until owner approves production art and tuning. Engineering must not silently replace or reorder them while implementing the initial alpha.

## Linear ladder

| Tier | Stable `drinkId` | Display name | Board visual silhouette | Score on creation by merge | Tier-1-equivalent cost |
|---|---|---|---|---:|---:|
| 1 | `citrus-shot` | Citrus Shot | squat amber tumbler, amber wedge | 10* | 1 |
| 2 | `sunny-lemon` | Sunny Lemon | tall golden lemon cooler | 25 | 2 |
| 3 | `sunset-splash` | Sunset Splash | medium orange-pink layered glass | 60 | 4 |
| 4 | `blossom-fizz` | Blossom Fizz | blush-pink soda with flower | 140 | 8 |
| 5 | `coral-martini` | Coral Martini | wide red coupe / coral garnish | 320 | 16 |
| 6 | `mint-lagoon` | Mint Lagoon | crisp green mint-and-lime glass | 720 | 32 |
| 7 | `ocean-cloud` | Ocean Cloud | tall blue frosted foam glass | 1,600 | 64 |
| 8 | `crown-of-isles` | Crown of the Isles | ornate tropical signature glass | 3,500 | 128 |

`*` Tier 1's nominal score exists in the content table for future item creation methods, but is **not awarded on a standard merge** because tier 1 is never created as a merge output in the alpha. Score always references **output tier**. All equivalence costs assume source tier-1 only and no special multipliers/spawns.

## Exact evolution edges

`1+1→2; 2+2→3; 3+3→4; 4+4→5; 5+5→6; 6+6→7; 7+7→8; 8+8→no merge`.

Different tiers do not merge even if artwork is similar. The same tier merges regardless of the angle, speed, origin shot or which customer wants the result. The new object receives a fresh `objectId`. If produced output qualifies for the oldest active order, it is reserved/served before an extra collision-chain opportunity (Batch 2 arbitration).

## Scoring example

Two tier-2 Sunny Lemon glasses contact -> one tier-3 Sunset Splash -> base **60** merge points; a chain multiplier may apply in the reducer. If this newly produced tier-3 satisfies an order worth 15 preview coins, the fulfillment adds **150** order-bonus score and **15 preview coins** exactly once. Physics itself awards zero coins and zero points.

## Art direction guidelines

An illustrated 2.5D style: readable shapes, warm tropical highlights, consistent top-down camera, semi-translucent drinks, rounded glass silhouettes, limited garnish per tier. Color progression should be perceptible, but color alone is insufficient; each item must have a distinct profile and accessory. Use restrained motion to preserve contact clarity.

Asset slots per tier: `board_main` (transparent sprite), `hud_icon` (small silhouette), `order_icon` (high contrast), `collection_art` (larger), `shadow` (shared/parametric), `fx_merge` (shared presets), `audio_family` (tiers can share). High-res collection art is not required for v0.1 if board art scales sufficiently.

## Max-tier behavior

Tier 8 never evolves in the alpha. Two tier-8s collide physically and can contribute to board pressure. An eligible newly produced tier-8 may be served automatically if an outstanding order requests it; otherwise it stays on the board. Do not silently auto-remove terminal items, transform them into coins, or overflow to tier 9. Explicit later game modes can introduce terminal-item disposal with separate rules.

## Art/QA acceptance

Each tier must be identifiable at 40–64 CSS px with accessibility labels and distinguishable outline; alpha may tolerate provisional art but final labels and scores must match the catalog. All eight icons load without leaking texture memory across retries. Two glasses with the same tier should have the same gameplay collision radius/physical body tuning. A test must affirm the complete sequence and reject illegal merges.

## Approved source links within earlier handoff

Batch 1 `05_DRINKS_CUSTOMERS_SCORING.md`, `26_CONTENT_AND_CONFIG_EXAMPLES.md`; Batch 2 `07_MERGE_ARBITRATION_AND_CHAIN_REACTIONS.md`, `29_BATCH1_INTEGRATION_NOTES.md`. The documents here deliberately preserve the original alpha chain instead of inventing a new one.
