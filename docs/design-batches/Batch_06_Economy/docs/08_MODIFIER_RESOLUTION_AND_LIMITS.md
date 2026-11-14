# 08 — Modifier Engine, Caps and Mode Fairness

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Shared modifier contract
`ShopModifiers` is a pure computed projection derived from published upgrade levels, equipped decorations with explicit bonuses, skills (Batch 7), and temporary event buffs (Batch 10). Systems consume typed effects rather than SQL queries in the simulation loop.

## Calculation order
1. Load eligible base stat from current rules profile.
2. Add flat bonuses and percentage-point adjustments.
3. Combine multiplicative factors in a documented deterministic order, applying a hard cap.
4. Enforce mode gates: competitive normalized modes receive the canonical mode profile instead of economic or skill benefits.
5. Round using fixed integer/decimal strategy; emit source breakdown for tooltips and QA.

Example: `vipBaseProbability = 0.05`; VIP Seating I adds `+0.02`, VIP Seating II another `+0.02`, shop reputation eligible bonus `+0.01`; total `0.10`, clamped to a global 0.20 maximum. Treat these as sample figures pending balance.

## Never silently change physics
A VIP attraction upgrade must not modify `linearDamping`, `friction`, `restitution`, `worldStep`, merge eligibility or tier progression. A campaign-mode board modifier, if ever needed, is an explicit versioned mission rule and must be recorded in session proof.

## UI explainability
Show `Base 5% + Seating 2% = 7% VIP chance` when it is an actual statistical probability. Never promise “always rich customers” when the backend implements only a probability boost.
