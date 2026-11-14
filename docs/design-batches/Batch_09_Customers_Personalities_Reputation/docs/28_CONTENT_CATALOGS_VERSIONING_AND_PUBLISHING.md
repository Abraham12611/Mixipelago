# 28 — Customer Catalog IDs, Versioning, Publication and Migration

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Content separation
Store customer definitions, segments, dialogue, art references, preference tags, encounter pools, and satisfaction/reputation policies in independently validated but cross-referenced catalogs. Each published manifest receives a content hash, revision and validity range. A mission pins its relevant catalog version before start.

## Authoring state machine
`draft -> validated -> reviewed -> staged -> published -> retired`. Publishing requires mission/recipe reference checks, asset availability, translation fallback, probability cap tests and seed fixture replay. No manual direct production DB update bypasses review. Draft characters and gated VIP/critic entries cannot surface in ordinary live customer pools.

## Stable identity and backward compatibility
Never repurpose an existing `customerId` or `poolId` for a different semantic person/selection policy. Changes to display name or portrait can use versioned localization/art but must retain historic journal continuity. Retiring a character preserves a read-only tombstone to resolve receipts; do not silently rewrite existing encounter history.

## Anti-mismatch
Do not let an old client request a new customer requiring a recipe unavailable to its pinned drink catalog. For unsupported catalog version return `CONTENT_VERSION_MISMATCH` with safe restart or pinned compatibility response, not an invented substitute order.

## Gate control
Content visibility alone is not sufficient: server gate, client route/UI gate, authorized reward issuer and mission-pool validation must agree before a system is enabled. Rollback disables new encounters while preserving finalized receipts and existing journal state.
