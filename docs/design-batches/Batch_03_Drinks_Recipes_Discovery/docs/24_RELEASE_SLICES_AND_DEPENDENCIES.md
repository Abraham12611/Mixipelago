# 24 — Incremental Release Strategy, Version Scope and Dependencies

## Version nomenclature

Use SemVer-inspired pre-1.0 cadence: `v0.1.0` playable alpha, `v0.1.1` first polish, `v0.1.2` next maintenance/polish, `v0.2.0` campaign expansion. During `0.x`, minor versions may introduce breaking *internal* changes but public persisted/replay contracts still require migration and pinned versions. App version, physics version, catalog version and save version are independent.

## Alpha v0.1.0 — target 72 hours if team capacity supports it

Deliver real physics-based shots, two identical objects merging, eight distinct tier IDs/icons (placeholder art allowed), one curated service mission, two visible customer orders, one next preview, score, preview coins, restart/win/loss, input for mobile+desktop, basic SFX and local save. **Do not** build pantry, rarity ownership, recipe branches, albums or account-linked mastery. Critical tests DRK-001..018 apply as feasible; all core functional tests must pass. Any unfinished capability is clearly deferred rather than simulated as working.

## v0.1.1 — first-week stabilization

Polish collision art, animation and sound hierarchy, recipe progression strip, tutorial hints, accessibility labels, asset loading/fallback, responsive UI, error recovery and mission seed proofs. Expand to a few authored missions only after manual feel approval. Keep the same logical eight-tier chain. Build a minimal catalog validation script and debug recipe/tier inspector.

## v0.1.2 — quality and content iteration

Tuning based on owner playtests, curated sequence balance, replay export/debug tools, more controlled stages, first draft recipe-card UI as noninteractive/future-gated, performance improvements. No trusted economy until its backend validation requirements are ready.

## v0.2.0+ — campaign and controlled feature growth

Introduce first island graph and progression (Batch 5). Decide whether a local recipe journal showing seen tiers is appropriate without promising persistent trusted ownership. Server-based identities/economy when workstreams and security allow; explicit migration policy prevents client coin import.

## v0.3.0+ — economy integration (proposed)

Shop upgrades and coin sinks require trusted wallet. Recipe collections might be introduced as cosmetics but should not increase collision power. Scope with Batch 6 and server data contracts.

## Later minor releases — branching recipes and discovery

Recipe lab, additional drink families, hidden discovery, ingredient inventory, skin rarity and drink mastery each require explicit specs, source-of-truth backend, UI onboarding, content studio validation, replays and ranked eligibility. Do not infer that every listed feature must ship in one release or by a fixed calendar date.

## Dependency order

Contracts/catalog -> resolver -> simulation adapter -> reducer/scoring/orders -> rendering/audio -> UI/tutorial -> fixtures/replay tests -> trusted persistence and unlocks -> content authoring at scale -> collection/mastery/branching discovery.

## Release gates

For each version: build passes; schema and fixture lint; no duplicate rewards; game on representative desktop/mobile; owner manual UI/feel approval; asset licensing checked; rollback plan verified; updated docs/changelog; explicit owner approval for main promotion. No fabricated evidence of completed tasks.

## Coordinated work policy

Engineers may open PRs to feature branches and `develop` as authorized by coordinator; don't self-merge into `main` without explicit owner approval. Preserve versioned content contracts and link to the exact fixture tests changed by PR.
