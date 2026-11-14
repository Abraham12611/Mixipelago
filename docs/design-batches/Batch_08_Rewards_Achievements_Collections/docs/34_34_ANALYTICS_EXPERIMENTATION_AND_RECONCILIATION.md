# 34 — Telemetry, Experiments, Reconciliation and Operations

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Core events
`reward_eligible`, `reward_shown`, `claim_clicked`, `claim_succeeded`, `claim_pending`, `claim_failed`, `achievement_progressed`, `achievement_unlocked`, `album_opened`, `collection_milestone_claimed`, `cosmetic_equipped`, `program_disabled`. Analytics events are observational and **must not drive financial grants**.

## KPIs
Entitlement-to-claim conversion, time-to-claim, orphaned/unsettled entitlement count, grants per verified source, duplicate-event suppression, ledger reconciliation drift, item ownership uniqueness, album completion by cohort, UI understanding of reward states and event-pressure complaints.

## Fraud signals
Multiple accounts receiving unusually identical sequences, impossible time-to-achievement, repeated failed claim commands, mismatched source receipts, high-frequency choice requests, suspicious geographic switching, and abnormal compensation volume. Investigate carefully; avoid automatic unfair penalties from unproven correlations.

## Alerting
Notify on settlement pending > threshold, ledger inventory mismatch, unexpected reward rate spike, all-active-program decline, job failure, missing published asset and reward version mismatch. Reconciliation jobs compare entitlements ↔ claim lines ↔ owned items/wallet ledger.

## Experimentation
Use player-cohort feature flags for reward presentation and content, never secretly alter competitive payout rules mid-season. Keep control and variant economy effects separately auditable. No permanent advantage for ad engagement in ranked play.

## Data retention
Store immutable receipts as durable operational records under documented legal policy; minimize PII analytics retention. Separate profile privacy settings from public leaderboard display.
