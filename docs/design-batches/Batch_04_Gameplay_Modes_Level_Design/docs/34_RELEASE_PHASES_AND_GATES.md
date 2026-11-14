# 34 — Incremental Release Plan, Dependencies and Feature Gates

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Terminology
Use a SemVer-inspired `0.x` development series: patch for compatible polish (`v0.1.1`, `.2`), minor for feature additions (`v0.2.0`), and `v1.0.0` for general availability once quality/retention justify. App, physics, modeRules, scoring, mission and content catalog versions are separate and pinned.

## Proposed releases
| Release | Deliverables from Batch 4 | Hold until |
|---|---|---|
| `v0.1.0` | One Classic Service mission; two visible orders; goal counter; basic scoring; one win/loss/retry; responsive HUD | verified actual playable win path, physics, owner review |
| `v0.1.1` | More visible feedback; clearer pause/retry; collision/order test coverage; performance fixes | no duplicate reward, device feel passes |
| `v0.1.2` | 3–10 authored Classic missions; simple star thresholds and JSON validation; debug inspector | each authored mission has recorded winning run |
| `v0.2.0` | First island graph (Batch5), Precision/Score Attack initial mode if ready, rich level progress | new modes pass feasibility tests |
| `v0.3.0` | Trusted shop economy integration (Batch6), not merely previews | verified session → wallet pipeline |
| `v0.4.x` | Player profile/skills integration (Batch7), all ranked modifiers disabled | auth/save integrity |
| `v0.5.x` | Verified leaderboards/friends challenge foundation (Batch13) | replay verifier and fair ranked config |
| later minors | Rush Hour, Survival, VIP, Endless, Festival | each dedicated QA/release gate |

## 72-hour alpha plan (if existing foundation/team available)
**Day 1:** pin mission fixture and catalogs; implement mode registry, objective reducer and scoring tests; connect Service Policy to live physics session; playable basic run on desktop.
**Day 2:** mobile portrait aiming, customer display, win/loss/retry UI; validate serving priority; target baseline golden test; internal staging deployment.
**Day 3:** owner manual UI/feel test; fix critical blockers; stabilize content loading and error handling; smoke tests; cut pre-release `v0.1.0-alpha.1` then tag `v0.1.0` only if gates pass.
If physics itself isn't built, 72 hours is a target contingent on team capacity, not a guarantee; ship a smaller honest alpha rather than fake systems.

## Release checklist
- Every live mode supported by deployed client and backend profile.
- No unsupported future mode exposed.
- Mission schema + semantic validation pass; golden winning replay captured for all gated authored missions.
- Terminal outcome exactly once; no duplicate score/order/coins.
- Pauses and tab hiding safe; no time exploit in active clocks.
- Real device checks: small phone portrait, larger phone, desktop pointer, keyboard optional.
- Owner manually approves interface/game feel; coordinator approves merge to `develop`, owner approves promotion to `main`.
- Changelog, rollback flag, and content manifest version frozen; monitor errors/retention post release.

## Rollback
Disable new mode via flag, revert active content pointer without deleting published artifacts, preserve run/version compatibility, and stop new verified reward claims if integrity bug appears. Do not retroactively delete legitimate player achievements without a documented incident policy.
