# 20 — Mission Solvability, Feasibility Proofs and Automated Playtesting

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Why static checks cannot prove a physics puzzle
Tier equivalence can show insufficient resources (provably impossible) but cannot guarantee a winning trajectory. Glass placements, wall collisions, order consumption priority, danger grace, timing and aim resolution matter. Every gated authored mission must have a **golden winning playthrough** on its pinned simulation.

## Validation tiers
**A: JSON Schema** validates field types, enums, bounds and required objects.
**B: Cross-document semantic lint** checks tier IDs, supported mode, monotone star thresholds, spawn pool, board geometry, available target sources, event names and reward semantics.
**C: Necessary resource bound** calculates theoretical tier1-equivalent mass and optimistic merge capacities; reject obvious impossible cases, mark others unknown.
**D: Solver / input-search attempt** runs scripted, heuristic and randomized candidate shots (always reproducible seeds) against actual Rapier backend. Search needn't be complete; no solution found means review, not mathematical impossibility.
**E: Golden human run** records actual keyboard/mouse/touch aim commands/ticks and hashes; required before publish.
**F: Owner manual review** approves player feel and subjective difficulty.

## Gold proof format
```
{
  "missionRef": {"id":"coconut-cove-001","version":"1.0.0"},
  "physicsVersion":"...", "catalogHash":"...", "modeRulesVersion":"...",
  "seed": 12345,
  "commands": [{"tick": 10, "type":"launch", "direction":{"x":0.1,"y":-0.995}}],
  "expected": {"status":"won", "ordersServed":2, "scoreMin":1},
  "resultHash":"computed-from-engine-not-guessed"
}
```
This is a format sketch, NOT an executable winning fixture. Never fabricate a passing command trace or hash. Engineers populate them after running implementation.

## Solver strategy
For beginner missions, manually authored aim vectors + mutation search (angle offsets, shot timing) is adequate. For later complex modes, beam search over discretized launch angles and event-driven state snapshots can explore plausible sequences. Use a physics bridge that runs headless with same engine versions, not a simplified math engine claiming to certify real physics.

## Seed cohorts
Sample 100–1000 seeded runs per generated mode in CI or nightly jobs, measure fraction with at least one bot success, shot budget distribution and deadlock occurrence. Keep known edge seeds as regression fixtures. Do not replace seed mid-run if it is losing; that would break replays and trust.

## Owner sign-off conditions
Mission preview explains objectives and constraints; at least one reproducible solution exists with touch-friendly tolerance; optional 3-star proof; no required purchase; no hidden action that can't be discovered from visual affordances; fair recovery on losing state. Owner handles manual UI playtesting.
