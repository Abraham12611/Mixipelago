# 02 — Core Domain, Identities and Sources of Truth

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Do not collapse distinct concepts
`CustomerDefinition` is a versioned fictional character/archetype in published content. `Encounter` is a one-time selection/appearance scoped to shop, mission or mode. `Order` is a mission/session objective owned by the Batch 3/4 reducer. `ServiceReceipt` proves that a specific order was fulfilled in a verified run. `SatisfactionObservation` is a derived, bounded interpretation of service evidence. `Relationship` is a persistent player/shop-to-fictional-customer affinity projection. `ShopReputation` reflects quality of verified service; `ShopPrestige` is mostly visual/business status. `RewardReceipt` is the authoritative Batch 6/8 settlement record, never a local sparkle event.

| Record | Writer | May consume | Must not do |
|---|---|---|---|
| Session order | Batch 4/3 session reducer | Customer presentation, local audio | Award server currency directly |
| Customer encounter | Server Customer Director (future); authored mission for alpha | Order generator | Mutate a session already in progress |
| Fulfillment evidence | Verified session processing | Reputation, loyalty, achievements, economy | Trust browser-provided satisfaction/coins |
| Reputation projection | Customer reputation service | Shop, published eligible director pools | Rewrite historic mission score |
| Wallet ledger | Batch 6 economy | Purchase and reward UI | Accept raw client order reward amount |
| XP/skill modifiers | Batch 7 | Director next-encounter eligibility | Change the existing pending customer |
| Collections | Batch 8 | Customer souvenirs, journal decorations | Create an entitlement without receipt |

## Correlation chain
`runId -> orderId -> serviceClaimId -> verifiedResultReceiptId -> observationId -> optional reputationReceiptId / relationshipReceiptId`. Persist source version/hash at verification. A duplicate `serviceClaimId` or run result must not double-increment trust metrics.

## Consistency levels
The local game session is immediate and deterministic. The trusted customer profile/reputation data may arrive asynchronously after run verification; UI must show a processing state, not optimistically commit a monetary or relationship reward. A disconnected client may display last-known relationships as cached information, labeled appropriately.

## Explicit non-goals
No inference of actual user's real-world demographic traits, personal purchasing power or emotional state from player activity. Customer segment labels refer to fictional roles, not player identity. No targeted price discrimination using real-life sensitive data.
