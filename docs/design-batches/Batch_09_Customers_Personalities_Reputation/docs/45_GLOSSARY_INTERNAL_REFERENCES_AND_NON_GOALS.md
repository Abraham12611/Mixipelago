# 45 — Glossary, Internal References, Technical Links and Non-goals

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Terms
- **Customer Definition:** versioned fictional character/archetype identity.
- **Encounter:** one selected presentation/guest opportunity bound to a source entitlement.
- **Order:** deterministic mission-side requested drink lines.
- **Service claim:** one newly merged drink consumed by exactly one eligible order unit.
- **Satisfaction observation:** post-verification interpretation of service evidence.
- **Relationship:** persistent customer-specific affinity projection, optional.
- **Reputation:** shop service-quality score, distinct from prestige.
- **VIP pool:** published eligible premium encounter subset, not an economic permission.
- **Source receipt:** server-verified fact that can support a durable award.
- **Ranked normalized profile:** fixed competitive rules and modifiers for fairness.

## Required Mixipelago references
- Batch 2: `docs/07_MERGE_ARBITRATION_AND_CHAIN_REACTIONS.md`.
- Batch 3: `docs/09_CUSTOMER_ORDERS_AND_RECIPE_REQUIREMENTS.md` and eight-tier drink bible.
- Batch 4: `docs/18_CUSTOMER_DIRECTOR_AND_ORDER_PACING.md`, Classic Service spec and mission schema.
- Batch 5: campaign graph/result and treasure claim contracts.
- Batch 6: `docs/09_CUSTOMER_DEMAND_AND_VIP_ATTRACTION.md`, `10_PRICING_EARNINGS_AND_CUSTOMER_REWARDS.md`, `14_SHOP_PRESTIGE_AND_REPUTATION.md`, ledger.
- Batch 7: `docs/23_23_CUSTOMER_DIRECTOR_EFFECTS_AND_FAIR_SPAWNING.md` and normalized ranking.
- Batch 8: achievements/reward entitlement and collectibles owner.

## Technology reference starting points
- Rapier JS physics: https://rapier.rs/docs/user_guides/javascript/
- Phaser: https://docs.phaser.io/
- Supabase PostgreSQL/RLS: https://supabase.com/docs/guides/database/postgres/row-level-security
- JSON Schema: https://json-schema.org/
- Vitest: https://vitest.dev/
- Playwright: https://playwright.dev/

## Non-goals in this batch
No detailed story bible, real economy simulation, generated dialogue AI service, real weather, full rival-business competition, multi-user realtime social simulation, or production-ready migrations. Those are future workstreams with their own approval and testing requirements.
