# 23 — Mobile UX: Rewards Inbox, Achievements and Albums

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Navigation
From `Profile` or `More`, player can enter `Achievements`, `Collections`, and `Rewards`. Keep main puzzle UI focused; one small nonblocking notification badge is enough. Within a rewards hub: summary, claimable count, active achievements, album progress and past awards.

## Screen anatomy
- **Rewards Inbox:** tabs `Claimable`, `Claimed`, `History`; each card includes origin, exact award, expiry if any, claim button/status and help link.
- **Achievements:** filters `In Progress`, `Earned`, `Secret`; progress bar, evidence wording, requirement and milestone tiers.
- **Collections:** responsive two-column card grid on small devices, four-column equivalent on tablets; inspect item details and source hints; completion percent pinned to edition.
- **Profile showcase:** select up to approved slots; show ownership, equip feedback and preview without purchase pressure.

## Touch behavior
Minimum touch target around 44 logical CSS pixels where practical; claim button disable only during request, with retry after failure. Use native scrolling for large catalog lists, and avoid touch gesture conflicts with Phaser's aim canvas. A modal with animation cannot trap focus or intercept a game shot accidentally.

## Loading and errors
Skeletons should not fake reward amounts. Show offline banner, pending settlement state, current account sync, claimed state from trusted response, and `Already claimed` with receipt on concurrent retries. If an item image is missing, preserve text label and ownership status.

## Tutorial
After the first **verified** eligible achievement, show one brief explanation of the difference between unlocked achievement and claimable reward. Delay complex album management until the player has at least one genuine collectible.
