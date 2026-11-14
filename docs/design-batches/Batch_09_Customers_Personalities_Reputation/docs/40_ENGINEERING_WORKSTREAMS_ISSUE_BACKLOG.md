# 40 — Parallel Engineering Workstreams and Proposed Issues

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Responsibilities
Create isolated workstreams without requiring every engineer to touch the same reducer. **A: Customer catalog/director** owns pure selection and validation. **B: Session integration** owns read-only customer projection and order UI binding. **C: Backend trust** owns receipts, observations and RLS. **D: Reputation/loyalty** owns capped policies and projections. **E: Art/audio/UI** owns animation assets and journal screens. **F: QA/content tools** owns validators, fixtures and end-to-end tests.

## Proposed issue map (dependencies in parentheses)
| Issue | Owner | Deliverable | Dependencies |
|---|---|---|---|
| CUS-001 | A | Shared customer domain types | Batch 3/4 contracts |
| CUS-002 | A | Customer catalog schema and validator | 001 |
| CUS-003 | A | Published pool eligibility resolver | 002 |
| CUS-004 | A | Seeded weighted selection | 003 |
| CUS-005 | A | Reserved encounter idempotency | 004, C |
| CUS-006 | B | Two-order customer HUD adapter | Batch 4 |
| CUS-007 | B | Served reaction animation state | 006 |
| CUS-008 | B | Responsive customer cards and accessibility | 006 |
| CUS-009 | E | Two canonical alpha portraits/state atlas | art guide |
| CUS-010 | E | Voice/SFX cue adapter | 007, 009 |
| CUS-011 | F | Order reachability test harness | Batch 4 |
| CUS-012 | F | Pool/encounter negative fixtures | 003–005 |
| CUS-013 | C | Verified service observation ingest | Batches 4/6 |
| CUS-014 | C | DB/RLS and uniqueness constraints | 013 |
| CUS-015 | D | Satisfaction pure policy reducer | 013 |
| CUS-016 | D | Reputation bounded projection | 014–015 |
| CUS-017 | C | Read-only reputation endpoint | 016 |
| CUS-018 | E | Shop reputation panel | 017 |
| CUS-019 | D | Relationship point/level reducer | 013 |
| CUS-020 | C | Relationship source dedupe | 019, 014 |
| CUS-021 | E | Guest journal/portrait detail | 019–020 |
| CUS-022 | D | Optional loyalty milestone -> Batch 8 handoff | 020 |
| CUS-023 | A | VIP class probability and eligibility cap | 003/004/skill snapshot |
| CUS-024 | B | VIP contract UI with opt-in & disclosure | 023 |
| CUS-025 | F | 100k seed sampling + fairness matrix | 023 |
| CUS-026 | F | Cross-device, replay and anti-cheat tests | 013–025 |
| CUS-027 | F | Content Studio preview and publish gate | 002/003 |
| CUS-028 | F | Release gates, monitoring and rollback rehearsal | all release slices |

## Review rules
Engineers open focused PRs on feature branches targeting `develop` if present, otherwise agreed integration branch. They **never self-merge**. Main release merges require the owner's approval. The owner performs manual UI/gameplay checks; engineers provide preview deployment and precise test steps.

## Critical path
Alpha visuals 006–010 can proceed alongside backend types 001–005. The first trusted customer slice requires 013–018, not VIP/relationships. Relationship and VIP tasks are independently gated.
