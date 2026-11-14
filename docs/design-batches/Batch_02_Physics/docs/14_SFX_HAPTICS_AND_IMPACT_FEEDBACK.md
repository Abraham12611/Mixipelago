# 14 — Physics-Driven Sound Effects, Haptics, and Audio Priority

## Goal

The sound of a glass moving, touching another glass, merging, entering danger and completing an order should feel causally related to player action. Sound enhances physics; it never determines it. Runtime sound is produced from licensed/exported audio assets (e.g., custom sound design, ElevenLabs or curated library sounds) and mixed with Web Audio/Howler/Phaser sound manager as selected by audio engineer.

## Event-to-sound mapping

| Event | Sound family | Variation input | Priority |
|---|---|---|---|
| `aim_start` | none or nearly silent cue | input mode | low |
| `shot_fired` | gentle sliding swish | initial shot speed | medium |
| `body_contact_started: drink` | glass clink | relative normal impact speed / material | medium |
| `body_contact_started: wall` | wood/glass tap | impact speed | low |
| `drink_merged` | juicy splash + pitch-toned chime | output tier and chain depth | high |
| `drink_served` | cheerful confirmation | order value (small variations) | high |
| `danger_warning` | quiet low warning tick | remaining grace | high but sparse |
| `session_won` | celebratory musical sting | star rating | critical |
| `session_lost` | sympathetic soft fail sound | loss reason | critical |

Avoid real-world shattering glass on normal collision: no glass break happens physically in alpha; a subtle clink communicates durability. If future mechanics introduce breakage, create a separate sound family.

## Relative-speed mapping

Use threshold bands from contact speed `s` (world units/s), e.g. `s < 0.25 = silent`, `0.25–1.2 = soft`, `1.2–3 = medium`, `>3 = strong`. These are hypotheses. Dynamic gain can use `gain = clamp((s-min)/(max-min), 0.1, 0.75)` and a deterministic or presentation-only pitch variation of ±2–4%. The calculation of pitch can be nondeterministic **only if it cannot affect game state or replay**. Clamp high-speed impacts to prevent painful peaks.

## Voice management

Do not allow 40 sounds to play at once during a chain. Create per-family voice budgets: collision clinks 4, swishes 2, merge 3, UI taps 2, celebrations 1 (example). Set priority and cooldown: identical pair impact sound no more than once per 100–180 ms, wall tap no more than once per 80ms per body, danger tick every 300–500ms max. Collision sounds below a level-adjustable threshold are silent. When a new high-priority event arrives, oldest low-priority voice may be faded/stopped.

## Adaptive music

For alpha, one loopable tropical track with simple volume ducking during victory is sufficient. Later layering: calm beach base, energetic combo percussion, crescendo pad near goals and celebratory sting. Background music resumes after pause only on allowed user gesture. The music director listens to `combo_advanced`, `danger_warning`, and `session_won`, but may never mutate gameplay state or force mission outcomes.

## Haptics

Web haptic capability is inconsistent; `navigator.vibrate` is not widely available on iOS Safari. Make haptics a capability-checked progressive enhancement. Native Capacitor release can add proper haptic calls. Vibrate only on high-value events (first merge, chain, terminal result) and respect device/user preference. No requirement that haptics work for alpha browser acceptance.

## Audio source and licensing

Generated SFX must have documented origin, generation model/tool, plan/license at time of production, file name, derived variants, review date and usage rights. WeLoveIndies assets require proper commercial terms where applicable. ElevenLabs model use also requires review of plan rights. Do not use sounds lifted from Merge Shooter or unrelated games.

## Technical pipeline

- Production: clean source WAV/AIFF at consistent sample rate, export compressed web-ready OGG/MP3/AAC options with fallbacks.
- Normalize loudness and avoid clipping; keep music and SFX in separate buses.
- Cache/decode only common SFX at session start; lazy load later island themes.
- Unlock Web Audio on first user interaction with a clear fallback if browser blocks auto-play.
- Pause/visibility change fades loops appropriately and stops repeated events; resume does not replay every missed collision.
- Disposed scenes unsubscribe audio listeners; sound manager persists only if explicitly app-global.

## Accessibility

SFX cannot be the only indication of success; all key events have visible alternatives. Offer music and SFX independent sliders, a mute button and caption-like text for exceptional alerts. Reduced motion is separate from reduced audio. Avoid harsh sudden volume peaks during chain reactions.

## Test plan

Trigger 100 rapid nonmatching collisions and 10 chained merges; verify peak concurrent voice budget, no clipping, no browser audio exceptions, no repeated sound after restart. Simulate mute, background/resume and blocked autoplay. Owner qualitatively assesses whether music and FX enhance rather than overwhelm the game.
