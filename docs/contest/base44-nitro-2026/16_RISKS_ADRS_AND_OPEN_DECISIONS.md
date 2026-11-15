# 16 — Risk Register, Architecture Decisions and Open Questions

## High-impact risk register

| Risk | Likelihood/impact | Trigger | Mitigation / owner |
|---|---|---|---|
| Base44 eligibility interpretation | Unknown / critical | Platform only hosts iframe or imports old game | New app inside Base44, preserve edit history, written organizer clarification |
| Pre-existing-project/reskin concern | Medium / critical | Reuse of old source-game sprites/structure or project history before Nov 5 | Original expression, new implementation, provenance documentation |
| Phaser/Rapier incompatibility | Medium / high | WASM/import/WebGL failures on Base44 public site | 48h feasibility spike and simple Canvas fallback |
| Too many planned missions | High / high | 12 draft nodes, fewer valid solutions | 8 minimum polished, hide unpublished, cap scope |
| Mobile gesture errors | Medium / high | Touch scroll, lost pointer, safe-area clipping | Real device owner testing early |
| Unlicensed assets | Medium / critical | Missing music/font/AI usage rights | Provenance review, replace suspect assets |
| Guest save corruption | Medium / medium | localStorage blocked/version changed | Validate/migrate, RAM fallback, explicit reset |
| Deadline/hosting instability | Medium / critical | Base44 publish fails or private URL | Publish early, stable release/rollback, no custom domain |
| Competition vote abuse | Low/critical | Community asks for incentivized campaigns | Prohibit incentives/exchanges, moderate outreach |
| Solo reviewer bottleneck | Medium/high | Too many UI PRs await owner | Batch manual tests into meaningful milestones; no self-merges |
| Feature bloat | High/high | Backend/store/multiplayer creeps into MVP | Strict scope feature matrix and kill criteria |

## Proposed ADRs

- **ADR-CE-001:** New Base44 project created within contest period; separate edition codebase from long-term Mixipelago plans.
- **ADR-CE-002:** Frontend guest-only with local save; no auth, paid features or real-money purchases.
- **ADR-CE-003:** Reuse *rule intent* of eight-tier drink ladder, **not** old game assets/code without originality/eligibility review.
- **ADR-CE-004:** Phaser + Rapier only after proof on Base44; Canvas fallback allowed with test updates.
- **ADR-CE-005:** Contest release begins at 8 finished missions, targets 12; map shows published nodes only.
- **ADR-CE-006:** Local score/stars and preview currency have **zero real-world/trusted value**.
- **ADR-CE-007:** One festival visual/challenge layer optional; no live services.
- **ADR-CE-008:** No global ranking without verified backend; not on critical path.
- **ADR-CE-009:** Archive approved Base44 build and hold freeze during judging.
- **ADR-CE-010:** Preserve all manual UI/playtesting for owner, engineers only automate.

## Questions requiring owner/organizer decisions

1. Will the organizers accept a new Base44 app with locally developed Phaser/Rapier engine connected using CLI/GitHub? **Do not assume**.
2. Does the pre-existing game idea and prior design docs count as a prohibited pre-existing project? Clearly describe dates/historical facts in organizer inquiry.
3. Which person is entrant/team representative and who owns rights to contributions? Private decision, not stored here.
4. Is a free earned-coin **purchase** UI acceptable in an entry that must be free in full? Conservative plan disables shop purchase UI, adds decorative rewards automatically.
5. Is Base44's current public access mode compatible with anonymous save/play? Verify in published app.
6. Should festival finale be one extra level or a theme applied to final mission?
7. Which device set will owner actually validate?
8. What remains enabled if the app cannot sustain high frame rate on a low-end phone?

## Unknown ≠ approved

Mark unresolved fields as **TBD**, not "yes". Never present an architecture option, proposed endpoint or prize eligibility claim as a guaranteed capability.
