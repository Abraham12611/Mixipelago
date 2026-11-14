# 19 — Analytics, Telemetry, Growth and Live Operations

## Purpose

Measure whether the core game is fun and whether future systems improve retention. Instrument mechanics and funnel quality, **not** every pointer movement. No precise location/PII needed for alpha. Respect privacy preferences.

## Alpha metric definitions

| Metric | Definition | Use |
|---|---|---|
| Load success | `game_loaded / app_opened` | Reliability |
| First merge conversion | New sessions with ≥1 successful merge / tutorial started | Learnability |
| First order conversion | New sessions with order fulfilled / gameplay started | Clarity of purpose |
| Session win rate | Won / terminal sessions by mission | Difficulty |
| Session length | Active seconds excluding pause/background | Pacing |
| Retry rate | Restart after loss / losses | Frustration vs engagement |
| FPS p50/p95 | Frame time distribution per device tier | Performance |
| Merge chain average | Eligible merges per chain | Moment-to-moment delight |
| D1/D7 retention | Unique players returning by cohort | Traction (requires durable identifiers, consent where needed) |
| Account conversion | Guests linking account / eligible guests | Cross-device demand (later) |

## Event schema

All analytics events: `eventName`, `schemaVersion`, `timestamp`, `buildVersion`, `sessionId`, `missionId?`, `deviceClass`, `anonymousId`, `consentCategory`. No customer name, contact info, chat, real location in telemetry. Session and mission ID alone may still be linkable pseudonymous data; include in privacy policy and retention controls.

## Early essential events

`app_opened`, `game_loaded`, `tutorial_viewed`, `tutorial_completed`, `session_started`, `shot_fired`, `drink_merged`, `order_fulfilled`, `session_won`, `session_lost`, `session_restarted`, `audio_muted`, `client_error`, `fps_sample`. Use aggregation and rate limits for high-frequency events.

## Future product analytics

Map path chosen, node unlock, shop upgrade purchased, wallet source/sink balance, skill node selected, event choice outcome, friend invite accepted, leaderboard challenge started/submitted, event/season reward claimed. Analytics must not replace the trusted economy ledger.

## Experimentation principles

Randomized experiments require stable cohort assignment and explicit success metric. Never silently alter ranked fairness or offer different mission physics to players in the same competitive bracket. Version each experiment configuration and permit emergency kill switch. Events affecting economy or difficulty need balance simulation and rollback plan.

## LiveOps cadence (future)

Proposed weekly challenge, season rotations, special art packs and new missions. Stagger content releases to avoid giant downloads. A live event should never mutate an unpublished mission definition. Use admin staging/publishing with review and timestamps.

## Feedback loop

Collect in-app thumbs/feedback link and game version; triage bug types: crash, unclear controls, physics feels wrong, impossible goals, visual clutter, missing audio, performance. Prioritize first-merge and first-order problems before cosmetics or complex RPG systems.

## Traction decision for native release

Review retention, browser device mix, crash-free sessions, session completion, revenue potential, user demand for app install and native performance. Do not decide solely on a fixed one-month timer or vanity visit counts.
