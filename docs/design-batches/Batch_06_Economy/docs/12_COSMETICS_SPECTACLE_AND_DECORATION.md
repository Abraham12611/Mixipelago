# 12 — Cosmetic Ownership, Showrooms and Spectacle Purchases

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Core player value
Players can decorate and show off their own bars. Pure visual customizations include golden roofs, counters, light fixtures, tropical landscaping, shop signage, wall motifs, seating skins, particle flourishes and music themes.

## Asset layers
The shop scene uses stable slots: `roof`, `awning`, `counter`, `floor`, `seating`, `signage`, `backdrop`, `decor_foreground`, and `ambient`. Every art asset must declare safe render bounds, anchor, foreground depth, supported device tiers, accessibilty label and author/license metadata.

## Save model
`inventory_entitlements` says player owns a cosmetic; `shop_equipped_cosmetics` says it is currently displayed. Equipping is a free authenticated state update with revision checks. Duplicate ownership should result in a defined conversion/claim policy, not duplicate sale.

## Purchase UX
Preview shop before purchase, allow comparison with current look, show price and no-stat-benefit label, confirm purchase, then celebrate sparingly. Cosmetic previews must work offline but purchases must wait for trusted backend availability.

## Future showcase
Profile visitors may inspect a publicly shared shop, but public views must expose only opt-in information. Shop design contests are deferred to social batch with moderation and vote-abuse prevention.
