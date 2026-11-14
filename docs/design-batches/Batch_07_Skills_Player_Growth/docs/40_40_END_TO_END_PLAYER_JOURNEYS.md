# 40 — End-to-End Player Journeys and Failure Recovery

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## A: First point
A first-time player clears a published Coconut Cove mission; verified result settles; backend claims unique XP entitlement. At cumulative threshold level 2, server awards one point. UI presents `Choose a skill` or `Later`; player inspects Warm Welcome and purchases rank1, receives trusted new balance. Revisit profile on another device shows the same skill. No direct XP was awarded from raw `drink_merged` client events.

## B: Hospitality shop visit
A level 6 player invests in Guest Book + rank2 Golden Guestlist and buys eligible VIP Seating at a trusted shop. Server combines published 5% VIP base + 2 pp seating + 2 pp skill + 1 pp eligible reputation = 10%. Customer Director samples and persists next encounter. Refresh returns the same visitor, not a free chance to roll again. If no VIP appears, UI does not imply a bug—10% is statistical.

## C: Normalized weekly challenge
A highly progressed player and a new player enter the same fixed challenge. Both receive the same published profile and spawn seed; personal discount, tip and hint perks are suspended or normalized. Their scores depend on actual skill, not rank purchased. Challenge proof includes profile hash.

## D: Respec conflict
Player previews a 4-point refund. Another device allocates a point, changing revision. The first player's stale preview fails with `REVISION_CONFLICT`; UI refreshes the diff. No partial refund or point duplication happens. Owner confirms explanatory copy on both screen sizes.

## E: Unpublished skill
Player deep-links to a future Risk node. API returns `NODE_UNPUBLISHED`, UI shows a benign locked/future state without leaking internal event data or allowing allocation. No shop incident can trigger from viewing the skill.

## F: Catalog rollback
Designer publishes a faulty discount effect. Feature gate disables it for future purchases; invoices already settled remain intact; the rollback restores the previous catalog pointer. Affected builds show a temporary suspended state and a refund option after review. No destructive DB rollback erases player XP.
