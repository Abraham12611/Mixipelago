# 38 — Example End-to-End Player Journeys

## Journey A — First mission clear
Player completes `coconut-cove-001` (two customer orders per Batch 3/4 fixture) → result shows one star → local preview result saved → campaign projection reevaluated → `cove-n002` becomes available → map camera gently highlights the route → player taps next mission. At no point is a trusted wallet credited from browser preview data.

## Journey B — Replay for mastery
Player cleared a later mission with one star, returns to the node and chooses Replay. They win with three stars, though their score is lower than previous best. Store `bestStars=3` and retain independently higher prior score. Unlock a star-gated treasure only if authored rule requires these stars; do not grant first-clear a second time.

## Journey C — A branch choice
After an earlier published milestone, player sees two named optional paths (Precision route and Service route). Both are visibly selectable. They choose the Service branch. On completion, downstream `anyOf` gateway opens. Precision branch remains optional and replayable later.

## Journey D — Hidden route revealed
Player completes an authored 3-star requirement; the system records a discovery flag. On map, a scenic fog marker becomes a visible hidden pier and one optional treasure route appears. Device locks during animation; re-open resumes at completed reveal state rather than re-issuing entitlement.

## Journey E — New island download failure
Player clears Harbor Gate and taps Travel. Target island assets fail on slow connection. Show offline/retry message and keep the current map interactive. A cached preview thumbnail can be shown, but the gameplay session never starts with missing level assets.

## Journey F — Old returning save
Guest opens map after version update. Content revision moved a node's anchor but kept `nodeId` and `missionId`. Projection recomputes from local best results, retains the completed node and focuses camera at new coordinates. A corrupted optional camera preference resets without deleting mission clears.

## Journey G — Cheating attempt
Malicious client edits localStorage to claim three stars and calls an account API to unlock Golden Archipelago. Backend uses verified receipt records, ignores local preview, returns requirement-not-met and logs a bounded security event. No durable currency, leaderboard placement or gateway permission is granted.
