# 07 — Upgrade Catalog, Tiering and Prerequisites

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Upgrade identity
Each entry has stable `upgradeId`, `shopArchetype`, `category`, `maxLevel`, `priceByLevel`, prerequisite expression, incompatible group, effect references, art refs, published version and whether it is cosmetic. Cap upgrades to a finite tier and have a clear preview of next-level impact.

## v0.3 vertical slice proposal
| Upgrade | Type | Example starting cost | Clear benefit |
|---|---|---:|---|
| Blender I | utility | 250 | +1 eligible bonus order slot in campaign only, where mission supports it |
| Storage Rack I | utility | 400 | +1 future inventory capacity; initially display as staged until inventory feature live |
| VIP Seating I | attraction | 750 | +2 percentage points eligible VIP weight, capped, campaign only |
| Hibiscus Planters | cosmetic | 150 | decoration only |
| Sunrise Awning | cosmetic | 350 | visual shop exterior only |
| Golden Roof | prestige | 15,000 | visual prestige, no puzzle advantage |

**Important:** A proposed upgrade must be made mechanically real before becoming spendable. If inventory isn't implemented, disable Storage Rack rather than selling a promise. Prices and effects are hypotheses, not shipped values.

## Unlock logic
Costs use authoritative catalog, not UI-submitted numbers. Dependencies can reference owned prior levels, campaign milestones, shop archetype and reputation. No cyclical prerequisites; validator rejects duplicate IDs, unbounded multipliers and missing asset references.

## Refund/respec policy
v0.3 purchases are normally permanent; preview and confirmation reduce errors. Support support-driven reversal with an explicit compensating ledger receipt. Later respec/refund policies require versioned entitlements and exploitation analysis.
