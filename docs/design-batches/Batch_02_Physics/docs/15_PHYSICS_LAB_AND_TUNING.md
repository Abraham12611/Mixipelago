# 15 — Physics Laboratory, Telemetry, Preset Comparison, and Owner Feel-Test

## Why a lab is required

The hardest part of this game is subjective motion feel. Source screenshots do not reveal true friction, elasticity, impulse, radius, mass or solver behavior. Hardcoding arbitrary values creates days of iteration. Build an isolated developer-only `/dev/physics-lab` route with repeatable fixtures and one-click parameter changes. It must never be exposed to untrusted public users as a way to alter competitive physics.

## Layout

- Center canvas: exact same Rapier adapter and render layer used by actual game, not a separate approximate demo.
- Left control panel: presets, contact geometry, shot input mode, setup fixtures, world params.
- Right telemetry: step times, body count, velocities, event count, score-free contact history, replay hash, warnings.
- Bottom timeline: simulation step scrub/play/pause, previous/next fixture, export JSON and short metadata report.
- Desktop is primary lab. Mobile simplified lab may expose preset switches and performance overlay to owner testers.

## Slider controls

| Control | Min | Max | Default | Live mutation policy |
|---|---:|---:|---:|---|
| Launch impulse | 2 | 9 | 4.5 | Restart fixture to compare fairly |
| Linear damping | .02 | .65 | .12 | Restart fixture; record version |
| Angular damping | .1 | 2 | .65 | Restart fixture |
| Contact friction | 0 | .5 | .06 | Restart fixture |
| Glass restitution | 0 | .85 | .38 | Restart fixture |
| Rail restitution | 0 | .85 | .28 | Restart fixture |
| Radius | .25 | .55 | .34 | Restart fixture, avoid overlap |
| Density | .5 | 3 | 1 | Restart fixture |
| Max speed | 6 | 20 | 10 | Restart fixture |
| CCD | off | on | on | Restart fixture |
| Step Hz | 60 | 120 | 60 | Restart fixture and record build |
| Danger grace | 400 ms | 1500 ms | 850 ms | Content rule version change |

Even though UI looks like sliders, altering settings mid-session changes state and invalidates preset comparison/replay. For lab experiments, sliders change *next run's preset*, and a clear "Restart with Changes" action rebuilds the session. An explicit hot-edit mode may be available, marked nonreplayable.

## Canonical presets for first review

| Preset ID | Damping | Friction | Restitution | Impulse | Character |
|---|---:|---:|---:|---:|---|
| `glide-soft-alpha` | .18 | .08 | .22 | 4.5 | Smooth, gentle contacts |
| `glide-balanced-alpha` | .12 | .06 | .38 | 4.5 | Default hypothesis |
| `glide-pinball-alpha` | .07 | .03 | .58 | 4.2 | Lively ricochet, higher crowding risk |

No preset is approved until owner feedback and automated stability checks. Preset changes need ID/hash, not just name: otherwise replay result becomes ambiguous after someone edits a JSON file named `balanced`.

## Fixture catalog

- `F001-empty-glide`: one moving drink, no other drinks.
- `F002-head-on-equal`: two equal bodies along same axis, different tiers.
- `F003-glance-quarter`: offset hit at ~0.25 radius, different tiers.
- `F004-glance-half`: offset hit at ~0.5 radius.
- `F005-tangent`: near-grazing contact; ensure no unexpected merge.
- `F006-wall-oblique`: wall at 45° incoming direction.
- `F007-three-way`: one drink simultaneously contacts two matching bodies.
- `F008-chain-three`: a t2→t3 result can contact another t3.
- `F009-crowded`: 20 bodies in partial dense arrangement.
- `F010-danger-rescue`: contact nudges endangered body back above line.
- `F011-high-speed-ccd`: maximum valid shot toward thin wall and body.
- `F012-resume-hidden`: hidden tab then resume; no catch-up.

Each fixture includes seed, initial positions/velocities, action command list, expected invariants, and optional baseline state hash. Do not assert exact velocities until approved physics binary and preset are pinned.

## Instrumentation

Collect: per-step elapsed time; average render frame time; p95 step time in one-second windows; active/sleeping bodies; contact pairs; merge transactions committed/rejected; voice count; memory signals when available; dropped accumulator time; blocked launch reasons; hit/merge ratio. No player personal data needed. Lab can export `.json` and `.csv` locally.

For visuals, overlay collider circles, centers, contact normals, velocity vectors, collision IDs, object statuses, danger zone and transformed grid. Toggle overlay with keyboard shortcut and never accidentally show it in production.

## Owner review protocol

A. Engineer posts a preview build and automated fixture results. B. Owner tries three presets in shuffled order on one desktop and one physical mobile device. C. Owner provides a score 1–5 on glide, precision, collision satisfaction, chain readability, control comfort, motion stability. D. Engineer logs issues and adjusts one variable family at a time. E. Coordinator approves canonical preset and locks its physics version.

Avoid misleading A/B where one preset uses different shot forces or crowding fixtures. Compare identical seeds and inputs, and call out when presets change trajectories inherently.

## Acceptance

Physics lab opens in development, can load/restart fixtures, show at least 8 metrics, export preset JSON, record screenshots/video manually by owner, and reproduce a preset by hash. Runtime output must come from the same underlying simulation as the product.
