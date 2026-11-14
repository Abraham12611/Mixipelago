# 35 — Customer Balance Models, Probability Simulations and Fairness

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Candidate parameters
Base VIP probability example 3% (300 bps), skill bonus 2.5% (250 bps), shop bonus 1.5% (150 bps), published cap 20% (2000 bps). Satisfaction bounded 0–10000; rep deltas `[-30,30]` per encounter with `[-60,60]` per verified eligible run. Relationship thresholds `0/100/300/700/1300` points. These are design experiments, not committed tuning.

## Monte Carlo and scenario testing
Sample at least 100,000 deterministic encounters per catalog revision and assert VIP observed rate within statistically justified tolerance of the expected distribution. Stratify by shop tier/skill rank and demonstrate no player hits unauthorized VIP/critic classes. Check fallback pools under disabled content and missing recipe assets.

## Mission fairness
Run mission feasibility checks against each candidate guest pool; prove any generated order fits the initial board, shot queue and automatic serving behavior. Even if an order's tier cost is feasible on paper, the scene may be physically unwinnable—retain replay traces for published mission-level configurations.

## Economy modeling
Estimate verified order income and reward liability before activating VIP or loyalty extras. Income is a separate Batch 6 decision; do not insert fictional satisfaction directly into coin payouts. Cross-check expected rewards vs ability to purchase the first shop upgrade without compulsive repetition, consistent with Batch 6 balancing.

## Safeguards
No penalty for missed calendar day, disabled purchases, or declining VIP. Prevent players with low reputation from being trapped below minimum accessible mission/customer set. Standardized competition must show identical customer demand to all participants for a given profile/version.
