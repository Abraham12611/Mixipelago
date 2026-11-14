# 01 — Economy Vision, Scope and Non-Negotiable Rules

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Player promise
Coins are useful, earned through skillful service, and spent on visible choices: more efficient shops, customer quality, new property, or beautiful prestige items. They are never a disguised mandatory toll. The player starts as a small beach-bar owner and can grow into an island entrepreneur; the puzzle remains enjoyable even without spending.

## Locked preceding contracts
- **Batch 2:** fixed-step Rapier simulation and exactly-once merge arbitration own drink physics; an economy modifier must not silently mutate collider mass, restitution, gravity, or collision rules.
- **Batch 3:** alpha has one eight-tier chain, tier 8 terminal, and newly merged drink auto-serves the oldest matching active order before chain continuation.
- **Batch 4:** Classic Service mission results, stars, objective reducers and replay receipts are the progression source. Scores and coins are separate units.
- **Batch 5:** published campaign graph references mission versions; first-clear and treasure claims are individually idempotent. A map node is not a wallet.
- **v0.1.x / v0.2.x:** **preview coins are local and untrusted**. They must never be imported into an authoritative wallet as cash-equivalent funds.

## Release decisions
**v0.3.0 target:** one owned Coconut Cove shop, one trusted coin wallet, immutable ledger, limited utility upgrades, cosmetic decoration, upgrade preview, server-controlled first-clear rewards, anti-farming limits and owner-directed UI testing. Future staffing, franchises, insurance, credit, dynamic markets and cross-player trading are deferred.

## Economy rules
1. Server is authoritative for grants, prices, spending, inventories and derived upgrade effects.
2. All currency writes are transactional, audited, idempotent and reversible only through compensating entries, never historical mutation.
3. No pay-to-win advantage in normalized ranked modes; use a standardized, versioned `competitive_profile`.
4. Avoid forced maintenance bankruptcy, paywall progression, infinite reward replay, accidental negative balances and recursive multiplier feedback.
5. Cosmetic purchases may have **zero** gameplay benefit; this must be clearly disclosed.
6. No hidden event that punishes a broke player merely for being broke; soft-landing options are required.
7. Numeric values are initial balancing hypotheses, not promises or published game pricing.

## Decision owner and scope boundaries
Economy lead owns source/sink policy; game director approves play-feel and tuning; gameplay lead owns merge rules; backend owns trusted transaction code; content staff author versioned catalogs but cannot grant assets to themselves in production. Any changes to scoring, drink tiers or mission objectives require explicit ADR and integration review.
