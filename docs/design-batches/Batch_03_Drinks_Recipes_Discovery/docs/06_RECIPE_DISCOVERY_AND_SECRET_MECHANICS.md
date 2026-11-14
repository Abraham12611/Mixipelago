# 06 — Recipe Discovery, Secrets and Experimentation

**Status:** Future feature (candidate starting v0.4+; exact release gated). This document specifies discovery as a system without forcing it onto first-week alpha.

## Promise to the player

The player should feel like a creative inventor when they uncover a recipe. Successful discovery must be understandable after the fact: 'I did X because of hint Y and got drink Z.' Avoid opaque slot-machine outcomes where the player blindly repeats expensive actions.

## Discovery types

1. **Progression:** unlock a recipe when an island mission is completed. Reliable, simple, non-secret.
2. **Experimentation:** combine authorized ingredients at a separate workshop station according to a visible or clue-backed schema.
3. **Environmental:** find a clue in a landmark, merchant dialogue or collectible to unlock a recipe contract.
4. **Mastery:** earn enough repeat performance with a drink family to unlock a specialist form or cosmetic technique.
5. **Event:** obtain a limited-season variation, with transparent future availability and no irreversible ranked power.
6. **Cooperative (later):** crew milestone shares a cosmetic recipe discovery with eligible contributors.

## Discovery state machine

`unknown` → `hinted` → `researchable` → `available_to_attempt` → `discovered` → `mastered`.

Not every recipe uses all states. Unlock logic should be data-driven and auditable; do not store an untyped text flag like `hasSecretX`. `discoveredAt`, `discoverySource`, `ruleVersion`, optional crafting `sourceTransactionId`, and a deduplication key are retained for trusted grants.

## Experiment flow

Player opens Recipe Journal → sees available clue and required station → enters Research mode (never silently while serving customers) → chooses ingredients or explicit merge branch → preview displays costs, rules, odds if any, and possible result category → player confirms → server validates requirements for resource-consuming action → system resolves deterministic recipe → discovery animation and one-time grant → journal entry, collection progress, achievement evaluation.

In physics-based puzzle discovery variants, the game must display a dedicated `Research Mode` label and a selectable recipe intent **before launch**. A normal tier-3 collision must not unexpectedly create a secret recipe and sabotage a customer's order.

## Hint system

Hints have three tiers: `environmental` (vague island story), `ingredient` (recognizable input or family), `procedure` (exact crafting station/sequence). Unlock hints predictably via progress or exploration. A player shouldn't have to search external wikis to understand a mandatory gameplay objective. Secret recipes are optional until explicitly revealed and made reachable.

## Discovery surprise and reveal

Animation: brief input gather → silhouette reveal → name plaque → recipe journal card → optional shareable moment. Keep the novelty animation skippable and nonblocking for repeat unlocks. A recipe is *discovered* only after the grant transaction is committed; if saving fails, display a recoverable pending state rather than lying about ownership.

## Anti-spoiler design

Unknown recipes can appear as silhouettes with category hints. User settings may hide secret recipe names and other players' collection displays. Avoid leaderboard reward text revealing protected puzzles. For localization, maintain tier/hint language quality and avoid images that directly contain spoiler strings.

## Failure cases

- Player tries a known invalid combination: no inventory debit if recipe isn't valid, unless an explicitly designed consumptive research mode clearly warns them.
- Repeated request/reconnect: one discovery grant only.
- Recipe removed after players discovered it: historical journal entry retained with retired indicator; grant not erased silently.
- Feature flag disabled: no crafting transaction, but previously earned journal remains viewable.
- Player lacks station/skill: show unlock path rather than a generic error.

## Acceptance criteria for future launch

Onboarding explains experimentation; all required inputs displayed; duplicate grants impossible; every publishable secret has at least one obtainable hint; player can complete campaign without discovering optional secret recipes; ranked gameplay unchanged; screen reader has a textual discovery description; analytics track hinted→attempted→discovered conversion without tracking sensitive user messages.
