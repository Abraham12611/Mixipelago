# 22 — Onboarding, Recommendations, Breadcrumbs and Player Guidance

## Teaching sequence
Introduce the map **after** the core merge-and-serve win, not before the player understands how to play. Transition from winning `coconut-cove-001` to an explicit new route highlight; show one tiny card explaining "New missions unlock as you play." Later teach route forks, stars, secrets and gateways only at first use.

## Recommended next action
`getRecommendedNextNode()` only considers published, supported and eligible mission nodes. Ranking proposal: critical route first when player is progressing normally; current unfinished branch if the player intentionally selected one; then mission tier/difficulty fit and proximity. Never use hidden unpublished content to guide a player.

## Clear explanations
Node labels should include mode icon, title, star progress and requirement summary. Gate text must be actionable: "Clear Mission 2" or "Earn 4 stars across Missions 2–4", not "Requirement 1027 unavailable". Provide a `Show on Map` deep link where possible.

## Skip and retry
A failed node stays selectable for Retry; losing doesn't de-unlock a route already earned. After repeated difficulty, optional hint surfaces can suggest a nearby alternate path or practice mission, but should not force monetization or penalize the player.

## Return navigation
From gameplay Results screen: `Replay`, `Next Mission` if available, `Map`. On map: `Resume` jumps to last attempted node; `Find Next` chooses a recommended available one; player can browse an island without entering a mission.

## User-driven accessibility
Offer list mode, show progress by chapter, reduce animated focus swoops, and support large text in contextual cards. Mobile touch controls for map are independent from the active game's aim gestures, preventing one screen's drag behavior from leaking into another.

## Analytics and improvement
Measure time to first map tap, unlocked-node understanding, next-mission click success, lock confusion, branch choice and return frequency. Pair data with owner manual UI testing and user feedback rather than optimizing solely for taps.
