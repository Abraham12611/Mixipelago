# 29 — Content Studio: Author, Validate, Preview and Publish Skills

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Designer capabilities
Create branches/nodes, localized copy, icons, ranks, prerequisites, effect types, server mode permissions, point costs, minimum level, caps and feature gates. The editor should render a responsive skill graph and a readable table/list inspector.

## Publication stages
`DRAFT → VALIDATING → APPROVED → STAGED → PUBLISHED → ARCHIVED`. Authors cannot self-approve high-risk income/cap changes. The final package is immutable with a content hash; revisions create a new version, never overwrite an existing published blob.

## Validation pipeline
1. JSON Schema and semantic ID uniqueness.
2. DAG acyclicity, prerequisite reachability and level/point cap feasibility.
3. Effect registry type-check, numeric ranges, stacking bucket references and mode gates.
4. Screenshot comparison across mobile/desktop plus accessibility audit.
5. Simulated sample profiles for VIP, discounts, XP pacing, and rank normalization.
6. Economic/security owner approval for trusted effects.
7. Staged rollout to dev/QA and opt-in cohorts before production.

## Rollback
Revert the *active catalog pointer*, not the historical record. Existing player investments into disabled nodes become `suspended` with clear explanation and a compensating respec policy; do not silently remove points. Change control requires an ADR, migration plan, and fallback for sessions pinned to old content.

## Authoring tests
Catalog with duplicate node ID, unknown target stat, circular prerequisite, unreachable enabled talent, invalid negative rank cost, or missing locale string must fail publishing.
