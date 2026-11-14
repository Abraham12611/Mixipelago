# 28 — Replay Protocol, Verification, Anti-Cheat and Trust Boundaries

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Authority layers
At alpha, physics, objectives, score and preview coins run client-side for fast play. They are non-trusted and must never mint server currency. At verified competitive and economy phases, server validates a signed/issued challenge and normalized input trace, computes or verifies result, and transacts rewards.

## Replay requirements
Serialize mission/version/hash, catalog/hash, engine build/version, Rapier build, fixed Hz, initial world creation order, RNG state/seed, input commands with tick/pointer normalized direction/power, mode rule version, score rule version, checksum chain or final state digest. A source render recording is NOT equivalent to replay inputs. Window pixels/mouse coordinates are NOT replay-safe.

## Rapier caveat
Official JavaScript/WASM Rapier docs state cross-platform determinism for identical initial conditions, construction order, parameters and timesteps. Application code can undermine determinism with `Math.sin`/`Math.cos`, unstable object iteration order or nondeterministic command scheduling. Treat cross-device replay golden fixtures as a required gate before claiming fair verified ranking.

## Challenge lifecycle
Server issues `challengeId`, mode/mission fingerprint, seed and expiry. Client runs local simulation and sends trace plus result. Server verifies eligibility, ordering, seed, version compatibility and score against authoritative/replayed events; rejects tampered claims; writes unique score receipt and leaderboard update exactly once. Account limits/rate limits deter farming.

## Session modes
Unverified `solo_preview` supports instant play and local history. `verified_campaign` requires trusted receipt for XP/coins. `verified_ranked` requires same environment, no personal perks, no purchased power, stricter input bounds and potentially an authoritative live service. A user's offline play cannot silently become leaderboard eligible later.

## Security controls
Input validation (finite normalized direction, strength bounds, tick ordering), max events per session, max active bodies, request idempotency, signature/session token, replay storage TTL, privacy minimization, structured fraud flags, audit appeal procedure. Never trust UI result score or local best.

## QA
Corrupt trace, duplicate command tick, impossible angle, huge integer, altered catalog, replay across app version, dual submit and race, edited score, missing event, hidden-tab abuse, exactly-once wallet, stale leaderboard update, cross-browser replay divergence.
