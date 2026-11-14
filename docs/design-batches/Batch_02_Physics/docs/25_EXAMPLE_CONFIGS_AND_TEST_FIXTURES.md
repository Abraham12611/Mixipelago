# 25 — Reference Configuration, Mission Fixtures, Command Replays

**Note:** The following are proposed example configurations to illustrate engineering contracts. They are not canonical runtime schemas until engineers implement, validate and version the shared contracts. See the companion `examples/*.json` files in this package for machine-readable samples.

## Example physics preset

```json
{
  "schemaVersion": 1,
  "physicsVersion": "alpha-1-balanced",
  "stepHz": 60,
  "worldWidth": 10,
  "worldHeight": 15,
  "gravity": [0, 0],
  "drinkRadius": 0.34,
  "drinkDensity": 1.0,
  "linearDamping": 0.12,
  "angularDamping": 0.65,
  "friction": 0.06,
  "restitution": 0.38,
  "railRestitution": 0.28,
  "launchImpulse": 4.5,
  "maxSpeed": 10,
  "dangerLineY": 12.8,
  "dangerGraceSteps": 51,
  "launchCooldownSteps": 24,
  "ccd": true
}
```

## Example mission

```json
{
  "schemaVersion": 1,
  "missionId": "coconut-cove-001",
  "missionVersion": "alpha-1",
  "title": "First Splash",
  "physicsPresetId": "alpha-1-balanced",
  "seed": 740012,
  "startingBodies": [
    { "id": "setup-1", "tier": 1, "x": 4.7, "y": 6.0 },
    { "id": "setup-2", "tier": 2, "x": 6.4, "y": 3.7 }
  ],
  "spawnWeights": [
    { "tier": 1, "weight": 70 },
    { "tier": 2, "weight": 25 },
    { "tier": 3, "weight": 5 }
  ],
  "customerSlots": 2,
  "orderTargets": [2, 3],
  "objectives": [
    { "type": "orders_served", "target": 5 }
  ],
  "maxActiveBodies": 20,
  "maxShots": null,
  "autoServe": true,
  "maxTier": 8
}
```

This example would need a carefully authored tutorial queue to guarantee a first merge rather than relying only on the weighted random table. Engineers should add a `scriptedOpeningQueue` capability if tutorial acceptance requires it, and document precedence with generated sequence.

## Example replay

```json
{
  "replaySchemaVersion": 1,
  "sessionId": "demo-001",
  "missionId": "coconut-cove-001",
  "missionVersion": "alpha-1",
  "physicsVersion": "alpha-1-balanced",
  "rulesVersion": "merge-v1",
  "rapierPackageVersion": "PIN_DURING_IMPLEMENTATION",
  "seed": 740012,
  "commands": [
    { "step": 60, "seq": 1, "type": "launch", "dirX": 0, "dirY": -32767, "queueIndex": 0 },
    { "step": 170, "seq": 2, "type": "launch", "dirX": 8500, "dirY": -31646, "queueIndex": 1 }
  ]
}
```

Replay vector integers are illustrative and should be normalized by a precise, documented fixed-point conversion. The second vector should be checked for approximate norm and clamped by verifier; do not assume arbitrary input integers are normalized. A real canonical replay also needs `missionContentHash`, `rngAlgorithm`, schema IDs, and optional trusted challenge reference.

## Test fixture schema

```ts
interface PhysicsFixture {
  id: string;
  presetId: string;
  seed: number;
  startingBodies: Array<{
    id: string; tier: number; position: Vec2;
    velocity?: Vec2; angleRad?: number;
  }>;
  commands: Array<{step: number; direction: Vec2}>;
  runSteps: number;
  expected: {
    minMerges?: number;
    maxMerges?: number;
    exactTerminal?: string;
    noNan: true;
    noDuplicateConsume: true;
  };
}
```

## Fixture detail: 3-way collision

Initial: A tier-2 at (4.5,5.0) moving upward; B tier-2 at (4.2,4.4); C tier-2 at (4.8,4.4). Collision solver may report both AB and AC in same step. Arbiter stable sort chooses one; remaining third body stays active. After commit exactly two inputs consumed, one tier-3 result exists, one t2 body remains. No score from skipped pair. Test with reversed candidate event ordering and assert same result under canonical IDs.

## Fixture detail: angled nonmatching collision

Shooter tier-1 at (4.5, 11.8), target tier-3 at (5.0, 7.5). Launch direction `(0.13,-0.9915)` after canonical normalization; target collision should produce finite movement at an angle. Before approving numerical baselines, tune setup so the shot actually contacts the target under the chosen radius and damping; a fixture generator can compute a legal impact route or use a direct initial velocity fixture.

## Fixture detail: danger-rescue

Body tier-4 initially near `(4.6,12.5)` with bottom footprint near line and velocity slightly toward line; another body contacts and pushes it back. Test: warning appears if threshold intruded, resets after safe separation, no terminal loss before grace. Compare at different render FPS; outcome must be step-consistent.

## Content validator rules

- Nonempty `missionId` and `missionVersion`; well-formed seed.
- `worldWidth`, `worldHeight` positive finite, radius fits within board.
- All `startingBodies` positions inside legal play area and no severe invalid pre-overlap unless fixture specifically allows it.
- All tier values in [1,8] and reachable with configured evolution.
- `spawnWeights` positive total, entries sorted, no duplicates, no infinite/negative values.
- `maxActiveBodies` > setup body count and within testable hardware budget.
- Danger line above launch origin and below normal active play area.
- Order objectives possible under declared spawn/shot assumptions, or tagged experimental.
- `physicsVersion` known and config frozen in session.

## Production migration

Once schemas are accepted: move JSON to `content/physics/`, `content/missions/` and replay fixture directory; parse using Zod, generate TypeScript type exports and snapshot tests. The docs remain educational; live runtime reads machine-readable configs and versioned content manifest.
