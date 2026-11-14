# 11 — Shared Types, Command/Event Schemas, and Integration Boundaries

## One contracts package

`packages/domain-contracts` exports runtime-neutral TypeScript types and Zod schemas. No import from Phaser, Rapier, Next, browser APIs, database clients, or image generators. The implementations may depend on the contracts; contracts never depend on the implementations. Document version numbers for all public schemas and include backward migration path for persisted saves/replays.

## Required primitive types

```ts
export type SessionId = string;
export type DrinkId = string;
export type EventId = string;
export type MergeId = string;
export type CommandId = string;
export type Vec2 = Readonly<{ x: number; y: number }>;
export type DrinkTier = 1|2|3|4|5|6|7|8;
export type ObjectStatus =
  | 'arming'|'active'|'sleeping'|'merge_claimed'
  | 'serve_claimed'|'clear_claimed'|'consumed';
export type SessionStatus =
  | 'uninitialized'|'loading'|'ready'|'running'
  | 'paused'|'won'|'lost'|'abandoned'|'disposed';
```

All coordinates finite, within designated logical world bounds unless in explicit transitioning state. IDs are untrusted strings at external boundaries and must be validated; don't assume UUID format unless schema chooses one. `DrinkTier` is limited to eight for alpha; future drink catalog should generalize using an ID and versioned evolution graph instead of globally assuming only eight tiers.

## Simulation initialization

```ts
export interface SimulationInit {
  sessionId: SessionId;
  mission: MissionConfigV1;
  missionVersion: string;
  physics: PhysicsPresetV1;
  physicsVersion: string;
  rulesVersion: string;
  seed: number;
  initialQueue?: readonly DrinkTier[];
}

export interface PhysicsPresetV1 {
  schemaVersion: 1;
  stepHz: 60;
  worldWidth: number;
  worldHeight: number;
  drinkRadius: number;
  drinkDensity: number;
  linearDamping: number;
  angularDamping: number;
  friction: number;
  restitution: number;
  launchImpulse: number;
  maxSpeed: number;
  dangerLineY: number;
  dangerGraceSteps: number;
  launchCooldownSteps: number;
  ccd: boolean;
}
```

Physic config numeric fields require ranges; `dangerGraceSteps` avoids runtime floating millisecond conversion disagreement. Most configuration should be immutable for a run; a special modifier must generate a versioned configuration transition event and is out of alpha scope.

## Commands

```ts
export type GameCommand =
  | { type:'launch'; commandId:CommandId; sessionId:SessionId;
      step:number; direction:Vec2; queueIndex:number }
  | { type:'pause'; commandId:CommandId; sessionId:SessionId; step:number }
  | { type:'resume'; commandId:CommandId; sessionId:SessionId; step:number }
  | { type:'abandon'; commandId:CommandId; sessionId:SessionId; step:number };

export type CommandResult =
  | { ok:true; appliedAtStep:number; shotId?:string }
  | { ok:false; reason:
      'paused'|'terminal'|'invalid_direction'|'not_ready'|
      'launch_blocked'|'cooldown'|'stale_queue'|'duplicate'|'wrong_session' };
```

Important: `pause`/`resume` may be UI shell commands operating outside simulation step when hidden, so the actual implementation should declare which commands are deterministic and which are lifecycle controls. Ranked replay logs only gameplay-affecting commands with canonical step application.

## Simulation events

```ts
export interface EventBase {
  eventId: EventId;
  schemaVersion: 1;
  sessionId: SessionId;
  step: number;
  sequence: number;
  rulesVersion: string;
  physicsVersion: string;
  missionVersion: string;
}
export type SimEvent =
  | (EventBase & { type:'shot_fired'; payload:{shotId:string; drinkId:DrinkId; tier:DrinkTier; direction:Vec2} })
  | (EventBase & { type:'body_contact_started'; payload:{a:DrinkId; b:DrinkId|null; kind:'drink'|'wall'} })
  | (EventBase & { type:'drink_merged'; payload:{mergeId:MergeId; a:DrinkId; b:DrinkId; result:DrinkId; tierBefore:DrinkTier; tierAfter:DrinkTier; chainDepth:number} })
  | (EventBase & { type:'drink_spawned'; payload:{drinkId:DrinkId; tier:DrinkTier; position:Vec2; origin:'shot'|'merge'|'setup'} })
  | (EventBase & { type:'danger_warning'; payload:{drinkId:DrinkId; remainingSteps:number} })
  | (EventBase & { type:'simulation_fault'; payload:{code:string; recoverable:boolean} });
```

`body_contact_started` should be internal/sampled telemetry rather than forwarded to React every time. `SessionReducer` adds `order_progressed`, `drink_served`, `score_changed`, `session_won/lost`. Each has distinct schema. Do not let UI invent these names in parallel.

## Simulation snapshot

```ts
export type DrinkSnapshot = Readonly<{
  id: DrinkId;
  tier: DrinkTier;
  status: 'arming'|'active'|'sleeping';
  position: Vec2;
  velocity: Vec2;
  angleRad: number;
  angularVelocity: number;
}>;
export interface SimulationSnapshot {
  sessionId: SessionId;
  step: number;
  status: SessionStatus;
  drinks: readonly DrinkSnapshot[];
  queue: readonly DrinkTier[];
  danger: ReadonlyArray<{id:DrinkId; remainingSteps:number}>;
}
```

Snapshots must be deep-readonly at API level or documented immutable copies. Avoid returning live Rapier object references that renderers can mutate.

## GameShell bridge

```ts
export interface GameShell {
  initialize(init: SimulationInit): Promise<void>;
  start(): void;
  pause(): void;
  resume(): void;
  submit(command: GameCommand): CommandResult;
  read(): SimulationSnapshot;
  subscribeEvents(listener:(batch:readonly SimEvent[])=>void):()=>void;
  dispose(): void;
}
```

A production `submit()` may enqueue and return `accepted_for_next_step` rather than immediate `applied`, so revise the return types together with the input workstream before implementation. Choose one semantic distinction and test it; don't pretend an asynchronously enqueued command is committed at the moment of submission.

## Versioning and compatibility

- `schemaVersion`: shape of event/command JSON.
- `physicsVersion`: constants and solver/engine config including Rapier version.
- `rulesVersion`: arbitration, auto-serving, danger, score behavior.
- `missionVersion`: content and random distribution.
- `rendererVersion`: optional, not required for authoritative simulation.
- `appVersion`: deployed frontend release version, independent of physics semantic versions.

All replays must specify versions. Never load saved replays using the current physics preset if they were recorded on different settings; either retain compatible verifier or mark replay unverified.

## Data ownership and trust

Physics positions and input exist on client. `SessionReducer` owns preview points and preview coins in v0.1.0. Later server owns actual wallet, inventory and leaderboard state. Client event payload is not trusted for persistent rewards; server must validate or replay. Use UTC timestamps for telemetry, but simulation outcomes rely on step numbers.

## Integration checklist

The implementation team's first contract PR should include: TS types, schemas, sample fixtures, compile/typecheck, event ID invariants and no forbidden module imports. Ask dependency owners to approve schema changes before merging. Coordinator manages merges; main needs explicit owner approval.
