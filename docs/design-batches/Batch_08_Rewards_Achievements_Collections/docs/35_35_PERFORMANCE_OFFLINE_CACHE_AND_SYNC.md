# 35 — Performance, Offline Preview and Cross-device Sync

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Browser behavior
Lists and album grids should be virtualized for many items. Lazy-load high-resolution gallery art; do not preload every animation in the main gameplay scene. Use CDN content hashes, WebP/AVIF sprites when appropriate and fallback thumbnails. Minimize event-stream updates to avoid re-rendering Phaser.

## Offline semantics
- Local alpha can show ephemeral non-spendable reward previews.
- Read-only trusted inventory cache can show last synchronized claims with a 'Last updated' badge, but cannot authorize new claims.
- A user may queue a claim **intent** for retry only if entitlement ID and request key are known; server checks eligibility fresh upon reconnect. UI shows `Pending connection`, never `Claimed`.
- If an event ends during offline interval, use published grace rules; client clock is not authority.

## Sync strategy
On sign-in or reconnect, fetch latest inventory/claim revisions and reconcile locally selected items. Use server-driven deltas/cursors with strong authorization; stale tabs cannot override newer equipment revision. Optimistic equipment preview may roll back if server rejects ownership.

## Low-end targets
Keep reward hub memory lower than core gameplay asset budget; avoid persistent full-screen particles. Test slow 3G, backgrounding, app webview lifecycle, disabled audio and aggressive cache eviction.
