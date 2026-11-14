# 34 — Architecture Decision Records, Precedent and Open Questions

## Confirmed from earlier batches (do not reopen casually)
- The first playable physics session runs in browser; map is outside the collision simulation.
- Tier1–tier8 linear merge chain; auto-serving newly merged output before continuing chain; no changes here.
- `coconut-cove-001` is the canonical two-order win fixture; `-002` is a draft authored service candidate.
- Only server-verified sessions can generate future durable economy/ranked rewards; alpha coins are untrusted preview.
- Missions are versioned, pinned and immutable after publish.
- Main branch promotion requires owner approval; all manual UI tests are owner-directed.

## Proposed Batch 5 ADRs requiring owner signoff
**B5-ADR-01:** `CampaignNode` is separate from `MissionDefinition` and always references stable ID/version.
**B5-ADR-02:** Permanent unlock expressions use a bounded monotonic DSL, excluding unrestricted `not`.
**B5-ADR-03:** A separate published **graph** can be updated without changing mission content hashes.
**B5-ADR-04:** Initial map progress is local preview until verified account progression is implemented.
**B5-ADR-05:** Live campaign cannot have mandatory secret/event/disabled-service gates.
**B5-ADR-06:** Next Mission button exists independent of map gesture navigation.
**B5-ADR-07:** Stars are derived from Batch 4 results and best values are monotonic.
**B5-ADR-08:** Future first-clear and chest rewards are idempotent, using server-approved reward policy IDs.
**B5-ADR-09:** Cross-island travel is a gateway action, not a coin cost by default.
**B5-ADR-10:** Map uses Phaser scene + React overlays; no physics engine in map mode.
**B5-ADR-11:** Published placeholders are noninteractive; draft missions cannot appear as playable.

## Open questions
- Should optional branches rejoin after one mission or whole districts? Default: occasional rejoin, not excessive fragmentation.
- Should a `missionCleared` prerequisite reference any historic verified version or a bounded compatibility set? Default: stable mission ID + compatible verified result, explicit migration for major rule changes.
- When account sync ships, can local preview wins be imported for campaign-only cosmetics? Default: no trusted conversion until reviewed policy.
- Should gateway travel have a celebration cutscene? Default: short and skippable.
- Which map style balances 2.5D beauty with small-phone legibility? Requires user visual approval.

## Decision governance
Log ID, status (`proposed|approved|superseded`), owner decision date, rationale, affected schemas, migration, tests and release flag. Do not describe proposed values as already deployed. If owner changes a design assumption, update authoritative schemas and examples first, then dependent docs.
