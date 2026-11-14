# Mixipelago — Design Batches 1–21

These batches are canonical engineering handoff documents organized by subject. Each folder contains a README/index and independent specifications, plus example assets and validators when applicable.

1. [Batch 01 — Foundation](Batch_01_Foundation/docs/00_README.md)
2. [Batch 02 — Physics](Batch_02_Physics/docs/00_INDEX.md)
3. [Batch 03 — Drinks & Recipes](Batch_03_Drinks_Recipes_Discovery/docs/00_INDEX_AND_README.md)
4. [Batch 04 — Gameplay Modes](Batch_04_Gameplay_Modes_Level_Design/README.md)
5. [Batch 05 — Campaign & Islands](Batch_05_Islands_Maps_Mission_Progression/docs/00_INDEX_AND_README.md)
6. [Batch 06 — Economy & Shops](Batch_06_Economy/docs/00_INDEX_AND_README.md)
7. [Batch 07 — Skills & Player Growth](Batch_07_Skills_Player_Growth/docs/00_INDEX_AND_README.md)
8. [Batch 08 — Rewards, Achievements & Collections](Batch_08_Rewards_Achievements_Collections/docs/00_INDEX_AND_README.md)
9. [Batch 09 — Customers, Personalities & Reputation](Batch_09_Customers_Personalities_Reputation/docs/00_INDEX_AND_README.md)
10. [Batch 10 — World Simulation & Dynamic Incidents](Batch_10_World_Simulation_Dynamic_Incidents/docs/00_INDEX_AND_README.md)
11. [Batch 11 — Stories, Characters, Quests & Rival Businesses](Batch_11_Stories_Characters_Quests_Rivals/docs/00_INDEX_AND_README.md)
12. [Batch 12 — Events, Festivals & Live World](Batch_12_Events_Festivals_Live_World/docs/00_INDEX_AND_README.md)
13. [Batch 13 — Leaderboards, Rankings & Tournaments](Batch_13_Leaderboards_Rankings_Tournaments/docs/00_INDEX_AND_README.md)
14. [Batch 14 — Friends, Crews, Cooperation & Multiplayer](Batch_14_Friends_Crews_Cooperation_Multiplayer/docs/00_INDEX_AND_README.md)
15. [Batch 15 — Complete UI/UX & Design System](Batch_15_UI_UX_Design_System/docs/00_INDEX_AND_README.md)
16. [Batch 16 — Art Direction, Characters & 2.5D Asset Production](Batch_16_Art_Direction_Characters_2_5D_Assets/docs/00_INDEX_AND_README.md)
17. [Batch 17 — Music, Sound Effects, Animations & Game Feel](Batch_17_Music_SFX_Animations_Game_Feel/docs/00_INDEX_AND_README.md)
18. [Batch 18 — Backend, Database, Game Services & Admin Studio](Batch_18_Backend_Database_Services_Admin/docs/00_INDEX_AND_README.md)
19. [Batch 19 — Security, Anti-Cheat & Game Integrity](Batch_19_Security_Anti_Cheat_Game_Integrity/docs/00_INDEX_AND_README.md)
20. [Batch 20 — Monetization, Analytics, Retention & Live Operations](Batch_20_Monetization_Analytics_Retention_LiveOps/docs/00_INDEX_AND_README.md)
21. [Batch 21 — Native Mobile, Performance, Scaling & Release Engineering](Batch_21_Native_Mobile_Performance_Release_Engineering/docs/00_INDEX_AND_README.md)

## Precedence

- Batch 02 owns physics/merge simulation semantics.
- Batch 03 owns the eight-tier alpha catalog and automatic order-serving priority.
- Batch 04 owns mission objectives, result interpretation, and scoring.
- Batch 05 owns world graph and unlock state.
- Batch 06 owns trusted wallet, economic ledger, purchases, and shop upgrades.
- Batch 07 owns trusted player XP, level milestones, skill allocation and respec; Batch 06 remains authoritative for shop/economy modifiers, and standardized ranked profiles ignore personal build power.
- Batch 08 owns achievement evidence, claim entitlements, collectible ownership and presentation. It does not mint coins or XP directly; Batch 06 and Batch 07 remain authoritative issuers.
- Batch 09 owns fictional customer identity, future deterministic encounter reservation and derived verified satisfaction/relationship observations. Batch 03/04 own order service; Batch 06 owns shop reputation/economics; Batch 07 owns skills; Batch 08 owns souvenir entitlements.

- Batch 10 owns world condition snapshots and incident offers; Batch 06 alone moves coins and insurance payouts.
- Batch 11 owns story/quest flags and authored NPC arcs; Batch 04/05 own mission and campaign evidence.
- Batch 12 owns event calendar editions and participation; Batch 08 owns collectibles; Batch 13 owns ranked event scoring.
- Batch 13 owns certified replay verification, official rankings, season freezes, tie-breaks and prize eligibility.
- Batch 14 owns consented friend/crew relationships and match orchestration; only server-authoritative live matches can establish real-time outcomes.
- Batch 15 owns semantic UI tokens, responsive components and route visibility; it never changes gameplay/financial authority.
- Batch 16 owns original artwork, asset IDs, rights provenance and 2.5D exports; it never changes collision physics.
- Batch 17 owns original audio, cue bus mixing, sensory presentation and haptic preferences; it never changes rules or rewards.
- Batch 18 owns trusted backend transactions, database schemas, content publishing, admin access and outbox projections.
- Batch 19 independently owns security verification, negative tests, anti-cheat and incident response; risk controls apply across all domains.
- Batch 20 owns optional commerce policies, analytics and live experiment controls; provider receipts issue only verified entitlements via owning backend.
- Batch 21 owns native packaging, performance, platform adapters, store compliance and release engineering; all game rules remain shared.

[Read the Batches 10–15 authority and release matrix](CROSS_BATCH_AUTHORITY_AND_RELEASES.md), and the [Batches 16–21 integration/release matrix](Batch_16_to_21_Integration/CROSS_BATCH_AUTHORITY_AND_RELEASES.md).

Conflicts must be resolved through an explicit ADR and versioned contract changes. Local preview coins must never become authoritative balances.

## Status

**Documentation only.** Validate example schemas and test fixtures before implementation; run actual physics/UI tests during engineering development. Product owner approves manual UI/gameplay tests.
