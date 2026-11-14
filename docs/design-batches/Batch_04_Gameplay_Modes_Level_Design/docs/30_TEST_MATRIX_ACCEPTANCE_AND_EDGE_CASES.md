# 30 — Gameplay Modes QA Matrix and Acceptance Requirements

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Test levels
1. Unit pure objective/scoring reducers; property-based events and state machines.
2. Headless Rapier integration: collisions, merge/serve priority, terminal results, event trace.
3. Schema and content lint: static shape, cross-field and release-status checks.
4. Replay golden tests: same seed, commands and pinned builds yield expected outcomes.
5. E2E UI automation: layout, buttons, overlays, routing, browser interruption.
6. Owner-driven manual touch/mouse playtest: feel, clarity, fairness, polish.

## Core cases (stable IDs)
| ID | Scenario | Required assertion |
|---|---|---|
| MOD-001 | service-001 win | 2 order fulfillments → one session win |
| MOD-002 | same-tick win and danger | win takes precedence, no loss |
| MOD-003 | same output eligible for chain and order | oldest matching order auto-served first |
| MOD-004 | duplicate merge event | one score increment |
| MOD-005 | duplicate fulfillment event | one order increment and preview coin credit |
| MOD-006 | tier8 + tier8 | no tier9 |
| MOD-007 | precision last shot triggers late chain | wait for resolution, win |
| MOD-008 | precision cancelled launch | no shot debit or queue advance |
| MOD-009 | rush hidden tab | active time unchanged |
| MOD-010 | rush timer vs goal same tick | goal success wins |
| MOD-011 | survival wave double event | one wave completion |
| MOD-012 | static insufficient tier mass | mission flagged infeasible |
| MOD-013 | invalid Tier 9 target | config rejected |
| MOD-014 | invalid shot/time budget | config rejected |
| MOD-015 | old manifest saved replay | use pinned version / safe error |
| MOD-016 | paused physics / danger | counters do not advance |
| MOD-017 | score overflow or NaN | reject, no corrupted result |
| MOD-018 | restart during FX | old event cannot affect new session |
| MOD-019 | unsupported future mode | hidden from live UI; backend refuses session |
| MOD-020 | unverified local preview coins | cannot spend in wallet / rank |
| MOD-021 | same objective satisfied twice | counted once by event ID |
| MOD-022 | max tier output served | once, not duplicated |
| MOD-023 | same seed two clients | stable logical replay under validated setup |
| MOD-024 | keyboard/touch aim UI | no distorted world direction |
| MOD-025 | schema + fixture validation | zero malformed enabled missions |
| MOD-026 | incomplete golden proof | cannot publish level requiring proof |
| MOD-027 | missing visual asset | placeholder, not physics crash |
| MOD-028 | WebGL context interruption | safe recovery/restart messaging |
| MOD-029 | endless 15-minute run | bounded bodies/FX/history |
| MOD-030 | boss multi-line order | no early full-order count |

## Mode-specific exit criteria
Classic: playable physical aim, known eight-tier catalog, two orders, win/loss/retry. Precision: shot budget correct after settle. Rush: active timer paused, fixed expiry. Chain: correct ancestry and score. Survival: deterministic wave states. VIP: line-based completion exactly once. Endless: bounded resources, clear finish action. Ranked: verified replay, standard rules and anti-cheat.

## CI commands (proposal)
`pnpm lint`, `pnpm typecheck`, `pnpm test`, `pnpm test:sim`, `pnpm test:content`, `pnpm test:e2e`, `pnpm build`. Current documentation pack includes a Python fixture validator; it does not claim to run a deployed Phaser simulation.

## QA evidence
Every release PR includes test run link, fixture version/hash, screenshots/video when meaningful, browser matrix, asset license additions, known issues and rollback plan. Only the owner approves manual interface behavior. No claims of passed gameplay simulation from static JSON validation alone.
