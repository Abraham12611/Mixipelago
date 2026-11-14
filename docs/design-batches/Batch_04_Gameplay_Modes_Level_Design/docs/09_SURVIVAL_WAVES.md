# 09 — Survival Shift: Wave Survival and Board Pressure

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Promise
Survive successive waves of drink arrivals while maintaining physical space and achieving wave objectives. This mode creates tension from long-term table management rather than a countdown alone.

## Wave state machine
`wave_pending → wave_active → wave_resolution → wave_completed → next_wave` with terminal `mode_completed|overwhelmed`. A wave describes deterministic or seeded arrivals, interval ticks, per-wave objective, and capped board pressure. For initial survival mode, use a fixed number of waves (3–5), not a truly infinite job with unbounded memory.

## Board pressure rules
Retain Batch 2 danger line per-body grace. A separate `maxActiveDrinks` capacity may be configured, but must use a documented rule (e.g., block next launch and prompt cleanup) rather than silently destroy items. Wave advancement cannot spawn inside occupied footprint; author fallback nodes or defer arrivals within bounded ticks. If placement impossible, return a diagnosable content error rather than teleporting a glass through other bodies.

## Arrival scheduling
Spawn waves only at specified fixed ticks relative to start of wave; external wall clock doesn't alter physics. Spawn manifest states tier, source, position, and grace duration. Unique seeded IDs and stable ordering guarantee replay. The simulation is paused while showing between-wave results and wave selection.

## Fairness
Cap wave density; include opportunity to resolve threat, at least one feasible plan and optional reserved recovery shot. Warn before the board is overloaded. Later power-ups may help, but normal victory must not require paying for one. Physics speed/weight not secretly increased between waves; new surface material must be listed in challenge rules.

## Optional variations
Survive X waves, score at least Y by end of wave, serve Z customers by wave 3, save an endangered shop within fixed waves. Crossovers with world incidents are future Batch 10/12 and should use mission configuration, not bespoke simulation forks.

## Test vectors
Pausing across scheduled spawn, multiple arrivals at same tick, deterministic order, board full with deferred arrival, terminal win vs danger, no duplicate wave-completed reward, memory/particle cap over 15-minute sessions.
