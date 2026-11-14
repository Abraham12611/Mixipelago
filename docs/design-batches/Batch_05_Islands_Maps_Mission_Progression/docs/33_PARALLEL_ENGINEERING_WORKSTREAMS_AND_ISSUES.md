# 33 — Parallel Engineering Workstreams and Proposed Issue Backlog

## Coordination
Use distinct package ownership; integrate against typed contracts. Engineers open scoped branches and PRs to `develop`, post validation evidence and handoff notes. **Engineers do not merge their own PRs**; coordinator reviews merges. Promotion to `main` requires explicit owner approval. All manual UI/feel testing is assigned to owner.

## Workstreams and proposed tickets
| ID | Owner lane | Ticket / deliverable | Dependencies | Release |
|---|---|---|---|---|
| B5-01 | Domain | Graph/node/edge TypeScript contracts and schema | Batch 4 IDs | v0.2.0 |
| B5-02 | Domain | Unlock DSL pure evaluator and reason codes | 01 | v0.2.0 |
| B5-03 | Domain | Dependency DAG/topology validator | 01–02 | v0.2.0 |
| B5-04 | Domain | Projection + recommended-next-node helper | 02–03 | v0.2.0 |
| B5-05 | Content | Two-node published starter graph | 01 | v0.2.0 |
| B5-06 | Content | Cove district and branch design cards | 01 | v0.2.x |
| B5-07 | Content | Curated new mission fixtures with golden replays | Batch 4 proof | v0.2.x |
| B5-08 | Rendering | Phaser WorldMapScene scaffold | 01 | v0.2.0 |
| B5-09 | Rendering | Camera pan/zoom, touch and mouse hit tests | 08 | v0.2.0 |
| B5-10 | Rendering | Node/route drawing and unlock state skins | 04,08 | v0.2.0 |
| B5-11 | UI | Mobile mission detail bottom sheet | 01 | v0.2.0 |
| B5-12 | UI | Desktop mission side panel and keyboard nav | 01 | v0.2.0 |
| B5-13 | UI | Accessible mission list and lock reasons | 02,04 | v0.2.0 |
| B5-14 | UI | Results → Map/Replay/Next handoff | Batch4 adapter | v0.2.0 |
| B5-15 | Persistence | Preview progress migration/upsert | 04 | v0.2.0 |
| B5-16 | Art | First Cove map chunks and node marker atlas | Art spec | v0.2.0 |
| B5-17 | Art | Island/route unlock transition states | 16 | v0.2.1 |
| B5-18 | Content tooling | Graph JSON validator and CLI gates | 01–03 | v0.2.0 |
| B5-19 | QA | Golden rule vectors, error fixtures, CI integration | 02–04 | v0.2.0 |
| B5-20 | Performance | Chunk loading and mobile memory instrumentation | 08,16 | v0.2.0 |
| B5-21 | Content | Optional route + hidden discovery teaser | 06–07 | v0.2.1 |
| B5-22 | Content | Checkpoint and gateway prototype | 06 | v0.2.1 |
| B5-23 | Tooling | Dev map-lab graph preview/editor | 01,08 | v0.2.1 |
| B5-24 | Backend | Auth-backed progress + RLS implementation | Batches 6/18 | future |
| B5-25 | Backend | Idempotent treasure/reward service | 24 + economy | future |
| B5-26 | Ops | Feature gate, CDN manifest + rollback pipeline | 18 | v0.2.0 |
| B5-27 | Analytics | Map funnel and error instrumentation | UI + domain | v0.2.0 |
| B5-28 | QA | Owner manual test checklist/cross-device matrix | all core | v0.2.0 |

## Parallel lane plan
Domain engineer owns 01–04 and exposes stable interfaces. Rendering team can build 08–10 against sample projections. UI team can build 11–14 against fixture cards. Content team authors 05–07 independently, conditioned on Batch 4 replay verification. QA/CI team develops 18–19 alongside them. Backend trusted progress is intentionally later, not forced into the first map UI.

## PR evidence contract
Every PR: scope, changed files, typed contract changes, tests run, screenshots or video if visual, known gaps, rollback notes, and explicit claim of whether a human owner test remains pending. Each ticket gets an owner, reviewer, dependency labels and Done criteria in issue tracker.

## Critical dependency path
`B5-01 → B5-02/B5-03 → B5-04 → B5-10/B5-14/B5-15 → integrated map → owner QA → release`. Artist/content/QA work can run alongside this path. Do not put every available agent on the same shared scene file.
