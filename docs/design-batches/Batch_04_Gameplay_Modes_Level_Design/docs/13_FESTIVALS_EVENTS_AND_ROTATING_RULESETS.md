# 13 — Festival Events and Rotating Rule Sets: Overview

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Scope boundary
This chapter describes integration only. Full festival stories, global events, schedules and seasonal economy live in Batch 12/20. Here we define the gameplay form: an event is a version-pinned mission template or series of missions governed by a scheduled availability window.

## Example concepts
- Island Sunset Festival: Rush Hour missions with a sunset background, deterministic target orders and a leaderboard score band.
- Market Rush Weekend: Classic Service with many small orders and limited shots; an alternate art/background skin.
- Coral Celebration: score-attack route rewarding chain mastery, with no unique physics exploit.
- Community Mixathon: collective served-order totals validated server-side once multiplayer/event service exists.

## Technical boundary
The world event service publishes an `EventDefinition` and `MissionVersion` list; `MissionLoader` resolves the exact mode and rules snapshot for launch. Session simulation never calls external scheduling APIs mid-run. If event closes during an active puzzle, allow a documented grace policy (finish current session; reward eligibility determined by start receipt or submission deadline). Time zone windows stored in UTC; UI localizes.

## Fairness and anti-fraud
Event modes use fixed standard seed or documented seed classes where rankings are compared. Reward grants require idempotent backend verification. Cached event banner does not authorize expired rewards. Future paid cosmetics cannot modify standardized tournament physics. Event paths are optional to the base campaign.

## Content rollout
`planned → QA → staged → live → retired`, with immutable content IDs and manifest digest. Live config updates affect NEW runs; in-progress sessions remain pinned. Rollback disables entry and preserves prior results without corrupting stores.

## Accessibility
All themed assets have non-sensory goal descriptions; lights/flash are reduceable; all events have clear deadlines and rules independent of promotional artwork.
