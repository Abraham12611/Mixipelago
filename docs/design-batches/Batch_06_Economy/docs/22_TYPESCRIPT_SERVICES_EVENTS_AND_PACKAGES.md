# 22 — TypeScript Domain Services, Events and Integration

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Suggested packages
`packages/economy-core` (pure pricing, policy, eligibility), `packages/shop-domain` (shop projections, upgrade dependencies), `apps/game-api/modules/economy` (commands and DB), `apps/game-api/modules/rewards` (verified receipts settlement), `apps/web/features/shops` (React views), `packages/shared-contracts` (versioned types), and `apps/admin/features/economy` (catalog editor).

## Domain events
`economy.reward_eligible.v1` is not a grant; `economy.coins_credited.v1` confirms ledger settlement; `economy.purchase_committed.v1`; `shop.upgrade_installed.v1`; `shop.cosmetic_equipped.v1`; `shop.reputation_changed.v1`. All include stable event ID, source receipt ID, aggregate revision, schema version, happenedAt and trusted actor provenance.

## Event processing
Use transactional outbox in source DB; consumers are idempotent. Never call payment, analytics or UI event emitters while holding SQL locks. Projections can update asynchronously; mutation response still contains authoritative status.

## Deterministic modifier reducer
`deriveShopModifiers(shop, upgrades, skills, events, modeProfile): ModifierProjection` is pure and testable. Persist snapshots for verified mission runs that use campaign perks. For competitive modes, supply normalized profile before simulation starts.

## Failure policy
If frontend cannot reach API, allow cosmetic preview and core offline game but **disable new trusted spending or earning claims**. Queue only explicit, replay-safe claim requests where feasible; never show a successful coin credit before server confirmation.
