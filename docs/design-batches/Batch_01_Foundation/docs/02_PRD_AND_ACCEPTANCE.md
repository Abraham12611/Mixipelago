# 02 — Product Requirements Document (PRD)

**Status:** v0.1.0 build contract + v0.1.1 prioritized improvements.  
**Owner:** Product lead; gameplay + UI + QA leads sign off.  
**Priority legend:** P0 = release blocker; P1 = first-week / next incremental release; P2 = later.

## Product problem

Casual merge games often offer satisfying short interactions but shallow context. Mixipelago connects the merge skill loop to future meaningful progression without burdening first-time users. Initial alpha must validate core gameplay **before** adding metagame complexity.

## Personas and jobs-to-be-done

| Persona | Need | Success signal |
|---|---|---|
| First-time casual player | Understand mechanics instantly | Completes first merge and first order without written manual |
| Mobile player | One-handed or comfortable two-thumb touch | Accurate launch, no page scroll while aiming, no clipped controls |
| Desktop player | Mouse/keyboard clarity | Clear centered arena, readable side panels, pointer feedback |
| Puzzle optimizer | Predictable physics and combos | Similar inputs produce intelligible outcomes, clear scoring |
| Returning player | Resume and pursue improvement | Best score/settings preserved; obvious continue action |
| Future collector/social player | Long-term goals | Architecture supports account, campaign and shop systems |

## P0 functional requirements

| ID | Requirement | Acceptance criteria |
|---|---|---|
| G-001 | Start session | From `/`, player can reach an interactive board in at most two actions after loading |
| G-002 | Aiming | Touch-drag/release and mouse-drag/release launch from a visible bottom source; cancel possible |
| G-003 | Fixed-step physics | Bodies advance at fixed timestep independent from rendering; no frame-rate-dependent motion |
| G-004 | Collision response | Different-tier drinks deflect, translate and optionally rotate based on collision state |
| G-005 | Valid merges | Two *eligible same-tier* drinks consume exactly once and create one next-tier drink |
| G-006 | Chain merges | New item may recursively merge, with correct order and no duplicate awards |
| G-007 | Catalog | At least eight tier IDs, distinct assets/fallbacks, accessible labels |
| G-008 | Order engine | Two visible orders with clear target tier, quantity, coin reward, completion state |
| G-009 | Session goals | A round ends on success or failure; result shows score, earned coins, reason, restart/next |
| G-010 | Score and currency | Scores and preview coins derive only from defined events; values cannot become NaN/negative inadvertently |
| G-011 | Mobile portrait | No horizontal scroll, safe-area support, touch targets, gameplay table dominant |
| G-012 | Desktop landscape | Clear game arena, responsive order and controls panels; keyboard escape/pause |
| G-013 | Local persistence | Tutorial seen, settings, preview wallet, latest unlocked mission and best score survive refresh |
| G-014 | Pause/recover | Visibility change pauses simulation; session can resume or be restarted without corruption |
| G-015 | SFX/control | Launch, clink, merge, success, fail audible after user gesture; music and SFX mute separate |
| G-016 | Deploy | Production URL reachable on common browsers; repeatable build; source-map/error reporting configured |
| G-017 | Test gates | Automated unit tests for merge logic and storage; manual UI verification requested from owner |

## P1 first-week requirements

- Tutorial hints, shot trajectory preview, improved score cascade and merge FX.
- Accessible control descriptions and keyboard aiming alternative.
- 3–10 **authored** mission configurations, difficulty ramps and a simple mission selection view.
- Persistent active-session snapshot if replay validation approach supports it safely; otherwise explicit restart after reload.
- Better orientation and viewport handling, quality presets, lazy audio loading.
- CI smoke tests on Safari/iOS and Chrome/Android via device QA.
- Minimal local achievements and polished result screen.

## P2 future feature buckets (overviews only)

- Branching island map, missions editor, economy ledger and shop upgrades.
- Real accounts, guest upgrade and cross-device progression.
- Server verification, leaderboard seasons and rewards.
- Skill trees, specializations, incidents, weather, NPC relationships, rival businesses, crews.
- Full content admin tools, push messaging, localization and native wrappers.

## Player stories + edge cases

1. **As a newcomer**, when I drag a drink, I see where it will launch; releasing sends it onto the table. A tap without drag does not accidentally spend a shot if below the launch threshold.
2. **As a puzzle player**, when an orange tier-2 collides with another orange tier-2, both become one tier-3. If it hits tier-4, no merge occurs and both move physically.
3. **As a player**, if three items overlap during a chain reaction, the simulation resolves a deterministic conflict priority and rewards each input at most once.
4. **As an order completer**, when an eligible output matches the next order, I see confirmation, the item is consumed as served, and the correct coin reward is awarded once.
5. **As a mobile player**, I can play at typical phone resolutions with the keyboard closed and no accidental browser zoom or page scroll on the arena.
6. **As a player returning after browser refresh**, I retain preferences/best score/preview coins, see clear local-save limitations, and can start a new round.
7. **As a player who loses**, I receive a reason (e.g., danger line reached after grace period), know the mission is replayable, and have a single prominent retry button.
8. **As a sound-sensitive player**, I can mute music without muting every gameplay sound or vice versa.
9. **As an offline or unstable-network player**, my local alpha does not stop moving glasses if the network pauses.

## Main product flow

```
Load app → Local profile/session hydrate → Title/Play
 → Tutorial (first launch only) → Start round
 → Aim → Launch → Physics contacts
 → Nonmatching collision OR eligible merge
 → Merge events → score/order evaluation → audio + visuals
 → New spawn/next preview → continue until win/fail
 → Summary → Local save → Replay/next mission/title
```

## Explicit session state machine

`boot → loading → ready → aiming → launched → settling → (resolving → ready)* → completed|failed → results → ready/new-session`.

`paused` overlays any active state and must preserve prior state. Pending collision operations must not continue while paused. `results` should never allow additional reward emissions from the just-ended session. Detailed state rules: `04` and `05`.

## UX acceptance checkpoints

- Current and next drink obvious at a glance.
- Order icons do not overlap launch zones.
- Badges/currency never crowd the central playable area.
- Critical button labels remain legible at smallest supported width.
- Text contrast and non-color signaling for states.
- No fake live backend components. Future links visibly disabled or labeled Preview.

## Analytics events (alpha)

`app_opened`, `game_loaded`, `tutorial_started/completed`, `session_started`, `shot_fired`, `collision_observed` (sampled), `drink_merged`, `order_fulfilled`, `session_completed`, `session_failed`, `session_retried`, `settings_changed`, `client_error`.

No sensitive or precise location data in alpha telemetry. See `19` and `25`.

## Nonfunctional requirements

- Responsive across phone portrait and desktop landscape; supported baseline browsers documented in QA.
- FPS target: 60 on target mid-range hardware, stable 30 fallback; thresholds tested, not assumed.
- Do not block input awaiting backend requests.
- No auth or secret key embedded in game build; no service-role credentials in client.
- Accessible keyboard interactions for core flow where practicable.
- Bundle budget and texture budget enforceable via CI reports.
- Release every approved incremental version behind feature flags as needed.

## Release acceptance: v0.1.0

All G-001 to G-017 checked; owner manually tests mobile and desktop; there is an accessible live URL; no known duplicate merge, frozen simulation, blank canvas or unhandled restart bug; game is fun enough to play repeatedly with placeholder assets. Future systems must not be depicted as operational if they are not.
