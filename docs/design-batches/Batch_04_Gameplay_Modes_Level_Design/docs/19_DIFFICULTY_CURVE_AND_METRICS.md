# 19 — Difficulty Curves, Mission Pacing and Quantitative Balancing

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Difficulty is multidimensional
Do not attach one arbitrary integer to a level and assume it is balanced. Model factors independently:
`initialDensity`, `requiredTier`, `ordersTarget`, `spawnEntropy`, `shotsBudget`, `activeTimeBudget`, `layoutComplexity`, `hazardIntensity`, `previewDepth`, `chainRequired`, `boosterAllowance`.

## Early campaign ramp (proposed)
| Missions | Mechanics | Difficulty purpose | New on-screen information |
|---|---|---|---|
| 001 | two orders, tier 1 pair, unlimited shots | teach launch+merge+serve | aim / order bubble |
| 002 | repeated t2 orders | customer priority | multiple requests |
| 003 | t4 with seed assistance | tier-equivalent planning | chain/pacing hint |
| 004 | two-link chain without conflicting t3 order | arrange contact path | combo badge |
| 005 | score goal under modest pressure | risk-management | target score |
| 006–010 | bank shots and board density | mastery and adaptation | optional trajectory / hazard hint |
| 011+ | limited-shot/alternate goals once modes ship | new player decisions | mode-specific tutorial |

## Intended experiential pacing
- Tutorial intro: player comprehends aiming and first merge with minimal text and obvious objective.
- First 3 wins: short satisfying sessions with substantial forgiveness; no hidden stamina gate.
- Early island: alternate straightforward and stretch goals to avoid difficulty spikes; optional missions can reward mastery.
- Mid campaign: layered constraints but only one new mechanic at a time.
- Late game: combinations, alternative solutions, controlled complexity, transparent ranking.

## Metrics
`firstShotDelaySec`, `completionRate`, `retryRate`, `sessionDurationActiveSec`, `shotsPerWin`, `meanMaxChainDepth`, `medianBoardOccupancy`, `dangerWarningsPerRun`, `timeSpentAiming`, `boosterUsePerAttempt`, `abandonAtMission`, `starDistribution`, `generatedSeedWinVariance`.

## Indicative targets (hypotheses, not measured)
First tutorial completion >85% under friendly instructions; early missions ~65–85% first-attempt completion; advanced optional challenges may be lower. More important than any numeric target is distribution by input type, device tier, new/returning player and accessibility settings. Do not publish targets as facts until actual analytics.

## Balance process
1. Designer drafts mission and estimates resource requirements.
2. Static checker validates schema and necessary arithmetic bounds.
3. Automated solver/bot and recorded human paths prove existence of a plausible win.
4. Engineer QA checks physics, UI and terminal conditions.
5. Owner manually tests subjective feel and clarity.
6. Beta telemetry assesses failure spikes and fairness; tune in a NEW version.
7. Re-run golden replay and migration checks before publishing.

## Watch for deceptive difficulty
RNG-induced unwinnable seed, undetectable danger pressure, shots consumed on rejected inputs, pressure tied to device rendering speed, unseen tier confusion, excessive VFX obscuring board, customer priority silently sabotaging chain, mode-specific rules omitted from mission preview.

## Difficulty curves and content authoring
Content studio should display predicted required tier1-equivalent units, starting mass, expected spawned units before failure, shot constraint, theoretical minimal merge count, current golden-solution shots, simulator result hash, target stars, telemetry trends, and unresolved warnings. Hard-block invalid; allow warnings with explicit owner-approved justification.
