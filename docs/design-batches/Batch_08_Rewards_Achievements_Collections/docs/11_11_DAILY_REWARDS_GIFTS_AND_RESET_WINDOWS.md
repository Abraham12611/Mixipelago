# 11 — Optional Daily Rewards and UTC Windows

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Product stance
Daily gifts are **optional gratitude**, not a mandatory chore. The player should be able to take days off without losing campaign access, essential skill points, or their shop. No streak-based punitive debt or skill loss. The program remains **deferred**, not part of the initial alpha.

## Eligibility
A published daily program defines its UTC day window, start/end, `windowId`, claim-once scope, optional regional display locale, and reward list. A player's physical timezone may be used to display the next reset but cannot move the backend eligibility window. Define an explicit reset such as `00:00 UTC` initially, or choose account-anchored windows if fairness research supports it; do not mix policies silently.

## Claim behavior
`GET /v1/rewards/daily` shows today status (`locked|claimable|claimed|ended`) and next UTC reset. `POST /v1/rewards/daily/claim` uses the same entitlement + idempotent settlement flow. A second device claiming the same window receives the existing receipt, not a second grant.

## Grace and travel
Time changes, DST and geographic movement never reopen the same UTC window. A claim that begins just before the cutoff may be honored based on durable reservation time and explicit grace policy; avoid 'time expired' after wallet commitment. No last-minute false countdown pressure.

## Reward balancing
Small cosmetics and bounded coins are acceptable; no unique competitive power. Publisher must model 7-, 30- and 90-day maximum payout scenarios to verify the economy. A player who misses days can still progress through normal play. Potential 'welcome-back' gifts are separate policies with anti-abuse review.

## Abuse cases
Clock manipulation, rapid tab reloads, claims across devices and geographic spoofing do not alter authorization. Server receipt and window identity are the sole deciding inputs.
