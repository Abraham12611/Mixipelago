# 02 — Rewards Taxonomy and Authority Matrix

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Reward catalog
| Type | Example | Durability | Owning service |
|---|---|---|---|
| Score | +150 order bonus | Run-scoped | Batch 4 session reducer |
| Stars | 2/3 on a completed mission | Monotonic best | Batch 5 campaign |
| Preview coins | +15 visual alpha coins | Local, untrusted | Alpha game shell only |
| Trusted coins | 150 first-clear coins | Wallet ledger | Batch 6 economy |
| XP | 120 first-clear XP | Cumulative grant ledger | Batch 7 progression |
| Skill points | 1 on level attained | Derived milestone | Batch 7 progression |
| Achievement | First Clear badge | Persistent verified record | Batch 8 achievement service |
| Collectible | Coral recipe card | Inventory ownership | Batch 8 inventory service |
| Cosmetic | Hibiscus counter skin | Inventory + equip state | Batch 8 ownership / Batch 6 shop equip |
| Title/trophy | Cove Trailblazer | Durable entitlement | Batch 8 trophy service |
| Ranked medal | Gold season medal | Season-scoped receipt | Future Batch 13 awards service |

## Canonical event sources
`mission_result_verified` and `customer_order_verified` come only from the server's accepted session pipeline; `campaign_node_completed` and `treasure_eligible` from Batch 5; `economy.purchase_settled` from Batch 6; `xp_awarded`/`level_attained` from Batch 7. A client's `drink_merged` or `achievement_completed` message is never authoritative for a durable grant.

## Derived vs owned state
An achievement may be **derived** from a verified counter but should be checkpointed as achieved once (with rules version and source snapshot) for durable display. A claimable award is an independent grant record. A collectible can exist in inventory without being equipped. Changing equipment changes presentation, not acquisition history. Deleting a cosmetic asset from the shop does not revoke existing ownership without an explicit policy.

## Reward envelope
Every server-owned award records: `playerId`, `sourceKind`, `sourceId`, `sourceScope`, `policyId`, `policyVersion`, `contentHash`, `rewardType`, `quantity`, `entitlementId`, `receiptId`, `occurredAt`, and `traceId`. `sourceScope` specifies once-ever, once-per-season, once-per-day-window, or once-per-authored-claim; no implicit repeatability.

## Safety constraints
Never convert preview earnings, local mission badges, client-computed achievements, ad views or purchase UI clicks into spendable rewards. API requests name a claim target; the server resolves full content and amount. Never let achievement grants create recursive infinite achievement-grant loops.
