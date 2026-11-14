# 11 — Boundary Contract: Physics, Drink Identity, Recipe Rules and Renderer

## Ownership matrix

| Question | Owning system | Must not own it |
|---|---|---|
| Where is the glass? | Rapier adapter / simulation state | React orders |
| Which colliders touched? | Rapier contact collector | Asset sprites |
| Which pair may merge this step? | Merge arbiter | Audio/UI |
| Is pair chemically/recipe compatible? | Pure catalog/recipe resolver | Rapier collider callbacks |
| What is created? | Deterministic merge reducer + catalog | Visual animation |
| Who gets served? | Session order reducer | Customer portrait |
| How much score/coins? | Session rules / later trusted backend | Phaser particle handler |
| Which art/audio asset? | Asset resolver/presentation | Physics engine |

## Alpha adapter

`DrinkPhysicsBridge` holds mapping between logical `objectId` and runtime Rapier handles plus `drinkId`, `tier`, status and chain ancestry. Asset IDs are not trusted for merge decisions. A named sprite `Sunset Splash` could display tier-3 artwork even if loading failed; gameplay must rely on logical definition. If a catalog ID is invalid at mission boot, fail validation before creating the physics world, not after a round is in progress.

## Collision timeline

At each fixed step, normalize any queued input command; advance Rapier; drain contact events; map handles to stable object IDs; sort candidate pairs; ask pure recipe resolver; claim eligible inputs; commit body removal and creation; allocate output ID; apply score/order reducer; reserve eligible output for service; update session terminal status; emit versioned gameplay events; finally notify presentation observers. No sound or React callback is allowed to mutate the simulation when events emit.

## Pre-creation and post-creation behaviors

The next drink preview isn't a physics collider. On launch, active logical drink identity is resolved from queue and the collider is instantiated. On merge, both inputs become ineligible immediately when claimed; the output is a new object. It may collide with others on later steps if not service-claimed. Hover effects or skins never change collision eligibility.

## Collider scaling

For alpha, all drink tiers should use same effective collider radius and approximate density unless the physics preset explicitly says otherwise; larger-looking tier 8 should not have secretly wider reach. In later modes, if a drink's radius changes as part of a visible gameplay mechanic, it must be part of the versioned physics preset and explained before playing.

## Rendering and cosmetics

2.5D board sprites should be positioned using interpolated physics poses. Juice slosh, glass tilt, sparkles, trail particles and stylized splash FX are separate non-authoritative layers. FX lifecycle can be killed when scene changes, but it must never cancel an already committed merge. A slow device can reduce particles without changing the collision result.

## Diagnostics

Debug overlay: logical drink ID, tier, object status, collision circle, velocity vector, current recipe rule ID, contact pair IDs, pending merge, chain root, order service claim, catalog hash. Test mode must export snapshot+commands to repeat failed cases. Never include personal player data in shared debug export.

## Acceptance and escalation

Same run with same seed and pinned hashes yields identical logical drink outcomes in the test environment. When a recipe/rule change would modify contact behavior, file an ADR, bump `rulesVersion`, test golden replay fixtures and obtain owner signoff. Batch 2's contact/sorting algorithm remains unchanged unless explicitly approved.
