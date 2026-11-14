# 14 — Typed Modifier Engine: Sources, Projections and Ownership

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Domain input contract
The source resolver accepts `playerId`, `context` (`casual_session|shop_service|map_view|ranked`), `shopId?`, `missionVersion?`, `competitiveProfileId?`, and `skillCatalogVersion`. It loads the server-validated skill allocation snapshot plus Batch 6 owned shop upgrades and eligible temporary event effects.

## Typed effect registry
Each effect has `effectId`, `targetStat`, `operation` (`flat_add|percentage_point_add|multiplier_add|bool_unlock|capacity_add`), `value`, `rank`, `sourceId`, `contextTags`, `stackingGroup`, `capId`, `expiry?`, and `version`. No arbitrary script or JSON function execution. Example: `hospitality.vip_chance_pp` adds `0.01` absolute probability per rank; it is not a 1% relative multiplier.

## Application boundaries
- **Economy:** a trusted receipt calculation may use `trusted.order_tip_multiplier`, `shop.upgrade_discount_percent`, or `guest.vip_chance_pp` after authorization.
- **UI:** render `ui.next_spawn_preview_count`, `ui.map_hint_visibility` without granting score or currency.
- **Game physics:** **no skill target** may be a Rapier friction/restitution/mass, RNG spawn rule or eight-tier compatibility without an explicit future ADR, mission authoring contract, and competitive proof version.
- **Ranked:** resolver substitutes `competitive_profile` and excludes profile/shop modifiers in `NORMALIZED` mode.

## Projection correctness
Do not store a single mutable `effectiveStats` row as the source of truth. Compute from versioned inputs, optionally cache by `(player, context, contentVersion, allocationRevision, shopRevision)`; invalidate on purchases, respec, shop transfer and event expiry. Include source explanations for UI and diagnostics.

## Cross-system event timing
An XP grant during a completed session must not retroactively alter its score or payouts. New skills apply to the **next eligible session/order** after a committed allocation. Active gameplay snapshots pin the resolver outputs at session start.
