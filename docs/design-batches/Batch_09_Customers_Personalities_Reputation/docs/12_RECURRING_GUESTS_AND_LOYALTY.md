# 12 — Recurring Visitors, Loyalty, Affinity and Return Journeys

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Why recurring visitors exist
Players should recognize faces, favorite drinks and short character arcs across islands. A returning fictional guest can react to previous *verified* service events and display a small relationship progression. This is a narrative/collection layer, not a daily-login coercion mechanic.

## Relationship domain
Key: `(playerId, shopId, customerId, programVersion)` for an authored named guest. Candidate points: verified first eligible visit `+100`, successful eligible follow-up `+180`, optional matching favorite (declared before encounter) `+40` with per-visit cap `+220`. These values are provisional and source-bound; limit to one relationship progression per reserved encounter source to prevent mission replay farming.

## Suggested tiers
`stranger:0`, `acquaintance:100`, `regular:300`, `friend_of_shop:700`, `island_legend:1300`; thresholds are candidate only. Tier unlocks can be aesthetic: greeting change, journal entry, photo/portrait frame, optional side quest availability. Any coin/XP benefit requires a separately published Batch 6/7 policy and verified entitlement; no hidden multiplier.

## Privacy and progression
Relationship is with a fictional NPC, not a real-world contact. The client should let players view and hide the guest journal; the UI must not imply an actual person is tracking them. Do not expose precise player location, real social graph or behavioral surveillance in dialogue.

## Recoverability
Loyalty never decays because a player took a week off. Retired named characters remain in a read-only journal with their historical milestones. Unverified alpha encounters can create a local tutorial illustration but cannot be auto-converted into verified affinity points on account signup.
