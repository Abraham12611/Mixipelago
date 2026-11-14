# 06 — Shop Domain, Archetypes, Locations and Ownership

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Core entity
A `Shop` belongs to a player and has an immutable `shop_id`, `location_id`, `archetype_id`, persistent shop level, optional cosmetic loadout, equipment slots, reputation, operating state and server-derived capability projection.

## Proposed archetypes
Beach Starter (Coconut Cove), Market Juice Stand, Sunset Lounge, Luxury Resort Bar, Festival Pop-up, Mountain Tea/Mocktail Kiosk, Experimental Mixology Lab and Franchise Flagship. Archetypes are **future content candidates**, not all launch shops; only one starter shop is functional in v0.3.

## Shop state machine
`available` → `owned` → `renovating` → `operational`; future incidents may enter `temporarily_closed` → `recovering` → `operational`. A shop cannot be sold or abandoned while active obligations are unresolved without explicit policy. A cosmetic preview does not change persistent state.

## Catalog versus ownership
`ShopArchetype` and `ShopTemplate` are versioned authored content. `PlayerShop` represents ownership and progress. `InstalledUpgrade` has separate provenance and level. A later catalog change must not erase previously purchased items. Replacing an upgraded building must preserve entitlements or grant compensation by policy.

## Unlock integration
Batch 5 campaign map owns node eligibility; opening a shop from a map node can navigate to its shop detail screen, but the map itself cannot mint shop ownership. Acquisition command validates graph unlock on the backend. Store unlocking must never block the core puzzle's minimum free path.
