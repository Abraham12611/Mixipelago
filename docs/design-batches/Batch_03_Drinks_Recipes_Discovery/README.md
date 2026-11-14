# Mixipelago — Batch 03: Drinks, Recipes & Discovery

A standalone engineering documentation pack with **35 Markdown documents** (`docs/00` through `docs/34`) plus machine-readable example fixtures, a schema, rule vectors and a validation script.

Start at [`docs/00_INDEX_AND_README.md`](docs/00_INDEX_AND_README.md), then read `03_ALPHA_EIGHT_TIER_DRINK_BIBLE.md`, `09_CUSTOMER_ORDERS_AND_RECIPE_REQUIREMENTS.md`, `11_PHYSICS_TO_CONTENT_BOUNDARIES.md`, `18_TYPES_EVENTS_AND_API_CONTRACTS.md`, `22_TEST_PLAN_AND_EDGE_CASES.md`, `24_RELEASE_SLICES_AND_DEPENDENCIES.md` and `32_FORMAL_RULES_AND_PSEUDOCODE.md`.

**This is Batch 3 documentation, not a playable implementation.** The current alpha remains an eight-tier linear merge game; branching recipes, ingredients, rarity ownership, collections and mastery are concept-level future modules protected by feature gates.

### Sources of truth

This pack was aligned with the earlier Batch 1 and Batch 2 documentation. In the combined ZIP they live at `Batch_01_Foundation/` and `Batch_02_Physics/`. This directory is `Batch_03_Drinks_Recipes_Discovery/`.

### Validation

Run `python tools/validate_batch3.py` from this folder. It performs structural, graph, fixture and consistency checks. It does **not** substitute for actual game engine/playability tests.
