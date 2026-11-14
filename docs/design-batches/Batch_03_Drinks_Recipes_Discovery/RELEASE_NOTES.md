# Mixipelago Batch 3 Documentation Release Notes

**Created:** November 14, 2026. **Status:** proposed design specifications / engineering handoff, not an implemented game build.

## What's new

- Eight-tier canonical drink bible, preserving Batch 1 names and output-tier scoring.
- Explicit compatibility and future recipe graph design, without modifying alpha merge behavior.
- Detailed design for ingredients, secret discoveries, collectible rarity, recipe journal and drink mastery (future gated).
- Customer order servicing, spawn fairness, theoretical input costs and mission feasibility guidance.
- TypeScript contract sketches, data models, API boundaries, content authoring workflow, versioning, analytics and QA.
- Parallel engineering workstreams and release slices aligned with the first playable alpha.
- JSON catalog, JSON schema, candidate mission, future-disabled crafting example, rule vectors, conceptual session log and validation tool.

## Key compatibility safeguards

- **Tier 8 is terminal.**
- **Only equal tiers 1–7 merge into the next tier in alpha.**
- **New merge output is auto-served to oldest eligible order before remerge.**
- **Reward currency remains preview-only in alpha.**
- **Catalog and simulation rules are pinned per run.**

## Outstanding questions

See `docs/26_DESIGN_DECISIONS_RISKS_AND_OPEN_QUESTIONS.md`. No implementation is required for future features until owner acceptance.
