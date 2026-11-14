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
| MX16-001 | A/Contracts | Product vision, visual goals and first-ship boundaries | Contract + negative fixture + accessible fallback; **At 44 CSS pixels each of the eight starter drinks is identifiable without relying on hue alone.** |
| MX16-002 | A/Contracts | Visual grammar, shapes, silhouettes and material families | Contract + negative fixture + accessible fallback; **In blind recognition testing testers distinguish tier 2 from tier 3 in grayscale.** |
| MX16-003 | A/Contracts | Palette, lighting, reflections and tropical atmosphere | Contract + negative fixture + accessible fallback; **Day/night scene changes preserve readable orders and accessibility contrast.** |
| MX16-004 | A/Contracts | Camera, perspective, anchors and world scaling | Contract + negative fixture + accessible fallback; **Two independently authored drinks land on the same visual baseline when placed at equal Rapier positions.** |
| MX16-005 | A/Contracts | Eight-tier alpha drink artwork bible | Contract + negative fixture + accessible fallback; **Asset manifest contains board sprite, order icon, accessible name and thumbnail for each of eight tiers.** |
| MX16-006 | B/Core | Drink glass geometry, liquid and garnish rules | Contract + negative fixture + accessible fallback; **Glancing-collision sprite overlap stays visually plausible across all tier silhouettes.** |
| MX16-007 | B/Core | Future recipe variants, rarity skins and themed drinks | Contract + negative fixture + accessible fallback; **A cosmetic skin changes sprite key while preserving canonical drink ID and simulation hash.** |
| MX16-008 | B/Core | Customer portraits, body proportions and expressive faces | Contract + negative fixture + accessible fallback; **Character reactions cannot call merge, wallet, or rating mutations.** |
| MX16-009 | B/Core | NPC animation pose library and lip-sync exclusions | Contract + negative fixture + accessible fallback; **Sprite state machines stop animation when a customer card unmounts and obey reduced-motion.** |
| MX16-010 | B/Core | Island atlas and map landmark art | Contract + negative fixture + accessible fallback; **Hidden islands are visually concealed until graph projection says discovered.** |
| MX16-011 | B/Core | Buildings, kiosks, bars and shop upgrade visuals | Contract + negative fixture + accessible fallback; **Reconnect restores installed decor from the backend without replaying a payment animation.** |
| MX16-012 | B/Core | Furniture, props, hazards and interactive affordances | Contract + negative fixture + accessible fallback; **Level fixture tests compare board collision trace before/after cosmetic changes.** |
| MX16-013 | C/Integrations | Backgrounds, compositing and layered parallax | Contract + negative fixture + accessible fallback; **Low-end profile disables distant parallax without altering hitboxes.** |
| MX16-014 | C/Integrations | UI art production and Batch 15 token mapping | Contract + negative fixture + accessible fallback; **Each decorative UI export passes focus/contrast checks in light and dark token contexts.** |
| MX16-015 | C/Integrations | Badges, rarity framing and collection illustration | Contract + negative fixture + accessible fallback; **Unknown reward placeholders never leak unrevealed loot art or hidden identity.** |
| MX16-016 | C/Integrations | Weather, seasons and environment visual states | Contract + negative fixture + accessible fallback; **Reduced-motion and photosensitivity modes remove aggressive effects without losing critical weather text.** |
| MX16-017 | C/Integrations | Animation states and frame budgets | Contract + negative fixture + accessible fallback; **Force-disabling all tween updates leaves identical physics and customer service results.** |
| MX16-018 | C/Integrations | Merge, glint, liquid slosh and particle FX | Contract + negative fixture + accessible fallback; **A 10-merge synthetic chain remains inside a measured particle and GPU budget.** |
| MX16-019 | C/Integrations | Blender master scenes and 3D source hygiene | Contract + negative fixture + accessible fallback; **Clean-room regenerate all eight tier sprites from a pinned render preset.** |
| MX16-020 | C/Integrations | AI-assisted concept generation and human review | Contract + negative fixture + accessible fallback; **Provenance record captures generator, prompt synopsis, input permission and reviewer approval.** |
| MX16-021 | C/Integrations | Licensing, attribution, releases and provenance ledger | Contract + negative fixture + accessible fallback; **CI rejects unknown license state and expired third-party source permission.** |
| MX16-022 | D/QA-Publish | Asset IDs, versioning, hashing and dependency graph | Contract + negative fixture + accessible fallback; **Rolling back art manifest does not change canonical drink or reward identity.** |
| MX16-023 | D/QA-Publish | Sprite formats, atlases, compression and texture RAM | Contract + negative fixture + accessible fallback; **Measured low-tier Android memory remains under a device-class budget during a scene transition.** |
| MX16-024 | D/QA-Publish | Scale variants, DPR, safe areas and responsive output | Contract + negative fixture + accessible fallback; **Narrow phone, tablet and desktop layout tests show correct transparent padding and hot zones.** |
| MX16-025 | D/QA-Publish | Phaser loaders, texture lifetimes and fallback visuals | Contract + negative fixture + accessible fallback; **Simulate offline missing texture, scene restart and repeated navigation with no GPU leak.** |
| MX16-026 | D/QA-Publish | Accessibility, color-blind modes and visual comfort | Contract + negative fixture + accessible fallback; **Grayscale screenshots and keyboard-only UI pass review.** |
| MX16-027 | D/QA-Publish | Asset QA, golden captures and quality signoff | Contract + negative fixture + accessible fallback; **Overlaying collision outlines on rendered board shows no deceptive interactive footprint.** |
| MX16-028 | D/QA-Publish | Automated asset pipeline and CI gates | Contract + negative fixture + accessible fallback; **Corrupt asset file fails CI with a precise path and rule ID.** |
| MX16-029 | D/QA-Publish | Content Studio visual review and publication | Contract + negative fixture + accessible fallback; **Can unpublish new art while old gameplay sessions retain their pinned revision.** |
| MX16-030 | D/QA-Publish | Engineering workstreams and release slices | Contract + negative fixture + accessible fallback; **One PR per asset slice includes source files, license proof, previews and tested fallback.** |
| MX16-031 | D/QA-Publish | Decisions, risks, source references and traceability | Contract + negative fixture + accessible fallback; **Every alpha visual requirement maps to a named owner, fixture and evidence link.** |

## Parallelization policy

- Stream A first freezes IDs and event schema. Pure calculations in stream B can begin simultaneously against fixtures. UI/Content Studio stream C can mock stable read models but cannot invent grant or rank writes.
- Stream D authors negative tests and performance/a11y harness concurrently; avoid waiting until all UI is complete.
- Every PR describes precise files affected, tests run, fixture output, dependent batch contracts, rollout gate and fallback. A migration requires isolated staging verification and an explicit read/write compatibility window.
- If a feature requires another service that is not implemented, merge only its gated read-only contract and document the blocked dependency; never hide placeholder functionality behind a working button.
