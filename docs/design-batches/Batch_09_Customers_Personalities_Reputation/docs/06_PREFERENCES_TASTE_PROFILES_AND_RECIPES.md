# 06 — Taste Profiles, Favorite Drinks and Recipe Compatibility

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Two systems, never conflated
`OrderTarget` is mechanical demand defined by Batch 3: canonical tier in alpha; exact drink/family/variant later. `TastePreference` is presentation flavor: a guest may like citrus or tropical fruit, providing dialogue, journal entries or *eligible* recommendations. A preference cannot make a requested drink differ from the pinned mission or change the current eight-tier output identity.

## Candidate preference tags
`citrus`, `berry`, `herbal`, `creamy`, `fizzy`, `tropical`, `spicy`, `frozen`, `classic`, `experimental`. Tags require catalog definitions; allow multiple favorites, neutral tags and dislikes. Do not add real-world allergies or medical claims as flavor roleplay without explicit deliberate design and safety review.

## Eligibility pipeline
Mission's published order pool -> allowed drink catalog and tier -> available future spawn resources -> optional guest preference weighting -> deterministic sample -> mission feasibility validator. If a preferred recipe is unavailable, the director falls back to an eligible authored target; it must never produce a locked secret recipe demand by accident.

## Matching precedence from Batch 3
For later variants, exact drink > family+tier > compatible variant. `tagsAll` does not silently override an explicit tier target. For v0.1 the only effective match is `requestedTier`; creative garnish cosmetics do not create a new gameplay identity.

## Transparent product implications
Favorites may contribute to story dialogue or a *published* loyalty bonus after trusted verification. They should not alter the nominal score already defined by the mission. An optional personal order can be placed as a separate challenge, not as a stealth replacement for a clearable tutorial order.

## Testing
Check that all generated targets exist in the active catalog, are allowed by the mission and are feasible with remaining resources. If an order is invalid after a content update, reject the new content version and preserve the already-pinned mission rather than silently replacing its objective.
