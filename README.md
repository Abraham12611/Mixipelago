# Mixipelago

**Web-first tropical drink-shooting and merging game.** Responsive desktop/mobile browser experience, designed for rapid playable-alpha releases and iterative expansion into islands, shops, skills, events, and social competition.

## Engineering documentation

The complete design handoff for **Batches 1–21** is under [docs/design-batches/](docs/design-batches/README.md), with separate Markdown chapters, schemas, content examples, QA fixtures, and validation scripts.

| Batch | Subject | Start here |
|---|---|---|
| 01 | Foundation & Engineering Handoff | [Index](docs/design-batches/Batch_01_Foundation/docs/00_README.md) |
| 02 | Physics, Shooting & Merging | [Index](docs/design-batches/Batch_02_Physics/docs/00_INDEX.md) |
| 03 | Drinks, Recipes & Discovery | [Index](docs/design-batches/Batch_03_Drinks_Recipes_Discovery/docs/00_INDEX_AND_README.md) |
| 04 | Gameplay Modes & Level Design | [Index](docs/design-batches/Batch_04_Gameplay_Modes_Level_Design/README.md) |
| 05 | Islands, Maps & Mission Progression | [Index](docs/design-batches/Batch_05_Islands_Maps_Mission_Progression/docs/00_INDEX_AND_README.md) |
| 06 | Economy, Businesses & Shop Management | [Index](docs/design-batches/Batch_06_Economy/docs/00_INDEX_AND_README.md) |
| 07 | Skill Trees, Specializations & Player Growth | [Index](docs/design-batches/Batch_07_Skills_Player_Growth/docs/00_INDEX_AND_README.md) |
| 08 | Rewards, Achievements & Collections | [Index](docs/design-batches/Batch_08_Rewards_Achievements_Collections/docs/00_INDEX_AND_README.md) |
| 09 | Customers, Personalities & Reputation | [Index](docs/design-batches/Batch_09_Customers_Personalities_Reputation/docs/00_INDEX_AND_README.md) |
| 10 | World Simulation & Dynamic Incidents | [Index](docs/design-batches/Batch_10_World_Simulation_Dynamic_Incidents/docs/00_INDEX_AND_README.md) |
| 11 | Stories, Characters, Quests & Rival Businesses | [Index](docs/design-batches/Batch_11_Stories_Characters_Quests_Rivals/docs/00_INDEX_AND_README.md) |
| 12 | Events, Festivals & Live World | [Index](docs/design-batches/Batch_12_Events_Festivals_Live_World/docs/00_INDEX_AND_README.md) |
| 13 | Leaderboards, Rankings & Tournaments | [Index](docs/design-batches/Batch_13_Leaderboards_Rankings_Tournaments/docs/00_INDEX_AND_README.md) |
| 14 | Friends, Crews, Cooperation & Multiplayer | [Index](docs/design-batches/Batch_14_Friends_Crews_Cooperation_Multiplayer/docs/00_INDEX_AND_README.md) |
| 15 | Complete UI/UX & Design System | [Index](docs/design-batches/Batch_15_UI_UX_Design_System/docs/00_INDEX_AND_README.md) |
| 16 | Art Direction, Characters & 2.5D Asset Production | [Index](docs/design-batches/Batch_16_Art_Direction_Characters_2_5D_Assets/docs/00_INDEX_AND_README.md) |
| 17 | Music, Sound Effects, Animations & Game Feel | [Index](docs/design-batches/Batch_17_Music_SFX_Animations_Game_Feel/docs/00_INDEX_AND_README.md) |
| 18 | Backend, Database, Game Services & Admin Studio | [Index](docs/design-batches/Batch_18_Backend_Database_Services_Admin/docs/00_INDEX_AND_README.md) |
| 19 | Security, Anti-Cheat & Game Integrity | [Index](docs/design-batches/Batch_19_Security_Anti_Cheat_Game_Integrity/docs/00_INDEX_AND_README.md) |
| 20 | Monetization, Analytics, Retention & Live Operations | [Index](docs/design-batches/Batch_20_Monetization_Analytics_Retention_LiveOps/docs/00_INDEX_AND_README.md) |
| 21 | Native Mobile, Performance, Scaling & Release Engineering | [Index](docs/design-batches/Batch_21_Native_Mobile_Performance_Release_Engineering/docs/00_INDEX_AND_README.md) |

**Cross-batch contract and release matrix:** [Batches 10–15](docs/design-batches/CROSS_BATCH_AUTHORITY_AND_RELEASES.md). [Batches 16–21](docs/design-batches/Batch_16_to_21_Integration/CROSS_BATCH_AUTHORITY_AND_RELEASES.md). The new systems are documented, not deployed; all future-specific gates default OFF.

## Initial development target

**v0.1.0:** a minimal, playable browser alpha: physics-driven glass launches, angled collisions, same-tier merges, eight-tier drink evolution, customer orders, scoring, and responsive controls. Extend with small, tested releases (v0.1.1, v0.1.2, v0.2.0...).

**Important:** These documents are *design and engineering specifications*, not evidence that a feature or deployment is already working. The trusted currency/shop economy described in Batch 6 is targeted at **v0.3.0+**; Batch 7's trusted XP and first skill slice target **v0.4.0+**. Batch 8's first verified achievement, entitlement and cosmetic ownership slice is proposed for **v0.4.1+**, behind backend verification and feature gates. Batch 9 customer satisfaction and trusted shop reputation are a proposed **v0.4.2+** feature; dynamic guests, loyalty and VIPs are further gated. Alpha preview coins and local scores are not trusted wallets, XP, guest reputation, or durable collectible entitlements.

The art/audio pipeline (16–17) supports the browser alpha, backend/security (18–19) gates trusted grants and competitive proof, monetization (20) remains optional and OFF by default, and native packaging (21) follows web playability and current store reviews.

Engineers submit PRs and do **not** merge their own work. Manual UI/gameplay testing is directed to the project owner.
