# Mixipelago — Batch 14: Friends, Crews, Cooperation & Multiplayer

**Design-only engineering packet.** Start with [chapter index](docs/00_INDEX_AND_README.md), [engineer kickoff](ENGINEER_START_HERE.md), and [content manifest](CONTENT_MANIFEST.md).

Welcoming, privacy-conscious social play that starts with safe asynchronous challenges and only adds real-time competition after authoritative networking is proven.

## Release sequencing
Candidate v0.7.0 friends + asynchronous ghost challenges; v0.7.1 crew projects; v0.8.0+ real-time matches only after authoritative simulation, reconnect and moderation tests.

## Core boundaries
Friend consent, blocking and privacy protections are product primitives. A real-time client cannot authoritatively determine match score, collision or winner. In early releases there are no unrestricted public DMs or player-to-player coin trades.

## Validation
Run `python tools/validate_batch14.py` from this directory (Python 3.11+, `jsonschema`). Fixtures are proposed and OFF by default, not a claim of any deployed feature. The engineer handoff has review and rollback criteria. Manual UI/gameplay acceptance belongs to the project owner.
