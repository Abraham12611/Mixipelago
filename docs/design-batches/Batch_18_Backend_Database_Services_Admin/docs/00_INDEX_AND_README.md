# Batch 18 — Backend, Database, Game Services & Admin Studio

**Status:** Detailed engineering design pack; not an implemented/deployed feature. **Prepared:** 2026-11-14.
**Owner:** Backend / Data / Admin Platform. **Candidate release:** trusted foundation v0.3.x+; advanced services by feature. **Advanced gate:** `TRUSTED_BACKEND_ENABLED` default OFF.

## Critical earlier rules
Two visible scripted orders; newly merged matching drink auto-serves the oldest eligible order before a further chain reaction. The baseline drink chain is eight tiers, with tier 8 terminal. Alpha coins are local previews and never convertible to trusted currency. v0.1.0 remains a browser-first playable target, not a proven deployment.

## Source-of-truth responsibilities
Accounts, server-verified state, database writes, domain API routes, content publishing, admin controls and durable event delivery.
Batches 02–04 physics/missions, 05 campaign, 06 ledger, 07 XP, 08 entitlements, 09 guests, 10 world, 11 stories, 12 events, 13 rankings, 14 social and 15 UI.

## Specification chapters
- [01 — Backend system vision and authoritative boundaries](./01_BACKEND_SYSTEM_VISION_AND_AUTHORITATIVE_BOUNDARIES.md)
- [02 — System context, domains and bounded contexts](./02_SYSTEM_CONTEXT_DOMAINS_AND_BOUNDED_CONTEXTS.md)
- [03 — Technology baseline, environments and dependency pins](./03_TECHNOLOGY_BASELINE_ENVIRONMENTS_AND_DEPENDENCY_PINS.md)
- [04 — Package and monorepo layout](./04_PACKAGE_AND_MONOREPO_LAYOUT.md)
- [05 — Identity, authentication and account linking](./05_IDENTITY_AUTHENTICATION_AND_ACCOUNT_LINKING.md)
- [06 — Authorization, tenant and player ownership](./06_AUTHORIZATION_TENANT_AND_PLAYER_OWNERSHIP.md)
- [07 — Session start, input trace and verification API](./07_SESSION_START_INPUT_TRACE_AND_VERIFICATION_API.md)
- [08 — Mission result ingestion and progression bridge](./08_MISSION_RESULT_INGESTION_AND_PROGRESSION_BRIDGE.md)
- [09 — PostgreSQL schema governance and migrations](./09_POSTGRESQL_SCHEMA_GOVERNANCE_AND_MIGRATIONS.md)
- [10 — Wallet, coins and purchase handoff](./10_WALLET_COINS_AND_PURCHASE_HANDOFF.md)
- [11 — XP, skills and player progression handoff](./11_XP_SKILLS_AND_PLAYER_PROGRESSION_HANDOFF.md)
- [12 — Inventory, achievements and collectible ownership](./12_INVENTORY_ACHIEVEMENTS_AND_COLLECTIBLE_OWNERSHIP.md)
- [13 — Campaign graph, island and mission catalog service](./13_CAMPAIGN_GRAPH_ISLAND_AND_MISSION_CATALOG_SERVICE.md)
- [14 — Customer, reputation and encounter reservation](./14_CUSTOMER_REPUTATION_AND_ENCOUNTER_RESERVATION.md)
- [15 — World, quests and event authoring handoffs](./15_WORLD_QUESTS_AND_EVENT_AUTHORING_HANDOFFS.md)
- [16 — Leaderboards and tournament backend service](./16_LEADERBOARDS_AND_TOURNAMENT_BACKEND_SERVICE.md)
- [17 — Social graph, crews and notifications](./17_SOCIAL_GRAPH_CREWS_AND_NOTIFICATIONS.md)
- [18 — Catalog versioning, content hashes and dependency graph](./18_CATALOG_VERSIONING_CONTENT_HASHES_AND_DEPENDENCY_GRAPH.md)
- [19 — Internal admin roles, access reviews and break glass](./19_INTERNAL_ADMIN_ROLES_ACCESS_REVIEWS_AND_BREAK_GLASS.md)
- [20 — Admin Studio: catalog editors and publishing](./20_ADMIN_STUDIO_CATALOG_EDITORS_AND_PUBLISHING.md)
- [21 — Admin Studio: player support and reversible operations](./21_ADMIN_STUDIO_PLAYER_SUPPORT_AND_REVERSIBLE_OPERATIONS.md)
- [22 — Admin Studio: QA simulation and replay console](./22_ADMIN_STUDIO_QA_SIMULATION_AND_REPLAY_CONSOLE.md)
- [23 — API conventions and TypeScript contract envelopes](./23_API_CONVENTIONS_AND_TYPESCRIPT_CONTRACT_ENVELOPES.md)
- [24 — Transactional outbox, event bus and delivery](./24_TRANSACTIONAL_OUTBOX_EVENT_BUS_AND_DELIVERY.md)
- [25 — Background jobs, scheduling and queues](./25_BACKGROUND_JOBS_SCHEDULING_AND_QUEUES.md)
- [26 — Cache, object storage and CDN contracts](./26_CACHE_OBJECT_STORAGE_AND_CDN_CONTRACTS.md)
- [27 — Realtime, subscriptions and consistency choices](./27_REALTIME_SUBSCRIPTIONS_AND_CONSISTENCY_CHOICES.md)
- [28 — Offline preview, sync and conflict resolution](./28_OFFLINE_PREVIEW_SYNC_AND_CONFLICT_RESOLUTION.md)
- [29 — Auditability, reconciliation and data lineage](./29_AUDITABILITY_RECONCILIATION_AND_DATA_LINEAGE.md)
- [30 — Analytics events, metrics and observability](./30_ANALYTICS_EVENTS_METRICS_AND_OBSERVABILITY.md)
- [31 — Security, secrets and deployment isolation](./31_SECURITY_SECRETS_AND_DEPLOYMENT_ISOLATION.md)
- [32 — Performance, concurrency and capacity planning](./32_PERFORMANCE_CONCURRENCY_AND_CAPACITY_PLANNING.md)
- [33 — Backup, restore, disaster recovery and runbooks](./33_BACKUP_RESTORE_DISASTER_RECOVERY_AND_RUNBOOKS.md)
- [34 — CI/CD, previews and release flags](./34_CI_CD_PREVIEWS_AND_RELEASE_FLAGS.md)
- [35 — API security, quotas and abuse budgets](./35_API_SECURITY_QUOTAS_AND_ABUSE_BUDGETS.md)
- [36 — Engineering workstreams and first trusted release](./36_ENGINEERING_WORKSTREAMS_AND_FIRST_TRUSTED_RELEASE.md)
- [37 — ADRs, schema ownership and requirement traceability](./37_ADRS_SCHEMA_OWNERSHIP_AND_REQUIREMENT_TRACEABILITY.md)

## Implementation and governance
- [90 — Engineering Implementation Blueprint](./90_IMPLEMENTATION_BLUEPRINT.md)
- [91 — Atomic Engineering Issue Backlog](./91_ENGINEERING_ISSUE_BACKLOG.md)
- [92 — QA and Golden Fixtures](./92_QA_GOLDEN_FIXTURES.md)
- [93 — Release Gates and Rollback](./93_RELEASE_GATES_AND_ROLLBACK.md)
- [94 — ADRs and Traceability](./94_ADRS_AND_TRACEABILITY.md)
- [95 — Official Sources and Precedence](./95_OFFICIAL_SOURCES.md)

## Machine-readable materials
- `../examples/catalog/catalog.draft.json` — candidate domain catalog; nothing enabled or production-approved.
- `../examples/schemas/catalog.schema.json` — example JSON schema.
- `../examples/tests/pure-rule-vectors.json` — expected pure behavior.
- `../examples/tests/invalid-case-mutations.json` — intentionally invalid catalog mutations.
- `../examples/contracts/reference.ts` — TypeScript reference functions.
- `../examples/contracts/api-examples.json` — sample event/HTTP envelopes.
- `../examples/sql/schema_draft.sql` — illustrative, not a deployable migration.
- `../tools/validate_batch18.py` — Python validator using `jsonschema` for full schema checks.

## Start implementation
1. Read the first six chapters and the implementation blueprint.
2. Pin content and rules versions, prove fixtures and agree on event boundaries.
3. Build a small feature-gated integration slice with accessible fallback.
4. Run negative authorization and replay tests, then owner-directed visual/audio/gameplay acceptance.
5. No engineer self-merges; owner approval required for main/production promotion.

**Next batch/dependency:** 19 — Security and game integrity.
