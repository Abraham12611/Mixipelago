# 24 — Requirements Traceability, Definition of Done, Release Evidence

## Purpose

Every core physical behavior must map to a public contract, a measurable test, an owner/team and the target release. This file is the bridge between the specification and engineering issues. Keep issue IDs/PR URLs updated once the repo exists; placeholders below are not claims that issues were created.

## Requirement-to-test matrix

| Requirement ID | Requirement | Spec | Test(s) | Release | Owner |
|---|---|---|---|---|---|
| B2-R001 | Table world uses logical coordinates | 02 | viewport roundtrip/INP-010 | v0.1.0 | UI/Input |
| B2-R002 | Rapier fixed 60Hz simulation | 03,05 | PHY-001, PHY-024 | v0.1.0 | Physics |
| B2-R003 | Responsive mouse/touch aim | 04 | INP-001..007 | v0.1.0 | Input |
| B2-R004 | Keyboard accessible fire | 04,18 | INP-008..009 | v0.1.0 | UI/Input |
| B2-R005 | Fixed impulse + valid launch cone | 04,08 | PHY-001,022,028 | v0.1.0 | Physics/Input |
| B2-R006 | Distinct glass/nonmerge collisions | 03,06 | PHY-002..005 | v0.1.0 | Physics |
| B2-R007 | Exactly-once same-tier merges | 07 | PHY-006,009,010 | v0.1.0 | Rules |
| B2-R008 | Max-tier no evolution | 07 | PHY-008 | v0.1.0 | Rules |
| B2-R009 | Chain merge descendant rule | 07 | PHY-011 | v0.1.0 | Rules |
| B2-R010 | Two-customer auto-serve | 07,08 | PHY-012 | v0.1.0 | Game core |
| B2-R011 | Seeded preview queue | 08 | queue seed test | v0.1.0 | Game core |
| B2-R012 | Nonphysical danger line with grace | 09 | PHY-015..018 | v0.1.0 | Game core |
| B2-R013 | Pause, resume, restart, dispose | 05,10 | PHY-019..023 | v0.1.0 | Integration |
| B2-R014 | 2.5D glass sprites track physics | 02,13 | visual/physics alignment | v0.1.0 | Renderer |
| B2-R015 | Collision/merge SFX optional | 14 | PHY-026, audio tests | v0.1.0 | Audio |
| B2-R016 | Event schema stable | 11 | TS/Zod contract | v0.1.0 | Contracts |
| B2-R017 | Basic headless physics fixtures | 15,19 | PHY-001..023 | v0.1.0 | QA |
| B2-R018 | Physics lab preset export | 15 | lab integration/owner test | v0.1.1 | Physics/QA |
| B2-R019 | Replay record and hashes | 17 | PHY-024,025 | v0.1.1 or later | Security/Physics |
| B2-R020 | Quality profiles cosmetic-only | 18 | low/high same physics result | v0.1.1 | Renderer |
| B2-R021 | No fake online rewards | 17,21 | API/trust check | v0.1.0 | Backend/Security |
| B2-R022 | Resource cleanup after repeated restart | 05,18 | PHY-023 | v0.1.0 | Integration |

## Definition of Done — individual engineering issue

- Implements a scoped requirement with tests and contract references.
- Does not rewrite unrelated feature modules or game rule semantics.
- Validates/handles bad input and lifecycle/disposal if relevant.
- Includes `pnpm` test command and deterministic fixture where feasible.
- Performance implications considered and measured for hot-path code.
- Any new asset is original/approved with stable asset ID and provenance.
- No server secret or trusted coin balance exposed through client code.
- PR description includes screenshots or clip for visual changes and structured test results.
- Public API/schema changes approved by dependent workstream owners.
- No engineer self-merges contrary to project coordination policy.

## Definition of Done — v0.1.0 playable alpha

1. A player can enter a mission on mobile browser or desktop browser.
2. Table appears with correct world screen transform; input targets map accurately.
3. Player can aim via pointer/touch (and alternate keyboard controls) and launch a drink.
4. Physics glides, visibly deflects on at least one angled nonmatching contact, and does not tunnel through rails at legal speed.
5. Two same-tier drinks create one higher-tier result; chains can occur, with correct score and no duplicate ID use.
6. A generated drink that matches an order is served automatically once; two customer requests shown.
7. Current/next queue, simple goal, score/coins preview and danger warning are understandable.
8. Session win and loss are reachable and trigger correct UI once; retry creates a clean new world.
9. Pause and browser background/resume do not fast-forward active physics.
10. No baseline performance or browser compatibility blocker in target test matrix.
11. Automated required tests pass; owner manual feel and UI tests approved; main merge explicitly authorized.

## Go/no-go evidence

Engineer should provide a short release evidence bundle containing: commit SHA, deployment preview URL, `physicsVersion`, `missionVersion`, test summary, failure list, device/browser notes, 10–30 second reproduction video(s) for shot/merge/chain/danger, memory/restart report and known issues. Owner performs manual UI test based on link and steps. If a blocking issue exists, publish another pre-release build or defer instead of announcing production completion.

## Regression discipline

When the physics preset changes, compare before/after fixture trajectories and replay hashes. A deliberate balance change requires owner signoff and physics version bump. Existing user saves must either retain compatible physics state or migrate/restart safely. Visual-only asset changes must not alter logical state or score.
