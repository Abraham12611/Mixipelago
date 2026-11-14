# 16 — Insurance, Incidents, Debt and Business Risk — Overview

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Owner's example
An uninsured shop fire may create repair decisions, a timed optional recovery challenge, or a loan offer, but it must not trigger merely because a player is poor. More detailed incidents/weather are intentionally deferred to Batch 10.

## Event flow
Event Director chooses eligibility fairly → backend creates unique incident case → user sees credible choice/costs and deadlines → player accepts option → event command settles wallet/quest/shop state transactionally → scheduled resolution records outcome → player retains playable route.

## Insurance design candidate
Players may buy coverage to cap incident cost, but never need insurance to keep playing the core game. Publish deductible, insured incidents, claim caps and expiry in plain English. Avoid presenting coverage as a real financial product; game economy only.

## Loan design candidate
Explicit principal, repayment total, installment schedule, debt cap and default consequences. No compounding negative balances. Loan cannot be used for gambling, player-to-player arbitrage or external withdrawal.

## Avoid economic traps
Do not schedule simultaneous incidents that exhaust both liquidity and all business capacity. The Event Director should enforce an exposure budget and cooldown, with a rescue route after failure. Incident results must not silently rewrite purchases or erase achievements.
