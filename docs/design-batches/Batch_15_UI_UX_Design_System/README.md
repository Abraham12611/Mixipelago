# Mixipelago — Batch 15: Complete UI/UX & Design System

**Design-only engineering packet.** Start with [chapter index](docs/00_INDEX_AND_README.md), [engineer kickoff](ENGINEER_START_HERE.md), and [content manifest](CONTENT_MANIFEST.md).

An original, polished tropical 2.5D game interface that stays calm, readable and fast from 320px mobile portrait to desktop landscape, with consistent components and accessible interactions.

## Release sequencing
Foundational tokens, responsive gameplay shell and core routes affect v0.1.x immediately; campaign/shop/profile views rollout with their systems; social, events and live interfaces are feature-gated until owned backends work.

## Core boundaries
Phaser owns the visual tabletop and immediate collision effects; React owns accessible application controls and HUD projections. Every route is feature-gated, no fake functionality. User-generated illustrations can be decorative but interactive UI remains semantic and responsive.

## Validation
Run `python tools/validate_batch15.py` from this directory (Python 3.11+, `jsonschema`). Fixtures are proposed and OFF by default, not a claim of any deployed feature. The engineer handoff has review and rollback criteria. Manual UI/gameplay acceptance belongs to the project owner.
