# Batch 12 — Events, Festivals & Live World Activities

**Status:** design and engineering pack · 2026-11-14 · not an implemented feature.

## Product promise
Optional festivals, seasonal challenges and live community moments that refresh the tropical world without exploiting missed days or bypassing score verification.

## Source-of-truth boundaries
- Batch 02 alone owns fixed-step Rapier physics, collision/merge arbitration, and immutable simulation outcome semantics. No new feature writes physical contacts or awards rewards from visual effects.
- Batch 03 owns the eight-tier alpha ladder and newly merged drink auto-serving to oldest compatible active order; Batch 04 owns mission goals, stars and win/loss state.
- Batch 05 owns campaign graph visibility/unlocks; Batch 06 owns wallet and financial ledger; Batch 07 owns XP/skills; Batch 08 owns reward/collectible entitlements; Batch 09 owns customer/relationship facts while shop reputation settlement remains under Batch 06.
- Client previews and unverified sessions are not currency, XP, competitive score, badge provenance, or trusted activity evidence. All durable grants derive from unique verified receipts.
- Ranked play freezes the physics/scoring/content/seed profile and disables non-normalized world, shop, skill, story, social and cosmetic advantages.
- Every stage is a proposal, not a claim of implementation. Manual browser and gameplay acceptance belongs to the owner. Engineers open PRs and do not self-merge.

**This batch specifically owns:** Event calendar editions, schedule semantics, activity enrollment, eligibility, participation projections and event orchestration.

**External integrations:** Batch 10 weather and world conditions; Batch 11 story quests; Batch 04 missions; Batch 06/08 rewards; Batch 13 tournament rankings; Batch 14 crews.

## Documents and reading order
- [01 — Event product scope and fairness principles](01_EVENT_PRODUCT_SCOPE_AND_FAIRNESS_PRINCIPLES.md)
- [02 — Event calendar, UTC windows and time zones](02_EVENT_CALENDAR_UTC_WINDOWS_AND_TIME_ZONES.md)
- [03 — Event types and capability matrix](03_EVENT_TYPES_AND_CAPABILITY_MATRIX.md)
- [04 — Event state machine and publication lifecycle](04_EVENT_STATE_MACHINE_AND_PUBLICATION_LIFECYCLE.md)
- [05 — Festival worlds and cosmetic transformations](05_FESTIVAL_WORLDS_AND_COSMETIC_TRANSFORMATIONS.md)
- [06 — Festival service mission rules](06_FESTIVAL_SERVICE_MISSION_RULES.md)
- [07 — Community goals and aggregate milestones](07_COMMUNITY_GOALS_AND_AGGREGATE_MILESTONES.md)
- [08 — Seasonal quests and event task boards](08_SEASONAL_QUESTS_AND_EVENT_TASK_BOARDS.md)
- [09 — Seasonal collectibles and souvenirs](09_SEASONAL_COLLECTIBLES_AND_SOUVENIRS.md)
- [10 — Limited-time economy and reward budgets](10_LIMITED_TIME_ECONOMY_AND_REWARD_BUDGETS.md)
- [11 — Weather, dynamic incidents and event coordination](11_WEATHER_DYNAMIC_INCIDENTS_AND_EVENT_COORDINATION.md)
- [12 — Story scenes, guests and named event characters](12_STORY_SCENES_GUESTS_AND_NAMED_EVENT_CHARACTERS.md)
- [13 — Tournaments and ranked event boundaries](13_TOURNAMENTS_AND_RANKED_EVENT_BOUNDARIES.md)
- [14 — Crews, friends and cooperative event scopes](14_CREWS_FRIENDS_AND_COOPERATIVE_EVENT_SCOPES.md)
- [15 — Event registration, eligibility and opt-in](15_EVENT_REGISTRATION_ELIGIBILITY_AND_OPT_IN.md)
- [16 — Notification, reminder and attention policy](16_NOTIFICATION_REMINDER_AND_ATTENTION_POLICY.md)
- [17 — Live event hub UX and navigation](17_LIVE_EVENT_HUB_UX_AND_NAVIGATION.md)
- [18 — Event art, audio and asset streaming](18_EVENT_ART_AUDIO_AND_ASSET_STREAMING.md)
- [19 — Event Content Studio and editorial approval](19_EVENT_CONTENT_STUDIO_AND_EDITORIAL_APPROVAL.md)
- [20 — Scheduling, workers, leases and cache](20_SCHEDULING_WORKERS_LEASES_AND_CACHE.md)
- [21 — Event APIs, domain messages and authorization](21_EVENT_APIS_DOMAIN_MESSAGES_AND_AUTHORIZATION.md)
- [22 — Database, privacy and immutable event editions](22_DATABASE_PRIVACY_AND_IMMUTABLE_EVENT_EDITIONS.md)
- [23 — Security, fraud and legal/compliance overview](23_SECURITY_FRAUD_AND_LEGAL_COMPLIANCE_OVERVIEW.md)
- [24 — QA scenario atlas and simulated calendar](24_QA_SCENARIO_ATLAS_AND_SIMULATED_CALENDAR.md)
- [25 — Event analytics and live operations dashboard](25_EVENT_ANALYTICS_AND_LIVE_OPERATIONS_DASHBOARD.md)
- [26 — Release slices, workstreams and rollback](26_RELEASE_SLICES_WORKSTREAMS_AND_ROLLBACK.md)
- [27 — ADR, requirements, glossary and source links](27_ADR_REQUIREMENTS_GLOSSARY_AND_SOURCE_LINKS.md)

## Supporting machine-readable files
- `../examples/catalog/catalog.draft.json` — feature-gated sample definitions, never production-approved.
- `../examples/schemas/catalog.schema.json` — strict JSON schema for the sample catalog.
- `../examples/tests/pure-rule-vectors.json` — expected pure-rule behavior.
- `../examples/tests/invalid-case-mutations.json` — intentionally invalid content mutation cases.
- `../examples/contracts/api-examples.json` — endpoint and event shapes; not deployed routes.
- `../examples/contracts/domain-reference.ts` — typed rule reference; not integrated runtime code.
- `../examples/sql/schema_draft.sql` — illustrative PostgreSQL design, NOT an approved migration.
- `../tools/validate_batch12.py` — local static validator (requires `jsonschema`).

## Target release policy
Candidate first opt-in festival and a single authored event mission after campaign and trusted rewards (v0.6.2); calendar rotation, community goals and seasonal live programs staged later.

## Engineer order
1. Publish event read model and UTC clock fixtures
2. Build event hub, single activity and limited calendar
3. Wire verified contribution to existing mission result
4. Grant one owned cosmetic via Batch 08 trusted entitlement
5. Add archive, cancellation operations and community goals later

## Acceptance not implied
Schema, fixture and documentation validation do not prove actual game physics solvability, performance, user delight, secure production APIs, compliance or manual UI approval. Those are separate implementation gates.

## Companion document references
- `Batch 01 / docs/19_ANALYTICS_AND_LIVEOPS.md`
- `Batch 08 / docs/06_06_ATOMIC_SETTLEMENT_IDEMPOTENCY_AND_OUTBOX.md`
- `Batch 10 / docs/00_INDEX_AND_README.md`
