# 33 — Parallel Engineering Workstreams, Tickets, Dependencies and Ownership

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Coordination rule
Create small, reviewable PRs on feature branches. Engineers **must not merge their own PRs into `main`**. Coordinator reviews and integrates into `develop`; moving to `main` requires explicit owner approval. All manual UI/UX and gameplay feel tests go to owner; automated QA is engineer-owned. Cross-cutting decisions tracked in ADR log.

## Issue board (proposed; not yet created on GitHub)
| Issue | Owner lane | Deliverable | Prerequisite | Target |
|---|---|---|---|---|
| B4-001 | Domain | Define ModeId / ModePolicy types | Batch2 contracts | v0.1.0 |
| B4-002 | Content | Mission v1 adapter and schema validator | B4-001 | v0.1.0 |
| B4-003 | Domain | Objective reducer `orders_served` | B4-001 | v0.1.0 |
| B4-004 | Domain | Scoring reducer dedupe and pinned table | Batch3 catalog | v0.1.0 |
| B4-005 | Gameplay | Service policy + session terminal ordering | B4-003/004 | v0.1.0 |
| B4-006 | UI | Mission goal, order and result HUD | B4-003/005 | v0.1.0 |
| B4-007 | QA | Service fixture and win/loss tests | B4-005 | v0.1.0 |
| B4-008 | Domain | Final-shot resolving state | B4-005 | v0.1.1 |
| B4-009 | Content | 3–10 curated service missions + solution traces | B4-007 | v0.1.1+ |
| B4-010 | QA | Schema+cross-field CI gate | B4-002 | v0.1.1 |
| B4-011 | DevTools | Mission lab/import/export | B4-002 | v0.1.2 |
| B4-012 | Domain | Star criteria and best-result monotonicity | B4-003 | v0.1.2 |
| B4-013 | Domain | Precision policy + shot budget | B4-008 | v0.2+ |
| B4-014 | Domain | Score Attack / combo ancestry | Batch2 chain events | v0.2+ |
| B4-015 | UI | Mode-specific goals and shot HUD | B4-013/014 | v0.2+ |
| B4-016 | Content | Mission solver harness + golden proof receipts | B4-009 | v0.2+ |
| B4-017 | Domain | Active-tick clock | B4-005 | future |
| B4-018 | Domain | Rush Hour policy + timer QA | B4-017 | future |
| B4-019 | Domain | Survival wave scheduler | B4-017 | future |
| B4-020 | Content | Configured rails/surface zones | Batch2 physics | future |
| B4-021 | Domain | VIP multi-line order schema | Batch3 order contract | future |
| B4-022 | Domain | Endless reset/compaction | B4-005 | future |
| B4-023 | Backend | Verified session challenge & receipts | Batch1 API/security | future |
| B4-024 | Social | Friend challenge fingerprint | B4-023 | future |
| B4-025 | QA | Cross-mode regression + mobile matrix | all live modes | ongoing |

## Parallel lanes in initial week
Lane A: game/domain reducer implementation; Lane B: mode HUD and responsiveness; Lane C: mission JSON schema/test fixtures; Lane D: testing and performance; Lane E: content art/audio adaptation. Work should be compartmentalized so that only necessary engineers are active.

## Ticket template
```
Goal:
In scope / explicitly out of scope:
Dependencies + affected versions:
Contracts changed:
Implementation steps:
Automated tests + fixture IDs:
Manual checks requiring owner:
Screenshots/recordings needed:
Rollback/release flag:
Acceptance criteria:
```

## Merge policy
CI required: lint/typecheck, domain tests, schema+fixture validation, build, appropriate E2E. Reviewer checks compatibility and release status. Migrations require additive/backfill strategy. No unreviewed large generated code changes, no hidden paid advantages, no promises of manual QA by agents.
