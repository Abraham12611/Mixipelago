# 00 — Batch 2 Source of Truth, Scope, and Navigation

## Document authority

This batch **expands rather than silently replaces** Batch 1. The Batch 1 constraints remain: browser-first TypeScript; Phaser 4 renderer and input; Rapier 2D WASM proposed for rigid body physics; React/Next.js app shell; one eight-tier drink ladder; two active customer slots; automatic service upon creation of an eligible output; fixed shot impulse initially; danger line with grace period; short local-only alpha; owner-directed manual UI tests; coordinator controls PR merges; owner approval for main.

If anything here appears to conflict with the earlier pack, consult `22_ADRS_RISKS_AND_OPEN_DECISIONS.md`. The implementation needs an explicit approved decision before a conflicting behavior is shipped. Source code with passing tests becomes the canonical *implemented* contract after the spec is accepted; maintain docs in the same PR.

## Releases versus documentary depth

| Release | Required behavior | Excluded even though documented |
|---|---|---|
| v0.1.0 (~72-hour alpha target) | One tabletop, eight drink tiers, circular bodies, fixed-direction shot impulse, mouse/touch aim, same-tier merge, different-tier collision, basic chains, 2 customers, score and local preview coins, simple win/loss, minimal SFX | Server rank claims, skill bonuses, magnets, complex geometry, 3D runtime, online economy |
| v0.1.1 (~first-week polish) | Better visual/audio feel, pause/reload recovery, input options, debug telemetry, quality modes, curated configs and test hardening | Multiplayer and advanced level generation |
| v0.1.2+ | Selectively enable field-tested techniques: trajectory guide variants, special collision materials, tier footprints, more FX | No feature ships solely because included in documentation |
| v0.2.0+ | Data-driven mission campaign uses same simulation contracts | Island-story depth belongs in later batches |
| Ranked modes (later) | Input records, replay harness, anti-tamper backend, season verification | No claim that a local browser score is trusted |

## Normative language

- **MUST**: acceptance requirement for the scope stated, unless changed by approved ADR.
- **SHOULD**: strongly advised design with engineering latitude and documented alternatives.
- **MAY**: future or experimental behavior, feature-flagged and not automatically in alpha.
- **PROPOSED**: not measured or owner-approved; prototype required.

## System-wide invariants

1. Exactly one physics engine owns glass bodies in a scene; Phaser never applies a second body solver to the same objects.
2. Every shot has a stable ID and is consumed once. Every drink object has a stable ID. A merged object can be consumed only once.
3. All simulation mutations occur at fixed-step boundaries; rendering and audio observe events but never decide scores.
4. Order and score rules are pure and never depend on wall-clock frame count, pixel density or GPU output.
5. No private or precise user location needed for alpha.
6. No unbounded catch-up after hidden-tab suspension.
7. No global scores or valuable inventory awarded from local-only clients.
8. A missing sprite or sound has a graceful fallback, not a logic failure.
9. Session `won` or `lost` is terminal and cannot award multiple times.
10. Every major physics change increments an explicit physics/rules configuration version and regenerates baselines.

## Architecture at a glance

```text
DOM/React HUD                    Phaser renderer + InputController
    |                                      |
    | UI commands/subscriptions            | normalized aim input
    v                                      v
                 GameShell / SessionHost
                          |
                   SimulationCore
                          |
             FixedStep Clock + RapierWorld
                          |
           ContactCollector → MergeResolver
                          |
               typed SimulationEvents
                          |
        SessionReducer / Orders / Scoring
                 |                  |
             React ViewModel      FX/Audio Directors
                 |
           LocalSaveRepository

Future: server receives candidate results and replay records; independently validates before durable rewards.
```

## Workflow dependency graph

`coordinates` → `input conversion` → `launch command` → `physics stepping` → `collision collector` → `merge arbiter` → `session reducer` → `HUD / persistence`. Sprite and sound production can proceed against event/asset contracts without changing the simulation implementation.

## Original screenshot interpretation, not fact

User images suggest a portrait tabletop with a lower launch/danger line, an upcoming drink, two customer requests, an evolution ladder and boosters. The precise collision rules, whether glass sprites physically spin, whether shots have variable force, how merges are chosen in crowded chains, and the exact win/loss formula **cannot be proven from static images**. Batch 2 defines original, testable Mixipelago behavior; it does not claim to have extracted the source game's code.

## Owner checkpoints

- **Gate A:** Select the preferred aim interaction after playing two variants.
- **Gate B:** Approve the glide/collision feel using three recorded physics presets on desktop + mobile.
- **Gate C:** Approve chain merge readability, serving feedback and danger warning.
- **Gate D:** Authorize release to main and production after automated passes and owner manual test.

## Deliverable inventory

Docs 01–29 cover targeted game-feel, geometry, physics, shot input, deterministic simulation, contact pairs, merging, spawn queue, mission boundaries, contracts, code skeletons, VFX, SFX, tuning, difficulty, replay, performance, QA, resilience, delivery tasks, ADRs, references, traceability and fixtures. Keep each connected to an issue/PR. Do not mistake these documents for a finished application.
