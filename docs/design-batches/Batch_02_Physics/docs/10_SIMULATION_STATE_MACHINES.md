# 10 — Session, Input, Drink and Merge State Machines

## Rationale

Physics bugs often arise from unclear ownership of mutable state rather than inaccurate collision math. Define explicit states, admissible transitions and invariants; do not infer states from sprite visibility. The renderer may animate a drink after its physics body is removed, but that does not make the drink active or eligible for another merge.

## Session machine

```text
uninitialized → loading → ready → running
                       ↘ load_failed
running ↔ paused
running → won | lost | abandoned
paused  → abandoned
won/lost/abandoned → disposed (new run requires new session ID)
```

- `ready`: assets and physics initialized; tutorial/first launch may begin.
- `running`: fixed physics and session reducer accept simulation events.
- `paused`: no physics steps or command mutation; pause overlay visible.
- Terminal states cannot transition to `running` for the same session ID.
- `restart` constructs new session ID and clears all old commands/events; no live state recycled incorrectly.

## Input machine

```text
idle → aim_pending → aiming → commit_pending → launched → cooldown → idle
        ↘ cancelled ↗                ↘ rejected → idle
```

`aim_pending` means pointer captured but below drag threshold; `aiming` means aim vector valid. `commit_pending` waits for fixed-step acceptance; it must not visually debit a shot. `launched` occurs after actual body creation; `cooldown` prevents spam. `cancelled` and `rejected` leave queue untouched. Only owner pointer ID can update this state.

## Drink machine

```text
preview-only → spawned/arming → active ↔ sleeping
                      active → merge_claimed → consumed
                      active → serve_claimed → consumed
                      active → clear_claimed → consumed
```

A merge-claimed drink must not be claimed for serving by two orders. A serve-claimed drink cannot merge and cannot be cleared for another reward. Use a single `claimKind`/owner, not separate booleans that can accidentally both be true. `sleeping` is a Rapier optimization flag while logical drink remains active. `preview-only` has no rigid body.

## Merge state

```text
candidate_detected → validated → claimed → committed → presentation_complete
               ↘ rejected
```

Validation and claim happen synchronously within one fixed-step arbiter; side effects are staged and committed once. Presentation completion never triggers score; score is driven by committed event. A renderer may be late and that's fine.

## Invariants

1. Every active logical drink has exactly one live Rapier body+collider pair.
2. One live collider is mapped to at most one logical drink; fixed walls and sensors use a different map/type.
3. Claimed objects are never eligible in later merge candidates.
4. Every commit changes active count by `-1` for a two-to-one merge, except if the result is immediately auto-served, in which case count becomes `-2`.
5. `shotFired` count increments only once when a valid committed launch creates its body.
6. Event sequence is strictly increasing within session; no consumer emits simulation-authoritative events.
7. `won` and `lost` are mutually exclusive for same session; terminal reason immutable.
8. No state may have a pending pointer capture after route unmount.
9. Visible `Next` queue must represent the *next committed* launch, not the last submitted/rejected command.
10. React and Phaser are projections of these states; neither directly mutates the physics world.

## State transition table

| Entity | Event | From | To | Side effect |
|---|---|---|---|---|
| Session | `start` | ready | running | initialize mission timer |
| Input | `pointerdown` | idle | aim_pending | capture pointer |
| Input | `move_valid` | aim_pending | aiming | preview aim ray |
| Input | `release_valid` | aiming | commit_pending | enqueue command |
| Input | `command_accepted` | commit_pending | launched | advance queue, body created |
| Input | `command_rejected` | commit_pending | idle | display reason, no debit |
| Drink | `entered_field` | arming | active | enable danger evaluation |
| Drink | `merge_claim` | active | merge_claimed | remove from eligibility |
| Drink | `serve_claim` | active | serve_claimed | reserve for order |
| Drink | `remove_completed` | claimed | consumed | release body reference |
| Session | `goal_complete` | running | won | one result, one reward event |
| Session | `danger_elapsed` | running | lost | one terminal event |

## Reducer behavior

SessionReducer accepts a batch of semantic events sorted by `(step, sequence)`, applies idempotency against observed event IDs and returns next immutable state. It must not call Rapier or Phaser, read `Date.now()` for gameplay rules, or use `Math.random()`. All needed randomness supplied as explicit events or a seeded state transition.

## Testing

Generate random event sequences using property-based tests. Assert every transition is legal or yields a predictable rejection. Test restart mid-merge and pause during input. Assert that presentation animation completion cannot mutate session score. Store a graph/state diagram in dev docs and update it whenever a new power-up introduces states.
