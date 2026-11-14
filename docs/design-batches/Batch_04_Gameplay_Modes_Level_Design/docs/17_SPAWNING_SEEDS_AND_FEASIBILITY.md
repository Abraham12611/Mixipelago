# 17 — Spawn Director, RNG, Queue Fairness and Anti-Softlock Design

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Why this needs an independent subsystem
A deterministic next-item queue is as important to perceived fairness as physical movement. A perfect shooter can still produce unwinnable levels if it supplies incompatible tiers or order targets.

## Alpha
Per Batch 3 `coconut-cove-001`: spawn `seedMode='per-run'`, pool tier1 weight100, `firstItems:[1,1,1,1,1]`, initial two tier1 bodies. One next preview is shown. Use a documented RNG with explicit seed. A content fixture listing five initial items is NOT a mathematical proof that a player can complete both required orders after auto-serve.

## Director API
`peekNext(session)` pure/read-only; `commitLaunch(session,command)` performs atomic shot count + queue advance only if launch accepted; `scheduleOrderReplacement` creates IDs in deterministic order; `snapshotRng` captures generator state; `generateNext` requires mode registry and `spawnPolicyVersion`.

## Fairness controls (later)
- `maxConsecutiveTier` prevents too many repeated difficult spawns.
- `reserveUsefulTierWindow` guarantees a helpful tier within a window without changing a visible already-previewed item.
- `orderReachabilityCheck` estimates whether an outstanding requested output could be generated from remaining resources.
- `startingAssist` gives pre-placed lower-tier items in beginner levels.
- `antiSoftlockRecovery` offers explicit free reset or mission restart in failed generated scenarios, never stealth coin purchase pressure.

## Tier-equivalent capacity
In a linear 2→1 ladder, tier k requires 2^(k−1) source tier1 units when created from scratch. A rough necessary resource condition for an order of tier k is sufficient cumulative tier-equivalent mass after considering serving consumption. This is NOT sufficient for reachability: geometry, loss rules, launch budgets and auto-serve can still prevent completion.

## Deterministic generation
Avoid raw `Math.random()` inside the session reducer. Choose one small verified seeded PRNG, fixed integer operations, serialize internal state. Sequence ID and item tier are part of replay. For ranked missions, seed issued/validated by backend, not selected by user. Live event content may rotate but active session generation remains pinned.

## Queue exhaustion
When authored `firstItems` are consumed, fall back to configured pool, unless mode says `finiteSequenceOnly`. In precision mode, short authored queue should never be silently extended by random items past shot cap. The UI must show `Next` based on the next item actually selected by director.

## Quality gates
A legal launch with blocked spawn does not advance RNG/queue/shot counter. Repeated run with same seed and command sequence reproduces queue and order sequence. Automated sampled seeds check win rate feasibility; golden winning replay required for every hard-gated authored mission; statistical QA for generated modes across many seeds. Zero draw or missing pool never crashes, returns content error.
