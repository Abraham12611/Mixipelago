# 09 — Service Lifecycle, Event Ordering and Exactly-once Fulfillment

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Canonical path
`shot -> Rapier contacts -> MergeArbiter commit -> new drink output -> SessionReducer score -> oldest eligible order matching -> reserve/consume output -> order progress -> order completion -> mission objective -> result receipt`. Presentation plays reactions after the semantic reducer; never emits economic/XP consequences itself.

## Exactly-once keys
A service claim ID binds `{runId, mergeId, outputDrinkId, orderId, orderLineId}`. A fulfilled-order event binds `{runId, orderId}`. Persistent reputation or loyalty receipts bind verified run/result and eligible order/encounter source. Require database unique keys; local duplicate delivery is normal and should be harmless.

## State transitions
`placed -> active -> partially_served -> fulfilled`; later timed modes may use `expired` or `canceled`. `fulfilled` and `expired` are terminal and mutually exclusive. Lines have `quantity` and `servedQuantity`; neither may exceed the authored target. An ineligible output remains a physical body; an eligible output is claimed before the next merge arming step.

## Presentation and rewards
A short drink-transfer animation can show an animated glass from merge location to customer avatar, but its input body is already logically consumed. Score uses Batch 3/4 rules and preview coins remain preview in alpha. Trusted wallet credits only after the Batch 6 verified settlement path. Failure to play the animation cannot undo the legitimate result.

## Critical regression suite
Duplicate contact -> one merge; duplicate merge event -> one service claim; two simultaneous outputs -> stable order sequence; served output can't re-merge; order fulfilled twice -> one payout; mission won -> no replacement; a stale customer avatar doesn't mutate session state. Log correlation IDs for replay and incident triage.
