# Mixipelago — Design Batches 1–7

These batches are canonical engineering handoff documents organized by subject. Each folder contains a README/index and independent specifications, plus example assets and validators when applicable.

1. [Batch 01 — Foundation](Batch_01_Foundation/docs/00_README.md)
2. [Batch 02 — Physics](Batch_02_Physics/docs/00_INDEX.md)
3. [Batch 03 — Drinks & Recipes](Batch_03_Drinks_Recipes_Discovery/docs/00_INDEX_AND_README.md)
4. [Batch 04 — Gameplay Modes](Batch_04_Gameplay_Modes_Level_Design/README.md)
5. [Batch 05 — Campaign & Islands](Batch_05_Islands_Maps_Mission_Progression/docs/00_INDEX_AND_README.md)
6. [Batch 06 — Economy & Shops](Batch_06_Economy/docs/00_INDEX_AND_README.md)
7. [Batch 07 — Skills & Player Growth](Batch_07_Skills_Player_Growth/docs/00_INDEX_AND_README.md)

## Precedence

- Batch 02 owns physics/merge simulation semantics.
- Batch 03 owns the eight-tier alpha catalog and automatic order-serving priority.
- Batch 04 owns mission objectives, result interpretation, and scoring.
- Batch 05 owns world graph and unlock state.
- Batch 06 owns trusted wallet, economic ledger, purchases, and shop upgrades.
- Batch 07 owns trusted player XP, level milestones, skill allocation and respec; Batch 06 remains authoritative for shop/economy modifiers, and standardized ranked profiles ignore personal build power.

Conflicts must be resolved through an explicit ADR and versioned contract changes. Local preview coins must never become authoritative balances.

## Status

**Documentation only.** Validate example schemas and test fixtures before implementation; run actual physics/UI tests during engineering development. Product owner approves manual UI/gameplay tests.
