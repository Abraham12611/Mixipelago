# 41 — End-to-End Journeys and Failure Case Stories

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Journey A: first earned achievement
Player completes published `coconut-cove-001` for the first time. Server verifies the run, records mission receipt and first-clear facts. Batch 6 grants eligible coins and Batch 7 grants eligible first-clear XP exactly once. Batch 8 evaluates `first-mission`, creates a badge entitlement, displays a ready-to-claim state, and on claim commits inventory item. Refresh shows badge owned and receipt history. Replaying the mission upgrades best stars but does not regenerate first-clear coins, XP or achievement badge.

## Journey B: chest during offline transition
Player sees a published revealed treasure, taps claim as network drops. Client keeps pending intent, but does not add coins locally. Reconnection sends same request key; server verifies map eligibility and produces one receipt. On another device, inventory shows the reward once. A second click returns the same receipt.

## Journey C: album completion
Player owns four unique items in a five-item album. A new claim delivers the fifth eligible item. Inventory grant triggers album projector, which marks edition complete and creates one trophy entitlement. Even if inventory event is redelivered three times, album completion and trophy grant remain single. Added future items are placed in a new album edition.

## Journey D: duplicate cosmetic reward
Player already owns `badge-first-service` and a future authored chest includes it. The claim uses the published duplicate policy: either no second copy (and clear explanation), or a specified fallback with separate budget. No hidden reroll and no infinite duplicate compensation chain.

## Journey E: seasonal dispute
Leaderboard season finalizes with verified placements. Award snapshots create claims. Correction is issued later with audit; original trophies stay traceable, and adjustments follow a compensating/reconciliation policy. A screenshot alone cannot prove rank.

## Journey F: catalog retirement
An old milestone is replaced. Existing earners retain historical badge edition and date. Current players see the new milestone. Rollback restores read paths without erasing receipts.
