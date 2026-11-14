# 11 — Risk Strategist Skill Branch: Preparedness and Recovery

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Purpose
Provide agency during shop disruptions without introducing punitive systems that target players for having fewer coins.

## Proposed nodes
- `rs_weather_eye`: earlier notice of eligible published weather modifiers (later Batch 10).
- `rs_safety_checklist`: guided repair and preparation checklist for owned shops.
- `rs_reserve_plan`: optional wallet budgeting buckets and an advisory savings goal, **not locked or confiscated currency**.
- `rs_insurance_reader`: comparison of documented insurance choices and claims, not an automatic purchase.
- `rs_recovery_coach`: one bounded recovery assistance option on eligible incidents, with cooldown and audit record (later).

## Event fairness
A user experiencing recent losses or low funds is not targeted with economically destructive random incidents. Keep protection ceilings, cooling-off periods and accessibility accommodations. Do not create negative coin balances, forced interest loops or permanent demotions due to time away from the game.

## Engineering boundaries
No risk skill may directly mutate trusted ledger entries. It can produce authorized *eligibility* or a bounded discount for a future transaction, processed through Batch 6 transaction semantics. The event system owns incident resolution and idempotency.
