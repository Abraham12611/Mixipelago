# 14 — Asynchronous Ghosts, Friends Challenges and Ranked Constraints

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Design principle
Competitive score must measure mastery, not coin purchases, GPU speed, frame rate, network quality or player skill tree depth. This design chapter is an integration bridge to Batch 13/14; the alpha DOES NOT have rankings.

## Ghost challenge (proposed)
A player records normalized shot commands against a fixed mission version, seed, catalog hash, physics preset and scoring rules. Friend sees a reference score/ghost trajectory and attempts the same scenario. The ghost is playback-only; it cannot physically interact with the competitor's board. If the replay is validated, the score can participate in friends rankings.

## Level equivalence
A competitive challenge fingerprint includes `missionId`, `missionVersion`, `modeRulesVersion`, `physicsVersion`, `catalogHash`, `seed`, `allowedBoosters`, `perkNormalization`, `startLayoutHash`, and `scoringVersion`. Two runs are comparable only if their fingerprints match or a documented compatibility equivalence exists.

## Ranked constraints
Standardize starting board, spawn queue, input rate and relevant boosters. Disable unbounded premium advantages. The browser sends input command trace and hashes, not trusted totals. A server verifier reconstructs or checks the result; long-term design may include fully authoritative tournament servers. Replay checks must pin exact Rapier JS/WASM version, creation/removal order, deterministic math and command tick, as outlined in Batch 2.

## Exploit vectors
Client clock speed change, altered level JSON, spoofed event IDs, tampered score, fake seed, modified physics, rapid input injection, forged replay, replay reused across seasons, duplicate submission, mobile browser pause abuse. Mitigate with server challenge issuance, one-use session tokens, signatures where applicable, rate limits and replay verification.

## Fairness caveats
Even deterministic physics can produce skill unfairness if one input device enables more precise aim or preview than another. Validate touch versus mouse control, consider separate queues if needed and publish tournament rules. Avoid location-based disclosure; city rankings are opt-in and never expose precise addresses.
