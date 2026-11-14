# 30 — Compatibility Matrix With Batches 1–5

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Contract precedence
Batch 2 authoritative for physics; Batch 3 for drink tiers and auto-serving; Batch 4 for objective and score; Batch 5 for graph and star unlocks; Batch 6 for wallet/economy and shop purchase rules. No changes to prior code paths without ADR and cross-batch regression.

## Compatibility matrix
| Earlier contract | Batch 6 reads | Must not overwrite |
|---|---|---|
| `drink_merged` | optional verified feature and analytics | merge result or item identity |
| `order_fulfilled` | eligible order reward source | original order fulfillment priority |
| `session_won` | reward eligibility | objective reducer or stars |
| `mission_result_verified` | first clear/replay policy | game session proof |
| `campaign.node_unlocked` | optional shop location eligibility | graph visibility or content publication |
| `campaign.treasure_claimed` | one-time reward settlement request | treasure eligibility/claim identity |

## Alpha upgrade path
Local preview coins remain local diagnostic values. On account creation, create a wallet at **zero or an explicit one-time onboarding grant** from a server-approved campaign rule, not the client's balance. Import only permitted nonfinancial progress after reconciliation; client cannot mint shop ownership. If player already had verified server progress, recompute eligible historical grants from trusted receipts under an explicit migration policy rather than current client state.

## Version and pinning
Separate `physicsRulesVersion`, `drinkCatalogVersion`, `missionVersion`, `campaignGraphVersion`, `economyCatalogVersion`, `rewardPolicyVersion` and `modifierProfileVersion`. Maintain immutable published references in receipt records. A catalog retirement does not mutate past grant source values.
