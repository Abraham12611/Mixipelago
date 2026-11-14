# 21 — Seasonal, Ranked and Social Reward Contracts

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Boundaries
Batch 13 will own verified ranking math, divisions, tie-breaks, season cutoffs and final placement. Batch 14 will own friends and crews. Batch 8 consumes only a signed, finalized award-source receipt and creates entitlement/ownership. It does not trust a client screenshot showing rank #1.

## Season award identity
`(playerId, seasonId, leaderboardId, rewardStage, policyEpoch)` must be unique. Award policies are published before leaderboard season begins; after finalization, preserve snapshot and tie-break rule version. If corrections occur, issue audited compensating or supplementary entitlements rather than mutating past history secretly.

## Reward style
Prioritize trophies, frames, profile titles, limited but non-predatory decorative rewards. Significant spendable payouts require independent Batch 6 caps and normalized competitive fairness. Players should not be able to buy stronger ranked physics through cosmetics or skill-tree prizes.

## Crew co-op (future)
Crew milestone completion is authenticated and finalized by the crew service; players eligible at snapshot time receive one award each using a member entitlement key. Changes in crew membership after award do not duplicate rewards. Avoid invite-spam requirements and pay-to-compete contribution schemes.

## Regional/local leaderboards
Location should be opt-in and coarse enough to protect privacy. Prize entitlement should not rely on unverified geolocation claims or precise address. A player moving locations mid-season requires an explicit published league policy.
