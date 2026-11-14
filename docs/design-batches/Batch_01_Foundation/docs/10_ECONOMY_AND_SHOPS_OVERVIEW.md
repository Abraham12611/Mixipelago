# 10 — Economy, Coin Purpose and Shop System (Overview)

**Status:** Concept architecture; not an approved full economic model. No real persistent shop purchases until server-wallet transactions and balancing are implemented.

## Product rule

Coins must retain meaningful utility without feeling like compulsory upkeep. The player chooses between spending on utility, prestige and expansion. Aesthetic purchases can remain purely cosmetic, while functional upgrades have clear mechanical effects.

## Main systems

- **Earn:** fulfill orders, complete missions, milestones, challenges, season rewards (bounded).
- **Spend:** blender/equipment, staffing, customer seating, decor, new shops, repairs/insurance (later), certain consumables.
- **Save/invest:** bigger shops, new islands, capital-heavy prestige purchases.
- **Risk/recovery:** costs and incidents must create interesting decisions, not bankruptcy spirals.

## Core product entities

`Currency` (`COINS` initially), `Wallet`, immutable `WalletLedger`, `Shop`, `ShopArchetype`, `UpgradeCatalog`, `OwnedUpgrade`, `InventoryItem`, `EconomicModifier`, `PurchaseTransaction`.

## Shop upgrade categories

- **Utility:** capacity, preparation, storage, booster handling, customer throughput.
- **Customer attraction:** atmosphere, comfort, premium service; influences eligibility/probability of customer segments.
- **Spectacle:** golden roof, rare furniture, lighting, waterfalls, signs; prestige/cosmetic.
- **Expansion:** acquire new premises, change shop archetype, unlock branch opportunities.

Do not make marketing copy claim a permanent reward if upgrade only affects probability. Show exact or bounded effect in UI.

## Trusted purchase flow

Client requests `upgradeId` → server derives current price and verifies ownership/eligibility → SQL transaction debits wallet and adds upgrade → ledger and reward/milestone event recorded → client refreshes view. Requires idempotency and fraud monitoring. See `07`, `08`, `14`.

## Economic balancing needs before activation

- Define coin sources/sinks per hour of normal play, across player stages.
- Set earning and spending curves, retry costs, upgrade costs, optional upkeep policy.
- Prevent exponential earning loops from skills + customer multipliers.
- Define no-purchase path; a user should never be permanently unable to progress.
- Design soft caps or sink expansion for long-term players without punitive inflation.
- Simulate multiple play styles and low-activity accounts using synthetic agents.

## Alpha vs later

v0.1: coins are preview-only feedback and stored locally. v0.3: authoritative economy, a single shop, first functional and cosmetic purchases. Later: franchises, staffing, contracts, loans, insurance, dynamic markets and leaderboards for business success. Detailed formulas deferred.
