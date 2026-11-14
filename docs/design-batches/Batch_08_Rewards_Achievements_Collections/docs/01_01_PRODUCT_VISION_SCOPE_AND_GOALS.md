# 01 — Vision, Player Promise and Scope

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## What Batch 8 changes
Mixipelago players should feel recognized for **skill, exploration, craftsmanship, persistence and taste**. A reward is never a substitute for the intrinsic pleasure of merging drinks; it records meaningful accomplishments and opens new forms of personal expression. Collections encourage curiosity, while achievements acknowledge feats in Classic Service, island exploration and business ownership.

## Distinct concepts
- **Achievement:** a versioned rule and durable evidence that a player met a condition.
- **Entitlement:** a server-validated right to a particular reward once a condition is satisfied.
- **Claim:** the act (automatic or explicit) that converts an entitlement into ownership or a ledger grant.
- **Inventory:** an authoritative record of owned objects; physical cosmetic equipment is a separate projection.
- **Collection:** a versioned definition of which unique objects count toward an album, possibly with milestone rewards.
- **Reward policy:** a published mapping from a qualifying event to eligible grants, with frequency/cap restrictions.
- **Reward receipt:** immutable accounting of settled grant(s), source, catalog version and idempotency identity.

## Release boundaries
- `v0.1.x`: preview celebratory badges and clear outcomes; no spendable or trusted wallet. No preview rewards may be migrated to durable coins.
- `v0.2.x`: campaign stars, chapter progress, draft treasure markers; any nonmonetary preview badges remain clearly labeled local-only.
- `v0.3.x`: Batch 6 wallet/ledger supports verified first-clear and one authored treasure claim, subject to gateway checks.
- `v0.4.x`: Batch 7 trusted XP/points; Batch 8 adds a minimal verified achievement tracker + starter collection **after** issuer and ownership services exist.
- Future: daily/weekly activity, themed collections, vanity showrooms, event rewards, ranking prizes, seasonal trophies and optional mystery reward packs behind independent gates.

## Design principles
1. Readable progress: every visible goal says what counts, what does not, its window and how to claim.
2. Earned permanence: no silent removal of a legitimately earned achievement when a content patch changes rules.
3. Scalable content authoring: adding a collectible or achievement should not demand new TypeScript gameplay code.
4. Fairness by default: no daily login requirement for essential XP or campaign access; no randomized paid progression power.
5. Integrity: raw browser physics events cannot mint resources; verified domain facts drive settlement.
6. Player control: cosmetics are optional, collections do not clutter the core playfield, notifications are dismissible.
7. Economy integrity: Batch 6 settles spendable coins; Batch 7 alone determines valid XP/skill-point milestones.

## Proposed goals and diagnostics
Aim for a clear first achievement soon after a verified clear; measure reward explanation comprehension, claim failures, distribution by ability, collection engagement, and stalled/unclaimable entitlements. Set production targets only after testing, not from arbitrary engagement pressure.
