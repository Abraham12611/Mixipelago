# 22 — Future World Events, Weather, Incidents and Rivals: Interface Overview

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Scope boundary
Weather, economic conditions, unforeseen shop incidents and complex rival businesses belong to Batches 10–12. This chapter defines only the customer-side **input/output envelope**. Do not implement unreviewed penalties or simulate a living world that is unsupported by persistence.

## Read-only context
Customer Director may receive `{worldEventId?, eventContentHash?, regionDemandModifier?, festivalPoolId?, shopStatus?}` from a server-validated world state snapshot. Encounter selection uses a pinned snapshot; a weather change after order placement cannot rewrite that customer's request.

## Potential later scenarios
Tropical heat might increase eligibility of frozen drinks *in an explicitly authored festival mission*; a music festival can increase tourist segment weight; a rival's promotion can create a quest offer or alternate VIP contest. The first alpha does none of this. Real weather APIs are unnecessary to serve fictional game weather.

## Ownership
Batch 10 owns world-state event transitions and reliability; Batch 11 owns story/character arcs and rivals; Batch 12 owns event schedules and festival content. Batch 9 validates resulting customer pool and order eligibility and emits only approved encounter events.

## Anti-chaos rule
No incident can silently subtract trusted coins or generate an impossible customer order. An event that conflicts with mission feasibility must be excluded, postponed or offered as optional content. Restore standard pools on server outage rather than running partially invalid economics.
