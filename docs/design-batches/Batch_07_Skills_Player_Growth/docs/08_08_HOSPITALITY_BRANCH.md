# 08 — Hospitality Skill Branch: Guests, Tips and Loyalty

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Identity
Hospitality shapes *who* visits eligible player-owned shops and how they respond. All numerical outcomes are probabilistic and server-driven; puzzle serving rules remain unchanged.

## Proposed skills
- `hp_warm_welcome`: rank 1 gives +3% tip *multiplier* for eligible trusted shop service payouts, subject to overall payout cap; no effect on preview coins.
- `hp_guest_book`: rank 1 increases eligible returning-customer weight; no forced VIP guarantee.
- `hp_golden_guestlist`: up to rank 3, each rank +0.01 absolute probability of a VIP arrival (1 percentage point), subject to server-side caps; requires Guest Book and level 5 in draft.
- `hp_queue_whisperer`: clearer indicators of order impatience or upcoming guest preferences (later customer personalities).
- `hp_regulars_circle`: unlocks a loyalty-track bonus on future customer relationships; no immediate guaranteed coin payout.

## VIP probability example
Base VIP rate 0.05 + shop VIP seating 0.02 + Guestlist rank2 0.02 + shop reputation 0.01 = 0.10, clamped to a **candidate absolute cap of 0.20**. For 100 eligible arrivals, the expectation is 10 VIP customers, *not* a promise of exactly ten. Instrument actual arrival rates and compare to expected stratified by shop and level.

## No rich-customer exploit
Player cannot relaunch a shop, change tabs, or restart a mission to reroll a pending customer encounter. Customer Director uses server-seeded encounter IDs persisted before display. Premium/season purchases must not increase competitive VIP odds.

## Compatibility and failure
When `ENABLE_TRUSTED_CUSTOMERS` is off, the projection shows this talent as `inactive_in_current_mode`, not a fake reward. If the shop is temporarily closed, benefits do not generate passive customers or wealth out of nowhere.
