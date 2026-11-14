# 33 — Balancing, Economy Impact and Fairness Simulation

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Rewards are an economic faucet
Any item that grants coins or consumable value must be included in Batch 6's faucet/sink model. A seasonal league with 10,000 eligible recipients can create a massive supply even when individual rewards look small. Simulate maximum eligible accounts, repeatability, first-clear overlap, event concurrency, and abuse.

## Example budget equation
For program p: `maximum_liability(p) = eligible_players_max × claims_per_player_max × maximum_coin_grant_per_claim`. For recurring weekly programs multiply by active windows per measurement period. This is an upper bound; model realistic median and high-engagement cohorts separately.

## Fairness considerations
No title or collectible should modify normalized competitive physics or scoring. Avoid hiding necessary puzzle instructions behind earned perks. Rarity distribution must not be misrepresented and must have accessible alternative recognition paths. Standard campaign remains completeable without daily gifts, paid randomness or friend invitation.

## Stress cases
Zero-spend, low-frequency, return-after-60-days, skilled high-frequency, brand-new late-season, multi-device, slow-network, timezone-traveler, color-blind and motion-sensitive players. Analyze value per minute without rewarding self-destructive activity patterns.

## Tuning process
Publish a spreadsheet/counterfactual snapshot before changing grants. Use feature gates, small cohorts, budget alerts and before/after measurements. Economic changes should never retroactively alter already claimed receipts. Do not use player frustration as the primary optimization target.
