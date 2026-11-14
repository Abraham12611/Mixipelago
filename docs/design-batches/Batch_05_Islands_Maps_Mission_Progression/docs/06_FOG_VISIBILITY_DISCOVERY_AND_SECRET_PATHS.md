# 06 — Visibility, Fog of War, Secrets and Discovery

## Three concepts that must remain separate
1. **Visibility:** Does the map reveal a node/route to this player?
2. **Eligibility:** Is the player permitted to start/claim/travel now?
3. **Completion:** Has the player satisfied and recorded the content's success condition?
A hidden mission can be eligible on paper but not shown until a discovery trigger. A visible treasure may be locked. A completed node always remains visible, even if a later manifest retires the exact original level.

## Visibility tiers
`undiscovered` (no node marker, safe terrain teaser only), `rumored` (question mark and generic hint), `revealed` (title, icon, requirement and button), `completed` (achievement art). Route segments use parallel states; never draw a secret line and then rely on users not noticing.

## Discovery mechanics
- First three-star clear in a designated chapter.
- Inspect a scenic landmark after completing an adjacent mission.
- Clear a precision challenge to reveal a side pier.
- Find a clue in a treasure claim.
- Future event/NPC discovery: a **durable flag** assigned by a trusted service.
Each secret declares a `discoveryId`, one clear trigger expression, a static reveal animation key, authored copy and fallback hints.

## Secret route fairness
Secret paths should reward exploration, not become opaque mandatory gates. Mandatory island progression must be possible with the published critical path. A secret route can grant cosmetic collectibles or optional mastery challenges, but no irreplaceable power for competitive modes.

## UX expectations
A clear icon hierarchy distinguishes **locked** (padlock), **mysterious** (question mark), **available** (pulsing star), and **completed** (filled stars/check). Do not communicate state by color alone. An accessible list view can expose known secrets and discovery hints without leaking their undiscovered coordinates.

## Discovery event flow
`mission_won` (or stable profile flag) → campaign reducer evaluates discovery predicates → emits `discovery_revealed` once → persists discovery state/receipt → map updates nodes/edges → optional short reveal animation → focus button. A failed reveal animation must not prevent a durable discovery receipt.

## Version changes
If a secret trigger changes after publication, previous discoveries remain claimed. Content migration should grant safe equivalents where necessary. Removing the visual route should not delete earned collectibles. Analytics never reveal undiscovered content names to ordinary player clients before eligibility.
