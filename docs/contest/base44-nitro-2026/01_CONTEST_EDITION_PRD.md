# 01 — Product Requirements: Coconut Cove Contest Edition

## Product thesis

A playful seaside cocktail bar becomes a tactile physics puzzle: aim a glass, shoot it onto the bar top, merge identical tiers into more elaborate tropical creations, and fulfill customer requests before the serving area jams. The novelty is **physical collisions + drink evolution + timed service fantasy + an island route map**, not copying another game's UI.

## Primary player

Casual mobile and desktop browser player who has never visited Mixipelago. Must discover the basic interaction and enjoy the first success within the first minute. The experience should reward clever rebounds and merge chains, not just repeated random tapping.

## Non-negotiable user stories

- As a visitor I can open the public Base44 URL in a private window and press **Play** without account, card, downloads or browser extension.
- As a new player I can learn aim → release → collide → merge → serve, with an interactive 30–60 second tutorial and **Skip/Replay** controls.
- As a player I see the next launch drink, active customer orders, session progress, board danger and pause.
- As a player I can retry failed missions immediately without a penalty or mandatory ad.
- As a player I can move across a small Coconut Cove island map and replay accessible missions.
- As a player I can see score, optional stars and personal-best records; every prize/coin is **local and illustrative**, not a trusted wallet.
- As a player on a phone I can play with touch gestures; as a desktop player with mouse and keyboard.
- As a player sensitive to sound/motion I can mute audio, pause, use reduced-motion options and understand icons with labels.

## Core session loop

1. **Home → Play → Coconut Cove map** (new visitor may go directly to first mission).
2. Select mission; see the goal in one concise preview.
3. Launch glasses via drag and release; physics progresses at a fixed-step rate.
4. Identical tiers merge; a newly produced drink that matches an active request automatically serves **oldest qualifying order first**.
5. Player completes order/mission goal, or loses to danger/shot budget per mission config.
6. Results show performance, preview coins / non-spendable decorative stars, personal best, replay, and next mission.
7. Local save advances map only; no account, payout, remote competition or economic transaction.

## Core content target

- One art-complete Coconut Cove environment and map with **12 tested missions**, 3 four-mission chapters.
- Eight canonical tier identifiers from Batch 3; tier 8 does not merge.
- Two active customer orders in the starter level; later authored levels may vary deliberately.
- Classic Service in every level. Optional **Festival Rush** special stage only after the core is polished and proven feasible.
- Three or four distinct customer portraits (not necessarily authored persistent loyalty profiles).
- Original visual/sonic identity and one visible replay reason: best score/stars or a clean special challenge.

## Success metrics (internal targets, not contest rules)

- Load playable home quickly on a mainstream smartphone/network; target first interactive feedback in about 3 seconds on a warm connection, record actual devices and network tests.
- Tutorial completion and first successful merge without ambiguous gestures.
- No persistent loss of local progress after refresh.
- 30–60 FPS presentation as device permits; **fixed-step simulation** correctness is independent of FPS.
- Zero P0/P1 bugs, no dead-end campaign node, no broken game controls on representative mobile and desktop browsers.
- Every of the 12 published missions has a recorded verified winning playthrough or automatic feasibility evidence plus owner signoff.

## Out of scope

Online ranked results; social/friends; live incidents; shops with purchase flows; skill trees; subscriptions; rewarded ads; account sync; debt/insurance; native mobile packaging; new drink families; event server; admin CMS. They remain in the main 21-batch roadmap and must not leak into contest navigation.
