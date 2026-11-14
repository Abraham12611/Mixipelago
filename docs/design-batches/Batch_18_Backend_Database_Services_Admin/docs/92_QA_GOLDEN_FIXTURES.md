# 92 — QA, Golden Fixtures and Acceptance Matrix

**No real device, physics playtest, API or production billing verification is claimed.** These tests are engineering acceptance specifications.

## Test levels

- **Static:** schema validation; unique IDs, safe feature flags, source rights, version pins and supported references.
- **Pure rule:** test vectors under `examples/tests/pure-rule-vectors.json`; run `python tools/validate_batch18.py`.
- **Integration:** actual game engine/API/DB or OS capability as needed; do not assume passing fixture means implemented system is safe.
- **Security:** actor/resource matrix, idempotent retry, stale version, race and revoked permissions.
- **Manual:** user-directed gameplay/art/audio/native feel acceptance; engineers report evidence rather than marking it approved themselves.

| ID | Feature scope | Named failure/golden case | Evidence |
|---|---|---|---|
| QA-18-01 | Backend system vision and authoritative boundaries | Disable trusted backend and observe a fully playable offline alpha with explicit preview status. | Automated fixture + owner-directed manual UI when visual |
| QA-18-02 | System context, domains and bounded contexts | Architecture linter identifies duplicate ownership of wallet or mission score. | Automated fixture + owner-directed manual UI when visual |
| QA-18-03 | Technology baseline, environments and dependency pins | Local dev boots without cloud credentials for preview gameplay and hosted staging uses separate secrets. | Automated fixture + owner-directed manual UI when visual |
| QA-18-04 | Package and monorepo layout | Dependency checker rejects domain package depending on web or admin app. | Automated fixture + owner-directed manual UI when visual |
| QA-18-05 | Identity, authentication and account linking | Guest-to-account upgrade never turns local preview coins into spendable funds. | Automated fixture + owner-directed manual UI when visual |
| QA-18-06 | Authorization, tenant and player ownership | Authenticated player cannot fetch another player's wallet or hidden campaign discovery. | Automated fixture + owner-directed manual UI when visual |
| QA-18-07 | Session start, input trace and verification API | Tampered shot direction, orphaned session or invalid hash rejects result without reward side effects. | Automated fixture + owner-directed manual UI when visual |
| QA-18-08 | Mission result ingestion and progression bridge | Multi-tab double-submit creates one session result and at most one entitlement of each type. | Automated fixture + owner-directed manual UI when visual |
| QA-18-09 | PostgreSQL schema governance and migrations | CI applies migrations to empty and upgraded databases and checks rollback strategy. | Automated fixture + owner-directed manual UI when visual |
| QA-18-10 | Wallet, coins and purchase handoff | Two simultaneous buys with one remaining budget settle only one debit. | Automated fixture + owner-directed manual UI when visual |
| QA-18-11 | XP, skills and player progression handoff | Replay same mission cannot increase first-clear XP twice. | Automated fixture + owner-directed manual UI when visual |
| QA-18-12 | Inventory, achievements and collectible ownership | Duplicate chest claim returns original receipt, not second collectible. | Automated fixture + owner-directed manual UI when visual |
| QA-18-13 | Campaign graph, island and mission catalog service | A stale client gets explicit content update and retains valid previous progress. | Automated fixture + owner-directed manual UI when visual |
| QA-18-14 | Customer, reputation and encounter reservation | Repeated GET to encounter endpoint returns same customer, not new VIP rolls. | Automated fixture + owner-directed manual UI when visual |
| QA-18-15 | World, quests and event authoring handoffs | Event ends while session active: pinned eligibility policy resolves deterministically. | Automated fixture + owner-directed manual UI when visual |
| QA-18-16 | Leaderboards and tournament backend service | Same proof cannot appear twice in leaderboard or duplicate tournament prize settlement. | Automated fixture + owner-directed manual UI when visual |
| QA-18-17 | Social graph, crews and notifications | Blocked user cannot invite, view private profile or ping via notification retries. | Automated fixture + owner-directed manual UI when visual |
| QA-18-18 | Catalog versioning, content hashes and dependency graph | Rollback pointer changes new sessions only and preserves old proof verification. | Automated fixture + owner-directed manual UI when visual |
| QA-18-19 | Internal admin roles, access reviews and break glass | Quarterly access review spots stale support access and revoked account. | Automated fixture + owner-directed manual UI when visual |
| QA-18-20 | Admin Studio: catalog editors and publishing | Publishing invalid dependency returns reviewer-visible error with path. | Automated fixture + owner-directed manual UI when visual |
| QA-18-21 | Admin Studio: player support and reversible operations | Two support agents cannot credit same incident twice due to unique compensation case. | Automated fixture + owner-directed manual UI when visual |
| QA-18-22 | Admin Studio: QA simulation and replay console | Synthetic replay in staging never lands in public ranking. | Automated fixture + owner-directed manual UI when visual |
| QA-18-23 | API conventions and TypeScript contract envelopes | Same key with changed payload returns IDEMPOTENCY_CONFLICT. | Automated fixture + owner-directed manual UI when visual |
| QA-18-24 | Transactional outbox, event bus and delivery | Kill worker after commit, restart, and assert one wallet grant and one inventory item. | Automated fixture + owner-directed manual UI when visual |
| QA-18-25 | Background jobs, scheduling and queues | Re-run same nightly job produces identical settled totals. | Automated fixture + owner-directed manual UI when visual |
| QA-18-26 | Cache, object storage and CDN contracts | Cross-account cache-poison test does not expose profile or ledger. | Automated fixture + owner-directed manual UI when visual |
| QA-18-27 | Realtime, subscriptions and consistency choices | Offline reconnect refetches authoritative state and resolves revision conflicts. | Automated fixture + owner-directed manual UI when visual |
| QA-18-28 | Offline preview, sync and conflict resolution | Reinstall without account does not claim durable cloud saves; signed-in account restores verified inventory. | Automated fixture + owner-directed manual UI when visual |
| QA-18-29 | Auditability, reconciliation and data lineage | Reconciliation detects missing, double-processed and orphaned entitlement records. | Automated fixture + owner-directed manual UI when visual |
| QA-18-30 | Analytics events, metrics and observability | Redaction test against trace/log export catches bearer token patterns. | Automated fixture + owner-directed manual UI when visual |
| QA-18-31 | Security, secrets and deployment isolation | Build artifact scan fails if service-role credential appears in source map. | Automated fixture + owner-directed manual UI when visual |
| QA-18-32 | Performance, concurrency and capacity planning | Benchmark 100 concurrent synthetic verified-result settlements without duplicate payout. | Automated fixture + owner-directed manual UI when visual |
| QA-18-33 | Backup, restore, disaster recovery and runbooks | Simulate corrupt catalog pointer and recover prior published version with no ledger loss. | Automated fixture + owner-directed manual UI when visual |
| QA-18-34 | CI/CD, previews and release flags | CI blocks PR if contract fixtures or permissions regress. | Automated fixture + owner-directed manual UI when visual |
| QA-18-35 | API security, quotas and abuse budgets | Oversized JSON and replayed signed receipt fail safely and are audited. | Automated fixture + owner-directed manual UI when visual |
| QA-18-36 | Engineering workstreams and first trusted release | First end-to-end trusted grant survives retry, reconnect and worker restart. | Automated fixture + owner-directed manual UI when visual |
| QA-18-37 | ADRs, schema ownership and requirement traceability | Every backend feature maps to source domain, table owner, API, test and rollback. | Automated fixture + owner-directed manual UI when visual |

## Required failure drills

1. Restart browser or native app between request acceptance and UI confirmation; durable state must recover from canonical receipt.
2. Retry an identical command 10 times and a changed-payload command using the same key; observe one effect and one conflict.
3. Expire or unpublish current content pointer while an old pinned run is in flight; its rules remain consistent or a clear safe rejection is delivered.
4. Switch to narrow mobile viewport, large text/reduced motion, offline and low-quality device profile; required UI text and gameplay remain usable.
5. With the relevant release gate OFF, every future route or action is explicitly unavailable and does not create a hidden write.

## What static validation does *not* prove

Schema and pure vector checks are not proof of licensed source delivery, live reward/financial correctness, deterministic cross-machine Rapier replay, actual web/native performance, store approval, privacy compliance or accessibility conformance. Track these separately on an owner-approved acceptance checklist.
