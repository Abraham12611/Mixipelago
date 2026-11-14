# 20 — Internal Admin, Level Editor and Content Pipeline

## Strategy

Game content should be authored as data, validated, reviewed and published independently of core engine changes. The first alpha uses local JSON files and CLI validation, **not** a full admin dashboard.

## Tooling staged rollout

### v0.1.0–0.1.1: repository content workflow

- Store tier catalog, order sequences and missions in `content/*`.
- Validate with Zod/JSON schema + custom graph validator.
- Provide content preview/test fixtures, stable IDs, sequential versions.
- Bundle selected missions into web client; CI fails on missing referenced assets or invalid goals.

### v0.2.0: visual mission/content editor

- Tabletop preview with object placements, spawn table, order list, mission rules.
- Adjustable physics preset per mission but limited to certified presets; disallow arbitrary freeform values without designer review.
- Mission difficulty simulator, save draft, validate, preview on local game, publish immutable version.
- Island graph viewer with nodes/edges, prerequisites, cycle detection, locked-path explanations.

### Later: world / shop / event admin

- Shop and skill catalogs, price balance, event definitions, schedule/cooldowns, reward caps, seasonal challenges.
- Audit log and role-based approvals (designer, reviewer, publisher, owner).
- Rollback to last published content version, no silent changes to active ranked levels.

## Content lifecycle

`draft → review → validated → approved → published → deprecated/archived`. The published content is immutable by hash. Editing creates a new version, never changes a prior run's underlying mission. Source file or DB record logs creator, reviewers, timestamp, validation result and parent version.

## Starter CLI requirements

`pnpm content:validate` ensures: unique IDs, correct tier bounds, valid order references, score/reward nonnegative, all asset IDs exist, no impossible prerequisites, no missing route target and no uncapped reward recurrence. `pnpm content:preview <missionId>` launches the relevant mission in dev build. `pnpm content:hash` emits content manifest checksums.

## Balancing and simulation (future)

Scripted test agents with different aim policies to estimate win rate, number of shots, average active time and reward distribution. Do not use synthetic agent results as sole evidence of human enjoyment; owner playtest remains authoritative for subjective quality.

## Admin security

Protect route and underlying APIs with authenticated admin authorization and audit logs. Never rely on hiding links. Generated assets may originate from AI; capture provenance and licensed use. Avoid direct production editing or service-role keys in browser.
