# 19 — Cosmetics, Ownership, Equipment and Showrooms

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Types
Player avatar frames, nameplate backgrounds, badges, shop decor, counter textures, drink-trail VFX, victory celebrations, profile titles and trophies. Inventory stores durable ownership; equip state maps a slot to an owned item.

## Equipment rules
Server checks authenticated owner, valid slot, appropriate shop ownership for shop decor, item compatibility, current catalog publication, and active equipment limits. Equipment transactions do **not** spend coins unless the player is buying a new item through Batch 6. `PUT /v1/inventory/equipment/{slot}` with `expectedRevision` rejects conflict; repeat same item is idempotent.

## Visual composition
Illustrated, layered assets may be AI-generated and polished offline. UI renders item thumbnail using a versioned asset manifest; no client-supplied SVG scripts or remote HTML. Cosmetics should not cover the aim line, active glass, customer order bubble or critical HUD. Provide a low-effects quality mode and reduced-motion mode.

## Shop scene handoff
Batch 6 shop-equipment ownership and prestige calculations remain authoritative. Pure spectacle items show **no hidden multiplier**. If a published shop item has utility, label it explicitly as a utility or hybrid upgrade and route the effect through the economy modifier engine, not Batch 8 item acquisition.

## Missing assets
If CDN fetch fails, render a safe fallback icon while preserving owned ID and equip state. Never delete item ownership because a texture is temporarily unavailable. Stale equipment requests return current state for reconciliation.
