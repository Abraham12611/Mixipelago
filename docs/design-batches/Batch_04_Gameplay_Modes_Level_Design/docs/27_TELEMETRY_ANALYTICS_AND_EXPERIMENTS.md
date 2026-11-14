# 27 — Mode Telemetry, Difficulty Analytics, Experiments and Privacy

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Event taxonomy
Log semantic, sampled analytics separately from authoritative game events. Analytical data is not used to award rewards. Key events: `mission_viewed`, `mission_started`, `first_aim`, `shot_committed`, `drink_merge_committed`, `order_completed`, `danger_warning_shown`, `mission_won`, `mission_lost`, `mission_abandoned`, `retry_clicked`, `hint_viewed`, `mode_selected`, `mission_content_error`, `device_performance_sample`.

## Required fields
`eventId`, `anonymousPlayerId` or authenticated ID, `sessionId`, `missionId`, `missionVersion`, `modeId`, `contentHash`, `physicsVersion`, `clientVersion`, `deviceClass`, `inputKind`, `durationActiveTicks`, `experimentAssignments` if any. Never include precise player location, raw free text, or sensitive device identifiers unnecessarily. Consent/privacy disclosures required for analytics features.

## Aggregates
First-try win %, attempts per win, abandonment and softlock rates, 3-star distribution, median active session duration, average shots used, danger warning frequency, tutorial first-shot success, chain-depth histograms, time-to-first-merge, mobile-vs-desktop performance, progression funnel drop-off by mission node.

## Diagnostics vs production monitoring
Diagnostics may include world snapshots for opted-in or internal runs; analytics generally gets summaries, not unbounded physics traces. Apply event sampling/deduplication and retention limits. A local alpha can record anonymous console/debug aggregates without requiring third-party analytics immediately.

## A/B testing guardrails
A/B experiments may alter UI hints, timing of tutorial prompts, or mission difficulty only at run start through pinned manifest assignment. Do not change physics or reward rules mid-run. Compare cohorts with the same underlying seed distribution and device mix. Experiment must have rollback flag and success/guardrail metrics.

## Useful experiments
- Portrait order card size improves order comprehension?
- Gentle guided aim vs free aim affects first merge success?
- 2 visible orders vs 1 affects session complexity?
- Clear shot counter reduces Precision frustration?
- Brief score FX improves perceived feedback without slowing input?

## Measurement risk
Clients can suppress/spoof analytics. Use it for product insight, not economic truth. Season/rank and trusted coin awards derive from verified server data, not PostHog event counts.
