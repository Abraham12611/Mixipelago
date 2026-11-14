# 08 — Spawn, Next-Drink Queue, Director, and Shot Pacing

## Responsibilities

The `GameDirector` determines which drink tier is next, validates mission-defined spawn distributions, enforces shot eligibility, avoids impossible first shots and manages active drink count. It does **not** move rigid bodies, draw sprites or award coins. The renderer displays the queue and active shooter; the physics adapter constructs the body only when a shot command is committed.

## Alpha drink distribution

Eight ordered tiers exist, but alpha's random launch queue should primarily use the first two or three tiers, never routinely spawn tier-7/8, so upgrading feels earned. One possible default distribution for a beginner board is tier 1 = 70%, tier 2 = 25%, tier 3 = 5%. This is a **proposed balance fixture**, not a verified distribution from the reference game. Advanced missions can provide alternate weighted distributions. Preserve a predictable `Next` indicator.

```ts
type SpawnTable = {
  entries: Array<{ tier: number; weight: number }>;
  maxActiveBodies: number;
  previewCount: number;
  launchCooldownSteps: number;
  seed: number;
};
```

All weights must be nonnegative finite numbers and sum to >0. Normalize weights deterministically at load time; use stable ordered tier entries. For replay, use a tiny explicitly defined seeded PRNG whose version is documented (e.g., PCG variant or xorshift32). Do **not** use `Math.random()` in any simulation or queue decision.

## Queue ownership

`nextQueue` contains logical tiers waiting to be launched. The currently armed shooter is represented separately from bodies on table. Minimum alpha preview of 1 (current + next) and optional lookahead of 2 in later quality-of-life improvements. Queue advances *only* after a validated launch command, not pointer down or visual animation. A cancelled aim leaves queue unchanged. A rejected shot due to overlap leaves queue unchanged, with user feedback.

## Shot eligibility

Before accepting launch:

1. Session is `running`, not terminal or paused.
2. Input gesture valid and launch cone respected.
3. `nextQueue` has an item and command queue index matches expected position.
4. Launch slot is not already occupied by a still-arming body or active collider that would cause an immediate overlap.
5. Prior shot cooldown/settle criterion has elapsed.
6. Board active drink count is below configured hard capacity (or mission defines overflow behavior explicitly).
7. Command ID not previously applied.

Return structured rejection `{kind:'rejected', reason:'...'}`; do not silently consume a drink. Prevent animated UI from accepting input when physics is not ready.

## Spawn position

Use a stable launcher center from board config. It may be fixed in alpha; later unlock left/right launcher positions as mission mechanics. Spawn a dynamic body at a non-overlapping legal point, wake it, apply fixed impulse at center of mass. Always count this as one `shot_fired`. New launch bodies have a brief danger-exemption/arming state until they cross into the playable field or a defined maximum arming interval. When launched, they become merge eligible according to rules; clarify whether same-tier collision while arming can merge (proposal: once moving into playable field).

## Pacing choice: cooldown vs settling

A strict "wait until all glasses sleep" policy can make the game unusably slow on a near-frictionless tabletop. Proposed alpha: short fixed cooldown (24 fixed steps ≈400ms) plus a safety check that the previous shooter has cleared the spawn region; **not** a full-table settling requirement. If the scene has severe movement or a merge animation in progress, a configurable soft delay may improve readability. Always show when the next shot is eligible.

## Difficulty and fairness

Dangerous outcomes can arise from malicious/unlucky spawn queues. For the first few missions, seed curated sequences or use a fairness filter that avoids long streaks of impossible useful tiers. But any fairness filter affects future ranked replay and must be implemented deterministically and versioned. Designer-authored tutorial sequence should override random distribution and include a guaranteed initial merge. Later modes may intentionally challenge with fixed next sequences.

## Spawn effects

The visual "next drink slides into launch circle" does **not** create an actual physics body until launch. This prevents accidental pre-shot collisions and browser-layout-dependent spawn placement. A phantom preview uses a separate renderer layer, not a collision object. FX state and body state remain distinct.

## Director configuration and authoring

Missions specify: allowed starting tiers, queue seed, weighted spawn table, starting bodies, launching frequency, maximum active objects, target order tiers, and max shot budget if applicable. Validate content offline against schemas: never target a tier higher than reachable within mission budget unless intended as an explicit survival/score challenge.

## API sketch

```ts
interface GameDirector {
  peek(): { currentTier: number; nextTier?: number };
  canLaunch(state: SessionState): RejectionReason | null;
  commitLaunch(cmd: LaunchCommand): SpawnDecision;
  onSessionEvent(event: SessionEvent): void;
  reset(seed: number, mission: MissionConfig): void;
}
```

Director commits and queue advance in same logical transaction; it should not mutate the renderer or issue sounds directly.

## Test cases

- Same seed + mission version -> exact same tier queue.
- Rejected command and cancelled input -> no queue advance.
- Duplicate command ID -> one shot and one queue advance.
- Fast input spam at cooldown -> correct rejections and clear UI state.
- Hundreds of spawns -> no invalid tier or `NaN` weight.
- Tutorial seed guarantees intended first merge fixture.
- Future content version changes queue only after intended session/version boundary.
