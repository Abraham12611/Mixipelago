# 92 — QA, Golden Fixtures and Acceptance Matrix

**No real device, physics playtest, API or production billing verification is claimed.** These tests are engineering acceptance specifications.

## Test levels

- **Static:** schema validation; unique IDs, safe feature flags, source rights, version pins and supported references.
- **Pure rule:** test vectors under `examples/tests/pure-rule-vectors.json`; run `python tools/validate_batch17.py`.
- **Integration:** actual game engine/API/DB or OS capability as needed; do not assume passing fixture means implemented system is safe.
- **Security:** actor/resource matrix, idempotent retry, stale version, race and revoked permissions.
- **Manual:** user-directed gameplay/art/audio/native feel acceptance; engineers report evidence rather than marking it approved themselves.

| ID | Feature scope | Named failure/golden case | Evidence |
|---|---|---|---|
| QA-17-01 | Audio vision and player promise | Mute all sound and repeat a session; score, physics and customer order outcomes remain identical. | Automated fixture + owner-directed manual UI when visual |
| QA-17-02 | Sound category taxonomy and naming | The sound registry rejects orphaned or duplicate cue IDs. | Automated fixture + owner-directed manual UI when visual |
| QA-17-03 | Original composition direction and island leitmotifs | Blind review confirms that main theme and island music sound like a consistent original family. | Automated fixture + owner-directed manual UI when visual |
| QA-17-04 | Launch, aim and gesture feedback | A cancelled drag never emits launch sound and never consumes a shot. | Automated fixture + owner-directed manual UI when visual |
| QA-17-05 | Glass contact material response | Gentle wall taps play at reduced gain and never flood when dozens of contacts happen in one step. | Automated fixture + owner-directed manual UI when visual |
| QA-17-06 | Merge tiers, chain arcs and anticipation | Same mergeId delivered twice never produces two payout or two signature chimes. | Automated fixture + owner-directed manual UI when visual |
| QA-17-07 | Serving, customers, failure and celebration | Deferred network reward creates a quiet pending cue, not the full payout stinger. | Automated fixture + owner-directed manual UI when visual |
| QA-17-08 | UI navigation, toggles and notifications | Repeat opening settings does not leak audio nodes or play multiple copies. | Automated fixture + owner-directed manual UI when visual |
| QA-17-09 | Ambient island soundscapes | Loop transition at boundaries has no click or gain spike. | Automated fixture + owner-directed manual UI when visual |
| QA-17-10 | Dynamic soundtrack layers and musical states | Mid-chain pause then resume restores appropriate layer without duplicating stem playback. | Automated fixture + owner-directed manual UI when visual |
| QA-17-11 | Music loops, stems, tempo and edit points | Sample-accurate loop test detects audible transient at wrap. | Automated fixture + owner-directed manual UI when visual |
| QA-17-12 | Original SFX authoring and synthesis | Unknown source license blocks publication. | Automated fixture + owner-directed manual UI when visual |
| QA-17-13 | Audio format matrix and download budgets | iOS and Android smoke test decode each emitted cue without stalling gameplay. | Automated fixture + owner-directed manual UI when visual |
| QA-17-14 | Mixer buses, volumes and ducking | Simultaneous win + chain + customer stingers retain headroom in measured output. | Automated fixture + owner-directed manual UI when visual |
| QA-17-15 | Collision rate limiting and audio voice budget | In a 100-contact stress fixture, active voices remain bounded. | Automated fixture + owner-directed manual UI when visual |
| QA-17-16 | Spatial audio and board position mapping | Left/right panning matches scene visual positions and collapses cleanly in mono. | Automated fixture + owner-directed manual UI when visual |
| QA-17-17 | Web Audio initialization and autoplay policies | Reload with audio blocked still enters playable alpha immediately. | Automated fixture + owner-directed manual UI when visual |
| QA-17-18 | Phaser and React audio ownership | Remount GameShell 20 times and assert constant listener count. | Automated fixture + owner-directed manual UI when visual |
| QA-17-19 | Audio lifecycle, focus, pause, interruption and background | Phone call interruption resumes at user-selected volume without unprompted loud playback. | Automated fixture + owner-directed manual UI when visual |
| QA-17-20 | Audio preferences and accessibility | A deaf player can recognize queued orders, invalid shot and mission victory. | Automated fixture + owner-directed manual UI when visual |
| QA-17-21 | Voice, character utterances and localization boundaries | Changing locale never breaks nonverbal core audio or order readability. | Automated fixture + owner-directed manual UI when visual |
| QA-17-22 | Haptics and multisensory feedback contract | Web on unsupported hardware does not show missing-haptic errors. | Automated fixture + owner-directed manual UI when visual |
| QA-17-23 | Audio event schema and priority routing | Two consumers racing same semantic event result in one cue for exclusive cues. | Automated fixture + owner-directed manual UI when visual |
| QA-17-24 | Adaptive quality and low-end fallback | Low-power mode stays responsive with 20 concurrent visual game objects. | Automated fixture + owner-directed manual UI when visual |
| QA-17-25 | Recording, mastering and loudness QA | Win, order and error cues remain discernible at low system volume. | Automated fixture + owner-directed manual UI when visual |
| QA-17-26 | Music and sound licensing/provenance | Audit retrieves licensor and approved use for every ship-ready cue. | Automated fixture + owner-directed manual UI when visual |
| QA-17-27 | Audio Content Studio and review publishing | Rollback returns previous master manifest and clear cache identities. | Automated fixture + owner-directed manual UI when visual |
| QA-17-28 | Telemetry, tuning and sensory health | Sensitive source data absent from telemetry events. | Automated fixture + owner-directed manual UI when visual |
| QA-17-29 | Audio QA matrix and device verification | Reconnection, pause/resume and multi-scene tests do not duplicate AudioContext instances. | Automated fixture + owner-directed manual UI when visual |
| QA-17-30 | Workstreams, alpha deliverables and release gates | Audio branch PR includes playable capture references, licensed masters and no-regression checks. | Automated fixture + owner-directed manual UI when visual |
| QA-17-31 | Risks, decisions, event matrix and glossary | Every cue maps to one semantic event or documented UI action, and every release gate has a test owner. | Automated fixture + owner-directed manual UI when visual |

## Required failure drills

1. Restart browser or native app between request acceptance and UI confirmation; durable state must recover from canonical receipt.
2. Retry an identical command 10 times and a changed-payload command using the same key; observe one effect and one conflict.
3. Expire or unpublish current content pointer while an old pinned run is in flight; its rules remain consistent or a clear safe rejection is delivered.
4. Switch to narrow mobile viewport, large text/reduced motion, offline and low-quality device profile; required UI text and gameplay remain usable.
5. With the relevant release gate OFF, every future route or action is explicitly unavailable and does not create a hidden write.

## What static validation does *not* prove

Schema and pure vector checks are not proof of licensed source delivery, live reward/financial correctness, deterministic cross-machine Rapier replay, actual web/native performance, store approval, privacy compliance or accessibility conformance. Track these separately on an owner-approved acceptance checklist.
