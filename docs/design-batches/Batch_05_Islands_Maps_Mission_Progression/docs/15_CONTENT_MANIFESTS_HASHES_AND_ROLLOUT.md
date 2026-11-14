# 15 — Immutable Content Manifests, Hashes, Publication and Rollback

## Required version axes
- App version `v0.2.0` tells players what release they have.
- `graphVersion` identifies published nodes, edges and prerequisite rules.
- `mapLayoutVersion` identifies coordinates and visual references.
- `missionVersion` and `contentHash` continue as Batch 4's immutable mission contract.
- `catalogHash`, `physicsPresetHash` and `scoreRulesVersion` remain pinned by a gameplay session.
Never replace these with one universal version property.

## Publication model
Build a staged draft manifest → schema validation → semantic graph lint → map asset integrity → simulation/mission replay proof → owner manual review → immutable publication → targeted rollout → public pointer update. Keep old manifest versions accessible for historical receipts and archived active runs.

## Canonical hashing
Sort keys, define numeric serialization and calculate SHA-256 over canonical rule-bearing JSON. Prefer separate manifest hashes for graph/visuals. If localized copy changes only, don't change gameplay rules hash. Maintain a signed or trusted server-delivered active pointer for authenticated clients; compare digests against downloaded bytes.

## Content states
`draft`: internal only; `staged`: preview audience; `published`: eligible for public gameplay; `retired`: historical, no new sessions unless compatibility exception. **A node can be physically drawn in draft but not publishable**, and unpublished missions must never appear as playable.

## Rollout strategy
Feature gate `CAMPAIGN_MAP_ENABLED` starts off during alpha. Enable first for internal, then canary players, then full audience after QA. Graph rewrites require migration of completion receipts by stable IDs. Node renumbering is visual metadata only; mission IDs don't change.

## Fail-safe rollback
If a graph release is broken, restore previous `activeGraphVersion` pointer for **new selections**, keep any safe pinned sessions, stop new reward grants if trust is compromised, and preserve historic completions. Never delete progression rows as a quick rollback fix.

## Content integrity validation
Unknown mission IDs, missing art chunks, invalid unlock DSL, dependency cycles, unreachable critical path, unsupported mode, broken gateway and cross-island references, duplicate IDs and hidden mandatory content all fail publication. Tool output separates errors from warnings, with machine-readable diagnostics for CI.
