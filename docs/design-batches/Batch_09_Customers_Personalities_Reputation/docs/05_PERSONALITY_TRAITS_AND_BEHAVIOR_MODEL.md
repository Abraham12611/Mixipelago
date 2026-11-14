# 05 — Personality Traits, Expressions and Behavioral Policies

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Goals
A customer should feel distinct without becoming a hidden difficulty modifier. Model authored personality as a vector of *presentation* traits: `energy`, `curiosity`, `sociability`, `patienceStyle`, and `tasteAdventure`, each integer 0–100, plus fixed tags such as `collects_shells`. Behavior follows a published presentation profile; developers must not read trait numbers as secret economic or physics multipliers.

## State vs trait
A trait describes a persistent fictional tendency. A state is transient: `greeting`, `waiting`, `served`, `celebrating`, `disappointed`, `departing`. Expressions, bubble pacing and dialogue selection can reflect these, but only server/mission-approved `deadlineTicks` or reward policies have game consequences. For v0.1.x all expression transitions are visual only.

## Bounded state machine
`idle -> greet -> request_shown -> wait -> receive -> celebrate -> depart`; optionally `wait -> deadline_warning -> disappointed -> depart` in a later timed mode. A serve animation must be driven by `order_line_progressed`/`order_fulfilled`; never emit its own reward event. A second callback to the same animation must not create additional progress.

## Personality-to-dialogue mapping
Each customer references `dialogueSetId`, with lines keyed by situation (`first_visit`, `repeat_visit`, `order_placed`, `service_received`, `mission_failed`, `festival`). The dialogue writer provides tone and localization notes; no runtime LLM call is needed for moment-to-moment NPC speech. Use a seeded, bounded choice of valid authored lines for replayable missions.

## Accessibility and comfort
Support turning off voice, subtitles, text speed control, high-contrast order icons and reduced-motion facial reactions. Avoid relying on color changes or microexpressions to communicate an urgent timer. Animated characters must not cover the launch zone on narrow phones.
