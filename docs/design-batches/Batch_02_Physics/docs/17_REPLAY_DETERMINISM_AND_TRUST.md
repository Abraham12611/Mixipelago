# 17 — Deterministic Replays, Physics Snapshots, Competitive Trust

## Important technical clarification

According to Rapier's **JavaScript/WASM determinism guide**, a WASM/JavaScript build can produce **cross-platform deterministic** results when simulation parameters, initial state, insertion/removal order, fixed timesteps, and underlying library version are identical. Rapier also publishes specifically named **`-deterministic` and `-deterministic-compat` package variants** intended to guarantee deterministic execution; we must verify which exact build the app installs, rather than assuming any generic `-compat` build carries the strongest guarantee. This is a meaningful option for Mixipelago. However, the whole application is *not automatically deterministic* merely because Rapier is; user input encoding, RNG, JS transcendentals, event order, game rules, async effects and serialization must also be controlled.

Primary source: https://rapier.rs/docs/user_guides/javascript/determinism/ . Package build variants: https://www.npmjs.com/package/@dimforge/rapier2d-compat .

Batch 1 prudently said not to assume cross-platform replay without testing. Batch 2 **refines** that caveat: Rapier documents deterministic WASM execution under strict conditions and provides deterministic-specific package variants. Our exact selected build must demonstrate those conditions with cross-browser hash tests before trusting replays for rankings.

## Threat boundary

Client owns local rendered simulation and can be modified by an adversary. A browser can fabricate a high score or event log. Uploading `score: 999999` to the server is not sufficient. Future leaderboard uses canonical mission seed and approved content/rules versions, plus input sequence or authoritative computation, then accepts only a validated score.

## Replay record

```ts
type ReplayRecord = {
  replaySchemaVersion: 1;
  appVersion: string;
  rapierPackageVersion: string;
  physicsVersion: string;
  rulesVersion: string;
  missionId: string;
  missionVersion: string;
  missionContentHash: string;
  assetManifestVersion?: string; // visual reference only
  rngAlgorithm: string;
  seed: number;
  commands: Array<{
    step: number;
    seq: number;
    type: 'launch';
    dirX: number;       // canonical quantized integer
    dirY: number;
    queueIndex: number;
  }>;
  periodicStateHashes?: Array<{step:number; hash:string}>;
  declaredResult?: {score:number; ordersServed:number; outcome:string};
};
```

Only gameplay-affecting commands belong in authoritative replay. Mouse raw pixels, real timestamps, cosmetic FX and music choices do not. If future mechanics include boosters or tap-to-serve, record those commands explicitly with validated IDs and step indices.

## Deterministic RNG

Use a named/versioned integer PRNG (e.g., xorshift32 or PCG32 with thoroughly tested implementation). Store internal seed/state. Use integer arithmetic with explicit overflow behavior and reproducible normalization to spawn weights; avoid `Math.random`, `Date.now` or remote network data in simulation decisions. If using trigonometric functions to derive angles, pre-quantize direction or use deterministic lookup/number representation; Rapier documentation warns `Math.sin`/`Math.cos` initial-condition differences can violate deterministic assumptions.

## Ordering determinism

Stable IDs generated from monotonic counters with session prefix, not object memory handles. Body insertion/removal order must match replay. Contact events can be gathered then sorted by canonical pair key so application merge arbitration order is stable. Because collision callbacks may deliver handle IDs in different order, normalize before comparing. All event mutation occurs at fixed-step boundaries; no `Promise` scheduling decides merge order.

## State hashes and verifier

Every N fixed steps (e.g., 120) generate a canonical digest of logical state (drink IDs, tiers, positions, velocities, PRNG state, queue, session rules) and optionally Rapier `World.takeSnapshot()` bytes. Hashes are for debugging and integrity comparisons; do not assume byte-level snapshot stability across engine upgrades. Rapier world snapshots can be useful for exact same-version state persistence; versioned logical save is preferable for long-term migration.

A verifier rebuilds the same mission/physics world, applies commands at recorded steps, and compares final score and periodic hashes. It must run with identical Rapier WASM version and **package build flavor** (prefer a tested deterministic variant for ranked verification), content/preset hashes, and deterministic app logic. A client-submitted replay is still untrusted: the verifier must reject illegal fire timings, impossible aims, stale queue indices and out-of-range commands.

## Cross-platform test matrix

- Chromium desktop Linux/Windows, Firefox desktop, Safari macOS, Android Chrome, iOS Safari.
- Same seed, mission version, physics version and command transcript.
- Collect logical state hashes at steps 60, 180, 600 and final.
- Identify divergences by first differing step, contact event order and body insertion sequence.
- On mismatch, pause ranked feature implementation; casual alpha can still operate with local progress.

## Replay compression and privacy

Input logs can be compact: delta-encoded step numbers plus quantized direction and command types, compressed for upload. Do not include raw pointer path or precise location in ranking payload. Limit replay size, command count and max session steps to protect verification infrastructure. Enforce authenticated identity and server-generated challenge IDs once online ranked mode ships.

## Ranked architecture options

1. **Server replay verification:** Client plays locally, sends input stream, backend re-simulates and validates final score. Best first candidate if deterministic reproduction is proven. Benefit: responsive play, modest server usage; cost: CPU for verification, replay infrastructure.
2. **Server-authoritative live simulation:** Dedicated authoritative service advances worlds and validates input in real time. Stronger for head-to-head play but adds latency and operational complexity; defer.
3. **Heuristic score checks:** Use only for anomaly alerts, never sole basis for rewards with meaningful value.

## Fraud patterns

Fabricated event results; illegal rapid-fire commands; impossible drag angles; stale/forged mission config; modified local rewards; replay spam; seed/queue manipulation; repeat submission for same challenge; time dilation attempts; accidental duplicate reward job. Address with validation, replay, idempotency, rate limits, durable signed challenge records and review tooling. **Do not promise anti-cheat perfection.**

## Alpha boundary

v0.1.0 stores *preview-only local scores and coins*. There is no public leaderboard, real prize, trusted progression or monetary purchase. Replay recording can be built as a dev feature in alpha, but ranking verification is not a 72-hour release blocker.
