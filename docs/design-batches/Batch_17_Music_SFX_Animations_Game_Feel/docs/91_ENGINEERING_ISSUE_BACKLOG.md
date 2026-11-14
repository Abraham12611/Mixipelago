# 91 — Atomic Engineering Issue Backlog and Ownership

Engineers create independent branches, open PRs against integration branch, and **do not merge their own PRs**. The coordinator reviews compatibility; `main` promotion requires owner approval. Manual UI, audio and gameplay feel tests are directed to the user.

## Workstreams

- **A — Contracts and fixtures:** freeze source IDs, JSON schema, typed event contracts and rules.
- **B — Pure core services:** implement business constraints and deterministic reference behaviors, no UI grants.
- **C — Integration adapters:** connect game/React/backend/native service through domain-owning APIs.
- **D — Tests, authoring, rollout:** automated proof, accessibility, owner acceptance guide and rollback.

## Issue map (31 atomic tickets)

| Issue ID | Stream | Deliverable | Acceptance proof |
|---|---|---|---|
| MX17-001 | A/Contracts | Audio vision and player promise | Contract + negative fixture + accessible fallback; **Mute all sound and repeat a session; score, physics and customer order outcomes remain identical.** |
| MX17-002 | A/Contracts | Sound category taxonomy and naming | Contract + negative fixture + accessible fallback; **The sound registry rejects orphaned or duplicate cue IDs.** |
| MX17-003 | A/Contracts | Original composition direction and island leitmotifs | Contract + negative fixture + accessible fallback; **Blind review confirms that main theme and island music sound like a consistent original family.** |
| MX17-004 | A/Contracts | Launch, aim and gesture feedback | Contract + negative fixture + accessible fallback; **A cancelled drag never emits launch sound and never consumes a shot.** |
| MX17-005 | A/Contracts | Glass contact material response | Contract + negative fixture + accessible fallback; **Gentle wall taps play at reduced gain and never flood when dozens of contacts happen in one step.** |
| MX17-006 | B/Core | Merge tiers, chain arcs and anticipation | Contract + negative fixture + accessible fallback; **Same mergeId delivered twice never produces two payout or two signature chimes.** |
| MX17-007 | B/Core | Serving, customers, failure and celebration | Contract + negative fixture + accessible fallback; **Deferred network reward creates a quiet pending cue, not the full payout stinger.** |
| MX17-008 | B/Core | UI navigation, toggles and notifications | Contract + negative fixture + accessible fallback; **Repeat opening settings does not leak audio nodes or play multiple copies.** |
| MX17-009 | B/Core | Ambient island soundscapes | Contract + negative fixture + accessible fallback; **Loop transition at boundaries has no click or gain spike.** |
| MX17-010 | B/Core | Dynamic soundtrack layers and musical states | Contract + negative fixture + accessible fallback; **Mid-chain pause then resume restores appropriate layer without duplicating stem playback.** |
| MX17-011 | B/Core | Music loops, stems, tempo and edit points | Contract + negative fixture + accessible fallback; **Sample-accurate loop test detects audible transient at wrap.** |
| MX17-012 | B/Core | Original SFX authoring and synthesis | Contract + negative fixture + accessible fallback; **Unknown source license blocks publication.** |
| MX17-013 | C/Integrations | Audio format matrix and download budgets | Contract + negative fixture + accessible fallback; **iOS and Android smoke test decode each emitted cue without stalling gameplay.** |
| MX17-014 | C/Integrations | Mixer buses, volumes and ducking | Contract + negative fixture + accessible fallback; **Simultaneous win + chain + customer stingers retain headroom in measured output.** |
| MX17-015 | C/Integrations | Collision rate limiting and audio voice budget | Contract + negative fixture + accessible fallback; **In a 100-contact stress fixture, active voices remain bounded.** |
| MX17-016 | C/Integrations | Spatial audio and board position mapping | Contract + negative fixture + accessible fallback; **Left/right panning matches scene visual positions and collapses cleanly in mono.** |
| MX17-017 | C/Integrations | Web Audio initialization and autoplay policies | Contract + negative fixture + accessible fallback; **Reload with audio blocked still enters playable alpha immediately.** |
| MX17-018 | C/Integrations | Phaser and React audio ownership | Contract + negative fixture + accessible fallback; **Remount GameShell 20 times and assert constant listener count.** |
| MX17-019 | C/Integrations | Audio lifecycle, focus, pause, interruption and background | Contract + negative fixture + accessible fallback; **Phone call interruption resumes at user-selected volume without unprompted loud playback.** |
| MX17-020 | C/Integrations | Audio preferences and accessibility | Contract + negative fixture + accessible fallback; **A deaf player can recognize queued orders, invalid shot and mission victory.** |
| MX17-021 | C/Integrations | Voice, character utterances and localization boundaries | Contract + negative fixture + accessible fallback; **Changing locale never breaks nonverbal core audio or order readability.** |
| MX17-022 | D/QA-Publish | Haptics and multisensory feedback contract | Contract + negative fixture + accessible fallback; **Web on unsupported hardware does not show missing-haptic errors.** |
| MX17-023 | D/QA-Publish | Audio event schema and priority routing | Contract + negative fixture + accessible fallback; **Two consumers racing same semantic event result in one cue for exclusive cues.** |
| MX17-024 | D/QA-Publish | Adaptive quality and low-end fallback | Contract + negative fixture + accessible fallback; **Low-power mode stays responsive with 20 concurrent visual game objects.** |
| MX17-025 | D/QA-Publish | Recording, mastering and loudness QA | Contract + negative fixture + accessible fallback; **Win, order and error cues remain discernible at low system volume.** |
| MX17-026 | D/QA-Publish | Music and sound licensing/provenance | Contract + negative fixture + accessible fallback; **Audit retrieves licensor and approved use for every ship-ready cue.** |
| MX17-027 | D/QA-Publish | Audio Content Studio and review publishing | Contract + negative fixture + accessible fallback; **Rollback returns previous master manifest and clear cache identities.** |
| MX17-028 | D/QA-Publish | Telemetry, tuning and sensory health | Contract + negative fixture + accessible fallback; **Sensitive source data absent from telemetry events.** |
| MX17-029 | D/QA-Publish | Audio QA matrix and device verification | Contract + negative fixture + accessible fallback; **Reconnection, pause/resume and multi-scene tests do not duplicate AudioContext instances.** |
| MX17-030 | D/QA-Publish | Workstreams, alpha deliverables and release gates | Contract + negative fixture + accessible fallback; **Audio branch PR includes playable capture references, licensed masters and no-regression checks.** |
| MX17-031 | D/QA-Publish | Risks, decisions, event matrix and glossary | Contract + negative fixture + accessible fallback; **Every cue maps to one semantic event or documented UI action, and every release gate has a test owner.** |

## Parallelization policy

- Stream A first freezes IDs and event schema. Pure calculations in stream B can begin simultaneously against fixtures. UI/Content Studio stream C can mock stable read models but cannot invent grant or rank writes.
- Stream D authors negative tests and performance/a11y harness concurrently; avoid waiting until all UI is complete.
- Every PR describes precise files affected, tests run, fixture output, dependent batch contracts, rollout gate and fallback. A migration requires isolated staging verification and an explicit read/write compatibility window.
- If a feature requires another service that is not implemented, merge only its gated read-only contract and document the blocked dependency; never hide placeholder functionality behind a working button.
