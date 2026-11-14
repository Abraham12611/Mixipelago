# 92 — QA, Golden Fixtures and Acceptance Matrix

**No real device, physics playtest, API or production billing verification is claimed.** These tests are engineering acceptance specifications.

## Test levels

- **Static:** schema validation; unique IDs, safe feature flags, source rights, version pins and supported references.
- **Pure rule:** test vectors under `examples/tests/pure-rule-vectors.json`; run `python tools/validate_batch16.py`.
- **Integration:** actual game engine/API/DB or OS capability as needed; do not assume passing fixture means implemented system is safe.
- **Security:** actor/resource matrix, idempotent retry, stale version, race and revoked permissions.
- **Manual:** user-directed gameplay/art/audio/native feel acceptance; engineers report evidence rather than marking it approved themselves.

| ID | Feature scope | Named failure/golden case | Evidence |
|---|---|---|---|
| QA-16-01 | Product vision, visual goals and first-ship boundaries | At 44 CSS pixels each of the eight starter drinks is identifiable without relying on hue alone. | Automated fixture + owner-directed manual UI when visual |
| QA-16-02 | Visual grammar, shapes, silhouettes and material families | In blind recognition testing testers distinguish tier 2 from tier 3 in grayscale. | Automated fixture + owner-directed manual UI when visual |
| QA-16-03 | Palette, lighting, reflections and tropical atmosphere | Day/night scene changes preserve readable orders and accessibility contrast. | Automated fixture + owner-directed manual UI when visual |
| QA-16-04 | Camera, perspective, anchors and world scaling | Two independently authored drinks land on the same visual baseline when placed at equal Rapier positions. | Automated fixture + owner-directed manual UI when visual |
| QA-16-05 | Eight-tier alpha drink artwork bible | Asset manifest contains board sprite, order icon, accessible name and thumbnail for each of eight tiers. | Automated fixture + owner-directed manual UI when visual |
| QA-16-06 | Drink glass geometry, liquid and garnish rules | Glancing-collision sprite overlap stays visually plausible across all tier silhouettes. | Automated fixture + owner-directed manual UI when visual |
| QA-16-07 | Future recipe variants, rarity skins and themed drinks | A cosmetic skin changes sprite key while preserving canonical drink ID and simulation hash. | Automated fixture + owner-directed manual UI when visual |
| QA-16-08 | Customer portraits, body proportions and expressive faces | Character reactions cannot call merge, wallet, or rating mutations. | Automated fixture + owner-directed manual UI when visual |
| QA-16-09 | NPC animation pose library and lip-sync exclusions | Sprite state machines stop animation when a customer card unmounts and obey reduced-motion. | Automated fixture + owner-directed manual UI when visual |
| QA-16-10 | Island atlas and map landmark art | Hidden islands are visually concealed until graph projection says discovered. | Automated fixture + owner-directed manual UI when visual |
| QA-16-11 | Buildings, kiosks, bars and shop upgrade visuals | Reconnect restores installed decor from the backend without replaying a payment animation. | Automated fixture + owner-directed manual UI when visual |
| QA-16-12 | Furniture, props, hazards and interactive affordances | Level fixture tests compare board collision trace before/after cosmetic changes. | Automated fixture + owner-directed manual UI when visual |
| QA-16-13 | Backgrounds, compositing and layered parallax | Low-end profile disables distant parallax without altering hitboxes. | Automated fixture + owner-directed manual UI when visual |
| QA-16-14 | UI art production and Batch 15 token mapping | Each decorative UI export passes focus/contrast checks in light and dark token contexts. | Automated fixture + owner-directed manual UI when visual |
| QA-16-15 | Badges, rarity framing and collection illustration | Unknown reward placeholders never leak unrevealed loot art or hidden identity. | Automated fixture + owner-directed manual UI when visual |
| QA-16-16 | Weather, seasons and environment visual states | Reduced-motion and photosensitivity modes remove aggressive effects without losing critical weather text. | Automated fixture + owner-directed manual UI when visual |
| QA-16-17 | Animation states and frame budgets | Force-disabling all tween updates leaves identical physics and customer service results. | Automated fixture + owner-directed manual UI when visual |
| QA-16-18 | Merge, glint, liquid slosh and particle FX | A 10-merge synthetic chain remains inside a measured particle and GPU budget. | Automated fixture + owner-directed manual UI when visual |
| QA-16-19 | Blender master scenes and 3D source hygiene | Clean-room regenerate all eight tier sprites from a pinned render preset. | Automated fixture + owner-directed manual UI when visual |
| QA-16-20 | AI-assisted concept generation and human review | Provenance record captures generator, prompt synopsis, input permission and reviewer approval. | Automated fixture + owner-directed manual UI when visual |
| QA-16-21 | Licensing, attribution, releases and provenance ledger | CI rejects unknown license state and expired third-party source permission. | Automated fixture + owner-directed manual UI when visual |
| QA-16-22 | Asset IDs, versioning, hashing and dependency graph | Rolling back art manifest does not change canonical drink or reward identity. | Automated fixture + owner-directed manual UI when visual |
| QA-16-23 | Sprite formats, atlases, compression and texture RAM | Measured low-tier Android memory remains under a device-class budget during a scene transition. | Automated fixture + owner-directed manual UI when visual |
| QA-16-24 | Scale variants, DPR, safe areas and responsive output | Narrow phone, tablet and desktop layout tests show correct transparent padding and hot zones. | Automated fixture + owner-directed manual UI when visual |
| QA-16-25 | Phaser loaders, texture lifetimes and fallback visuals | Simulate offline missing texture, scene restart and repeated navigation with no GPU leak. | Automated fixture + owner-directed manual UI when visual |
| QA-16-26 | Accessibility, color-blind modes and visual comfort | Grayscale screenshots and keyboard-only UI pass review. | Automated fixture + owner-directed manual UI when visual |
| QA-16-27 | Asset QA, golden captures and quality signoff | Overlaying collision outlines on rendered board shows no deceptive interactive footprint. | Automated fixture + owner-directed manual UI when visual |
| QA-16-28 | Automated asset pipeline and CI gates | Corrupt asset file fails CI with a precise path and rule ID. | Automated fixture + owner-directed manual UI when visual |
| QA-16-29 | Content Studio visual review and publication | Can unpublish new art while old gameplay sessions retain their pinned revision. | Automated fixture + owner-directed manual UI when visual |
| QA-16-30 | Engineering workstreams and release slices | One PR per asset slice includes source files, license proof, previews and tested fallback. | Automated fixture + owner-directed manual UI when visual |
| QA-16-31 | Decisions, risks, source references and traceability | Every alpha visual requirement maps to a named owner, fixture and evidence link. | Automated fixture + owner-directed manual UI when visual |

## Required failure drills

1. Restart browser or native app between request acceptance and UI confirmation; durable state must recover from canonical receipt.
2. Retry an identical command 10 times and a changed-payload command using the same key; observe one effect and one conflict.
3. Expire or unpublish current content pointer while an old pinned run is in flight; its rules remain consistent or a clear safe rejection is delivered.
4. Switch to narrow mobile viewport, large text/reduced motion, offline and low-quality device profile; required UI text and gameplay remain usable.
5. With the relevant release gate OFF, every future route or action is explicitly unavailable and does not create a hidden write.

## What static validation does *not* prove

Schema and pure vector checks are not proof of licensed source delivery, live reward/financial correctness, deterministic cross-machine Rapier replay, actual web/native performance, store approval, privacy compliance or accessibility conformance. Track these separately on an owner-approved acceptance checklist.
