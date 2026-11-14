# 23 — Gameplay Customer HUD: Mobile, Tablet and Desktop

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Priority
The merge tabletop is visually dominant. Customer information must answer: **what drink, how many, how much reward, which order will be served first?** The alpha shows two distinct order cards. Do not copy the inspiration game's exact composition; use Mixipelago's own visual grammar, content density and accessibility system.

## Mobile portrait
Use a compact horizontal guest strip above the tabletop with at most two fully visible alpha orders. Each card includes: portrait, display name or avatar label, drink icon plus textual tier, quantity/progress, coin reward with preview badge where applicable, order age priority badge, and optional VIP ribbon only in gated modes. A tap opens customer info overlay; overlay dismiss does not pause unless mode policy says so. Safe areas must respect notches and browser bars.

## Desktop landscape
Use a left-side or top-left order panel adjacent to a wide central board; preserve the same stable active order ordering. A sidebar may show recurring guest notes, but must not obscure trajectory or overlaps. Keyboard focus visibly navigates active orders, help tooltips and accessibility controls.

## Display states
`scripted`, `loading`, `active`, `serving`, `fulfilled`, `expired` (later), `paused`, `verification_pending`, `error_retry`. Short serve reaction animates from committed semantic event. If portrait fails, show accessible fallback text and the order target without delaying gameplay.

## Mode distinctions
No patience meter for Classic Service alpha. VIP risk/reward card requires explicit consent and separate button if optional; no fake scarcity timer. A guest emotion icon does not convey a financial or mission effect unless an associated visible rule describes it.

## Testing
320 px mobile width, desktop ultrawide, portrait-to-landscape rotation, high text zoom, low-motion settings, 30 FPS fallback, loading jitter, focus order and overlapping order cards.
