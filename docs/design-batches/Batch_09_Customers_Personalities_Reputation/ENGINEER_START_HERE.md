# Engineer Start Here — Batch 9

**Prior reading:** Batch 3 `09_CUSTOMER_ORDERS_AND_RECIPE_REQUIREMENTS.md`, Batch 4 `18_CUSTOMER_DIRECTOR_AND_ORDER_PACING.md`, Batch 6 demand/reputation/economy chapters, Batch 7 customer modifier chapter, Batch 8 reward entitlement index.

## Today: do not rewrite the game reducer
1. Adapt the existing `activeOrders` read model to two customer cards for `coconut-cove-001`.
2. Create provisional original portraits for Mira and Kai; match UI order labels to canonical drink tier targets, not invented recipe names.
3. Animate greeting/served using semantic event listeners; cosmetics have **no** physics/score/economy side effects.
4. Run `python tools/validate_batch9.py` and other earlier batch validators before publishing dynamic content.
5. Implement later customer systems on separate branches with OFF gates and verified source receipts only.

## Parallel owners
Gameplay/HUD, Art/Audio, Customer Catalog/Director, Server Trust/Reputation, Loyalty/Journal, Content QA. See chapter 40 for 28 proposed tickets.

## Non-negotiables
- Alpha has two scripted orders and two-order win; no extra active customer spawned after win.
- New output auto-serves oldest matching order before chain continuation; never retroactively serve resting drinks.
- No trusted XP/coins/reputation from local preview, unverified merge effects or browser-passed customer reactions.
- No automatic VIP in fixed beginner mission or standardized ranked mode.
- All manual UI/gameplay tests are directed to product owner; engineers submit PRs and **do not self-merge**.

## First review evidence
A tested UI preview build, screenshot/video of order states (engineer-supplied), reproducible mobile & desktop steps for owner, automated test results, feature-gate list, and unchanged Batch 3/4 regression fixtures.
