# 16 — Critics, Special Guests and Quest Integration

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Special guest taxonomy
`critic` is an authored challenge segment that may review *defined service goals*; `celebrity` or `island_ambassador` is a fictional narrative guest; `mentor` introduces tutorial guidance; `event_host` advertises a festival. These are roles, not separate physics systems. Story quests, friendship arcs and rival-business consequences belong to Batch 11; this chapter only specifies the customer-facing interface.

## Critic experience
A critic offers a clearly defined optional service rubric: e.g., fulfill two tier-4 orders with a maximum shot count. The player can inspect difficulty, known rewards, and the exact metric before opting in. A critic can't secretly penalize routine untimed service or retroactively fail an already completed mission.

## Quest handoff contract
`CustomerQuestOffer` contains `offerId`, `customerId`, `eligibleMissionIds`, `questDefinitionVersion`, `acceptedAt?`, `expiresAt?`, `rewardPolicyId?`, `state`, and consent/visibility flags. Quest engine validates progression and creates a separate published mission contract; customer display does not issue rewards. Batch 8 can issue collectible memorabilia after verified quest evidence; Batch 6 owns coins and Batch 7 owns XP.

## Narrative limits
This pack intentionally does not draft detailed scripts, arcs, interpersonal drama or rival dialogues. Batch 11 will own branching narrative, dialogue dependency graphs, NPC memory and conflict/recovery chapters. Keep this module disabled until those specifications and content moderation are approved.

## Tests
One offer per eligible source, reject unapproved mission ID, preserve accepted offer on client reconnect, no rewards on UI acceptance alone, and no critical progression blocked by declining a critic.
