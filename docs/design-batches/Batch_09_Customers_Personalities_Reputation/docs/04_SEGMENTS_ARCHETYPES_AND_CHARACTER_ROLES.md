# 04 — Customer Segments, Archetypes and Fictional Roles

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Proposed segments
Seven foundational gameplay *segments*: `local_regular`, `tourist`, `family_group`, `explorer`, `festival_crowd`, `vip_guest`, and `critic`. The first five may be styled for casual missions; VIP and critic are explicitly gated until contracts and balance are proven. Personality and behavior are additional properties, not aliases for a segment. A repeat local regular might be energetic or contemplative; a visiting tourist might be patient or curious.

| Segment | Design purpose | Typical presentation | Production timing |
|---|---|---|---|
| Local Regular | Familiarity, loyalty cues | Repeated appearance, favorite order | v0.4.3+ |
| Tourist | Island variety | Regional decor/phrasing; visible order | v0.4.2+ aesthetic |
| Family Group | Future bundles | Group illustration; bundle objective | deferred |
| Explorer | Discovery tie-in | Map journal, optional story | later with Batch 5/11 |
| Festival Crowd | Event pacing | Themed costume, event-only orders | later with Batch 12 |
| VIP Guest | Clear optional challenge/reward | Gold order border and explicit value | gated v0.5.x+ |
| Critic | Reputation narrative | Transparent optional review rubric | later |

## Archetype rule
Each archetype supplies default order animation family, greeting style, optional preference tags, and *published* eligibility; it does **not** supply invisible launch multipliers. Sprite variants should represent an inclusive range of fictional characters without associating facial features, ethnicity, or disability with wealth, patience, or kindness.

## Content limits
No player-facing insult, humiliation, or manipulative punishment loops. Critic and VIP labels describe narrative gameplay roles, not real demographic worth. A customer becoming dissatisfied should suggest one understandable game action, not threaten permanent irreversible loss of a shop.

## Starter plan
Alpha uses two static customer portraits with `customerId` bound to the mission; visual skin variants may be swapped without affecting target tier, payout, or order order. Later pools can use archetype/segment weights and authorable named guests.
