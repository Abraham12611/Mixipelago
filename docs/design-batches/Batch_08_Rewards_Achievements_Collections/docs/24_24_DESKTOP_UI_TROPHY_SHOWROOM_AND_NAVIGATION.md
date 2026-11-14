# 24 — Desktop UX: Gallery, Comparison and Navigation

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Layout
Use Next.js/React panels for browsable lists and modals, with Phaser only where a rich trophy-room or island scene adds value. Desktop rewards hub can use three columns: categories/filters, achievement list, details/claim card. Album view can use a large shelf scene with a keyboard-accessible item list and detail drawer.

## Interaction
Hover shows preview but never triggers a claim. Click and keyboard Enter/Space are equivalent. Claim action requires explicit button with text, no icon-only ambiguous financial affordance. ESC closes detail, not a pending transaction. Confirm optional multi-reward selection only when a choice affects durable ownership.

## Account sync
If the player signs in on a new device, the inventory and claims load from server. A local alpha badge should remain visually distinguishable from verified inventory. Do not silently grant old preview rewards to trusted account.

## Discoverability
Allow search by name, reward source and album; show locked reasons on approved public content without revealing hidden secret identities. Collapsed lists and progressive loading prevent browser memory pressure.

## Visual QA
Verify layout at 1024px laptop and 1920px desktop, at browser zoom 200%, dark/color-safe contrast settings and reduced motion. Manual subjective UI tests and player experience approval go to project owner.
