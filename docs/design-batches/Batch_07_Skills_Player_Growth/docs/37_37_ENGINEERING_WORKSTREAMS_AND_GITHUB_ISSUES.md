# 37 — Parallel Engineering Workstreams and Issue Backlog

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Owner responsibilities
Coordinator owns branch integration, PR reviews and merge sequencing. Engineers open feature branches and PRs and **do not self-merge**. The owner conducts all manual interface/visual/gameplay feel tests. Automation and service unit tests belong to engineers.

## Proposed independently assignable GitHub issues
| Ticket | Priority | Module | Dependencies | Deliverable |
|---|---|---|---|---|
| SK-001 | P0 | contracts | Batch 6 published modifier types | stable DTOs + error codes |
| SK-002 | P0 | pure rules | SK-001 | integer XP curve + property tests |
| SK-003 | P0 | content | SK-001 | catalog JSON schema + DAG validation |
| SK-004 | P0 | backend | SK-002 | trusted XP entitlement handler |
| SK-005 | P0 | database | SK-001 | audited progression schema + RLS |
| SK-006 | P0 | backend | SK-003,005 | transactional skill allocation |
| SK-007 | P0 | backend | SK-004,005 | level milestones + point ledger |
| SK-008 | P0 | UI | SK-001 | profile level & XP HUD |
| SK-009 | P0 | UI | SK-003,006 | 2-branch first-slice tree |
| SK-010 | P0 | integration | SK-004 | Batch4 verified result adapter |
| SK-011 | P0 | integration | SK-003 | Batch6 modifier registry + caps |
| SK-012 | P0 | QA | SK-004,006 | replay/race/idempotency tests |
| SK-013 | P1 | UI | SK-009 | bottom-sheet skill detail mobile |
| SK-014 | P1 | UI | SK-009 | desktop graph & keyboard list |
| SK-015 | P1 | backend | SK-006 | free respec preview + commit |
| SK-016 | P1 | UI | SK-015 | respec/build preview UX |
| SK-017 | P1 | gameplay | SK-011 | skill snapshot/pinning in session |
| SK-018 | P1 | analytics | SK-006 | privacy-safe talent funnel |
| SK-019 | P1 | content | SK-003 | Content Studio skill editor |
| SK-020 | P1 | docs | SK-003 | content author playbook and ADRs |
| SK-021 | P2 | gameplay | SK-017 | active skill loadouts after gate |
| SK-022 | P2 | game | Batch3 future | recipe mastery persistence |
| SK-023 | P2 | social | Batch13 future | standardized competitive profile |
| SK-024 | P2 | events | Batch10 future | risk-skill incident integration |
| SK-025 | P2 | QA | all shipped | owner-directed manual test kit |

## Critical path
SK-001+002+003+005 in parallel → 004/006/007/010/011 → 008/009/012 → owner manual acceptance → v0.4.0 gate. The others can progress in parallel without delaying a minimal trusted progression release.

## PR standards
One coherent area per PR. Include migration/rollback plan if DB changes, example payload, tests, feature flag, evidence, release note, and cross-batch contract note. Do not combine XP grants and animations into an inseparable PR. Coordinator resolves clashes with Batch 6 ledger or Batch 4 result semantics.
