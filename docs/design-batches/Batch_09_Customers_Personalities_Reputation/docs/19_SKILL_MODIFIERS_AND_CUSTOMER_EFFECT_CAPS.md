# 19 — Skill Tree Integration, Modifier Precedence and Caps

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Authority
Batch 7 defines trusted skill allocations and modifier resolution; Batch 6 defines shop modifiers. Customer Director consumes a **read-only, server-computed snapshot** scoped to a published encounter and never trusts an arbitrary client percentage.

## Example resolved snapshot
```
{ vipBaseBps: 300, vipSkillBonusBps: 250,
  vipShopBonusBps: 150, vipEventBonusBps: 0,
  vipPublishedCapBps: 2000, effectiveVipChanceBps: 700 }
```
Numbers represent 3.0%, +2.5%, +1.5% and 20% cap, yielding 7.0%. The active encounter outcome is pinned; a skill purchased in another tab takes effect only at the next eligible encounter reservation.

## Skills vs session scoring
Hospitality may alter **future eligible customer chance** and published reward policy factors. It must not alter the eight-tier merge rule or physically move a drink. Skills may not recalculate historic order points or grant previously missed first-clear rewards. Ranked modes use the standardized competitive profile and ignore personal build modifiers.

## Conflict resolution
Apply class eligibility first; reject incompatible/disabled effects. Sum absolute probability point bonuses using integer arithmetic, clamp once to cap, normalize subclass weights, then sample. Remove effects whose `effectSourceId` is duplicated. Do not stack a percentage-of-percentage without a separate approved ADR.

## Tests
Invalid negative weights, VIP chance > cap, skill respec mid-encounter, shop upgrade while active, missing published skill version, replay with old snapshot, and normalized ranked session must all fail safely or produce pinned existing output.
