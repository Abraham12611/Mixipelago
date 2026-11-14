# Mixipelago — Batch 12: Events, Festivals & Live World Activities

**Design-only engineering packet.** Start with [chapter index](docs/00_INDEX_AND_README.md), [engineer kickoff](ENGINEER_START_HERE.md), and [content manifest](CONTENT_MANIFEST.md).

Optional festivals, seasonal challenges and live community moments that refresh the tropical world without exploiting missed days or bypassing score verification.

## Release sequencing
Candidate first opt-in festival and a single authored event mission after campaign and trusted rewards (v0.6.2); calendar rotation, community goals and seasonal live programs staged later.

## Core boundaries
An event edition is immutable once opened. Eligibility is server-UTC based, and rewards require verified activity receipts. Event windows, score windows, and prize claim grace are different. Community contributions are bounded and idempotent.

## Validation
Run `python tools/validate_batch12.py` from this directory (Python 3.11+, `jsonschema`). Fixtures are proposed and OFF by default, not a claim of any deployed feature. The engineer handoff has review and rollback criteria. Manual UI/gameplay acceptance belongs to the project owner.
