# 05 — Fixed-Step Simulation, Body Lifecycle, Pause/Resume, Resource Management

## Clock authority

Game time is counted in **simulation step integers**, not based on the browser's wall clock or Phaser animation ticks. `stepIndex` begins at 0 per session and increments after each successful fixed physics step. `STEP_SECONDS = 1/60` is proposed. Time-limited missions distinguish **active game time** from real elapsed wall time; alpha uses active time. Event expiration in later worlds may require wall-clock time, but must not alter the physics loop unexpectedly.

## Render accumulator

```ts
const STEP_MS = 1000 / 60;
const MAX_STEPS_PER_FRAME = 5;
const MAX_ELAPSED_MS = 100;
let accumulatorMs = 0;

function renderFrame(elapsedMs: number) {
  if (session.paused) return;
  accumulatorMs += Math.min(elapsedMs, MAX_ELAPSED_MS);
  let advanced = 0;
  while (accumulatorMs >= STEP_MS && advanced < MAX_STEPS_PER_FRAME) {
    simulation.stepFixed(); // consumes scheduled commands, physics, merges
    accumulatorMs -= STEP_MS;
    advanced++;
  }
  if (advanced === MAX_STEPS_PER_FRAME && accumulatorMs >= STEP_MS) {
    // Do not run unbounded catch-up after a device stalls.
    recordOverload(accumulatorMs);
    accumulatorMs = 0;
  }
  renderer.renderInterpolation(accumulatorMs / STEP_MS);
}
```

In actual production verify that Phaser's update loop uses the expected delta units. A fixed step must set the Rapier world's fixed `dt`; never call Rapier's step with a dynamically varying timestep. An occasional frame can perform zero physics steps, which is correct.

## Pipeline order per simulation step

1. Validate the current session is `running` and not terminal.
2. Dequeue commands scheduled for this step; stable-sort by accepted command sequence, not event arrival timing.
3. Apply valid launch or other state commands at a safe mutation boundary; create bodies and issue impulses.
4. Advance Rapier world by exactly fixed timestep, collect collision events through `EventQueue`.
5. Translate collider handles into logical drink IDs and append normalized contact candidates; do not modify world inside event queue callback.
6. Resolve eligible merges in stable order, marking input IDs consumed.
7. Commit body removals and result spawns through a deferred mutation queue.
8. Resolve follow-up contact opportunities on *subsequent* step (unless a specific conflict-free policy allows within-step chained logic).
9. Run session reducer on committed semantic events: score, customer orders, danger and terminal state.
10. Emit read-only snapshot and ordered event batch; let renderer/audio consume asynchronously outside physics critical path.

## Drink lifecycle

```text
queued (logical next tier, no body)
   ↓ launch accepted
spawned/armed (body exists, danger exemption)
   ↓ enters playable area or grace arming ends
active (collidable, can merge)
   ├─→ merging/claimed ─→ consumed (remove body + sprite after FX)
   ├─→ serving/claimed ─→ consumed (order reward once)
   ├─→ cleared/claimed ─→ consumed (booster or level cleanup)
   └─→ active/sleeping (sleep is a physics optimization, not logical disable)
```

Use stable `drinkId` independent of Rapier collider/body handle. Handles can be reused by the physics runtime and must not be persisted across sessions. Deleting a physics body before collecting all queued contacts can create stale handle references; use stable lookup mapping and deferred destruction.

## Pause/resume correctness

Pause causes: user pause, page visibility hidden, app background, main menu overlay, device orientation change, WebGL context loss (rendering), game route unmount. On pause, cancel active aim, stop new commands, suspend step accumulation, freeze danger timers and active mission timers, mute or fade SFX/music as appropriate, and save a logical checkpoint if supported. On resume, first frame should not process accumulated hidden time. Ensure audio context resumes after user gesture where required.

A saved local checkpoint stores content/physics versions, PRNG state, step index, next queue and logical drink state; **never store raw live WASM handles**. For an exact in-memory quick resume, an engine snapshot may be used; for durable local save across app upgrades, use an explicit schema/migration and verify Rapier snapshot compatibility. If save validation fails, explain recovery and offer restart; don't corrupt existing player profile.

## Session and resource lifecycle

- One `SimulationCore` and Rapier world per running puzzle session.
- `initialize()` once, `dispose()` idempotent, no orphan RAF/timers/subscriptions.
- Sprite object pooling is recommended; Rapier handle reuse must be controlled by world API and distinct drink IDs.
- On route exit/retry: unsubscribe event listeners, stop any FX tied to removed entities, dispose physics world and interaction controller, release scene-specific textures only when safe to do so.
- Avoid repeated WASM initialization per drink. Initialize Rapier module once per runtime and construct/destroy worlds as needed.

## Consistency assertions

- After any step, a `consumed` drink ID cannot appear in active bodies, pending merges, active orders or launch queue.
- Number of logical active bodies equals number of active Rapier drink-body mappings, ignoring fixed walls/sensors.
- Event `sequence` increases monotonically; every emitted `drink_merged` corresponds to exactly two input IDs and exactly one result ID.
- Terminal `won`/`lost` blocks new launch and further reward events.
- Max active-body budget is never exceeded without a deliberate resolved loss/recovery rule.

## Slow-device policy

When render frame rate drops, the physics steps remain fixed; we cap catch-up and visibly degrade cosmetic effects or display a performance hint. For competitive fairness, dropping steps instead of running them changes real-time pace; future ranked modes should use a stricter clock/validation model than casual alpha. Measure and disclose if an assisted quality tier materially changes gameplay.

## Unit/integration tests

Test 60Hz and 30Hz render schedules with equal command step indices; 10-second background/foreground; restart 50 times without leaked listeners; pause exactly during contact/merge visual; input arriving one step after terminal state; repeated `dispose()`; corrupt saved checkpoint; zero render frames followed by a single frame; long frame of >5 seconds should not simulate five seconds instantaneously.
