# 17 — Engineer Workstreams, Issues, Dependencies and Coordination

## Coordination rules

Product owner approves release gates and all subjective/manual UI tests. Coordinator owns integration and release merges; **engineers must NOT merge their own PRs**. Work in short-lived issue branches, open draft PR early, request contract changes instead of changing shared types unilaterally. Automated CI may run without owner action; manual interaction with the UI should be handed to the user.

## Initial team layout (5 workstreams; scale only if justified)

| Team | Focus | Owns |
|---|---|---|
| A — Physics | Simulation, aiming, merge, debug lab | `packages/physics-rapier`, `packages/game-core` collision modules |
| B — Game UI | Phaser renderer, React layouts, scenes | `apps/web`, `packages/game-renderer`, UI |
| C — Session rules | Drinks, orders, score, mission loader, local save | `game-core` session, `content`, `save-local` |
| D — Art/Audio | Asset catalog, drink visuals, icon packs, audio | `assets`, `asset-pipeline`, audio adapters |
| E — QA/Infra | CI, deployment, analytics, tests, performance | test suites, tooling, workflows |

Shared source files get a named owner; schema changes go through an interface PR reviewed by impacted teams. Avoid 20 agents editing `GameScene.ts` concurrently.

## P0 issue board — create as atomic tasks

| Issue | Owner | Deliverable | Dependency | Acceptance |
|---|---|---|---|---|
| MX-001 | E | pnpm monorepo + CI | None | clean install/build/test |
| MX-002 | B | Next shell + client-only Phaser mount | MX-001 | canvas loads, cleans up |
| MX-003 | A | Rapier WASM world + fixed step | MX-001 | no SSR, stable 60Hz |
| MX-004 | C | Shared contracts/Zod schemas | MX-001 | imported by all packages |
| MX-005 | A | Touch/mouse aim & launch | MX-003/004 | predictable impulse; cancel |
| MX-006 | A | Rigid-body collision + boundaries | MX-003 | angle-dependent response |
| MX-007 | A | Merge arbitration + chain logic | MX-004/006 | exact-once merge tests |
| MX-008 | D | 8 drink sprites + fallback thumbnails | None | coherent original artwork |
| MX-009 | B | Render table, sprites, camera sync | MX-002/003/008 | responsive canvas |
| MX-010 | C | 2 customer orders + score | MX-004/007 | auto-serving, coin tally once |
| MX-011 | C | Session win/fail/danger line | MX-004/010 | terminal state safe |
| MX-012 | B | Portrait mobile gameplay UI | MX-009/010 | readable and touch-friendly |
| MX-013 | B | Desktop landscape gameplay UI | MX-009/010 | usable side panels |
| MX-014 | D | Audio director, SFX/mute | MX-004 | event-controlled and mobile unlock |
| MX-015 | C | Versioned local save/preferences | MX-004 | persists across refresh |
| MX-016 | E | Unit/integration/e2e tests | MX-003–015 | agreed P0 suite green |
| MX-017 | E | Vercel preview + prod pipeline | MX-001/002 | repeatable deploy + rollback |
| MX-018 | B/C | Results/tutorial/help/settings | MX-010/011 | complete app loop |
| MX-019 | E | Device test instructions + profiling | MX-012/013/017 | owner can sign off |
| MX-020 | Coordinator | Final integration and release | All P0 | v0.1.0 tagged with notes |

Optional P1 first-week: MX-021 physics lab presets, MX-022 3–10 missions, MX-023 tutorial polish, MX-024 advanced FX, MX-025 PWA cache, MX-026 settings/graphics presets, MX-027 accessibility regression, MX-028 event analytics, MX-029 initial map teaser, MX-030 Capacitor proof-of-concept.

## Dependency order (critical path)

```
MX-001 → MX-003 → MX-006 → MX-007 → MX-010 → MX-011 → MX-020
         ↘ MX-005 ↗
MX-001 → MX-002 → MX-009 → MX-012/013 → MX-018 → MX-020
MX-004 feeds A/B/C; MX-008 feeds renderer; E works continuously.
```

## Suggested engineering roles

- Coordinator: ADRs, merge/release, reviews, integration arbitration.
- Physics lead: owns simulation contracts and debug tuning.
- Gameplay lead: owns order/score rules and mission goal contracts.
- UI lead: owns responsive components and accessibility.
- Art/audio producer: owns consistent original assets and licenses.
- Test/release lead: owns reproducibility and quality gates.

## Branching and PR rules

Branch format `feat/MX-007-merge-resolver`, `fix/MX-015-save-schema`, `docs/MX-...`. Base on `develop`; engineers open PRs into `develop`, no self-merge. Coordinator reviews/contracts/CI and merges. `main` represents production and must have **explicit owner approval** before any promotion; coordinator performs the release merge/tag.

PR must contain summary, changed contract details, test evidence, screenshots/video for UI changes if available, performance impact, migration notes, owner-manual-test checklist, feature flags and rollback note. Engineer should leave concise unresolved questions in PR comments. Avoid giant PRs spanning several workstreams.

## Integration routine

- Hour 0: approve contracts and file ownership.
- Twice daily: integrate small PRs, run end-to-end suite.
- At each milestone: check dependency graph, actual builds and device reports.
- Release: freeze feature additions, clear P0, request owner manual testing, tag and deploy only after approval.

## What not to delegate simultaneously

Physics engine implementations competing with different coordinate conventions; UI teams inventing different drink catalogs; API and frontend inventing their own events; asset creators changing final filenames without manifest updates; several engineers merging to main. Coordinate shared contracts first.
