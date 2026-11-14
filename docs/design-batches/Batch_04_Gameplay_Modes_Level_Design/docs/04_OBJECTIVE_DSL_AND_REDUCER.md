# 04 — Objective DSL, Progress Evaluation and Dependency Graph

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Objective model
An objective is a pure, versioned, testable predicate over the ordered event stream and aggregate state; it should not inspect Phaser sprites. A compound goal may be expressed as `allOf`, `anyOf`, or ordered `sequence` groups, but the alpha uses a single goal `orders_served` count 2.

## Proposed objective types
| ID | Evidence source | Counter semantics | Shippable |
|---|---|---|---|
| `orders_served` | unique `order_fulfilled` events | +1 per unique order | alpha |
| `merge_count` | unique `drink_merged` | +1 per merge | alpha engine; later authored |
| `produce_tier` | unique newly produced outputs | +1 if outputTier = T | alpha engine; later authored |
| `score_at_least` | authoritative score aggregate | threshold, not event count | alpha engine; later authored |
| `serve_tier` | unique new output served for order | +1 matching tier | future |
| `combo_depth` | chain ancestor root and max depth | max value | future |
| `survive_waves` | committed `wave_completed` | +1 per wave | future |
| `serve_before_time` | fulfillment plus active elapsed bound | bounded count | future |
| `avoid_boosters` | committed booster use | hard/soft optional rule | future |
| `bank_shot` | first wall contact before valid merge | +1 per legal root shot | future |
| `customers_satisfied` | distinct customer IDs | unique satisfied clients | future |

## Canonical event-level meaning
- `orders_served` increments on `order_fulfilled`, NOT on each item in a multi-item order, and NOT when a progress bubble turns green.
- `produce_tier` observes produced output even if it is immediately auto-served; occurs once and remains counted.
- `merge_count` increments for each committed pair; a chain of 3 merges counts 3, but each event carries same shot ancestry.
- `score_at_least` reads finalized score after reducer has applied all scores in current tick; never count visual bounce numbers.
- `combo_depth` measures MAX number of sequential merges on a causally linked chain path, not total simultaneous unrelated merges.

## Compound objective grammar (future)
```ts
type Objective =
  | { type:'orders_served'; target:number }
  | { type:'merge_count'; target:number }
  | { type:'score_at_least'; target:number }
  | { type:'produce_tier'; tier:1|2|3|4|5|6|7|8; target:number }
  | { type:'combo_depth'; target:number }
  | { type:'survive_waves'; target:number }
  | { type:'allOf'|'anyOf'; children: Objective[] }
  | { type:'sequence'; children: Objective[] };
```
In `sequence`, decide if pre-completion events can retroactively satisfy future stages; **proposal: no**. Stage advancement activates the next child on the following tick, avoiding confusing same-event double consumption. UI must show current segment and upcoming step.

## Evaluation API
`applyObjectiveEvent(state, event, missionVersion) -> {state, changes[]}` must be pure. It tracks unique event IDs in a bounded or compacted idempotency ledger and raises type-specific progress events to the HUD. `evaluateObjectives(state)` returns `completed`, `progress`, and machine-readable unmet constraints. Keep reason codes stable.

## Star and optional goals
Distinguish primary victory predicates from optional `starCriteria`. Completing optional star criteria should NEVER deny mission victory after primary goal is satisfied. Example: win after 2 served orders; 2 stars if <=8 shots; 3 stars if <=6 shots. See doc 05. Conditions are independently validated and version-pinned.

## Feasibility warning
Because newly merged drinks are auto-served before next chain, a mission that requires both serving a tier-3 order and achieving a tier-4 chain from that exact tier-3 output might be impossible. Designer tools must simulate this priority, not assume uninterrupted chains. Disable conflicting orders during chain tutorials or specify chain goals before orders enter the queue.

## Validation constraints
No negative targets; no zero-length compound objectives; `tier` within catalog; maximum tree depth and node count bounded; no circular dependencies; required event feature must exist in deployed client; target achievable within shot/time limits by at least one tested path. Schema validation is only structural—simulation feasibility requires golden playthroughs.
