# 27 — Phased Releases, Feature Gates and Rollback Plan

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Build slices
- **v0.1.x:** preview-only coin number and nonspendable shop teaser; no trusted backend wallet.
- **v0.2.x:** map progression and preview treasury; authored reward policy IDs in config without spending.
- **v0.3.0:** authenticated wallet, immutable ledger, verified first-clear faucet, one starter shop, one real utility upgrade and one cosmetic purchase, shop screens, admin catalog basics, reconciliation and kill switch.
- **v0.3.1:** customer payout verification, more curated upgrades, transaction history, better hints and performance.
- **v0.3.2:** upgrade modifiers for campaign customer mix, cosmetics presets, tuning improvements.
- **v0.4+:** accounts/identity hardening, shops expansion, deeper player specializations and prestige.
- **later:** franchises, staffing, maintenance, insurance/loans, dynamic markets and events; require distinct design/security approvals.

## Feature gates
`ECONOMY_TRUSTED_WALLET`, `ECONOMY_ORDER_REWARDS`, `SHOP_PURCHASES`, `SHOP_COSMETICS`, `SHOP_VIP_MODIFIERS`, `SHOP_EXPANSION`, `ECONOMY_INCIDENTS`, `ECONOMY_PASSIVE_REVENUE`; default OFF until explicit launch gate and QA evidence.

## Release gates
All database invariants covered, duplicate credit/purchase concurrency tested, migration safe, wallet reconcile job healthy, real responsive UI tested by owner, anti-cheat verified reward source, ability to kill credit faucet and purchase writes without breaking gameplay, no first-clear farming and no ranked perk advantage.

## Rollback
Stop grants/purchases via feature gates, preserve immutable ledger, freeze payouts if verification compromised, patch forward or compensate. Never use an unsafe backward migration that drops confirmed purchases.
