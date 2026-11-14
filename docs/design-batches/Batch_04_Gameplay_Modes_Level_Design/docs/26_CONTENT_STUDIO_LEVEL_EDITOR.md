# 26 — Internal Level Editor, Preview, Validation and Publishing

**Status:** Design specification (not proof of implementation). **Batch:** 4 — Gameplay Modes & Level Design.

## Why build a content studio
An archipelago with hundreds of nodes needs a controlled authoring workflow. Designers should add levels, modify obstacle geometry, tune spawn sequences, and link objectives without editing production TypeScript. The studio is internal, access-controlled, and optional for first 72 hours.

## Editor information architecture
1. Mission Library: filter island, mode, difficulty, status, owner, content version, current build compatibility.
2. Canvas Editor: logical board grid; drag colliders, starting drinks, danger line and launch zone; overlay collision footprints and camera safe areas.
3. Order Planner: list requested tiers, arrival timing, reward values and completion goal.
4. Spawn Planner: seeded item queue, weighted tiers, next preview and first scripted items.
5. Rules Inspector: shots, active timer, materials, available boosters, victory/star conditions.
6. Simulation Preview: run exact physics, record aim commands, show timeline of merge/service/goal events.
7. Feasibility Panel: static bounds, warnings, solver attempts, human winning replay status.
8. Publishing Panel: schema lint, hashes, changelog, QA and owner approval, staged rollout, rollback.

## Workflow
Draft → schema valid → semantic lint → prototype playable → golden solution → design review → owner manual sign-off → locked content version → stage → publish. Every editorial write creates a new draft/revision; publish uses compare-and-swap against active pointer. Deleting a published mission cannot invalidate past receipts; retire it instead.

## Preview inspector
For a selected simulation tick, display all active objects, world positions, velocities, collision pairs, claim states, order priority queue, score, danger counters, current objectives, active-time, shot budget and current RNG state. Export a zipped debug session with sanitized config and command trace.

## Admin authorization
Content author may create drafts; reviewer can approve; publisher can advance active pointer. Maintain audit trail: actor, time, reason, before/after content hashes. Regular players must never access editor endpoints, hidden content or debug cheats.

## Developer MVP
Before full editor exists, mission JSON files in repo plus schema validation and a headless QA CLI are acceptable. Build a minimal `/dev/mission-lab` preview with imported JSON and save/export. No need to block v0.1.0 on a full SaaS content tool.

## Tests
Reject geometry overlaps, unknown drink tiers, missing asset slots, impossible time budget, invalid feature flags, duplicate node IDs, stale editor publish race, missing owner approval, and missions whose golden replay hash changed after tuning.
