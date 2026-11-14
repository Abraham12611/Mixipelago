# Mixipelago — Batch 13: Leaderboards, Rankings & Tournaments

**Design-only engineering packet.** Start with [chapter index](docs/00_INDEX_AND_README.md), [engineer kickoff](ENGINEER_START_HERE.md), and [content manifest](CONTENT_MANIFEST.md).

Competition that measures actual drink-shooting skill under equivalent rules, with clear tie-breaking, privacy controls, verifiable scores and trustworthy rewards.

## Release sequencing
One normalized weekly global challenge after verified server replay (candidate v0.5.0); historical seasons/divisions v0.5.1+; tournaments and opt-in regional boards after safeguards.

## Core boundaries
Only a verified competition profile enters ranked standings. The official comparator is score descending, shots ascending, activeTicks ascending, verifiedAt ascending, then playerId ascending. Redis is cache; PostgreSQL and replay receipts are authoritative.

## Validation
Run `python tools/validate_batch13.py` from this directory (Python 3.11+, `jsonschema`). Fixtures are proposed and OFF by default, not a claim of any deployed feature. The engineer handoff has review and rollback criteria. Manual UI/gameplay acceptance belongs to the project owner.
