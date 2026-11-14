# 12 — Implementation Blueprint: Modules, Algorithms, Representative Code

## Module topology

```
packages/game-core/
  src/session/SessionReducer.ts
  src/rules/MergeEligibility.ts
  src/rules/OrderMatching.ts
  src/rules/DangerEvaluator.ts
  src/director/GameDirector.ts
  src/random/SeededRng.ts
packages/physics-rapier/
  src/RapierWorldAdapter.ts
  src/BodyRegistry.ts
  src/ContactCollector.ts
  src/MergeArbiter.ts
  src/DeferredMutations.ts
  src/FixedStepClock.ts
packages/game-renderer/
  src/scenes/TabletopScene.ts
  src/input/AimController.ts
  src/visuals/DrinkSpriteView.ts
  src/visuals/MergeFxDirector.ts
  src/visuals/TrajectoryGuide.ts
packages/game-ui/
  src/GameHost.tsx
  src/GameHUD.tsx
```

All names are proposed. Actual implementations should export a tested public API from each package. Do not place business rules in Phaser Scene methods.

## Pure merge eligibility

```ts
export function canMerge(
  a: {tier:number; status:string; reservedForOrder?:boolean},
  b: {tier:number; status:string; reservedForOrder?:boolean},
  maxTier: number
): boolean {
  return a.status === 'active' && b.status === 'active'
    && !a.reservedForOrder && !b.reservedForOrder
    && a.tier === b.tier && a.tier < maxTier;
}
```

A future recipe graph can replace simple equality and next-tier mapping behind the same rules interface, but alpha must avoid unsupported cross-recipe logic.

## Contact collection and stable arbitration

```ts
function collectCandidates(
  raw: ReadonlyArray<[number, number, boolean]>,
  colliderToDrinkId: Map<number, string>
): ContactCandidate[] {
  const seen = new Set<string>();
  const out: ContactCandidate[] = [];
  for (const [h1, h2, started] of raw) {
    if (!started) continue;
    const a = colliderToDrinkId.get(h1);
    const b = colliderToDrinkId.get(h2);
    if (!a || !b || a === b) continue;
    const [lo, hi] = [a, b].sort();
    const key = `${lo}:${hi}`;
    if (seen.has(key)) continue;
    seen.add(key);
    out.push({a:lo,b:hi,key});
  }
  return out.sort((x,y) => x.key.localeCompare(y.key));
}
```

`localeCompare()` may be locale-dependent for some strings; for strict replay use stable byte-wise codepoint comparisons of canonical ASCII IDs or numeric monotonic IDs. The snippet is conceptual; production tests must lock sorting semantics. Do not use raw Rapier handle as the primary stable sort key.

## One fixed step

```ts
function stepFixed(): readonly DomainEvent[] {
  assertRunning();
  const step = currentStep;
  applyScheduledCommands(step);       // may spawn/launch a body
  world.step(eventQueue);             // Rapier dt remains fixed
  const raw = drainCollisionEvents(eventQueue);
  const contacts = normalizeContacts(raw, bodyRegistry);
  const txs = mergeArbiter.claim(contacts, gameState, step);
  commitMergesAfterDrain(txs);        // remove two, create one
  const domainEvents = collectCommittedEvents();
  const nextState = sessionReducer.reduce(gameState, domainEvents);
  gameState = evaluateWinLoss(nextState, step);
  currentStep++;
  assertInvariants();
  return domainEvents;
}
```

This is **not copy/paste-complete production code**. `claim` cannot mutate Rapier while events are drained; `commitMergesAfterDrain` must update collider mappings and logical states atomically. The `SessionReducer` should emit further semantic events from merges/serves and apply unique IDs. Include a `try/catch` boundary to recover from invalid content without continuing a corrupt world.

## Collision event queue sketch

```ts
const queue = new RAPIER.EventQueue(true);
world.step(queue);
const started: Array<[number, number, boolean]> = [];
queue.drainCollisionEvents((a,b,isStarted) => {
  started.push([a,b,isStarted]);
});
```

Rapier docs confirm this flow; pin library version and compile the adapter before the integration PR. Contact-force events are optional and should be disabled until evaluated for SFX.

## Spawn and impulse

```ts
const body = world.createRigidBody(
  RAPIER.RigidBodyDesc.dynamic()
    .setTranslation(origin.x, origin.y)
    .setLinearDamping(preset.linearDamping)
    .setAngularDamping(preset.angularDamping)
    .setCcdEnabled(preset.ccd)
);
const collider = world.createCollider(
  RAPIER.ColliderDesc.ball(preset.drinkRadius)
    .setDensity(preset.drinkDensity)
    .setFriction(preset.friction)
    .setRestitution(preset.restitution)
    .setActiveEvents(RAPIER.ActiveEvents.COLLISION_EVENTS),
  body
);
body.applyImpulse(
  {x: direction.x*preset.launchImpulse,
   y: direction.y*preset.launchImpulse}, true
);
```

## Render synchronization

Each active `DrinkView` stores its own sprite and logical drink ID. After each physics step, cache `posePrevious` and `poseCurrent`. Render at `alpha=(accumulator/stepDuration)`:

```
visualX = previous.x + (current.x - previous.x) * alpha
visualY = previous.y + (current.y - previous.y) * alpha
```

Angles require wrap-aware interpolation to avoid spinning the long way across ±π. If pose belongs to a newly spawned or consumed object, bypass interpolation or use a controlled spawn/despawn visual animation. Renderer must not affect physics pose. Camera transform applied after interpolation.

## Event-to-effects integration

```ts
const effectMap = {
  shot_fired: 'launch_swish',
  drink_merged: 'merge_pop',
  danger_warning: 'danger_tick',
  session_won: 'victory_sting'
} as const;
```

EffectsDirector looks up assets and uses object pooling. It reads `eventId` once to avoid double-playing when UI resubscribes. If asset unavailable, log diagnostic and skip FX, not scoring.

## Session unit testing without Phaser

Instantiate a simulation with stubbed asset/audio adapters. Advance N fixed steps with a deterministic command list. Assert active body IDs, tiers, score events and terminal state. It must run headless under a Node-compatible WASM import/test runner. For visual E2E, mount Phaser in a browser and drive pointer commands through actual game canvas; no direct mutation of internal state to fake a passing UX test.

## Engineering tasks

1. Create `domain-contracts` types and validate them with Zod.
2. Implement `RapierWorldAdapter` (module init, static rails, bodies, snapshots).
3. Build `FixedStepClock` and pause/resume instrumentation.
4. Implement `BodyRegistry` and safe deletion.
5. Add `ContactCollector` and `MergeArbiter` with exactly-once test suite.
6. Add deterministic `GameDirector` queue and command validation.
7. Connect `SessionReducer` (orders, score, danger).
8. Mount Phaser scene and display sprites/interpolation.
9. Bind mouse/touch aim and keyboard alternative.
10. Wire HUD projections, FX, audio and persistence adapter.
11. Integrate physics lab, metrics and browser QA.

## Dependency gates

No renderer PR should change merge rules. No collision solver PR should change scoring. No input PR should manipulate Rapier directly except through GameShell/SimulationCore. Content artists only supply asset IDs and metadata, not body physics. Coordinator approves public contract changes and integration merges; owner controls promotion to main.
