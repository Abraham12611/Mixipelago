# 24 — Economy Content Studio, Authoring and Safe Publishing

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Content surfaces
Admin can author shop archetypes, upgrade definitions, price curves, display text, effect references, reward policies and feature gates. Save draft → validate → preview in synthetic shop → obtain approval → publish immutable catalog version → gradual rollout → compare metrics → promote or rollback.

## Validation
Reject duplicate IDs, missing localizations/assets, negative prices, unreachable tiers, dependency cycles, incompatible effect categories, over-cap multipliers, rewards without source limits, and shop purchases not assigned to a shop archetype.

## Release discipline
Catalog publications carry semver-like content version, cryptographic hash, author, reviewer, activation time, rollout segment, and rollback pointer. Active sessions and receipts pin relevant versions. Changes to previously owned upgrades must preserve entitlement or trigger a reviewed migration.

## Security
Browser-facing admin UI calls a permission-checked backend. Never expose Supabase service credentials or SQL write access to regular players. Do not allow the same role to edit live catalog and approve unlimited arbitrary wallet grants without independent audit.

## Operational tools
Wallet reconciliation dashboard, pending reward receipt queue, purchase failure explorer, catalog diff, economy simulator, version rollback UI, and compensation workflow with explicit justification.
