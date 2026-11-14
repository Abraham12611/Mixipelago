# 18 — Respec, Refunds, Previewing Builds and Undo

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Principle
Experimentation is a long-term retention asset. A player should be able to correct a skill-tree decision without losing their business, campaign progress, recipe mastery or earned levels.

## Candidate v0.4.1 policy
- Respec becomes available after the first allocated point and an onboarding explanation.
- Allow **free full respecs** in the first exploration window and at least one free respec token in later experience; do not require real-money payment to undo a mistaken talent.
- After the first free window, use a small, capped *optional* trusted-coin fee only if player research indicates this improves balance and doesn't punish low earners. A no-cost cooldown is a fairer default.
- Full respec refunds active allocations into available points. Account XP and level never change. Partial node refund requires safe cascade preview and explicit confirmation because dependent skills may become invalid.

## Transaction sequence
1. Fetch allocation revision and skill graph version.
2. Compute all affected nodes and effective modifier deltas.
3. Show a confirmation diff and point refund total; never hide the removal of an active skill.
4. Within one DB transaction, record `respec_operation`, update ranks, refund points (or adjust allocated tally), reset invalid loadouts, bump revision and emit outbox event.
5. Respec changes take effect for **future** activities; an already-started casual puzzle retains its pinned start snapshot. Competitive modes ignore custom allocation regardless.

## UX
A Build Planner allows users to preview hypothetical allocations offline. Save/load *draft builds* without spending points. `Apply Build` executes a server-validated sequence in one atomic command or refuses with explicit invalid-node errors. Provide undo history for last submitted build if policy permits, but never try to reverse a completed mission's rewards.

## Abuse cases
Free respec is not a loophole to repeatedly trigger first-allocation rewards, claim one-time benefits from multiple mutually exclusive branches or downgrade before a priced purchase and reupgrade afterward. Any one-time entitlement is tracked by immutable source ID, not by active skill rank.
