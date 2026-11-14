# 38 — Performance, Asset Streaming, Offline Preview and Sync

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Runtime budget
The client loads at most visible customer portraits, common fallbacks and the immediate next scripted asset; do not mount the complete guest catalog in a Phaser scene. Defer journal/gallery high-resolution art until navigation. Pool shared textures and audio, stop timers when scene unmounts, and profile JS/GPU memory across 50 level retries.

## Offline alpha
Scripted alpha customers, displayed orders and reactions work with bundled content and local preview state. Offline play does **not** mint trusted customer reputation, wallet balance, XP or collectible ownership. On reconnect, UI retrieves authoritative projection; it must not upload unverified cumulative "satisfaction" as truth.

## Trusted service latency
A verified run may be settled asynchronously. Player sees a stable result screen with `pending verification`; if customer reward/reputation arrives later, update the relevant UI on authenticated refetch/subscription. Avoid blocking immediate physics or gameplay navigation on a reputation request.

## Reconnect
`reserved` encounters are pinned; reconnect retrieves the same encounter, including customerId/orderId and policy hash. If server access is unavailable, do not silently reroll a different guest. Provide retry/fallback UX with clear status. Timeouts after commit use idempotency to recover the original result.

## CDN and versioning
Store versioned sprites and dialogue bundles by content hash; cache immutable URLs. Respect texture atlas constraints, provide image-size variants, use mobile resource detection rather than hard-coded per-tab RAM assumptions. Release old textures after map/mission transitions.
