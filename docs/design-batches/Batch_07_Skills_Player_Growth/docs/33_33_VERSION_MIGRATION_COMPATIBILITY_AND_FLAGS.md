# 33 — Feature Flags, Catalog Migration, Compatibility and Rollback

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Feature flags (default OFF unless explicitly enabled)
`PROGRESSION_TRUSTED_XP_ENABLED`, `SKILLS_TREE_UI_ENABLED`, `SKILLS_ALLOCATION_ENABLED`, `SKILLS_HOSPITALITY_EFFECTS_ENABLED`, `SKILLS_ACTIVE_LOADOUTS_ENABLED`, `RECIPE_MASTERY_ENABLED`, `SKILLS_RESPEC_ENABLED`, `SKILLS_RANKED_NORMALIZED_ONLY` (safe default ON for ranked when present).

## Version boundaries
- `xpPolicyVersion` freezes XP thresholds/rewards for grant interpretation.
- `skillCatalogVersion` identifies node IDs, costs, effects, graph and ranks.
- `modifierPolicyVersion` identifies caps/stacking.
- `competitiveProfileVersion` normalizes ranked runs.
- `missionVersion` and `physicsVersion` remain controlled by prior batches.

## Publication migration checklist
Compare old/new catalog graph, active profile distribution, deleted nodes, reordered effects and point-cost changes. Generate a reconciliation proposal and produce a dry-run report. If a published node becomes incompatible, suspend it safely and issue a refund or migration migration receipt, never silently remove the player's earned points.

## Kill-switch behaviors
Turning off trusted XP must stop **new** grants while preserving recorded history. Turning off allocation hides Learn commands and leaves ranks saved. Turning off a risky modifier prevents future payouts from applying it, but does not rewrite prior valid transactions. Turning off active loadouts reverts to mode baseline without corrupting loadout rows.

## Rollback test
Play v0.4.1 skill-purchased profile under v0.4.0 fallback: UI states the skill is temporarily inactive; backend reads remain valid; future upgrade resumes safely. Revert content pointer, not SQL migrations destructively.
