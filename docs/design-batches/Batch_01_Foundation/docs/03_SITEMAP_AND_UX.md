# 03 — App Map, Routes, Responsive UX and Interaction States

## Navigation principle

The **gameplay canvas** is full attention. Surrounding **application UI** is React. Small stable route hierarchy, with future routes registered behind flags. Do not render all panels and modals simultaneously. Desktop and mobile share feature semantics, not necessarily layout geometry.

## Route sitemap by version

```
/                              Landing/title [v0.1.0]
/play                          Gameplay shell + Phaser canvas [v0.1.0]
/play?mission=<slug>           Optional authored mission in v0.1.1
/help                          Controls, rules, accessibility [v0.1.0]
/settings                      Audio, graphics, controls [v0.1.0]
/results                       Optional route; preferably in-game result state [v0.1.0]
/map                           Mini mission chooser/teaser [v0.1.1]; full graph [v0.2.0]
/profile                       Local player stats [v0.1.1]; account identity later
/shop                          Future shop management [v0.3.0]
/shop/[shopId]                 Future property details [v0.3.0]
/skills                        Future skill tree [v0.4.0]
/leaderboards                  Future verified season rankings [v0.5.0]
/leaderboards/[seasonId]       Historical rankings [later]
/friends                       Social graph [later]
/crews                         Cooperative teams [later]
/events                        Global/individual event listings [later]
/events/[eventId]              Event details/decision flow [later]
/chronicle                     Player history [later]
/collection                    Discovered recipes/cosmetics [later]
/auth                          Sign in/upgrade guest [later]
/admin                         Auth-restricted content tools [later]
/privacy                       Privacy policy before broad public launch
/terms                         Terms before broad public launch
```

Routes may be internal overlays while feature maturity is low; do not create separate unauthenticated pages with nonfunctional CTAs just to fill a sitemap.

## Mobile portrait: primary game view

Vertical order (do not hardcode pixel positions; compute using safe-area + responsive constraints):

1. **Header (compact):** player/level badge, score, coins, pause/settings; no full-sized title logo during active play.
2. **Customer strip:** two order cards with requested drink icon, quantity/progress, reward; collapsible details if screen is short.
3. **Board:** visually dominant, canvas with playing surface, incoming shot/aim arrow, drink colliders, subtle danger line.
4. **Launch and next:** active drink anchored on board; next drink preview near lower edge.
5. **Controls/footer:** up to four future booster slots; v0.1 can show a single optional undo/test booster or omit paid-looking buttons entirely.
6. **Screen-level tabs:** only outside active play; pausing may expose map/shop/settings.

At 320 CSS px wide, favor board + active order over currency adornment. Use CSS safe-area insets. The game stage has a logical coordinate system and scales proportionally, with letterboxing or cropped decorative background rather than distorted physics coordinates.

## Desktop landscape: primary game view

- **Top:** compact navigation + stats.
- **Center:** large tabletop canvas, preserving aspect ratio and aim precision.
- **Left:** customer orders, level goals and tutorial/help.
- **Right:** next drink, tier ladder, current goal; boosters when unlocked.
- **Bottom:** compact progress/shortcuts, not a giant mobile footer stretched across the browser.

The canvas receives input only over its designated play interaction region; sidebar controls should not intercept drag gestures. Support mouse drag, click-to-aim/confirm (if chosen in settings), and keyboard alternative.

## Major screens and content hierarchy

### Title `/`
Hero illustration and wordmark (licensed original assets), big **Play** CTA, optional Continue when a save exists, Help/Settings. Avoid login wall. Show small "Alpha" label with clear offline/local preview policy.

### Play `/play`
One active aim source, 2 order cards, scoreboard, mission goal, next drink, pause. Turn off celebratory effects during a collision-heavy sequence if user's reduced-motion preference is set.

### Pause overlay
Resume, Restart (confirm if active), Audio/Graphics, Exit to title (confirm). Pausing on tab visibility is automatic; resuming requires explicit action if necessary.

### Results overlay
`Win`/`Lose`, score, coins earned, merges, orders served, best score, Replay, Continue (if next mission configured), Back to Title. Rewards displayed are explicitly local preview until server persistence is launched.

### Map `/map`
Early: simple cards or vertical mission selector; later: giant scrollable/isometric islands and mission nodes. A locked mission shows requirement, not fake interactivity. Future progress graph includes connectors, starred completion and a focus on current node.

### Shop (future)
Shop scene + summary + tabs `Utility / Décor / Prestige` + item cards with before/after stats and cost + purchase confirmation + insufficient-funds state. Should never allow double-spending.

### Skills (future)
Class overview, available points, connected nodes, prerequisite conditions, clear effects, and undo/respec policy.

### Leaderboards (future)
`Global / Country / Region / City / Friends`, ranking mode selector, active season, rewards preview, opt-in regional visibility and own placement. Unknown city must never be guessed or exposed.

## Core UI state list

`loading | ready | aiming | shooting | resolving | paused | success | failure | reconnecting | error`.

For buttons: `idle | hover (desktop) | focus-visible | pressed | disabled | loading`. Avoid generating every UI state as a different AI image if a consistent base asset plus CSS transform is better. See asset doc.

## Design tokens (provisional, not locked)

- Lagoon #17C7D8; deep lagoon #087E91; mango #FFC34B; coral #FF6E81; foliage #5EBB65; cream #FFF4DF; ink #4A3048; accent purple #7F49B5.
- Consistent rounding families: 12/20/28 px; prefer scalable units and tokens.
- Typeface: license-verified rounded sans for UI and display face for logo; exact fonts TBD.
- Illustration: playful, soft 2.5D, clean contours, restrained bevel/shadow.
- Functional first; avoid gradients, flowers, and large logos in all available spaces.

## Usability/accessibility

- Minimum practical tap areas target 44x44 CSS pixels; include spacing.
- Never depend on color alone for winning/losing/disabled states.
- High contrast text on cream panels; decorative art behind UI should not reduce readability.
- Provide motion toggle and mute; support keyboard alternative for gameplay.
- Touch gestures: prevent default scroll **only inside the actual gameplay surface**; normal scroll works elsewhere.
- Handle orientation changes and WebGL context-loss/recovery.
- Visual assets must have accessible names/labels in DOM equivalents where feasible.

## Mapping mockups to requirements

Generated reference mockups depict logo, title, gameplay, world map, shop, leaderboard and desktop game, but some contain overloaded decorations and placeholder numbers. Treat them as **directional moodboards**, not pixel-perfect accepted UI. Production layout must be redrafted as reusable components. See `29_VISUAL_REFERENCES.md`.
