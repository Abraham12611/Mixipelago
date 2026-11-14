# 31 — Example Player Journeys and Failure Paths

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## First affordable utility upgrade
Player clears Coconut Cove mission 1 with verified receipt → sees balance +150 and an affordable mini upgrade at the shop → opens utility tab → previews the actual mechanic → confirms server-authoritative purchase → visual/stat display updates. On disconnection, retry same idempotency key and show original receipt.

## Cosmetic-focused player
Player saves for a golden roof instead of buying customer boosts → buys purely decorative roof → sees shop scene visibly change, prestige collection advances, customer and ranked score unaffected. This is a legitimate, satisfying spending path.

## VIP-focused player
Player purchases a seating upgrade with a disclosed +2-point VIP arrival weight → next campaign mission's Customer Director builds allowed seed-driven mix → later VIP request appears, with proportionate difficulty and reward → leaderboard normalizes this effect away in competitive mode.

## Broke player
Player spends almost all coins on decoration → can still play Coconut Cove missions, earn allowed first clears and access tutorial mechanics. No insurance disaster is forced. Optional event offers a recovery quest rather than irreversible penalties.

## Double-click purchase
User taps Upgrade twice during lag. Both requests share same click's idempotency key, returning one receipt. A truly second intentional purchase uses a new key but is rejected if max-level already owned. UI never claims both succeeded.

## Concurrent treasure claim
Two devices claim same unlocked chest. Only one transaction creates the grant; second receives already-claimed receipt and state refresh, never a second credit.
