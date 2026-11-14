# Batch 15 — Complete UI/UX & Design System

**Status:** design and engineering pack · 2026-11-14 · not an implemented feature.

## Product promise
An original, polished tropical 2.5D game interface that stays calm, readable and fast from 320px mobile portrait to desktop landscape, with consistent components and accessible interactions.

## Source-of-truth boundaries
- Batch 02 alone owns fixed-step Rapier physics, collision/merge arbitration, and immutable simulation outcome semantics. No new feature writes physical contacts or awards rewards from visual effects.
- Batch 03 owns the eight-tier alpha ladder and newly merged drink auto-serving to oldest compatible active order; Batch 04 owns mission goals, stars and win/loss state.
- Batch 05 owns campaign graph visibility/unlocks; Batch 06 owns wallet and financial ledger; Batch 07 owns XP/skills; Batch 08 owns reward/collectible entitlements; Batch 09 owns customer/relationship facts while shop reputation settlement remains under Batch 06.
- Client previews and unverified sessions are not currency, XP, competitive score, badge provenance, or trusted activity evidence. All durable grants derive from unique verified receipts.
- Ranked play freezes the physics/scoring/content/seed profile and disables non-normalized world, shop, skill, story, social and cosmetic advantages.
- Every stage is a proposal, not a claim of implementation. Manual browser and gameplay acceptance belongs to the owner. Engineers open PRs and do not self-merge.

**This batch specifically owns:** Information architecture, token system, UI component API, responsive design, motion, accessibility, app page states and screen-to-domain contracts.

**External integrations:** Batch 01 React/Phaser boundary; Batch 02 board; Batch 03 drinks; Batch 04 missions; Batch 05 map; Batches 06–14 screens and projections; Batch 16 art production.

## Documents and reading order
- [01 — Experience principles and non-goals](01_EXPERIENCE_PRINCIPLES_AND_NON_GOALS.md)
- [02 — Information architecture and navigation map](02_INFORMATION_ARCHITECTURE_AND_NAVIGATION_MAP.md)
- [03 — Design tokens and semantic color](03_DESIGN_TOKENS_AND_SEMANTIC_COLOR.md)
- [04 — Typography, density and hierarchy](04_TYPOGRAPHY_DENSITY_AND_HIERARCHY.md)
- [05 — Layout grid, breakpoints and safe areas](05_LAYOUT_GRID_BREAKPOINTS_AND_SAFE_AREAS.md)
- [06 — GameShell, React and Phaser boundary](06_GAMESHELL_REACT_AND_PHASER_BOUNDARY.md)
- [07 — Title screen and first launch](07_TITLE_SCREEN_AND_FIRST_LAUNCH.md)
- [08 — Gameplay HUD and board framing](08_GAMEPLAY_HUD_AND_BOARD_FRAMING.md)
- [09 — Order cards, queue and serving feedback](09_ORDER_CARDS_QUEUE_AND_SERVING_FEEDBACK.md)
- [10 — Aiming, gestures and pointer affordances](10_AIMING_GESTURES_AND_POINTER_AFFORDANCES.md)
- [11 — Gameplay overlays, pause and results](11_GAMEPLAY_OVERLAYS_PAUSE_AND_RESULTS.md)
- [12 — Map, islands and mission selection](12_MAP_ISLANDS_AND_MISSION_SELECTION.md)
- [13 — Shop hub, upgrades and economy trust](13_SHOP_HUB_UPGRADES_AND_ECONOMY_TRUST.md)
- [14 — Skills and player growth interfaces](14_SKILLS_AND_PLAYER_GROWTH_INTERFACES.md)
- [15 — Rewards, albums and cosmetic inventory](15_REWARDS_ALBUMS_AND_COSMETIC_INVENTORY.md)
- [16 — Customers, portraits and shop reputation](16_CUSTOMERS_PORTRAITS_AND_SHOP_REPUTATION.md)
- [17 — World conditions, story and event screens](17_WORLD_CONDITIONS_STORY_AND_EVENT_SCREENS.md)
- [18 — Leaderboards, rankings and competition UX](18_LEADERBOARDS_RANKINGS_AND_COMPETITION_UX.md)
- [19 — Friends, crews and social safety UX](19_FRIENDS_CREWS_AND_SOCIAL_SAFETY_UX.md)
- [20 — Settings, help and accessibility hub](20_SETTINGS_HELP_AND_ACCESSIBILITY_HUB.md)
- [21 — Component library and interaction variants](21_COMPONENT_LIBRARY_AND_INTERACTION_VARIANTS.md)
- [22 — Motion, transitions, game feel and feedback](22_MOTION_TRANSITIONS_GAME_FEEL_AND_FEEDBACK.md)
- [23 — Art handoff and 2.5D production grammar](23_ART_HANDOFF_AND_2_5D_PRODUCTION_GRAMMAR.md)
- [24 — Localization, text overflow and culture](24_LOCALIZATION_TEXT_OVERFLOW_AND_CULTURE.md)
- [25 — Accessibility WCAG and motor control](25_ACCESSIBILITY_WCAG_AND_MOTOR_CONTROL.md)
- [26 — Loading, errors, offline and reconnect states](26_LOADING_ERRORS_OFFLINE_AND_RECONNECT_STATES.md)
- [27 — Frontend architecture, design tokens and QA harness](27_FRONTEND_ARCHITECTURE_DESIGN_TOKENS_AND_QA_HARNESS.md)
- [28 — Design system governance and collaboration](28_DESIGN_SYSTEM_GOVERNANCE_AND_COLLABORATION.md)
- [29 — Release slices and implementation backlog](29_RELEASE_SLICES_AND_IMPLEMENTATION_BACKLOG.md)
- [30 — Requirement traceability, ADR and glossary](30_REQUIREMENT_TRACEABILITY_ADR_AND_GLOSSARY.md)

## Supporting machine-readable files
- `../examples/catalog/catalog.draft.json` — feature-gated sample definitions, never production-approved.
- `../examples/schemas/catalog.schema.json` — strict JSON schema for the sample catalog.
- `../examples/tests/pure-rule-vectors.json` — expected pure-rule behavior.
- `../examples/tests/invalid-case-mutations.json` — intentionally invalid content mutation cases.
- `../examples/contracts/api-examples.json` — endpoint and event shapes; not deployed routes.
- `../examples/contracts/domain-reference.ts` — typed rule reference; not integrated runtime code.
- `../examples/sql/schema_draft.sql` — illustrative PostgreSQL design, NOT an approved migration.
- `../tools/validate_batch15.py` — local static validator (requires `jsonschema`).

## Target release policy
Foundational tokens, responsive gameplay shell and core routes affect v0.1.x immediately; campaign/shop/profile views rollout with their systems; social, events and live interfaces are feature-gated until owned backends work.

## Engineer order
1. Establish tokens, text hierarchy and component contract
2. Ship title/play/help/settings/pause/results with Phaser boundary
3. Build responsive map, shop, progression and collection slices with their gates
4. Add leaderboard/events/social pages only with real backend projections
5. Maintain accessibility, screen snapshots and owner manual approval with every slice

## Acceptance not implied
Schema, fixture and documentation validation do not prove actual game physics solvability, performance, user delight, secure production APIs, compliance or manual UI approval. Those are separate implementation gates.

## Companion document references
- `Batch 01 / docs/03_SITEMAP_AND_UX.md`
- `Batch 01 / docs/28_INTEGRATION_CONTRACTS.md`
- `Batch 02 / docs/18_PERFORMANCE_MOBILE_AND_ACCESSIBILITY.md`
