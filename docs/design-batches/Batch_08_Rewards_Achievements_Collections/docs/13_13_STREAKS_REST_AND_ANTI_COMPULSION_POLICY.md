# 13 — Streaks, Rest Days and Ethical Engagement

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Recommendation
If a streak system is introduced, track gentle **participation** rather than punishing missed days. Permanent skill points and high-value permanent advantages must not require continuous logins. Examples of benign streak rewards: temporary visual flourish, small bounded daily gift, a nonexclusive badge, and a celebratory milestone.

## Suggested optional streak logic
One eligible claimed daily gift per unique UTC window increments a participation streak. Two grants in the same window never increment twice. Missing a window either resets a visual streak or consumes an explicitly displayed grace day, but never removes earned inventory/currency. An alternative rolling-days metric (e.g. play 3 of 7 days) is often more respectful.

## User settings
Allow hiding streak UI and opting out of reminders. Do not send 'your shop will burn down if you miss tomorrow' messages. Notifications require clear opt-in and easy disabling. No artificial pressure on young players, no countdowns that obscure local time or change during checkout.

## Technical
Store individual daily-claim facts; derive current display streak from UTC window IDs. Backfill only verified facts. Maintain a versioned streak algorithm and test leap days, DST, timezone changes and late event delivery. Duplicate claims must not create additional participation entries.

## Decision gate
Before implementation, compare retention benefit to negative sentiment, anxiety complaints and opted-out usage. The default may be **no streaks**, with optional weekly activity instead.
