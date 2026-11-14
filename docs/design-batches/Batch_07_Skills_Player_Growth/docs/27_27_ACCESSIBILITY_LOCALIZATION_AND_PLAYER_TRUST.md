# 27 — Accessibility, Localization and Player Trust

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Accessible graph
Every node has a unique accessible name, rank/state, cost and prerequisite list; keyboard focus moves through a predictable reading order, independent of decorative graph layout. Provide a linear list alternative, contrast-safe badges, and descriptions that do not rely on red/green alone.

## Text and number formatting
Use ICU locale formatting for integer XP, prices, percentages, rank ordinals and cooldown durations. Present percentage-point changes distinctly from relative percent increases (`VIP chance +1 percentage point`, not `+1% VIPs`). Decimal separators and right-to-left language layouts require test coverage.

## Motion/audio
Reduced motion must suppress excessive pulsing, parallax and celebratory camera zoom while preserving success state. Sound and vibration optional; no critical information conveyed only by audio. Large text may expand panels without clipping the Learn button.

## Respectful design
- Do not pressure players to 'fix' a bad build with payment or lose accumulated progress.
- Do not gate basic control accessibility behind purchased perks.
- Do not require daily play to preserve earned points or level.
- Display exactly which modes ignore earned bonuses; avoid hidden losses.

## Privacy
A public profile may optionally display specialization and level; hide detailed build/inventory if user chooses. Do not reveal location, identifiable information or user social graph in telemetry by default.
