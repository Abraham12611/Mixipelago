# 03 — Reward Sources, Verification and Policy Precedence

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Source categories
Publish explicit source kinds: `mission_first_clear`, `mission_star_milestone`, `campaign_treasure`, `achievement_milestone`, `collection_completion`, `login_gift` (future), `daily_challenge` (future), `week_activity` (future), `season_placement` (future), `compensation` (operator-only). Each source maps to a separate scope and immutable identity.

## Validation chain
1. An authoritative source domain persists its event and independent source receipt.
2. Batch 8 verifies that the source is approved, published and belongs to this authenticated player.
3. Resolver looks up the pinned reward policy; checks mode (ranked or casual), gate, eligibility time and previously issued entitlements.
4. If eligible, creates an entitlement. Grant may be auto-settled only when policy explicitly says `auto`; otherwise waits for `claim`.
5. A claim delegates each resource to its owning service, with one orchestration receipt across all line items. Do not have Batch 8 directly mutate a wallet or XP total.

## Precedence and double-count prevention
An achievement for completing a mission does **not** grant the mission's first-clear coin reward again. The first-clear source belongs to Batch 6. An achievement may have its own independently budgeted cosmetic reward; if it includes coins, it must reference a distinct approved achievement entitlement and be subject to caps. When a collector acquires an item from a chest, a collection milestone may become eligible; the item source and milestone source have different keys.

## Repeatability table
- Mission first-clear: unique `(player, missionId, claimPolicyEpoch)`; a mission revision alone never resets eligibility.
- Star threshold: unique `(player, missionId, threshold)`; stars improve monotonically.
- Treasure: unique `(player, treasureId, seasonScope)`.
- Daily claim: unique `(player, rewardProgramId, UTC-window-id)`; no timezone spoofing.
- Achievement tier: unique `(player, achievementId, tierId, definitionEpoch)`.
- Collection completion: unique `(player, albumId, albumEdition, milestoneId)`.

## Failure isolation
If a collection completion grants coins and a cosmetic, all lines must settle with one durable coordinator outcome; otherwise keep explicit `pending` state and retry safely. Rendering a success animation before settlement is only a preview, not evidence of ownership.
