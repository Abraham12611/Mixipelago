# 08 — Branches, Optional Routes, Checkpoints and Gateways

## Route pacing
Keep the early Cove path linear long enough for users to understand merge-and-serve, then introduce a fork where both choices are clearly viable. A main mission unlocks one or two nodes; a branch may lead to a treasure or mastery route and reconnect to the mainline. The main objective remains visible and easy to return to.

## Branch policies
- `critical`: required for primary island completion; cannot be hidden behind a time-limited event.
- `optional`: can grant star, collectible, narrative or cosmetic rewards; safe to skip.
- `challenge`: high difficulty and explicit recommended mastery level.
- `secret`: appears after discovery; never silently blocks mainline.
- `seasonal`: time-limited under Batch 12; isolated from evergreen campaign progress.

## Branch unlock rules
For a split A → B or C, both B and C may unlock from A; a later node D can depend on `anyOf(B cleared, C cleared)` so the player is not forced into both branches. If designers want both branches before a collectible, express `allOf` and communicate that prerequisite.

## Checkpoints
Chapter checkpoints are progress summaries, not new physics missions. A checkpoint may award a non-coin cosmetic preview or mark district completion, but claims must use the same idempotent entitlement rules as treasure. First campaign can omit claimable checkpoints entirely to minimize complexity.

## Inter-island travel
Gateway nodes have destination island, anchor node and transition scene ID. Travel is unlocked by explicit campaign rules; the user can return to previously visited islands without spending resources. If new island files fail to download, retain current island and offer retry rather than leaving user on a blank map.

## Failure/retry behavior
A difficult optional mission should not stall progress toward the next main chapter. Failing a gateway test leaves existing paths available. A disconnected route visible in the art but without playable content must be clearly styled as coming soon, not as a misleading locked mission.

## World routing abstraction
Expose `getAvailableNextNodes(progress, graph)` sorted by editorial `priority`, proximity and recently visited context. UI can always highlight one recommended next step, but should not erase alternatives. A player who has explored past the default recommendation gets a path chooser rather than being teleported backwards.
