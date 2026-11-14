# 27 — Drink/Recipe Integration with Future Game Systems (Overview Only)

This document deliberately stays at the overview level. Detailed economy, story, customer, islands, social, events and skills designs will be specified in later batches. It defines minimum extension data to prevent incompatible future APIs.

## Island campaign (Batch 5)

Each island may feature region-specific drink families, unlockable recipes and themed ingredient art. A mission references a catalog hash and declares which family/ruleset is active. The island graph controls unlocking but not collision physics. Completing a level can grant a recipe hint or a cosmetic collection entry via a validated reward event. Do not require an island-specific recipe in a mission before its unlock is reachable.

## Business economy (Batch 6)

Shops could later improve menu availability or premium customer requests, but coins are server-owned. An upgrade might change customer probabilities or allow an off-board crafting station. It must not silently enlarge colliders or raise ranked score. Any pantry ingredient used for crafting has a separate inventory ledger and explicit purchase/earn route.

## Character skills (Batch 7)

Mastery milestones can serve as prerequisites for skill-tree nodes. Perks may offer visual aids, campaign-only bonuses or recipe clues; they are not infused into unranked physics through magic data tags. Each modifier declares mode eligibility, stacking semantics and version, with ranked standardization.

## Collections and achievements (Batch 8)

First production of a drink, completing a set or discovering a secret can create an achievement event. Achievement system consumes validated semantic activity and issues one-time grants, not UI effects. Set membership and denominators are versioned.

## Customers and reputation (Batch 9)

A named customer can request a known region-specialty recipe after unlock. Order generator checks catalog eligibility, and order matcher supports exact `drinkId` targets only after migration from alpha tier-only orders. Loyalty and reputation calculations belong to the customer service, not recipe resolver.

## World incidents (Batch 10)

Seasonal storms could temporarily restrict ingredient suppliers, and tourist events could favor certain flavors. No incident changes an in-progress ranked session's recipe rules. Event-driven changes take effect when starting a compatible session and are advertised in the level briefing.

## Narrative/rivals (Batch 11)

A rival's 'signature drink' becomes a published recipe definition plus story unlock. Dialogue/cutscenes own flavor; mission catalog owns actual achievable output and scoring. NPC text must not be trusted as the canonical ingredient cost.

## Live events (Batch 12)

Festival drinks are versioned content bundles with availability windows. A retired event skin remains in a player's collection after the event; the gameplay tier doesn't disappear from old verified replays. Limited-time collection rules require transparent eligibility and time-zone handling.

## Leaderboards (Batch 13)

Tournament level pins fixed catalog, seed, physics and rules. Cosmetic rarity/missing recipes cannot yield unequal competition. If tournament allows specialized drinks, all players receive equal access to identical recipes or enter separate brackets.

## Friends/crews (Batch 14)

Players may share recipe collection showcases or contribute verified discovery milestones to crew projects. Do not permit raw client-crafted items to be transferred to other players without trusted ledger and fraud controls.

## Admin/content (Batch 18), security (Batch 19), live-ops (Batch 20)

Editors need recipe graph validation, preview mode and rollback. Security guards prevent arbitrary client grants and content injection. Live-ops can compare tier reach/funnel by version, but should not stealth-modify probabilities for an individual spender. Changes are audited and scheduled through feature flags.

## Cross-system event contract

Use signed/validated domain records keyed by `playerId`, `runId`, `sourceEventId`, `catalogHash`, `recipeId`, `outputDrinkId`, `ruleVersion`. Future subscribers should be independent idempotent consumers; failure of a cosmetic collection update should not roll back an already accepted physics merge or make the board unplayable.
