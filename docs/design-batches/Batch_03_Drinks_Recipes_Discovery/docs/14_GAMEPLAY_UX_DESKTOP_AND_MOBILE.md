# 14 — Drink/Recipe UX Across Desktop and Mobile

## Primary user goal

During gameplay players need to know **what to shoot**, **what will merge**, **which drink is next**, and **which customer will receive a result**, with almost no reading. All advanced recipe/discovery UI should be tucked away until unlocked; the merge board must remain visually dominant.

## Mobile alpha layout

Top status bar: player level, energy if feature enabled, score, preview coin balance and accessible settings. Customers under top bar, maximum two orders with icons, quantities, and reward numbers. Merge table fills largest central section. At bottom of table, visible launch area and trajectory guidance during aim. Below: current/next preview and compact eight-tier evolution strip; boosters only if implemented. Reserve finger-safe margins around launch controls and device safe areas. Tap targets target at least 44 CSS px where possible.

## Desktop alpha layout

Central board scaled within landscape workspace; left customer panel plus order progress; right compact evolution strip, next shooter preview, mission objective and contextual controls. Do not let additional side panels change physics-world coordinates. All pointer events convert via viewport/camera transforms into logical world units and are tested at multiple aspect ratios.

## Evolution strip requirements

Eight fixed icons with current/available/locked treatments; each icon reveals name and tier by accessible tooltip/long press. Mark current spawn tier, recent merge target and highest tier created in the session. On narrow screens, use a horizontally scrollable strip with snap-to-current and a persistent overview indicator. Avoid tiny illegible text labels under every drink; icon+numeric tier works. Alpha ordering always follows tier 1–8.

## Customer order cards

Show required drink icon, remaining quantity (`1/2`), coin reward, and a clear completion state. If newly merged tier matches an order, animate an unobtrusive ghost/beam from board to that card with a quick checkmark and number increment. Do not physically yank the drink in a way that appears to collide with other objects after it has been service-claimed.

## Recipe Journal (future)

Navigation: World/Gameplay -> Recipe Journal -> family tabs -> recipe detail. States: locked silhouette, hinted, researchable, discovered, mastered, retired. Detail includes exact inputs when unlocked, discovery source, description, gallery, mastery progress and cosmetic skins. A Research button appears only if feature is enabled and the player meets prerequisites; prohibit crafting in the middle of a ranked physics session.

## Discovery and collection overlays

One-line unobtrusive toast for routine first sighting, full celebratory modal for significant first discovery, optional collection update badge. Modal includes dismiss and accessible text equivalent; respect reduced motion. Do not interrupt a timed competition to show a collectible reveal; queue it for the result screen.

## Screen-state matrix

| State | Required UI |
|---|---|
| Loading assets | Progress/fallback, Retry, not a fake playable board |
| Ready | Current drink, next preview, customers |
| Aiming | Trajectory guide, cancellation affordance |
| Shot rejected | Brief reason and unchanged next preview |
| Merge | Visible feedback tied to real event |
| Order served | Quantity and reward update |
| Won/lost | Result overlay, clear retry/next navigation |
| Disconnected | Local alpha unaffected; later trusted actions queued/marked pending |
| Content mismatch | Recover/reload compatible manifest; never silently change tier meanings |

## Copy examples

`Merge two matching drinks!`, `Next: Sunny Lemon`, `Order complete +15`, `Recipe locked — discover it in Mango Market`, `You already own this recipe`. Keep labels localizable and understandable to younger players; avoid text embedded in AI sprites.

## Test devices and accessibility

At minimum, manual owner testing on an actual mobile touchscreen and desktop browser covers aim cancellation, thumb occlusion, zoom/orientation, keyboard shortcuts, readable tier differences, screen-reader status announcements and low-motion feedback. Automated visual snapshots catch layout regressions; automated tests do not replace owner approval of game feel.
