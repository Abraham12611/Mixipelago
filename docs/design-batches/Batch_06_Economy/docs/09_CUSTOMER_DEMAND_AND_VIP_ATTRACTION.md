# 09 — Demand Director, Customer Wealth and Shop Reputation

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Customer director contract
A versioned customer selector receives mission mode, island region, shop archetype, reputation, customer eligibility, active events and derived modifiers. It returns an auditable, seed-driven weighted selection; order requirements still pass Batch 3 reachability and serving checks.

## Customer segments
Local Regular, Tourist, Family Group, Explorer, Festival Crowd, VIP Guest and Critic are candidate segments. Define behavior and reward policy separately from art. A VIP can offer greater coin payout, but should also require higher-tier drinks or longer chains; risk/reward should be visible.

## Balance and fairness
Players without purchased upgrades still receive a small chance of premium guests when content permits. Paid advantages must be excluded from normalized ranked sessions. Newbie missions retain guaranteed tutorial orders, independent of the player's shop perks.

## Reputation input and recovery
Positive verified service results improve shop reputation on capped schedules. Unverified UI actions do not. Temporary service failures may reduce reputation at a bound, but cannot softlock missions. Reputation tiers unlock cosmetic decorations and authored customer opportunities; published tier thresholds must be versioned.

## Integration
Batch 3 order events → verified Batch 4 session → optional reputation gain in trusted backend → updated Customer Director projection for the next eligible mission. No direct Client → `increaseVIPChance` or `grantVIP` mutation is permitted.
