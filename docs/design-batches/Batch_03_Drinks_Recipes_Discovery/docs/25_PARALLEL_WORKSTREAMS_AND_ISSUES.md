# 25 — Team Workstreams, Dependency Graph, PR Ownership and Initial Issues

## Engineering organization

Assign work by package/domain contracts. The number of available engineers does not justify assigning more agents than the dependency graph supports. First agree on the alpha catalog schema and event envelope to avoid incompatible implementations.

## Workstreams

**A — Catalog & pure rules (2 engineers initially):** typed schemas, canonical eight-tier content, simple recipe resolver, score function, content validator. Owns `packages/drink-catalog` and `packages/recipe-rules`.

**B — Simulation integration (2 engineers):** logical `drinkId` mapping, contact->recipe resolver adapter, collision fixture tests, auto-serving priority. Owns `packages/game-core` integration with Batch 2 physics.

**C — Game UI/UX (2 engineers):** evolution strip, order cards, next preview, tier labels, lightweight tutorial, mobile/desktop layout. Owns `apps/web` interface layer without touching physics internals.

**D — Art/audio pipeline (2 artists/engineers):** create approved silhouettes/icons, asset manifest, sound cues, fallback assets, packaging performance. Owns asset pipeline and presentation-only effects.

**E — QA/content tools (1–2 engineers):** test fixture runner, static linter, sample mission queue proof, debug inspector, CI smoke tests, performance measurement.

**F — Future R&D (optional, not critical path):** recipe graph prototype and authoring editor behind feature flags, explicit proposal PRs only, not included in alpha release.

## Candidate issue backlog

| ID | Issue | Depends on | Release |
|---|---|---|---|
| B3-001 | Canonical eight-tier catalog and stable IDs | none | 0.1.0 |
| B3-002 | Zod/JSON schema and catalog validator | B3-001 | 0.1.0 |
| B3-003 | Pure same-tier resolver | B3-001 | 0.1.0 |
| B3-004 | Merge arbitration adapter w/ content IDs | B3-003 + Batch 2 | 0.1.0 |
| B3-005 | Output-tier score and idempotent reducer tests | B3-003 | 0.1.0 |
| B3-006 | Two-order service resolver priority tests | B3-004 | 0.1.0 |
| B3-007 | Eight-tier drink sprites and small icons | Art brief | 0.1.0 |
| B3-008 | Asset manifest loader/fallback | B3-007 | 0.1.0 |
| B3-009 | Mobile/desktop evolution strip | B3-001, B3-007 | 0.1.0 |
| B3-010 | Order card state and transfer FX | B3-006 | 0.1.0 |
| B3-011 | Seeded tutorial fixture with replay proof | B3-004, B3-006 | 0.1.0 |
| B3-012 | Alpha end-to-end test/diagnostics | B3-001..011 | 0.1.0 |
| B3-013 | Art/SFX collision/merge polish | B3-007, B3-004 | 0.1.1 |
| B3-014 | Content balance estimator | B3-002 | 0.1.1 |
| B3-015 | High-contrast accessibility icons | B3-007 | 0.1.1 |
| B3-016 | Recipe Journal wireframes (not live) | 14 | 0.1.2 |
| B3-017 | General recipe graph design spike | 04 | Future |
| B3-018 | Discovery grant and ledger specification | 06, 17 | Future |
| B3-019 | Collection and mastery architecture plan | 07, 08 | Future |
| B3-020 | Admin Content Studio proposal | 19 | Future |

## PR template

`Scope; linked docs/issue; schema changes; behavior changes; content version/physics version impacts; screenshots only if code changes UI; automated tests run; golden fixtures affected; performance impact; known risks; owner manual test instructions; rollback path.` Each PR should be small enough to review, and no branch should change another workstream's contract silently.

## Integration cadence

At start: approve IDs/types, then implement independent units. Midcycle: integrate alpha vertical slice on `develop`; CI runs typecheck, lint, unit/property fixtures and gameplay E2E. Owner plays the actual UI and reports feel issues. Coordinator resolves conflicts and seeks explicit approval before main promotion.

## Definition of engineer done

Not 'code compiles'. It means documented behavior implemented, relevant tests passing, error cases handled, test evidence attached, no copy-rights issues introduced, and feature exposed appropriately to alpha or behind a disabled gate.
