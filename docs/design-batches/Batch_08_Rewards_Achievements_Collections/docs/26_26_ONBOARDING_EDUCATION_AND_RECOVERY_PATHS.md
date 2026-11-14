# 26 — Onboarding, Progressive Disclosure and Failure Recovery

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Explain progressively
First focus is merging, serving and mission results. After the first verified campaign clear and when rewards are available, introduce one claim example. Collections, daily gifts, season rewards and advanced trophies should appear only after their relevant features launch and players are eligible.

## Glossary in UI
Distinguish `Earned` (condition met), `Ready to claim` (entitlement available), `Claimed` (ownership committed), and `Displayed` (equipped cosmetic). Claim details should show whether it is permanent, time-limited or stackable. No blank 'Success!' toast when settlement failed.

## Recovery examples
- Tap claim with no connection → keep entitlement, show reconnect/retry; same request ID on retry.
- App closes mid-celebration → render claimed item from server on next visit.
- Different device claims first → current screen reconciles to claimed and shows receipt.
- Reward art missing → fallback icon, ownership unaffected.
- Mistaken duplicate reward → explain duplicate policy and any documented fallback.
- Local preview badge disappears on account sync → preserve in separate clearly labeled demo history if desired, but do not grant trusted currency.

## Help and support
Allow copying a `claimReceiptId` (not secret user credentials) and viewing a simple receipt history. Customer support can use trace ID and issuer provenance for investigation. Players should not need to know blockchain concepts or transaction internals.

## Do not nag
Avoid persistent claim red dots for programs that are still disabled, and avoid notifications every time a background counter changes. Players may dismiss reward promos without affecting entitlement.
