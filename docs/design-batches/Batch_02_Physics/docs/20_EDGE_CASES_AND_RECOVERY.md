# 20 — Edge Cases, Failure Handling, and Recovery Scenarios

## Core principle

A physics-heavy puzzle will encounter interactions not covered by happy-path scripts: near-simultaneous contacts, overlap after spawning, browser interruption, low FPS, sound autoplay blocks and corrupted persistence. Every surprising state must resolve deterministically, not freeze or duplicate reward.

## Contact and merge issues

**Stale collider handle:** a callback references handle removed earlier this step. Handler uses stable map with session version; unknown handle is ignored/logged, never mapped to newly recycled logical ID. **Duplicate collision started event:** `pairKey` deduplicated for step; claimed objects cannot merge twice. **Multiple pair priority:** sort by stable logical ID and step; conflict skipped. **Result already overlapping:** bounded next-step overlap query; no recursion. **No legal result location:** deterministic fallback search plus controlled fault/retry; never place inside a wall or leave body NaN. **Max tier:** no further merge; communicate when useful via catalog UI. **Two bodies claim same customer reward:** order matching and serving claim handled by one reducer; transaction ID idempotent.

## Physics numeric anomalies

Validate finite coordinates, velocities, mass/density, damping, restitution, direction vector length and normalized config on load and every command. Instrument severe penetration, extremely high speed and repeated solver instability. If values become nonfinite at runtime, pause session, capture safe diagnostic context and offer retry from last valid checkpoint; **do not** continue sim or submit score. Do not directly corrupt player wallet or other durable state.

## Spawn and boundary conditions

- Launcher blocked by resting glass: deny shot with clear visual cue; queue unchanged.
- Body rests exactly at danger threshold: define strict comparison and epsilon/hysteresis once, test.
- A merging input is over danger line: exclude claimed body from counting; result starts with defined grace.
- Three new bodies would exceed capacity due to scripted content: content validation should reject before mission starts.
- Very high impact knocks drink completely off-screen: static rails or rules should keep valid world state; if impossible, detect out of bounds and apply documented recovery/loss.
- Transparent/large sprite visually overlaps while foot colliders do not: fix visual footprint/pivot or add clear effect; don't secretly widen collider per image.

## Input interruptions

- Pointer capture lost when browser UI opens: `aim_cancelled` and no shot.
- Touch target under phone's home gesture: adjust safe area; don't rely on OS gesture suppression.
- Browser zoom mid-gesture: cancel and recalculate transform.
- Pointer-up fired twice by wrapper: command idempotency rejects duplicate.
- Keyboard fire repeatedly held: deliberate key repeat cadence, no accidental rapid launches.
- Screen-reader focus leaving canvas: pause assist or keep gameplay state appropriate to control mode.

## Rendering and audio failures

- WebGL context lost: pause physics, show reconnect/retry; reload textures from versioned manifest. Do not run invisible rounds that players cannot control.
- Missing sprite: show standard placeholder with correct size/pivot; log; gameplay remains valid.
- Texture OOM: select lower quality after safe restart, limit loading, provide diagnostic; no automatic coin loss.
- Audio blocked by autoplay: game still plays silently; once user interacts, initialize audio. Muting/volume cannot alter simulation.
- Missing SFX: no impact-sound crash or reward issue.

## Persistence and replay errors

- Corrupt `localStorage`/IndexedDB content: schema validation; offer reset local preview progress with explicit communication; keep original backup string if practical.
- Save from previous physics version: migrate if compatible; otherwise preserve historical progress summary, restart round under new version rather than loading inconsistent body handles.
- Browser kills tab: on reopen use checkpoint/retry path, not pretend to reconstruct every missed substep from wall-clock.
- Replay submitted with unknown/retired physics version: reject as unverifiable or route to matching pinned verifier; never validate against a different version without disclosure.
- Outbound API down: alpha offline play continues because local-only; future online purchases require server availability and safe idempotent retry.

## User-facing error taxonomy

| Code | UI explanation | Recovery |
|---|---|---|
| `PHYSICS_INIT_FAILED` | Unable to start physics engine | Retry/reload; diagnostics |
| `RENDER_CONTEXT_LOST` | Graphics temporarily unavailable | Restore or safe restart |
| `INVALID_MISSION_CONFIG` | Mission data couldn't load | Retry from menu; report ID |
| `LAUNCH_BLOCKED` | Clear space near the launcher | Wait or use available board move |
| `SHOT_ON_COOLDOWN` | Next drink isn't ready | Short cooldown feedback |
| `SAVE_MIGRATION_FAILED` | Local preview progress needs reset | Preserve backup and confirm reset |
| `SIMULATION_INVALID_STATE` | Something went wrong with the board | Safe retry, no phantom rewards |
| `AUDIO_UNAVAILABLE` | Sounds cannot play right now | Continue muted |

Use friendly UI strings with consistent localization keys. Avoid surfacing raw stack traces to users; error IDs help diagnostics.

## Diagnostics payload

Record `appVersion`, `sessionId` (ephemeral), `missionId`, `physicsVersion`, `rulesVersion`, `step`, `browserFamily`, `deviceQualityTier`, `activeBodies`, `lastCommandIds` and anonymized error code. Never upload full private profile or precise location for physics diagnosis. Sampling and retention policies belong to Batch 20 analytics/security.

## Stress playbook

Test 30 FPS throttle, 120Hz display, low memory mode, repeated pause/resume, 100 shots, 50 restarts, 40 body contacts, simultaneous multi-merge, immediate tab navigation, network disconnected, texture missing, sound missing and corrupt save. Distinguish service outages from game engine errors; don't introduce unnecessary runtime backend dependencies in v0.1.0.
