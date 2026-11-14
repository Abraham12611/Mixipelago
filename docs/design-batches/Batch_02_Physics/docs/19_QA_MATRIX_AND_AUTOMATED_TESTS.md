# 19 — Exhaustive QA: Unit, Property, Physics, Contract, E2E, Performance

## Test strategy

The goal is to make physics engine changes safe for a continuously released game. Unit tests verify pure logic. Simulation fixtures verify Rapier behavior. Contracts verify cross-package compatibility. Browser E2E verifies wiring and UI projection. Performance tests protect device responsiveness. Manual feel evaluation stays with the product owner.

## Test layers

1. **Pure TypeScript unit:** merge eligibility, queue PRNG, aim vector normalization/quantization, score reducer, danger step counter, event/idempotency.
2. **Property-based:** arbitrary contact graphs, positive finite parameters, random spawn distributions, state machine transition graphs. Suggested library `fast-check`, optional until integrated.
3. **Rapier headless integration:** actual WASM world with fixed-step command log and assertions on bodies, colliders, contacts, output IDs, finite velocity.
4. **Cross-package contract:** generated TypeScript schema parse/serialize, event shape, UI adapter, session save, no forbidden imports.
5. **Browser automated E2E:** Playwright pointer/keyboard actions, snapshots, tabs, reduced motion, viewport.
6. **Visual regression:** screenshots at stable fixture states; normal/low quality, portrait/desktop.
7. **Perf and resilience:** long-play, repeat-level, context-loss, tab background, object-limit stress.
8. **Owner manual QA:** tactile feel, art clarity, sound balance, small-screen controls and subjective acceptance.

## Required physics tests (IDs stable)

| ID | Setup | Assertion |
|---|---|---|
| PHY-001 | Empty board, legal launch | One body appears, finite velocity, correct direction |
| PHY-002 | Two equal circles head-on different tiers | Both react; no merge; no unbounded penetration |
| PHY-003 | 25% lateral offset different tiers | Oblique deflection with finite lateral velocity |
| PHY-004 | 50% lateral offset different tiers | Stronger geometric deflection than near-center fixture |
| PHY-005 | Tangential near-miss | No false merge or ghost contact |
| PHY-006 | Same tier eligible | Exactly one next-tier result, exactly one merge event |
| PHY-007 | Different tiers | Physically collide, never merge |
| PHY-008 | Two tier-8 collide | No tier-9; normal contact response |
| PHY-009 | A touches B and C in one step | A claimed at most once, deterministic pair selection |
| PHY-010 | Two disjoint pairs same step | Exactly two valid merges and stable output order |
| PHY-011 | Result touches matching third glass next step | One legal follow-up chain, no double counting |
| PHY-012 | Result matches open customer order | Auto-serve once, removed, chain priority correct |
| PHY-013 | Max-speed launch at thin rail | No tunneling with CCD configuration |
| PHY-014 | Angled rail collision | Finite rebound, stays within board |
| PHY-015 | Body goes into danger for <grace | Warning then recover, no loss |
| PHY-016 | Active body intrudes >grace | Exactly one loss event |
| PHY-017 | Shooter while arming below line | No immediate false loss |
| PHY-018 | Win and danger same step | Documented win-priority rule applied |
| PHY-019 | Pause during active motion | No steps/time/danger change while paused |
| PHY-020 | 5-minute hidden tab then resume | No physics fast-forward |
| PHY-021 | Restart during merge FX | Old bodies/events cannot affect new run |
| PHY-022 | 100 rapid input attempts | Count only legal shots; queue never double advances |
| PHY-023 | 50 reload/restarts | No monotonically increasing leaked listeners/body maps |
| PHY-024 | Identical seed + commands on same build | Identical final logical state/hash |
| PHY-025 | Cross-browser replay fixture | Compare hashes; divergent platforms reported not silently accepted |
| PHY-026 | Missing optional sprite/audio | Logic completes with placeholder/silence |
| PHY-027 | NaN/Infinity input or config | Rejected with structured error, no world corruption |
| PHY-028 | Spawn position blocked | Clean rejection, no queue consumption |
| PHY-029 | Packed 35-drink board | Stable step time and no physics explosion |
| PHY-030 | No active bodies before win | Correct terminal and next-step behavior |

## Input cases

`INP-001` desktop pointer drag straight; `002` angled drag near aim limit; `003` dead zone tap; `004` release outside canvas; `005` secondary pointer/two fingers; `006` orientation change while holding; `007` modal opens while aiming; `008` keyboard step left/right fire; `009` focus in text input; `010` DPR/layout change. Assertions: shot direction within angular tolerance, consistent world coordinate mapping, at most one command accepted per gesture.

## Merge correctness property

For any finite set of active object IDs and candidate pair graph, the committed merge set must be a **matching**: no object ID appears in more than one chosen edge. The transaction list is deterministic under any permutation of incoming contact event order after canonical sorting. Each committed transaction yields one result of legal next tier and one unique merge ID. Score only from the resulting unique semantic event stream.

Pseudocode:

```ts
fc.assert(fc.property(contactGraphArbitrary, graph => {
  const first = arbitrate(graph);
  const shuffled = arbitrate(shuffle(graph));
  expect(ids(first)).toEqual(ids(shuffled));
  expect(allConsumedIds(first).size).toBe(2*first.length);
}));
```

The example needs `fast-check` generators and a deterministic shuffle utility; it is not self-contained production test code.

## Golden replay fixtures

Store `missionVersion`, `physicsVersion`, `rulesVersion`, seed, input transcript, checkpoints and expected output hash under `tests/golden/`. Generate baselines only after owner approves the canonical preset. A PR changing golden snapshots must explain why, include visual/replay evidence, and get physics lead review. Do not auto-accept new baselines in CI.

## Browser UI E2E

- Page loads game without React hydration errors or duplicate Phaser canvas.
- Start mission, aim/launch, see body and eventual event updates in HUD.
- Next preview advances only after an accepted shot.
- Complete demo win; modal shows correct points/preview coins.
- Retry yields fresh session with clean physics state.
- Pause/resume freezes and unfreezes board.
- Reduced-motion and low-quality mode maintain same scoring results.
- No analytics or external API availability required for alpha gameplay.

## CI gating

PR required: typecheck, lint, unit, physics, contract and basic headless browser smoke. Staging required: full Playwright E2E on selected browser matrix, visual tests, memory/long-play smoke and owner manual approval of feel. Main merge requires owner permission under project policy. Failure artifacts include test logs, screenshots, video when feasible, config hash, browser version and full reproduction sequence.
