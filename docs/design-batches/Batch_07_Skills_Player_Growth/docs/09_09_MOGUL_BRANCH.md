# 09 — Business Mogul Skill Branch: Efficiency and Investment

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Identity
The entrepreneur branch makes shop upgrades and resource choices clearer and modestly more efficient. The effect must not compound multiplicatively without ceilings or create an optimal runaway snowball.

## Proposed nodes
- `bg_cashflow_lens`: show projected income, expense categories and investment payback estimates; not financial advice.
- `bg_smart_purchase`: +2% discount on specifically eligible *future* trusted utility upgrades, with a combined maximum discount cap. Cannot discount past purchases retroactively.
- `bg_vendor_relations`: later supplier contract quality-of-life or a bounded price improvement, not permanent free ingredients.
- `bg_showroom_curator`: unlock additional cosmetic layout presets; prestige-only, no automatic customer multiplier.
- `bg_portfolio_sense`: cross-shop reporting for franchise owners later; no shop grant.

## Pricing order
Use the Batch 6 pricing resolver: base price → catalog eligible discounts → caps and integer rounding → signed server quote → atomic purchase. A quote must include modifier snapshot/hash and expiration; clients may never pass a custom `price` or change negative prices via talent payload.

## Sample
Base upgrade price 7,500 coins; 2% eligible discount = 150; candidate final price 7,350, with rounding exact. If another discount applies, combine according to Batch 6 `08_MODIFIER_RESOLUTION_AND_LIMITS.md`, not an ad-hoc React calculation. Ranked matches use normalized profiles regardless of player investment.
