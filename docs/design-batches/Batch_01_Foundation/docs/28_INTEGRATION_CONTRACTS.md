# 28 — Cross-Team Integration Contracts

## Why this exists

Parallel engineers can independently build Physics, Phaser UI, React UI, session rules, assets and future APIs if the interface between them is stable. **No module imports implementation internals of another team's subsystem** when a public contract exists.

## A. GameShell public interface

```ts
export type GameShellCommands = {
  startMission(missionId: string): Promise<void>;
  pause(): void;
  resume(): void;
  restart(): Promise<void>;
  aimStart(input: { pointerId: number; world: Vec2 }): void;
  aimMove(input: { pointerId: number; world: Vec2 }): void;
  aimEnd(input: { pointerId: number; world: Vec2 }): void;
  aimCancel(pointerId: number): void;
  setQuality(profile: 'auto'|'low'|'high'): void;
};
export type Vec2 = {x: number; y: number};
```

React controls call `GameShellCommands`, subscribe to a throttled read model, and do not call Rapier APIs directly. Phaser input maps pointer to normalized world coordinates. Simulation events do not mutate React state at physics-frame frequency; UI is updated at bounded rate (e.g. 10–20Hz for HUD; immediate for critical discrete events).

## B. SimulationCore API

```ts
export interface SimulationCore {
  initialize(input: SimInit): Promise<void>;
  applyCommand(command: LaunchCommand): CommandResult;
  stepFixed(): ReadonlyArray<SimulationEvent>;
  getSnapshot(): SimulationSnapshot;
  pause(): void;
  resume(): void;
  dispose(): void;
}
```

`SimInit` contains mission config + physics preset + seed. `stepFixed` must process physics and candidate merges without awaiting network or UI. Renderer reads snapshot and interpolates. `dispose` is idempotent.

## C. SessionReducer

Input: simulation events (valid ones only), mission config, current session state. Output: new session state + semantic effects/events. Rewards are applied in one ordered reducer. Terminal state is irreversible per session. No JSX/DOM in reducer; pure TypeScript and seeded randomness only.

## D. UI projection

`GameHudViewModel` includes `status`, `score`, `combo`, `previewCoins`, `nextTier`, `activeOrders`, `goalProgress`, `shots`, `timeActiveMs`, `warning`, `lastFeedback`. Prefer derived values from reducer, not duplicated local state. Use selectors/memoization and do not force Phaser remount on each score change.

## E. Asset manifest contract

Every sprite is requested by stable `assetId`. Loading returns texture key or placeholder; map asset metadata includes width/height, pivot, and declared collision footprint independent of image pixel bounds. Audio assets have semantic IDs and optional fallback. Missing non-critical art cannot crash physics; log missing asset and display standardized placeholder.

## F. Storage contract

`LocalSaveRepository`: `load(): Promise<LocalSaveV1>`, `save(next): Promise<void>`, `reset(confirm): Promise<void>`, `migrate(raw): LocalSaveV1`. Save adapter must not store live rigid body handles. Later `RemoteProgressRepository` will return server-owned state and verification pending states explicitly.

## G. Backend interface (future)

`SessionService`, `WalletService`, `ShopService`, `ProgressionService`, `LeaderboardService`, `EventService` interfaces are imported from shared domain contract package. Use idempotency, authenticated subject, error enums and schema versions. No frontend code directly runs SQL wallet updates.

## H. Event naming and lifecycle

Events use consistent snake_case and have `eventId`, `schemaVersion`, `sessionId?`, `sequence`, `occurredAtStep?`, `payload`. Never emit the same `drink_merged` event twice; listeners must still be idempotent. Visual FX is a **consumer** of events, not an owner of scoring outcomes.

## I. Compatibility policy

When a contract changes: update types, schema, tests and docs in the same PR; request approval from dependent workstreams. Maintain at least one previous content/save schema during active early releases. Version the physics config separately from content, app and API.

## J. Package boundaries and imports

`game-core` must not import Phaser, React, `window`, localStorage or database clients. `physics-rapier` depends on Rapier + core types, not React. `game-renderer` depends on core + physics public bridge. `game-ui` depends on view models, not physical body implementation. Backend imports shared contracts, not Phaser.

## K. Integration test

Synthetic input command → valid Rapier contact → `drink_merged` → order complete → session result → UI projection and local save. This must be demonstrably possible without duplicated score, missing asset crash, or hidden network requirement.
