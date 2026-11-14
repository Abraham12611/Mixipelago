# 26 — Accessibility, Localization and Motion Comfort

## Core requirement
Navigating the campaign cannot depend exclusively on a GPU canvas, color alone, perfect vision or two-finger gestures. Every required mission can be found and launched through a DOM-accessible alternative path. Map visuals add delight; they must not become a barrier.

## Keyboard and assistive technology
Provide keyboard-focusable list of discovered missions grouped by island/chapter. Each row announces mission ID/display title, availability, best stars, game mode and requirement. Node selection uses standard Enter/Space where appropriate. Escape closes detail, focus returns to the previously focused node. Avoid auto-moving focus during path animation.

## Touch and contrast
Tap areas ~44–48 CSS px where feasible; color plus icons/patterns distinguish locked, available, completed. Don't rely on subtle glow for the only active-mission cue. Overlay text must have contrast independent of bright tropical artwork; add scrims behind labels.

## Reduced motion
When enabled, suppress long camera flights, parallax wobble, looping landmark effects, celebratory screen shakes and particle-heavy path unlocks. Preserve progress state changes and short static confirmation. If browser `prefers-reduced-motion` exists, use it as default with user override.

## Localization
Map text comes from localization keys: islands, chapters, gate reasons, mission labels and buttons. Don't bake English into background art or SVG path names. Test long German/French labels and languages with different text length; leave room for RTL layouts in cards even if world art remains spatially unchanged.

## Connectivity and status
Screen readers should hear "Mission 2 unlocked" once, not dozens of announcements when nearby routes animate. Offline cached/progress pending labels should be understandable. A server-rejected unlock must present a clear recovery action.

## Test plan
Keyboard-only navigate to next mission, screen-reader list mode, 200% browser zoom, reduced-motion, low bandwidth, high-contrast focus, portrait safe-area phone, tablet orientation change and overlapping node tap targets. Manual UX validation is assigned to the owner.
