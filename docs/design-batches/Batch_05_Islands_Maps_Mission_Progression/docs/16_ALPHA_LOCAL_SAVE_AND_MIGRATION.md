# 16 — Local Campaign Saves, Migration and Offline Preview

## Alpha source of truth
Carry forward the Batch 1 key **`mixipelago:save:v1`**; do not erase or repurpose it. A first campaign version can add namespaced `campaignPreview` projection with a migration adapter, or use `mixipelago:campaign-preview:v1` while preserving Batch 1's snapshot. The exact persistence strategy must be chosen in an ADR before implementing.

## Save payload
Recommended local projection: `schemaVersion`, `graphVersion`, `activeIslandId`, `lastSelectedNodeId`, `cameraByIsland`, `missionResultsPreviewById`, `discoveryFlagsPreview`, `claimedPreviewNodes`, `lastUpdatedAt`, `migrationHistory`. Save only player progress; don't duplicate huge published map manifests or generated assets inside localStorage.

## Transition model
Mission completes → Batch 4 returns result → add a monotonic preview result → recompute graph projection → persist atomically where possible → UI updates. LocalStorage write is synchronous but not transactional across keys; write one validated blob with checksum/backup, or use IndexedDB transaction if already adopted. If app crashes between result and celebration, rehydration must still recognize the clear.

## Guest mode and offline
A returning guest can replay cleared missions and browse cached islands. Local preview stars are a convenience, not a durable economic entitlement or proof for rank. Show "Saved on this device" where necessary. Changing device or clearing browser data may lose guest progress unless account sync exists.

## Corrupted data
Parse safely, bound sizes, validate schema, quarantine invalid data, preserve last known-good backup, and present a non-alarming recover/reset action. Never send raw corrupted save blobs to telemetry. If graph version has changed, resolve stable mission IDs and recompute projections; do not carry forward stale rendered statuses.

## Migration to accounts
When trusted progression ships, guest progress may be imported as a noncompetitive history marker only under an explicit trust policy. Do not convert client preview coins or achievements into authoritative economy balances without verifiable gameplay proof. Offer a transparent explanation of what carries over.

## Two-tab behavior
For local preview, use a storage/version conflict strategy: monotonic merge by mission ID for best stars and score, last-writer camera preference, stable union for discovery flags. Do not assume browser storage events provide perfect transactional coordination; account-backed trusted writes need server transactions.
