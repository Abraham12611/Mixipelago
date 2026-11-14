# 04 — Coin Sinks, Saving Goals and Late-Game Demand

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Sink portfolio
- **Functional utility:** blender upgrade, storage slot unlock, additional customer order capacity (outside normalized ranked), service-speed effect and training facilities.
- **Customer acquisition:** décor/amenity upgrades that increase a capped weighted chance for a relevant customer class.
- **Prestige:** fully cosmetic golden roof, themed counter, neon sign, seasonal exterior, fountains, banners and collectible trophy pedestals.
- **Expansion:** purchase/renovate a second shop, secure waterfront location, unlock showroom and future franchises.
- **Optional service expenses:** selected temporary boosts or upgrades, if recovery remains accessible.

## Sink health metrics
Track sinks in coins/player/day, ratio of balances held to expected weekly income, number of affordable meaningful purchases, and percentage of players who can progress without buying. Measure at new, midgame and endgame cohorts. Add cosmetic aspirational sinks for wealthy players without increasing mandatory upgrade prices for everybody.

## Purchase decision quality
Every meaningful utility purchase must specify cost, immediate benefit, future constraints, affected game modes and acquisition prerequisites. If a purchase reduces shop earnings due to an operational tradeoff, disclose that before payment. Do not disguise a mandatory upgrade behind a cosmetic tab.

## Passive revenue policy
**No offline idle currency generation in v0.3.** Later shops may earn bounded scheduled revenue, but its cap and exploitation model must be specified. Avoid exponential passive income compounding across multiple franchises, multipliers and temporary event buffs.

## Negative balance
Normal purchases fail with `INSUFFICIENT_COINS`, without partial ownership. Chargebacks, reversals and compensating repairs must never silently put ordinary players into a forced negative balance. Admin adjustments are separately auditable.
