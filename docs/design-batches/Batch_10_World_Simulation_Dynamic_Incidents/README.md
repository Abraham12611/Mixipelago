# Mixipelago — Batch 10: World Simulation & Dynamic Incidents

**Design-only engineering packet.** Start with [chapter index](docs/00_INDEX_AND_README.md), [engineer kickoff](ENGINEER_START_HERE.md), and [content manifest](CONTENT_MANIFEST.md).

An archipelago that visibly changes over time without turning play into punishment, involuntary debt or nontransparent ranked advantages.

## Release sequencing
Preview weather overlays after the first campaign (candidate v0.6.0); authored opt-in incidents and recovery (v0.6.1+); shop-economic world effects only after audited server-ledger integration (v0.7+).

## Core boundaries
World state is global only when explicitly authored; individual incident choices remain player-owned. Worker schedules are authoritative UTC; puzzle active-time is a different clock. Financial settlement always routes to Batch 06. Recovery options are mandatory for setbacks.

## Validation
Run `python tools/validate_batch10.py` from this directory (Python 3.11+, `jsonschema`). Fixtures are proposed and OFF by default, not a claim of any deployed feature. The engineer handoff has review and rollback criteria. Manual UI/gameplay acceptance belongs to the project owner.
