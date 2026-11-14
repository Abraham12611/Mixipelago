# 32 — Implementation Blueprint, Module Interfaces and Pseudocode

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Implementation packages
- `@mixipelago/game-core`: immutable domain types, session reducer, scoring, objective evaluation.
- `@mixipelago/physics`: Rapier adapter, collision arbiter, fixed-step ticker (Batch 2).
- `@mixipelago/content`: mode registry, mission loader, schema validator, catalog and version resolution.
- `@mixipelago/game-ui`: Phaser scene + React HUD bridge, not trusted business logic.
- `@mixipelago/analytics`: sampled events, guardrails, perf metrics.
- `@mixipelago/server` future: signed session challenges, verifier, rewards ledger, game services.

## Types
```ts
type ModeId = 'service' | 'precision' | 'score_attack' | 'rush_hour' |
  'survival' | 'vip_service' | 'endless' | 'festival' |
  'ghost_challenge' | 'ranked_duel';

type SessionPhase = 'loading'|'ready'|'running'|'paused'|
  'resolving'|'won'|'lost'|'abandoned';

interface ModePolicy {
  id: ModeId;
  rulesVersion: string;
  validateMission(mission: MissionDefinition): ValidationIssue[];
  onTick(state: SessionState, events: DomainEvent[]): ModeTransition[];
  decideTermination(state: SessionState): TerminalCandidate | null;
}

interface ObjectiveProgress {
  objectiveId: string;
  current: number;
  target: number;
  completed: boolean;
}
```

## Fixed-step orchestration (pseudocode)
```ts
function stepSession(session, inputQueue) {
  if (session.phase !== 'running') return session;
  const command = acceptLegalCommandAtTick(inputQueue, session);
  const contacts = stepPhysicsExactlyOnce(session.simulation);
  const merges = arbitratePairsAndCommit(contacts, session);
  const serveEvents = autoServeNewMergeOutputs(merges, session.orders);
  const events = orderedSemanticEvents(command, merges, serveEvents);
  session = scoreReducer(session, events);
  session = objectiveReducer(session, events);
  session = modeReducer(session, events);
  if (primaryGoalSatisfied(session)) return finishOnce(session,'won');
  const failure = evaluateDangerThenModeFailure(session);
  if (failure) return finishOnce(session,'lost',failure);
  return scheduleNextTickArrivals(session);
}
```
Actual implementation needs tick increment and event-stream capture at one designated location, not inconsistent redundant increments. Keep reducer pure and physics mutation isolated; do not copy pseudocode literally without bridging Batch 2 lifecycle.

## Module dependency rules
Physics package never imports React, score or backend. Catalog supplies tier metadata but does not modify collision geometry. Objective and score packages accept events, never physics callbacks. UI reads read-only snapshot, dispatches commands. Content validates supported mode before session instantiation. Server reuses pure domain rules with pinned engine and content versions.

## Order of development
1. Define shared domain types / v1 mission adapter / mode registry.
2. Build ServicePolicy with primary goal and no unexpected timer.
3. Add `ObjectiveEngine` and `ScoringEngine` pure reducers; reconcile existing rules/tests.
4. Connect Batch 2 semantic events and ensure exactly-once processing.
5. Build mode HUD and session overlay; manual owner review.
6. Add snapshot/export and deterministic fixtures.
7. Add new ModePolicies one by one behind feature gates.

## Error handling
Reject unknown mode, unsupported objective, missing scoring version, malformed mission, invalid seed, impossible board dimensions. Never reinterpret unknown mission JSON silently as Classic Service. Return error with stable reason code and telemetry context; show safe fallback/retry UI.
