# 26 — Typed Content Examples, Validation and Configuration

## Purpose

Provide concrete schemas/fixtures so engineering teams can implement in parallel. These are **proposed examples** and must be converted to Zod and JSON Schema in shared code. Do not assume exact values match final balance.

## 1. Example drink catalog

```json
{
  "schemaVersion": 1,
  "catalogId": "core-drinks-alpha",
  "catalogVersion": "0.1.0",
  "tiers": [
    {"id":"citrus-shot","tier":1,"name":"Citrus Shot","nextTierId":"sunny-lemon","assetId":"drink.tier1.board","mergeScore":10},
    {"id":"sunny-lemon","tier":2,"name":"Sunny Lemon","nextTierId":"sunset-splash","assetId":"drink.tier2.board","mergeScore":25},
    {"id":"sunset-splash","tier":3,"name":"Sunset Splash","nextTierId":"blossom-fizz","assetId":"drink.tier3.board","mergeScore":60},
    {"id":"blossom-fizz","tier":4,"name":"Blossom Fizz","nextTierId":"coral-martini","assetId":"drink.tier4.board","mergeScore":140},
    {"id":"coral-martini","tier":5,"name":"Coral Martini","nextTierId":"mint-lagoon","assetId":"drink.tier5.board","mergeScore":320},
    {"id":"mint-lagoon","tier":6,"name":"Mint Lagoon","nextTierId":"ocean-cloud","assetId":"drink.tier6.board","mergeScore":720},
    {"id":"ocean-cloud","tier":7,"name":"Ocean Cloud","nextTierId":"crown-of-isles","assetId":"drink.tier7.board","mergeScore":1600},
    {"id":"crown-of-isles","tier":8,"name":"Crown of the Isles","nextTierId":null,"assetId":"drink.tier8.board","mergeScore":3500}
  ]
}
```

`mergeScore` is awarded on **creation of that output tier**, not when consuming the two inputs. Tier 1 cannot result from a merge in this chain; tier 1 value is reserved for future alternate sources. This avoids double counting.

## 2. Example first mission (canonical goal)

```json
{
  "schemaVersion": 1,
  "missionId": "coconut-cove-001",
  "islandId": "coconut-cove",
  "missionVersion": "1.0.0",
  "mode": "service",
  "board": {
    "presetId": "standard-low-friction-alpha",
    "width": 10,
    "height": 15,
    "dangerLineY": 12.8,
    "maxActiveDrinks": 18,
    "startingDrinks": [
      {"tier":1,"x":4.25,"y":4.3},
      {"tier":1,"x":6.2,"y":4.3}
    ]
  },
  "spawn": {
    "seedMode": "per-run",
    "pool": [{"tier":1,"weight":100}],
    "firstItems": [1,1,1,1,1]
  },
  "orders": {
    "maxVisible": 2,
    "initial": [
      {"id":"ord-001","requestedTier":2,"quantity":1,"coinReward":10},
      {"id":"ord-002","requestedTier":3,"quantity":1,"coinReward":20}
    ],
    "replacementPoolId": "cove-beginner"
  },
  "goal": {"type":"orders_served","count":2},
  "rewards": {"previewCoins":20,"stars":1},
  "visualThemeId": "coconut-cove-day"
}
```

Note that a first mission requiring both tier 2 and tier 3 must have a *provably solvable* sequence. The first items and starting board should be tested in automated fixtures and owner playtest; configuration alone does not prove solvability. `rewards.previewCoins` is an optional completion bonus **in addition to** individual order rewards; display them separately to prevent confusion.

## 3. Minimal runtime types

```ts
type DrinkObject = {
  objectId: string;
  tier: number;
  state: 'active'|'merging'|'consumed'|'served';
  bodyHandle: number;
  colliderHandle: number;
};

type LaunchCommand = {
  commandId: string;
  sessionId: string;
  step: number;
  direction: { x: number; y: number };
  power: number;
};

type MergeEvent = {
  eventId: string;
  sessionId: string;
  step: number;
  inputObjectIds: [string, string];
  outputObjectId: string;
  outputTier: number;
};
```

Caution: `bodyHandle` and `colliderHandle` are runtime-only. They must not be accepted as durable IDs or written directly into long-lived saves.

## 4. Example content graph

```json
{
  "islandId": "coconut-cove",
  "nodes": [
    {"missionId":"coconut-cove-001","requires":[],"position":[0.25,0.85]},
    {"missionId":"coconut-cove-002","requires":["coconut-cove-001"],"position":[0.45,0.72]},
    {"missionId":"coconut-cove-003","requires":["coconut-cove-002"],"position":[0.32,0.6]},
    {"missionId":"coconut-cove-side-001","requires":["coconut-cove-002"],"position":[0.75,0.67]}
  ]
}
```

## 5. Validation rules

- Unique stable IDs, contiguous tier sequence, valid `nextTierId`, no accidental cycles.
- All `assetId` references exist in manifest, source license approved.
- Mission spawn pool weights >0; no negative rewards or unsafe integer overflow.
- `board.startingDrinks` positions inside playable bounds and nonoverlapping by collider radius.
- Customer requests refer to valid tiers and have finite quantities/rewards.
- No missing prerequisites, no forbidden island graph cycle, all nodes reachable as intended.
- Content hash stored with published mission; version conflicts produce visible recovery path.
- All math/read settings validated at runtime, including localStorage reads.

## 6. Configuration management

Use `contentVersion` independent of app release; lock a session's manifest upon start. Newly published content should not silently change an active run. Build deterministic test fixtures from seeded RNG. In v0.1, keep config JSON in repo; future admin publishes signed/hashed content manifests to CDN.
