# 34 — Common Failure Modes, Anti-Patterns and Prevention

This is a pre-mortem: anticipated ways a large team might accidentally damage the core game while implementing Batch 3.

## Failure 1: UI becomes the rule engine

**Symptom:** a sprite name/animation triggers a merge or a customer reward. **Why it fails:** art load races, animation retries and localized labels can change gameplay. **Prevent:** pure catalog resolver and deterministic reducer receive semantic events from physics; UI only renders state.

## Failure 2: 'Tier' means everything

**Symptom:** tier 3 is used as a unique ID across different island recipe families. **Why it fails:** a tropical and herbal tier-3 might incorrectly merge. **Prevent:** stable `drinkId`, family/ruleset and explicit recipe key; keep alpha's constrained `DrinkTier` until family migration.

## Failure 3: playing the reward animation grants reward

**Symptom:** closing/reopening a reward overlay credits the same coins again. **Prevent:** scoring/wallet event IDs are idempotent and committed before UI animations; UI subscription has no write access to economy.

## Failure 4: auto-service silently blocks puzzle paths

**Symptom:** player tries to create tier 4, but every tier 3 is consumed for an older order. **Prevent:** mission designs include service priority in reachability tests, order targets are visible and tutorial explains the rule. Never secretly change priority without rulesVersion.

## Failure 5: art footprint and collider disagree

**Symptom:** large garnish appears to hit another glass without a merge, or invisible circles touch before visible rims. **Prevent:** calibrated optical anchors, consistent collider debug overlays, distinct footprint + visual silhouette, test on phone screens.

## Failure 6: recipe branching introduced as random chance

**Symptom:** matching drink pair unexpectedly creates an alternate recipe and ruins an order. **Prevent:** explicit mode or preselected branch with deterministic rules; publish rejects ambiguous recipes.

## Failure 7: 'Secret' means impossible to understand

**Symptom:** player spends resources guessing recipes with no clues. **Prevent:** progressive hints, clear research mode and preview of potential costs/outcome; optional discoveries never block main campaign.

## Failure 8: tier costs explode without authored support

**Symptom:** mission asks for tier 8 but gives only 25 tier-1 shots and no preexisting bodies. **Prevent:** resource lower-bound analyzer, authored queues and recorded successful trace; mark 'feasibility unproven' until tested.

## Failure 9: content IDs are overwritten in live seasons

**Symptom:** previously won missions replay with different drink score or graph; leaderboard drift. **Prevent:** immutable catalog hash, rulesVersion, archived manifests, season brackets and replay verifier compatibility.

## Failure 10: cosmetics become invisible pay-to-win

**Symptom:** epic skin expands collision radius or secretly raises score. **Prevent:** cosmetic-only contracts, visual/physics decoupling, fairness review before functional variants.

## Failure 11: AI art pipeline produces 200 inconsistent objects

**Symptom:** each generated glass has different camera angle/lighting, and hover frame changes shape. **Prevent:** locked camera/style bible, asset acceptance tests, pre-rendered controlled states and source files.

## Failure 12: extra systems sink the first release

**Symptom:** engineers spend week building ingredient market and mastery database while physics still feels poor. **Prevent:** alpha scope gate, critical-path prioritization and single tabletop prototype with eight tiers; advanced modules stay design-only until explicitly approved.

## Incident-response worksheet

For any gameplay/regression issue collect: user-visible symptom, affected app/catalog/rules version, seed, input trace, session event IDs, expected vs actual logical outcome, minimal reproducible test, severity, rollback plan, owner manual reproduction instruction and tests added. Do not claim closure until the failing fixture passes and the owner approves changes affecting game feel.
