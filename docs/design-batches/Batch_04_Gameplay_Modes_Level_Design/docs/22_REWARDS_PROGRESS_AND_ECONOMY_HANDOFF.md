# 22 — Mode Rewards, Mission Progress and Trusted Economy Handoff

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Alpha is preview-only
Batches 1–3 explicitly state that v0.1 uses client-local preview coins. Batch 4 MUST NOT introduce a wallet via UI assumptions. Store `previewCoinsFromOrders`, `previewCoinsFromMission`, `previewTotal` separately and label them as demo rewards until trusted economy is shipped. The UI must not permit shop spending of unverified preview coins.

## Reward sources
- Merge points: visible scoring only; Batch 3 table by output tier.
- Customer fulfillment: adds `coinReward×10` session score plus `coinReward` preview coin tally, once.
- Mission completion: `rewards.previewCoins` after ONE win; no grant on loss unless authored consolation grant separately and validated.
- Stars: quality rating, monotonic best in saved local mission result, no cash value.
- Cosmetic/promo rewards: future Batch 8/12; need schema, ownership source and duplicate protection.

## Campaign integration (Batch 5)
The `MissionResult` exposes `missionId`, `missionVersion`, stars, score, shots, activeTicks, terminal reason, verified state, completion timestamp. Island graph engine chooses unlocks; the gameplay engine never checks map edges directly. A later campaign transition records a node-completion event and unlocks eligible graph edges under server-verified receipts.

## Trusted backend proposal
`POST /v1/sessions/start` returns run ID, fixed seed, config hashes, eligibility; `POST /v1/sessions/submit` accepts normalized commands and metadata; server verifies and writes idempotent result; transaction updates `mission_results` and creates wallet credits once. `purchase` endpoints are independent and should not accept client-preview values. No competitive scores without verification.

## Retry reward policy
A replay may improve score/stars. Whether repeated completions grant ongoing coins is a Batch 6 economy policy; proposal for first trusted campaign: unique first-clear reward plus limited repeat reward or zero repeat reward. Do not hardcode unlimited reward farming by replaying Cove 001.

## Cross-feature event bridge
`session_won` → (trusted receipt later) → `mission_completed` → campaign unlock evaluation → optional skill XP or daily quest → UI celebration. A side effect that fails should be retriable idempotently; avoid executing it in Phaser callback or raw local storage mutation.

## Integrity tests
Double client submit yields one grant; two browser tabs racing same mission do not double credit; submit altered mission version rejected; completed 3-star cannot regress; no preview balance migration; reward rules version pinned; ledger audit can reconstruct grant cause.
