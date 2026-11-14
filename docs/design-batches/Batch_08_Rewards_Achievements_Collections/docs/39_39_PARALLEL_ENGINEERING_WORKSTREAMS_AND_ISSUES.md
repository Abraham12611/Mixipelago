# 39 — Parallel Engineering Workstreams and Issue Backlog

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Roles and dependency lanes
**W1 Rules/content (4 engineers):** typed catalogs, schema, achievement DSL, program validator. **W2 Backend/DB (4):** entitlement state machine, idempotent settlement, inventory, source verification. **W3 UI/art (3):** rewards inbox, achievements, albums, profile equip, component assets. **W4 QA/security (2):** vectors, RLS and concurrent claims, economic reconciliation. **W5 integration/ops (2):** feature gates, PostHog/Sentry hooks, content publishing, runbooks. Reduce parallel lanes if team size smaller; don't force 15 agents into work with unresolved contracts.

## Proposed 25 issues with dependencies
| ID | Issue | Depends on |
|---|---|---|
| B8-01 | Catalog contracts and stable IDs | none |
| B8-02 | Versioned schema, policy linter | 01 |
| B8-03 | Verified event adapter | Batch 4/5 source receipts |
| B8-04 | Evidence inbox and dedupe | 03 |
| B8-05 | Achievement rule evaluator | 01/02 |
| B8-06 | Counter projections and threshold crossing | 04/05 |
| B8-07 | Reward eligibility resolver | 02/06 |
| B8-08 | Entitlement state machine | 07 |
| B8-09 | Claim command idempotency | 08 |
| B8-10 | Batch 6 wallet handoff adapter | 09 + B6 |
| B8-11 | Batch 7 XP handoff adapter | 09 + B7 |
| B8-12 | Inventory unique ownership | 09 |
| B8-13 | Cosmetic equip and revision | 12 |
| B8-14 | Collection album projector | 12 |
| B8-15 | Collection completion claims | 14/08 |
| B8-16 | Rewards inbox mobile | 08/09 |
| B8-17 | Achievement progress and details UI | 06 |
| B8-18 | Album UI desktop/mobile | 14 |
| B8-19 | Trophy/showcase UI | 12/13 |
| B8-20 | Reward SFX and reduced-motion variants | 16/17 |
| B8-21 | Admin authoring/publishing and diffs | 02 |
| B8-22 | Reconciliation and alerting | 09/10/12 |
| B8-23 | API security and RLS tests | 08/09/12 |
| B8-24 | Concurrency/migration/property test suite | 06/09/12 |
| B8-25 | End-to-end pilot feature flag and launch gates | 16/22/23/24 |

## PR rules
Engineers create isolated feature branches from the agreed development base, implement only assigned interfaces, attach test evidence, and open PRs. **Do not self-merge.** Coordinator reviews and may merge non-main branches per owner policy; merging into `main` for product code requires explicit owner approval. Documentation PRs may follow the existing approved documentation workflow.

## Parallel integration checkpoints
Freeze `RewardEntitlement`, `AwardReceipt`, `AchievementEvidence`, `InventoryItem` interfaces before W2/W3 work; pass mock responses for early UI; publish schema migrations only after CI and cross-team review. Require one working slice before expanding to daily programs.
