# 24 — Mobile UI: Skill Tree, Level-Up and Builds

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Mobile navigation
Recommended future route `Profile → Skills` or accessible from the campaign's level-up modal. On portrait mobile, show one branch at a time in an **interactive scrollable skill graph**, with a persistent compact header: level, XP-to-next, available points. Branch tabs use short accessible labels and distinct icons; never depend only on color.

## Layout states
1. **Locked introduction:** first point awarded → short explanation + one highlighted example talent.
2. **Tree browsing:** zoom/pan optional; screen-reader list view is always available.
3. **Node detail bottom sheet:** icon, name, rank, next-rank effect, requirements, source/cap, applicable modes, cost, `Learn` action.
4. **Confirmation:** `Spend 1 point on Warm Welcome? Eligible tips +3%, capped under shop payout rules`.
5. **Purchase success:** point counter animates modestly, new rank visibly highlighted; respect reduced-motion preference.
6. **Error:** stale profile, no points, unavailable node, auth expired or network failure; restore state and never show an unconfirmed success.
7. **Respec preview:** diff of removed perks, refunded points, invalidated active slots, and when it takes effect.

## Design constraints
Tap target ≥44 CSS px, no tiny parallel lines where players can accidentally hit a neighbor, stable viewport when keyboard/safe-area changes, optional haptic feedback, pinch/pan gesture not conflicting with browser back. Keep scroll positions across branch switches and returning from gameplay.

## Avoid UI clutter
During core tabletop play, only show an optional small skill effect indicator when it actually influences the current casual mode. Do not install a large permanent tree overlay that obscures customer orders or the aim line.
