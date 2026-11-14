# Mixipelago — Batch 6: Economy, Businesses & Shop Management

**Design batch 6/21 — authoritative cross-batch economy specification.** This pack documents the future trusted currency/shop domain; **no gameplay system is claimed to be implemented or deployed**.

## Read this first

- Prior contracts: Batch 2 physics and merge arbitration, Batch 3 eight-tier drinks and auto-serving, Batch 4 missions/stars, Batch 5 campaign graphs/claim identities.
- Alpha and early campaign use **untrusted preview coins**. Do not convert to the wallet. The trusted shop economy is staged for `v0.3.0+`.
- No accidental pay-to-win ranked competition, debt traps, mandatory maintenance, or preview spendable balances.
- Manual UI and gameplay approvals are directed to the product owner.

## Specification chapters

- [Economy Vision, Scope and Non-Negotiable Rules](01_ECONOMY_VISION_SCOPE_AND_INVARIANTS.md)
- [Currencies, Wallets and Accounting Units](02_CURRENCIES_ACCOUNTING_AND_WALLET.md)
- [Coin Sources, Reward Policies and Earn Rates](03_COIN_SOURCES_AND_REWARD_POLICIES.md)
- [Coin Sinks, Saving Goals and Late-Game Demand](04_COIN_SINKS_AND_LONG_TERM_UTILITY.md)
- [Trusted Ledger, Transaction Semantics and Idempotency](05_LEDGER_TRANSACTION_IDEMPOTENCY.md)
- [Shop Domain, Archetypes, Locations and Ownership](06_SHOP_TYPES_STATES_AND_OWNERSHIP.md)
- [Upgrade Catalog, Tiering and Prerequisites](07_UPGRADE_CATALOG_AND_DEPENDENCY_TREE.md)
- [Modifier Engine, Caps and Mode Fairness](08_MODIFIER_RESOLUTION_AND_LIMITS.md)
- [Demand Director, Customer Wealth and Shop Reputation](09_CUSTOMER_DEMAND_AND_VIP_ATTRACTION.md)
- [Order Pricing, Revenue and Reward Formulas](10_PRICING_EARNINGS_AND_CUSTOMER_REWARDS.md)
- [Staff, Training and Shop Operations — Later Design](11_STAFF_TRAINING_AND_OPERATIONS_OVERVIEW.md)
- [Cosmetic Ownership, Showrooms and Spectacle Purchases](12_COSMETICS_SPECTACLE_AND_DECORATION.md)
- [Expansion, Property, Franchises and Business Empire](13_EXPANSION_PROPERTY_AND_FRANCHISES.md)
- [Shop Prestige, Ratings and Brand Perception](14_SHOP_PRESTIGE_AND_REPUTATION.md)
- [Operating Costs, Maintenance and Anti-Punishment Policies](15_COSTS_UPKEEP_AND_RECOVERY.md)
- [Insurance, Incidents, Debt and Business Risk — Overview](16_INSURANCE_INCIDENTS_AND_LOANS_OVERVIEW.md)
- [Campaign, Mission Rewards, Treasures and Event Integration](17_CAMPAIGN_AND_EVENT_ECONOMY_HANDOFF.md)
- [Economic Balancing, Simulation Scenarios and Formulas](18_BALANCING_SIMULATION_AND_FORMULAS.md)
- [Economy Security, Exploit Cases and Abuse Prevention](19_EXPLOITS_FRAUD_AND_THREAT_MODEL.md)
- [PostgreSQL Schema, RLS and Migration Strategy](20_POSTGRES_SCHEMA_RLS_AND_MIGRATIONS.md)
- [HTTP API, Error Codes and Command Contracts](21_API_ENDPOINTS_AND_COMMAND_CONTRACTS.md)
- [TypeScript Domain Services, Events and Integration](22_TYPESCRIPT_SERVICES_EVENTS_AND_PACKAGES.md)
- [Shop & Economy UI/UX: Mobile and Desktop](23_SHOP_UI_UX_DESKTOP_AND_MOBILE.md)
- [Economy Content Studio, Authoring and Safe Publishing](24_ECONOMY_CONTENT_STUDIO_AND_PUBLISHING.md)
- [Economy Analytics, Experiments and Live Balancing](25_ANALYTICS_EXPERIMENTS_AND_ECONOMIC_HEALTH.md)
- [Economy QA, Security, Load and Regression Matrix](26_QA_SECURITY_AND_CONCURRENCY_TEST_MATRIX.md)
- [Phased Releases, Feature Gates and Rollback Plan](27_RELEASE_SLICES_GATES_AND_ROLLBACK.md)
- [Parallel Engineering Tickets and Coordination Rules](28_PARALLEL_ENGINEERING_ISSUES_AND_TEAM_PLAN.md)
- [Architecture Decisions, Risks and Owner Questions](29_ARCHITECTURE_DECISIONS_RISKS_AND_OPEN_QUESTIONS.md)
- [Compatibility Matrix With Batches 1–5](30_CROSS_BATCH_COMPATIBILITY_AND_MIGRATION.md)
- [Example Player Journeys and Failure Paths](31_PLAYER_JOURNEYS_AND_EDGE_CASE_STORIES.md)
- [Accessibility, Localization and Player Trust](32_ACCESSIBILITY_LOCALIZATION_AND_PLAYER_TRUST.md)
- [Requirement Traceability and Definition of Done](33_REQUIREMENTS_TRACEABILITY_AND_DEFINITION_OF_DONE.md)
- [Engineer Kickoff and First Trusted Increment](34_ENGINEER_KICKOFF_AND_FIRST_INCREMENT.md)

## Supporting artifacts

- `../examples/catalog/economy-catalog.draft.json` — sample shop + upgrade catalog, explicitly **draft**.
- `../examples/catalog/reward-policies.draft.json` — initial first-clear and order reward policies.
- `../examples/schemas/economy-catalog.schema.json` — schema validating example entries.
- `../examples/contracts/economy-api-examples.json` — illustrative requests/responses.
- `../examples/tests/economy-rule-vectors.json` — arithmetic and prerequisite test vectors.
- `../examples/sql/economy_schema_draft.sql` — illustrative PostgreSQL DDL, NOT production-ready migrations.
- `../tools/validate_batch6.py` — local static validation of JSON and sample rules.

## Engineer starting order
Contracts → pure rules → ledger → verified reward adapter → one-shop purchase → responsive UI → test and staged gate. See `34_ENGINEER_KICKOFF_AND_FIRST_INCREMENT.md`.
