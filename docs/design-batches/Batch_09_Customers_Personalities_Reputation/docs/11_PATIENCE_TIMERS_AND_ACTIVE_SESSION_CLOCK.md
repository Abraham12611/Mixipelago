# 11 — Customer Patience, Deadlines and Pause Semantics

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Initial position
No patience meter in `v0.1.x`, and no hidden impatience that reduces the score on standard Classic Service missions. Patience is a mode-owned, published challenge modifier for later Rush Hour/VIP event contracts. It is not a simulation of real-world shop customer annoyance.

## Clock model
`deadlineTicks` counts **active session ticks** at fixed 60 Hz (Batch 2/4). Paused game, backgrounded browser, disconnection freeze and app switch should not consume customer patience in local modes. Any future server real-time event has a distinct `serverDeadlineAt`, visible to the user before accepting the event, and must have a reconnection/grace policy.

## State transitions
`waiting -> warning -> served | expired`. A published policy defines warning thresholds, optional points-only consequences, replacement cadence and recovery. If served and deadline crossed in the same tick, the event ordering policy must be deterministic and tested; recommendation: apply committed service claims before expiration evaluation on that tick, matching Batch 4 terminal win precedence.

## Fairness
A deadline must have a feasible route given initial board, shot queue and the drink's tier-equivalent cost. Skill and decoration perks that affect customer patience can only apply where a mode explicitly permits, with caps and visible explanations. In normalized ranked challenges, ignore personal perks and use published standardized timing.

## UI and testing
Show a timer in text and a visually clear meter; add accessible alerts at predictable thresholds; avoid rapid flashing. Test tab switch, slow devices, 30 FPS fallback, frame drops, websocket reconnect, duplicate expiration events, foreground resume, and user-initiated pause. Avoid social penalties merely for closing the app.
