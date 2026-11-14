# Mixipelago — Batch 11: Stories, Characters, Quests & Rival Businesses

**Design-only engineering packet.** Start with [chapter index](docs/00_INDEX_AND_README.md), [engineer kickoff](ENGINEER_START_HERE.md), and [content manifest](CONTENT_MANIFEST.md).

Short, charming, optional story arcs and rival businesses that give emotional meaning to island progress without turning a quick puzzle session into forced dialogue.

## Release sequencing
Story introduction and one optional quest chain after basic map/player persistence (candidate v0.5.3); branching arcs and simulated rival businesses expand later behind distinct gates.

## Core boundaries
Narrative content never grants resources by itself. Quest evidence and story choices are stored independently. Mainline quests have an accessible no-spend route; prose is optional and can be skipped. Rival owners are fictional NPCs, not deceptive simulated human opponents.

## Validation
Run `python tools/validate_batch11.py` from this directory (Python 3.11+, `jsonschema`). Fixtures are proposed and OFF by default, not a claim of any deployed feature. The engineer handoff has review and rollback criteria. Manual UI/gameplay acceptance belongs to the project owner.
