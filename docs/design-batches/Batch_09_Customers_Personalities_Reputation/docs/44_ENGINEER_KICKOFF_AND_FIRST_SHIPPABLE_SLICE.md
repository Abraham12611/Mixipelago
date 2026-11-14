# 44 — Engineering Kickoff and First Shippable Customer Slice

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Handoff order
1. Read Batch 3 order matching and Batch 4 customer director first; preserve exactly two scripted orders in the alpha.
2. Read Batch 6 trusted reputation/economy interfaces and Batch 7 class modifiers; read Batch 8 collectible claim model.
3. Build pure customer catalog and order-presentation adapter; no backend needed for first visual slice.
4. Add schema/fixture validation and seeded customer pool tests with all feature flags OFF.
5. When verified result receipts and shop auth exist, implement observation + reputation in a strictly server-authoritative adapter.
6. Later add relationships and journal; VIP/critic only after disclosed mission variants and anti-cheat tests.

## The smallest deliverable
**Two readable animated guest cards** on a working physics/tabletop session that react to the existing `order_fulfilled` events, without changing the current session reducer at all. The customer identity is scripted for the published mission. Users may tap the card to see the requested drink, reward and accessible status label. There is no persistent satisfaction, XP, shop wallet or VIP in this slice.

## Independent tasks
Art team makes two character portraits, small/large states. Frontend builds HUD and audio cues. Gameplay engineer supplies read-only order event adapter. Content QA validates labels and portrait manifests. Backend team can build customer catalog/seeded pool behind OFF gates in parallel, without blocking the visual alpha.

## Integration sequence
`customer types` -> `HUD adapter` -> `scripted smoke run` -> `asset polish` -> `catalog validator` -> `server encounter reservation` -> `verified satisfaction` -> `reputation projection` -> `loyalty journal` -> `optional VIP`. Do not force later modules into the 72-hour alpha scope.

## Manual checks
All manual UI tests and subjective gameplay-feel review go to product owner. Engineers provide reproducible URL/build, device/viewport and exact actions. Engineers write PRs and cannot merge their own work; main release requires explicit owner approval.
