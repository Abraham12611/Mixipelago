# 07 — Master Mixologist Skill Branch: Design and Constraints

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Identity and gameplay
This branch makes the player better at reading the merge board, understanding craft progression and enjoying chain reactions. It rewards knowledge without turning the eight-tier chain into a different game for every account.

## Proposed node progression
1. `mm_clear_sight` — tier silhouette outline and recipe tooltip on tap; rank 1; baseline access to contrast/labels remains free.
2. `mm_combo_notebook` — clearer visualization of combo history and contributing sources; prerequisite Clear Sight.
3. `mm_recipe_student` — eligible recipe mastery XP bonus (later feature); does not grant permanent player XP; prerequisite Combo Notebook.
4. `mm_craft_memory` — show last-three merge evolution traces in session; no auto merging.
5. `mm_signature_finish` — cosmetic celebratory finish after higher-tier crafts; optional profile badge; no added tier score.

## Prototype values
- First three nodes are eligible to be piloted in v0.4.0 only when technical implementation and accessibility review are complete. `mm_recipe_student` remains gated until verified recipe mastery exists.
- Visibility features must not be counted as mandatory paid/premium assist; normal tier labels and color-independent recognition are basic UI.
- The branch does not increase physical shot force, collision restitution, aim friction, tier compatibility or ranked scoring.

## Testing
Compare board labels before/after perk on small screens; ensure the extra HUD can be dismissed, is keyboard-accessible and doesn't obscure a shot line. A chain reaction occurring while a help overlay is open must not stop the physics or duplicate an event.
