# 24 — Gameplay UI/UX, Responsive HUD and Screen States

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## UX architecture
Phaser canvas handles physical board, drink sprites, aim rays and particle effects; React overlay handles semantic text, counters, progress, menus, dialogs and accessibility. Render HUD from `SessionViewModel` derived from reducer state, not from ad-hoc Phaser instance properties. Cross-layer messages use typed event bridge.

## Mobile portrait (priority)
- Safe top bar: player level if available, score, energy (future) and preview coins (labeled accordingly).
- Customer row: up to two readable order cards with tier icon, quantity and reward; compress or scroll horizontally on smaller viewports.
- Dominant center: merge table occupying most interaction area; unobstructed launcher and danger line; aim input exclusively inside canvas; avoid OS gesture conflict.
- Footer: next drink, compact evolution strip, mode-specific target, pause, optional allowed boosters.
- Bottom navigation is NOT displayed during active aim if it steals touch targets; put Map/Shop/Leaderboards on pause or between rounds.

## Desktop landscape
- Left rail: active customers, mission description and score target.
- Center: stable aspect-ratio game field with letterboxing, full pointer coordinate transforms and no CSS distortion.
- Right rail: next drink, evolution guide, allowed boosters, objective progress and mode rules.
- Top: brand and optional account/profile; lower-priority features collapse rather than crowd puzzle.

## Screen route/state list
`/play/:missionId` (game), `/play/:missionId/intro` optional modal, `/dev/physics-lab` internal, `/map` future Batch5, `/modes` future gated, `/profile` future, `/leaderboards` future. In-game overlays: tutorial, pause, goals, timer warning, win, loss, result summary, help, network/recovery. Do not create publicly clickable placeholder routes for features unavailable in current release.

## Mode-specific HUD
- Service: `Orders 1/2`, current open bubbles.
- Precision: `Shots 3/6` prominent, with settle status after final shot.
- Rush Hour: active timer, order count.
- Score Attack: score target + max chain visual.
- Survival: wave `2/3`, remaining wave tasks.
- VIP: order lines progress and phase.
- Endless: score, personal-best, Reset Table and Finish.

## Responsive/accessibility acceptance
Canvas uses stable world geometry across layouts; accessible HTML goal descriptions; touch targets approx 44 CSS px where practical; keyboard alternatives for primary gameplay; no essential information conveyed by color alone; reduced motion; safe-area handling; text at 200% zoom where feasible; no input loss when changing orientation. A goal label must remain readable when animated score numbers are hidden.

## UI component states
Buttons: enabled, disabled, hover, pressed, loading, offline, focus-visible. Order cards: waiting, partially satisfied, complete, expiring (future), failed (future). Timer: normal, warning, expired. Session: ready, running, paused, resolving, won, lost, error. Expose precise state to accessibility tree and avoid duplicate announcements during rapid merges.

## Owner manual test brief
Tester verifies aim reachability, visibility of next item, objective comprehension, all pause/retry routes, overflow messaging, landscape responsiveness, one-handed portrait usability, real devices. Screenshots alone do not demonstrate mechanics.
