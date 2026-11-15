# 07 — Contest UI/UX Screens and Responsive Design

## Screen sitemap

~~~text
/                  Original logo + Play Now + How to Play + Sound
/play?mission=...  Game board, orders, controls, next shot, pause, hints
/map               Coconut Cove map, chapter gates, mission stars
/results           Outcome, score, local best, replay/next/map
/settings          Volume, motion, accessibility, clear save, privacy
/about             Credits, asset licences, contest-friendly note
~~~

Everything must work as a **guest**. Avoid dead-end navigation: every screen has a clear back/home route and accessible focus order.

## High-priority mockups

| Screen | Mobile | Desktop | Acceptance |
|---|---|---|---|
| Home | Stacked CTA over atmospheric island art | Centered compact hero | Play instantly, no login/paywall |
| Tutorial | Touch aiming mini-board with text+animation | Mouse/keyboard walkthrough | Skip/replay, distinct directions |
| Active play | Board dominant; 2 small order cards at top; launcher bottom | Board center-left, order panel right | No overlay hides launch trajectory |
| Pause | Readable centered modal | Keyboard escape + button | Sim frozen; resume safe |
| Results | Score, stars, retry and next in tap-friendly stack | Two-column results + stats | No false reward claims |
| Map | Vertical island path with pan/zoom or scroll fallback | Responsive scenic map and chapter paths | No unplayable draft nodes clickable |
| Settings | Volume, reduced motion, clear save | Same accessible controls | Settings persist locally |
| Credits | Scrollable rights/credits | Narrow reading column | All required attributions visible |

## Design vocabulary

Warm tropical dawn tones, airy cyan and sand backgrounds, high-contrast navy text, soft 2.5D shadows and stylized glass highlights. Use color **and shape** to identify tiers; never a color-only state. Animations should be economical so glass contact is comprehensible.

Suggested tokens are **proposals**, not immutable values: primary coral #EF6556; sea #3BADC0; navy #173A49; sand #FFF3DF; accent mango #F5B644. Validate contrast ratios in both default and high-contrast modes.

## Layout and input rules

- **Mobile portrait (320–430 CSS px):** viewport-safe top header, no horizontal overflow, touch targets approximately 44×44 CSS px or larger, board max width and responsive aspect; launch gesture area remains unobstructed.
- **Tablet (431–1024 px):** board + collapseable secondary panel, stable input scaling.
- **Desktop (1025+ px):** board centered with sidebar, visible instructions and keyboard help.
- Safe areas: honor viewport inset around notches; don't place pause or order close buttons under browser chrome.
- Game uses CSS pixel-to-world transform consistently; physical coordinates never derived from image dimensions or screen orientation alone.
- Touch scroll interference handled only within interactive game canvas; other pages scroll normally; allow pointer cancellation.

## Accessibility and interaction

- Every icon/button gets accessible name. Decorative art is hidden from assistive technology where appropriate.
- Provide non-gesture aiming alternative (keyboard arrow + confirm or touch aim buttons) as appropriate.
- Provide sound/music mute, nonessential motion toggle, readable non-flashing progress and large text within layout constraints.
- Show order tier names and quantities, not just colors.
- Reduced motion: disable camera shake and excessive particle flashes, keep progress feedback through text/icons.
- No forced registration dialogs or cookie walls to access gameplay.
- Never show decorative UI that appears functional but isn't; hide unavailable modes.

## State inventory

Loading, asset error, ready, tutorial, aiming, paused, win, loss, results, map, offline/reconnect, save corruption, unsupported WebGL/wasm and update available. Every state needs a way forward. A fallback canvas renderer still shows semantic HUD.
