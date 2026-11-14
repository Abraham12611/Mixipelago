# 14 — Shop Prestige, Ratings and Brand Perception

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Different metrics
`reputation` describes service quality and earned customer trust. `prestige` describes visible status/design. `businessValue` is a later modeled valuation and must not be spendable currency. `playerLevel` is a separate progression measure.

## Proposed reputation factors
Verified orders completed, service streaks, customer satisfaction, complaint resolution and campaign quest completion. Normalize input to prevent 100x farming in trivial missions. Use decaying influence only with clear communication and recovery paths.

## Prestige factors
Cosmetics, rare island-themed collections, upgrade tiers, legendary trophies and meaningful aesthetic accomplishments. Purely cosmetic purchases may increase *prestige rating* without improving coin income; avoid mislabeling the statistic as revenue.

## Player-facing communication
Separate stat panels for operational speed, customer appeal, reputation and visual prestige. Display all conditional effects and hard caps. A beauty upgrade should remain valuable visually even if it does not move an economic percentage.

## Leaderboard fairness
Economy/prestige leaderboards may rank wealth or decoration if clearly categorized as such. Skill-based puzzle rankings must not implicitly rank economic purchasing power.
