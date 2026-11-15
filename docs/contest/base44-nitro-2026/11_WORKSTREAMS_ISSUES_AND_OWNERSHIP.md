# 11 — Parallel Engineering Workstreams and Issue Backlog

## Coordination

These are **proposed GitHub tickets**, not issues automatically created. Coordinator assigns owners, engineers create branches/PRs with scope-limited changes, and **do not self-merge**. Owners perform manual UI/gameplay tests. Keep the 21-batch game roadmap unchanged.

## Critical path tickets

| Ticket | Workstream | Deliverable | Dependencies |
|---|---|---|---|
| CE-01 | Platform | New Base44 project created during contest, creation/history evidence | None |
| CE-02 | Platform | Public Base44 URL guest-play access and in-app game integration spike | CE-01 |
| CE-03 | Core | Pure engine contracts / event ordering / score/order unit tests | CE-02 |
| CE-04 | Physics | Launcher + same-tier collision/merge + fixed step | CE-02/03 |
| CE-05 | Art | Original style board, drink atlas, collision-aligned sprites | CE-01 |
| CE-06 | UI | Home/tutorial/gameplay responsive shell | CE-02 |
| CE-07 | Gameplay | Two-order auto-serving + terminal win/loss | CE-03/04 |
| CE-08 | Content | 12 draft mission fixtures + feasibility notes | CE-07 |
| CE-09 | Campaign | Playable missions only; guest map/progress | CE-08 |
| CE-10 | Audio | Original SFX/music, mute, browser unlocking | CE-04/05 |
| CE-11 | QA | Automated regression and asset/licence validation | CE-03 onward |
| CE-12 | Release | Base44 publish + cold browser access + rollback | CE-02 |
| CE-13 | Submission | Proof-of-build/rights/eligibility package and manual form | CE-12/QA |
| CE-14 | Community | Launchpad listing, authentic promotion, valid voting policy | CE-13 |

## Optional independent tickets

- CE-15: festival finale design and FX (**only after** 8–12 proven levels).
- CE-16: accessibility/keyboard/reduced-motion polish.
- CE-17: local best score + stars by score-profile version.
- CE-18: marketing cover and 30s authentic gameplay clip.
- CE-19: cross-device layout hardening.
- CE-20: post-submission uptime checks and freeze runbook.
- CE-21: organizer clarification email about Base44 custom engine.
- CE-22: IP provenance register and contributor-rights audit.

## Workstream partition

- **Platform/infra (1–2 engineers)**: Base44 proof, hosting, asset pipeline, CI.
- **Core gameplay (2–3)**: pure reducers, physics, orders and test vectors.
- **Content/balance (1–2)**: level authoring and solver fixtures; no art/code edits to unrelated systems.
- **Art/audio (1–3)**: artwork original masters, assets, icons and SFX, reviewed by owner.
- **UI/accessibility (1–2)**: responsive shell/hud/map/results.
- **QA/release (1–2)**: automated runs, smoke matrix, owner test requests, submission evidence.

No need to staff every workstream simultaneously. Avoid 20 parallel edits into the same Base44 project; define source ownership and stable integration branches.

## PR template

- Ticket ID and scoped files changed.
- Requirements/acceptance checklist.
- Screenshots/videos are **proposed UI evidence** until owner manually approves.
- Automated tests with logs and fixed seed.
- Risks / docs changes / feature flags.
- Base44 impact: prompt/edit history, sync direction, build URL.
- Asset provenance additions/changes.
- Explicit: **manual owner testing pending/passed**.
- Engineers shall not merge their own PRs.

## Release governance

A dedicated **contest branch/app**, not production feature toggles added opportunistically to mainline Mixipelago. Base44 sync ownership and conflict resolution must be agreed upon up front. No engineer should overwrite the Base44-generated project from an outdated local checkout.
