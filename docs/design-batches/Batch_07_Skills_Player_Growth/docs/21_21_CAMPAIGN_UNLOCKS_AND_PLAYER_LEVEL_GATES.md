# 21 — Campaign and Island Integration

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Design rule
A campaign mission's availability remains owned by Batch 5 published world graph. Player RPG level can be one *authored* precondition of optional advanced content, but a skill-point purchase never silently unlocks an unpublished or unverified mission.

## Gate design
- Main-route missions should be completable through gameplay; do not impose unreasonable grinding for points.
- Optional branches may require `player_level_at_least` or named `skill_rank_at_least` only when alternatives exist and the UI explains the prerequisite.
- Explorer talents only reveal **hints about eligible published content**, not unearned stars, unapproved server coordinates or secret unreleased content.

## Sequence example
Player wins `coconut-cove-021` → Batch 4 validated result → Batch 5 writes completion and recalculates campaign graph → Batch 7 XP grant receives the same verified result entitlement → player reaches level 6 → graph may show an optional branch requiring level 6 as available *if* its other prerequisites pass. Each transition uses separately idempotent events with source identifiers.

## Anti-softlock
An optional path cannot be the only way to earn the points required to access itself. Campaign validator must flag prerequisites that require a talent whose points are locked behind the same gated mission. Level-gated content must include accessible ways to earn XP without repeating zero-XP missions forever.
