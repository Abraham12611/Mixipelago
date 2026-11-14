# 08 — Order Generation, Difficulty Fairness and Spawn Integration

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Constraint ownership
Batch 4 owns mode order slots, target difficulty and mission feasibility. Batch 3 owns compatibility, oldest-first service reservation and remaining quantity. This chapter describes *customer-themed* selection only. Alpha `coconut-cove-001` retains two scripted active orders and a two-order win goal.

## Feasibility lower bound
An order for tier `T` produced from tier-1 inputs requires at least `2^(T-1)` base inputs if no existing higher-tier bodies are available. For multiple orders, consumed intermediate outputs change effective demand. An estimator must model order-serving priority: when a new tier-3 is immediately served, it cannot chain into tier-4. The solver must account for initial board bodies, fixed shot queue, danger conditions and already required orders.

## Fairness filters
- No secret/undiscovered recipe unless mission explicitly unlocks the required route.
- No request for a terminal tier if current available resources cannot support it.
- No generated mandatory customer deadline shorter than the conservative time to produce its drink.
- No replacement order after the mission's primary win becomes true.
- No immediate same-tick replacement that retroactively consumes the output that triggered completion.
- Optional VIP reward must show difficulty/risk before player commits, not spring upon them mid-shot.

## Order queue and deterministic order
IDs and issued ticks are stable, with `issuedTick` then `orderId` tiebreak. Two outputs from one physics tick resolve in stable merge sequence. A request added after a completed order may match a later same-tick output if the sequence explicitly places order creation first; it cannot match earlier outputs.

## QA obligations
Generate thousands of seeded pools and assert required goals have reachable resource estimates. For published missions, retain an actual winning trace or comparable solver proof; pure numeric bounds are necessary but **not sufficient** to prove physical solvability.
