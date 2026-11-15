# 22 — Compatibility with the 21-Batch Main Roadmap

The 21-batch engineering documentation remains authoritative for future Mixipelago releases; **contest scope supersedes broad feature ambition but never secretly changes the physics contract**.

| Main batch | Reused in contest edition | Deferred |
|---|---|---|
| 01 Foundation | Technical direction, web-first UX, acceptance discipline | Extensive production setup |
| 02 Physics | Aiming, friction feel, fixed step, merge arbiter, terminal priorities | Full physics tuning lab |
| 03 Drinks | Eight-tier linear catalog, score table, auto-serving | Branching recipes and ingredient inventory |
| 04 Modes | Classic Service, mission result, stars | Rush/Survival/VIP, rankings |
| 05 Islands | Small Coconut Cove mission graph and published-only map | Other islands, 100s missions |
| 06 Economy | Preview-only local coin label | Trusted ledger, shop purchase/insurance |
| 07 Skills | No skill changes to physics | XP and skill tree |
| 08 Rewards | Optional local decorative stars/badges | Trusted rewards/chests |
| 09 Customers | Simple original portraits, scripted orders | VIP pool, satisfaction/loyalty |
| 10–14 World/social | Festive cosmetic skin only, optional | Live simulation, quests, events, ranked/social/multiplayer |
| 15 UI/UX | Tokens, responsive game/HUD/map/results | Future disabled sections |
| 16 Art | Original 2.5D sprite pipeline, asset rights | World-scale asset production |
| 17 Audio | SFX/music, cue buses, reduced motion | Adaptive multi-stem soundtracks |
| 18–19 Backend/security | Safe local guest app, validate content and no exposed secrets | Trusted grants, server proof, anti-cheat league |
| 20 Monetization | None | Ad integrations, IAP, subscriptions, premium passes |
| 21 Mobile/release | Browser performance/device testing | Native App Store/Play deployment |

## Compatibility invariants

1. The original alpha tier-8 remains terminal.
2. Serving a newly merged matching output takes precedence over remerge.
3. Pure reducers, not audio/render callbacks, decide mission outcomes.
4. Physics world coordinates and UI coordinates stay separate.
5. No conversion from preview coins to trusted currency.
6. Contest guest saves are isolated from future main-game saves.
7. Owner manual testing requirement remains in force.
8. Future features default OFF until independently approved and tested.

## Branch/repository design

Keep this folder under **docs/contest/base44-nitro-2026** in existing repository. Build the new Base44 app as a separate codebase in Base44, optionally connected to a **separate source repository**. This reduces risk that Base44 sync clobbers the 21 design-batch library and preserves the new-build evidence. If the owner wants everything in one repo, add a scoped **apps/contest-base44/** source directory only after Base44 sync proof and documented synchronization policy.

## Intellectual property and timing

Reusing abstract design knowledge is not a guarantee of new-build eligibility. The organizer may review historic idea documents and game similarity. Preserve authentic timeline and request a binding clarification when uncertainty remains. Never backdate art, erase history or suggest a finished pre-existing project was newly created.
