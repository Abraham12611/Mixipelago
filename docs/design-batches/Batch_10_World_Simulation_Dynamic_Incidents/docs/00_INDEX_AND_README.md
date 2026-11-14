# Batch 10 — World Simulation & Dynamic Incidents

**Status:** design and engineering pack · 2026-11-14 · not an implemented feature.

## Product promise
An archipelago that visibly changes over time without turning play into punishment, involuntary debt or nontransparent ranked advantages.

## Source-of-truth boundaries
- Batch 02 alone owns fixed-step Rapier physics, collision/merge arbitration, and immutable simulation outcome semantics. No new feature writes physical contacts or awards rewards from visual effects.
- Batch 03 owns the eight-tier alpha ladder and newly merged drink auto-serving to oldest compatible active order; Batch 04 owns mission goals, stars and win/loss state.
- Batch 05 owns campaign graph visibility/unlocks; Batch 06 owns wallet and financial ledger; Batch 07 owns XP/skills; Batch 08 owns reward/collectible entitlements; Batch 09 owns customer/relationship facts while shop reputation settlement remains under Batch 06.
- Client previews and unverified sessions are not currency, XP, competitive score, badge provenance, or trusted activity evidence. All durable grants derive from unique verified receipts.
- Ranked play freezes the physics/scoring/content/seed profile and disables non-normalized world, shop, skill, story, social and cosmetic advantages.
- Every stage is a proposal, not a claim of implementation. Manual browser and gameplay acceptance belongs to the owner. Engineers open PRs and do not self-merge.

**This batch specifically owns:** World conditions, forecast snapshots, incident eligibility, individual incident lifecycle and player-world chronicle.

**External integrations:** Batch 05 map, Batch 06 wallet/insurance/shops, Batch 09 customer demand, Batch 12 live calendar, Batch 04 gameplay mode rules.

## Documents and reading order
- [01 — Product promise, scope and boundaries](01_PRODUCT_PROMISE_SCOPE_AND_BOUNDARIES.md)
- [02 — World time, clocks, schedules and freeze points](02_WORLD_TIME_CLOCKS_SCHEDULES_AND_FREEZE_POINTS.md)
- [03 — Island biomes and geographic conditions](03_ISLAND_BIOMES_AND_GEOGRAPHIC_CONDITIONS.md)
- [04 — Weather state, forecast and transitions](04_WEATHER_STATE_FORECAST_AND_TRANSITIONS.md)
- [05 — Tourism, crowds and visitor demand](05_TOURISM_CROWDS_AND_VISITOR_DEMAND.md)
- [06 — Supply conditions and price signals](06_SUPPLY_CONDITIONS_AND_PRICE_SIGNALS.md)
- [07 — Incident classification and severity](07_INCIDENT_CLASSIFICATION_AND_SEVERITY.md)
- [08 — Incident finite-state machine](08_INCIDENT_FINITE_STATE_MACHINE.md)
- [09 — Event Director eligibility and cooldown](09_EVENT_DIRECTOR_ELIGIBILITY_AND_COOLDOWN.md)
- [10 — Probability, seed, caps and fairness](10_PROBABILITY_SEED_CAPS_AND_FAIRNESS.md)
- [11 — Shop fire and emergency scenario](11_SHOP_FIRE_AND_EMERGENCY_SCENARIO.md)
- [12 — Repair, resilience and recovery flows](12_REPAIR_RESILIENCE_AND_RECOVERY_FLOWS.md)
- [13 — Insurance, liability and financial authority](13_INSURANCE_LIABILITY_AND_FINANCIAL_AUTHORITY.md)
- [14 — Positive world opportunities](14_POSITIVE_WORLD_OPPORTUNITIES.md)
- [15 — Dynamic challenge and rescue missions](15_DYNAMIC_CHALLENGE_AND_RESCUE_MISSIONS.md)
- [16 — Cross-system world handoffs](16_CROSS_SYSTEM_WORLD_HANDOFFS.md)
- [17 — Offline, missed windows and anti-punishment](17_OFFLINE_MISSED_WINDOWS_AND_ANTI_PUNISHMENT.md)
- [18 — World map, HUD and incident choice UX](18_WORLD_MAP_HUD_AND_INCIDENT_CHOICE_UX.md)
- [19 — World art, sound and animation budgets](19_WORLD_ART_SOUND_AND_ANIMATION_BUDGETS.md)
- [20 — Incident content authoring and moderation](20_INCIDENT_CONTENT_AUTHORING_AND_MODERATION.md)
- [21 — Versioning, snapshots and rollback](21_VERSIONING_SNAPSHOTS_AND_ROLLBACK.md)
- [22 — API, events and authorization](22_API_EVENTS_AND_AUTHORIZATION.md)
- [23 — Persistence, RLS and audit records](23_PERSISTENCE_RLS_AND_AUDIT_RECORDS.md)
- [24 — Scheduled workers, caching and resilience](24_SCHEDULED_WORKERS_CACHING_AND_RESILIENCE.md)
- [25 — Security, abuse and fairness review](25_SECURITY_ABUSE_AND_FAIRNESS_REVIEW.md)
- [26 — QA matrix and simulation fixtures](26_QA_MATRIX_AND_SIMULATION_FIXTURES.md)
- [27 — Analytics, balance and operations](27_ANALYTICS_BALANCE_AND_OPERATIONS.md)
- [28 — Release slices, tickets and sign-off](28_RELEASE_SLICES_TICKETS_AND_SIGN_OFF.md)
- [29 — Traceability, definitions and decisions](29_TRACEABILITY_DEFINITIONS_AND_DECISIONS.md)

## Supporting machine-readable files
- `../examples/catalog/catalog.draft.json` — feature-gated sample definitions, never production-approved.
- `../examples/schemas/catalog.schema.json` — strict JSON schema for the sample catalog.
- `../examples/tests/pure-rule-vectors.json` — expected pure-rule behavior.
- `../examples/tests/invalid-case-mutations.json` — intentionally invalid content mutation cases.
- `../examples/contracts/api-examples.json` — endpoint and event shapes; not deployed routes.
- `../examples/contracts/domain-reference.ts` — typed rule reference; not integrated runtime code.
- `../examples/sql/schema_draft.sql` — illustrative PostgreSQL design, NOT an approved migration.
- `../tools/validate_batch10.py` — local static validator (requires `jsonschema`).

## Target release policy
Preview weather overlays after the first campaign (candidate v0.6.0); authored opt-in incidents and recovery (v0.6.1+); shop-economic world effects only after audited server-ledger integration (v0.7+).

## Engineer order
1. Define immutable world condition read model and kill switch
2. Render harmless condition overlay on map, with reduced motion
3. Introduce authored opt-in offers and idempotent incident choice receipts
4. Integrate verified mission/world consequences through Batch 06 domain
5. Enable operator dashboards, audit, recovery and rollback

## Acceptance not implied
Schema, fixture and documentation validation do not prove actual game physics solvability, performance, user delight, secure production APIs, compliance or manual UI approval. Those are separate implementation gates.

## Companion document references
- `Batch 01 / docs/11_WORLDS_AND_EVENTS_OVERVIEW.md`
- `Batch 05 / docs/15_CONTENT_MANIFESTS_HASHES_AND_ROLLOUT.md`
- `Batch 06 / docs/05_LEDGER_TRANSACTION_IDEMPOTENCY.md`
