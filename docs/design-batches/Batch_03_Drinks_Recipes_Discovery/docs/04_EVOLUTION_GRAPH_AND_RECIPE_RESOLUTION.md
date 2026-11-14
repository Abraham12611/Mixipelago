# 04 — Evolution Graph and Recipe Resolution (Future-Safe Design)

## Why a graph

One linear chain is sufficient for early play but does not accommodate regional beverages, special festival editions, collection secrets and recipe experiments. We need a future-safe *recipe graph* with explicit directed edges rather than `if (tier === n) return n+1` embedded throughout renderer code.

**Alpha: exact one-chain recipe resolver.** The generalized graph is defined now but feature-gated off until a designated future minor release. No alpha engineer should ship branch selection or transform identical tiers into alternative outputs.

## Recipe rule shape

A recipe contains immutable ID/version, unordered or ordered ingredient/input multiset, context constraints, output drink ID, priority, unlock rule, repeatability, rarity of discovery (not combat power), score source, eligible modes and fallbacks. Recipe rules must be run through the content validator. If two possible rules match an input pair under the same context, publication fails unless explicit deterministic precedence/selection is declared and reflected in UI.

For the core ladder, the resolver maps `core tier N ×2 -> core tier N+1` and never consults runtime player preferences.

## Proposed resolution precedence for later modes

1. Determine mission's allowed rule-set and immutable recipe-manifest hash.
2. Determine input IDs, active/armed status, input order if recipe is ordered, and contact eligibility from Batch 2.
3. Filter rules by recipe input multiset and context gates (mode, island, player unlock, required station).
4. If a special selected recipe is activated by the player prior to launch/contact, resolve it explicitly and show an indicator.
5. Otherwise fall back to the canonical linear same-tier evolution where applicable.
6. If multiple active rules remain, reject publication or reject the action with a logged rule ambiguity; **never choose randomly during collision processing**.
7. Emit the chosen `recipeId` and version in the merge semantic event so replay/QA can reproduce outcome.

## Candidate mode families (not approved for alpha)

- **Regional ladder:** same matching rule but a different 8–10-tier theme; one active family per mission.
- **Crafting station:** ingredients combine outside the physics board to produce a discoverable recipe card, without changing the core 2-to-1 merge rule.
- **Festival variants:** skin/decoration changes the appearance of drinks while retaining canonical gameplay identity.
- **Branch-select puzzle:** choose a recipe path in advance at a signed recipe junction, e.g. route a tier-4 output to a tropical or herbal branch; the choice must be explicit and shown on the board.
- **Conditional infusion:** specific boost/station turns an output into a new item via a *separate post-merge transformation*, recorded as distinct event, never disguised as an ordinary merge.

## Graph validation

Run offline checks for missing nodes, accidental cycles, invalid tier regressions, unreachable target recipes, score farming loops, ambiguous matching, incompatible modes, retired outputs, unreachable unlocks, and locale/asset availability. A planned prestige loop may be cyclic only if explicitly bounded and cannot generate unlimited rewards.

## Algorithm and complexity

Precompile a recipe index from immutable manifest: `(mode, normalizedInputKey)` to candidate rules. For two-input recipes the index lookup is O(1) expected; context filtering is bounded by a small candidate set. Avoid walking the whole recipe graph for every Rapier collision. Graph traversals for UI reachability are done offline or cached. Resolve rules in pure TypeScript without Phaser/Rapier imports.

## Contract with Batch 2

`MergeArbiter` chooses unique candidate pairs and reserves body IDs; a pure `RecipeResolver` answers `eligible / output / recipeId / version`. The arbiter keeps responsibility for deterministic pair sorting, collision geometry, transition states, new body creation, next-step remerge and serving priority. The content system must never destroy physics bodies or award rewards directly.

## Tests and feature gate

Validate (a) every alpha same-tier pair, (b) every alpha mismatched pair, (c) max-tier no-merge, (d) precomputed graph exactness, (e) ambiguity rejection, (f) player-unlocked recipe eligibility, (g) same manifest+context gives same result, (h) retired recipe replay still resolves from pinned manifest. Rollout with a distinct `rulesVersion` and compare old/new golden fixtures before publish.
