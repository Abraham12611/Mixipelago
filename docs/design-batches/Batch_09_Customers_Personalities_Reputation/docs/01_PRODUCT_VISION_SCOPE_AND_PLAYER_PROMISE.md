# 01 — Product Vision, Scope and Player Promise

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Experience goal
Customers make the drink-merging board feel like a living seaside business rather than an anonymous scoring exercise. Each guest has recognizable visual character, readable order requirements, and a fair interaction loop. Over time, guests can become recurring visitors and build a lightweight relationship with the player-owned shop. The core game remains a **skillful puzzle first**: fictional personality effects must not override player input, physics, or mission solvability.

## Locked prerequisites
- Batch 2 owns Rapier simulation, contact/merge IDs and fixed 60 Hz step. Customers never create or transform physical drinks.
- Batch 3 owns drink IDs, eight-tier alpha ladder (tier 8 terminal), and **newly merged output serves the oldest matching active order before further chain continuation**. Same tier can satisfy any compatible alpha order, with exact output binding.
- Batch 4 owns session objectives, `orders_served`, scoring and win/loss precedence. `coconut-cove-001` has exactly **two visible orders and a two-order win target**.
- Batch 5 owns world graph eligibility and mission publication. Batch 6 owns wallet, reward policies, shop economics and reputation semantics. Batch 7 owns skills/modifier caps and normalized ranked profiles. Batch 8 owns achievement evidence and collectible entitlements.

## Batch 9 deliverable boundaries
This batch specifies customer definitions, fictional archetypes, preferences, authored dialogue, director selection, satisfaction, VIP eligibility, loyalty, reputation, shop feedback, accessibility, APIs, event contracts, persistence, QA, and staged release gates. It also defines *interfaces* for future narrative, seasonal incidents, and rival businesses without implementing their full stories.

## Player promises
1. A guest's requested drink is always visible and mechanically obtainable in its mission configuration.
2. Customers may feel expressive, but their personality never secretly changes published difficulty or launch physics.
3. Players are not punished financially for closing a tab, pausing, or not playing daily; default alpha missions have no guest patience timers.
4. All game-impacting effects (priority class, timer, bonus reward, reputation) are clearly disclosed in the relevant UI.
5. Paying for decorations or perks cannot create an unfair competitive advantage in standardized puzzle rankings.

## Release position
- `v0.1.x`: portraits, two scripted orders, expression-only animations, local preview rewards. No accounts/loyalty/reputation settlement.
- `v0.4.2` **candidate**: read-only customer catalog plus trusted satisfaction / shop reputation projection from verified completed orders.
- `v0.4.3+`: opt-in recurring visitor journal and loyalty milestones; VIP pools only after fairness gates.
- Later: critics, group orders, complex personality quests, seasonal encounters, and live-world customer behaviors.

Numerical values in this pack are **initial balancing hypotheses**. No customer feature is claimed to be already implemented or production-approved.
