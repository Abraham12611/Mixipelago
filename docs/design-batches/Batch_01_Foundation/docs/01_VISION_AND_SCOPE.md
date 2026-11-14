# 01 — Vision, Positioning, Product Principles and Scope

## Elevator pitch

**Mixipelago** is a premium-feeling, browser-first casual puzzle adventure. Players shoot colorful drinks across a low-friction tabletop; matching glasses merge into increasingly elaborate recipes. They serve customer orders, earn rewards, and eventually build shops and explore a branching archipelago of missions, upgrades, rivals, events, and friendly competition.

The gameplay should be understandable in 30 seconds, rewarding for 5-minute sessions and capable of supporting hundreds of hours of evolving content. **The drink-shooting and merging must remain the joyful heart of the experience.**

## Origin and originality

Source inspiration is an externally developed tropical casual game illustrated in the user's provided screenshots (named *Merge Shooter* in those screenshots). The source appears to combine launching drinks across a wooden tabletop, merging same-tier items, customer orders, scores, boosters and island-themed promotion. Exact hidden rules are **not** verified from screenshots. For Mixipelago, we are designing original systems and art; do not extract source code, reproduce original artwork/audio, or reuse third-party trademarks/character designs.

Distinctive Mixipelago identity (proposed): branching islands; persistent shop improvements; deep but gradual player specialization; meaningful coin sinks; a well-balanced event director; local-to-global competition; **Island Chronicle** to remember milestones. These future differentiators must not delay the first playable build.

## Six pillars and their initial implementation status

1. **Merge & Serve:** fully playable for v0.1.0; expand modes over time.
2. **Explore & Conquer:** teaser/placeholder in v0.1.0; mission configurations in v0.1.1; branching map from v0.2.0.
3. **Build & Prosper:** currency shown but local-only initially; trusted shop economy from v0.3.0.
4. **Specialize & Evolve:** architecture hooks; skill tree from v0.4.0 or after.
5. **Compete & Cooperate:** local high-score display initially; server-verified leaderboards from v0.5.0.
6. **Living Consequences:** design overview now, event implementation after core economy and recovery loops.

## Core experience pillars translated into product rules

- **Game first:** immediate load-to-play; never require the player to navigate a business simulator before the first merge.
- **Readable:** one obvious active drink, clear next drink, visible customer requests and rewards, unambiguous merge feedback.
- **Juicy but controlled:** responsive aim/release; smooth gliding; precise collisions; satisfying SFX/particles without excessive flashes or clutter.
- **Fair:** economy/upgrade choices must not make ranked competitive play pay-to-win; incidents must permit recovery.
- **Personal:** future business, skill and map choices are meaningful instead of decorative click-throughs.
- **Playable on real phones:** touch-first controls with desktop mouse parity, responsive viewports, quality fallback, save recovery.
- **Incremental:** independent feature flags and compatible data contracts support frequent web deployments.
- **Affordable to operate:** static/CDN art, local physics and judicious use of servers; no per-merge AI calls.

## Target audiences

- Casual puzzle fans seeking bright, satisfying 3–10 minute sessions.
- Progression-driven players who enjoy islands, achievements and unlocking content.
- Collection/decor enthusiasts who enjoy upgrades and world-building.
- Competitive players seeking legitimate skill-based leaderboards (future).
- Mobile web users who may install an app later.

## Player fantasy

Start with a tiny beach stand, create increasingly exotic drinks, become a well-known island entrepreneur, then cultivate a world that reflects personal decisions. Narrative flavor is friendly, optimistic, adventurous and lightly whimsical—not cynical or punishing.

## High-level journeys

**First-time session:** start → 20-second aim tutorial → first merge → serve first customer → earn coins → finish round → see next objective.

**Returning session (early):** resume → play puzzle → complete orders → check progress → continue.

**Future meta session:** world map → choose path → mission → rewards → upgrades/skill choice → return to map.

## Release boundaries

### In scope for v0.1.0 (must be true gameplay)

- Splash/loading; start game; one responsive tabletop, original placeholder/curated art.
- Aiming and launching a drink via touch/mouse and optional keyboard fallback.
- 2D rigid-body movement and collisions; 8 sequential drink tiers; compatible merges.
- Two customer requests and visible requested tiers; automatic serving on qualifying generated items (decision documented in `05`).
- Round goals (complete N orders or earn score), score, coins, completion/failure, restart.
- Local persistence of tutorial flag, settings, best score and *preview* coins.
- Game audio events, mute, pause, next preview, basic settings/help.
- Browser deployment; mobile portrait and desktop landscape.
- Error boundary, loading fallback, basic analytics and performance instrumentation.

### Deliberately excluded from v0.1.0

- Network-based coin wallet, cross-device account/sync, purchases, monetary prizes.
- Public/global/local/friends leaderboards, crews, tournaments or live multiplayer.
- Skill trees, equipment buffs, complex NPC dialogue, insurance, fires, loans.
- Rich island-map engine and hundreds of missions.
- Generative runtime quests, realtime weather, AI customer dialogue.
- Real-world location collection or precise geopositioning.

### In scope for later increments

Refer to `09`–`12` and `24`. Those are **overview/placeholder requirements**, not permission to build without further design work.

## Success criteria for alpha

Qualitative: users understand where to aim, recognize matching items, enjoy collisions, understand order completion and do not find UI distracting. Quantitative targets are proposed test gates: 0 critical blockers, consistent 30+ FPS on defined fallback devices, correct merge counts, no persistent coin duplication, and reproducible scripted gameplay tests. Retention targets require actual user data; do not invent success numbers.

## Tone and visual distinctiveness

Warm sunlight, lagoon blues, coral pinks, mango orange, cream panels, restrained purple highlights, lush isometric island backdrops and glossy drinks. **Cleaner than the reference screenshots**: fewer simultaneous badges, more consistent spacing, tighter UI hierarchy, unique iconography and characters, responsive states. Prefer original game-ready layered assets rather than flattened screenshot-like artwork.

## Design non-goals

- Not a realistic bartending simulation.
- Not a fully 3D open-world game at launch.
- Not a blockchain/NFT economy.
- Not an on-device AI generation app at runtime.
- Not a clone of specific copyrighted characters, UI artwork, or source progression.
