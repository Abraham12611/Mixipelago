# 91 — Atomic Engineering Issue Backlog and Ownership

Engineers create independent branches, open PRs against integration branch, and **do not merge their own PRs**. The coordinator reviews compatibility; `main` promotion requires owner approval. Manual UI, audio and gameplay feel tests are directed to the user.

## Workstreams

- **A — Contracts and fixtures:** freeze source IDs, JSON schema, typed event contracts and rules.
- **B — Pure core services:** implement business constraints and deterministic reference behaviors, no UI grants.
- **C — Integration adapters:** connect game/React/backend/native service through domain-owning APIs.
- **D — Tests, authoring, rollout:** automated proof, accessibility, owner acceptance guide and rollback.

## Issue map (37 atomic tickets)

| Issue ID | Stream | Deliverable | Acceptance proof |
|---|---|---|---|
| MX18-001 | A/Contracts | Backend system vision and authoritative boundaries | Contract + negative fixture + accessible fallback; **Disable trusted backend and observe a fully playable offline alpha with explicit preview status.** |
| MX18-002 | A/Contracts | System context, domains and bounded contexts | Contract + negative fixture + accessible fallback; **Architecture linter identifies duplicate ownership of wallet or mission score.** |
| MX18-003 | A/Contracts | Technology baseline, environments and dependency pins | Contract + negative fixture + accessible fallback; **Local dev boots without cloud credentials for preview gameplay and hosted staging uses separate secrets.** |
| MX18-004 | A/Contracts | Package and monorepo layout | Contract + negative fixture + accessible fallback; **Dependency checker rejects domain package depending on web or admin app.** |
| MX18-005 | A/Contracts | Identity, authentication and account linking | Contract + negative fixture + accessible fallback; **Guest-to-account upgrade never turns local preview coins into spendable funds.** |
| MX18-006 | B/Core | Authorization, tenant and player ownership | Contract + negative fixture + accessible fallback; **Authenticated player cannot fetch another player's wallet or hidden campaign discovery.** |
| MX18-007 | B/Core | Session start, input trace and verification API | Contract + negative fixture + accessible fallback; **Tampered shot direction, orphaned session or invalid hash rejects result without reward side effects.** |
| MX18-008 | B/Core | Mission result ingestion and progression bridge | Contract + negative fixture + accessible fallback; **Multi-tab double-submit creates one session result and at most one entitlement of each type.** |
| MX18-009 | B/Core | PostgreSQL schema governance and migrations | Contract + negative fixture + accessible fallback; **CI applies migrations to empty and upgraded databases and checks rollback strategy.** |
| MX18-010 | B/Core | Wallet, coins and purchase handoff | Contract + negative fixture + accessible fallback; **Two simultaneous buys with one remaining budget settle only one debit.** |
| MX18-011 | B/Core | XP, skills and player progression handoff | Contract + negative fixture + accessible fallback; **Replay same mission cannot increase first-clear XP twice.** |
| MX18-012 | B/Core | Inventory, achievements and collectible ownership | Contract + negative fixture + accessible fallback; **Duplicate chest claim returns original receipt, not second collectible.** |
| MX18-013 | C/Integrations | Campaign graph, island and mission catalog service | Contract + negative fixture + accessible fallback; **A stale client gets explicit content update and retains valid previous progress.** |
| MX18-014 | C/Integrations | Customer, reputation and encounter reservation | Contract + negative fixture + accessible fallback; **Repeated GET to encounter endpoint returns same customer, not new VIP rolls.** |
| MX18-015 | C/Integrations | World, quests and event authoring handoffs | Contract + negative fixture + accessible fallback; **Event ends while session active: pinned eligibility policy resolves deterministically.** |
| MX18-016 | C/Integrations | Leaderboards and tournament backend service | Contract + negative fixture + accessible fallback; **Same proof cannot appear twice in leaderboard or duplicate tournament prize settlement.** |
| MX18-017 | C/Integrations | Social graph, crews and notifications | Contract + negative fixture + accessible fallback; **Blocked user cannot invite, view private profile or ping via notification retries.** |
| MX18-018 | C/Integrations | Catalog versioning, content hashes and dependency graph | Contract + negative fixture + accessible fallback; **Rollback pointer changes new sessions only and preserves old proof verification.** |
| MX18-019 | C/Integrations | Internal admin roles, access reviews and break glass | Contract + negative fixture + accessible fallback; **Quarterly access review spots stale support access and revoked account.** |
| MX18-020 | C/Integrations | Admin Studio: catalog editors and publishing | Contract + negative fixture + accessible fallback; **Publishing invalid dependency returns reviewer-visible error with path.** |
| MX18-021 | C/Integrations | Admin Studio: player support and reversible operations | Contract + negative fixture + accessible fallback; **Two support agents cannot credit same incident twice due to unique compensation case.** |
| MX18-022 | D/QA-Publish | Admin Studio: QA simulation and replay console | Contract + negative fixture + accessible fallback; **Synthetic replay in staging never lands in public ranking.** |
| MX18-023 | D/QA-Publish | API conventions and TypeScript contract envelopes | Contract + negative fixture + accessible fallback; **Same key with changed payload returns IDEMPOTENCY_CONFLICT.** |
| MX18-024 | D/QA-Publish | Transactional outbox, event bus and delivery | Contract + negative fixture + accessible fallback; **Kill worker after commit, restart, and assert one wallet grant and one inventory item.** |
| MX18-025 | D/QA-Publish | Background jobs, scheduling and queues | Contract + negative fixture + accessible fallback; **Re-run same nightly job produces identical settled totals.** |
| MX18-026 | D/QA-Publish | Cache, object storage and CDN contracts | Contract + negative fixture + accessible fallback; **Cross-account cache-poison test does not expose profile or ledger.** |
| MX18-027 | D/QA-Publish | Realtime, subscriptions and consistency choices | Contract + negative fixture + accessible fallback; **Offline reconnect refetches authoritative state and resolves revision conflicts.** |
| MX18-028 | D/QA-Publish | Offline preview, sync and conflict resolution | Contract + negative fixture + accessible fallback; **Reinstall without account does not claim durable cloud saves; signed-in account restores verified inventory.** |
| MX18-029 | D/QA-Publish | Auditability, reconciliation and data lineage | Contract + negative fixture + accessible fallback; **Reconciliation detects missing, double-processed and orphaned entitlement records.** |
| MX18-030 | D/QA-Publish | Analytics events, metrics and observability | Contract + negative fixture + accessible fallback; **Redaction test against trace/log export catches bearer token patterns.** |
| MX18-031 | D/QA-Publish | Security, secrets and deployment isolation | Contract + negative fixture + accessible fallback; **Build artifact scan fails if service-role credential appears in source map.** |
| MX18-032 | D/QA-Publish | Performance, concurrency and capacity planning | Contract + negative fixture + accessible fallback; **Benchmark 100 concurrent synthetic verified-result settlements without duplicate payout.** |
| MX18-033 | D/QA-Publish | Backup, restore, disaster recovery and runbooks | Contract + negative fixture + accessible fallback; **Simulate corrupt catalog pointer and recover prior published version with no ledger loss.** |
| MX18-034 | D/QA-Publish | CI/CD, previews and release flags | Contract + negative fixture + accessible fallback; **CI blocks PR if contract fixtures or permissions regress.** |
| MX18-035 | D/QA-Publish | API security, quotas and abuse budgets | Contract + negative fixture + accessible fallback; **Oversized JSON and replayed signed receipt fail safely and are audited.** |
| MX18-036 | D/QA-Publish | Engineering workstreams and first trusted release | Contract + negative fixture + accessible fallback; **First end-to-end trusted grant survives retry, reconnect and worker restart.** |
| MX18-037 | D/QA-Publish | ADRs, schema ownership and requirement traceability | Contract + negative fixture + accessible fallback; **Every backend feature maps to source domain, table owner, API, test and rollback.** |

## Parallelization policy

- Stream A first freezes IDs and event schema. Pure calculations in stream B can begin simultaneously against fixtures. UI/Content Studio stream C can mock stable read models but cannot invent grant or rank writes.
- Stream D authors negative tests and performance/a11y harness concurrently; avoid waiting until all UI is complete.
- Every PR describes precise files affected, tests run, fixture output, dependent batch contracts, rollout gate and fallback. A migration requires isolated staging verification and an explicit read/write compatibility window.
- If a feature requires another service that is not implemented, merge only its gated read-only contract and document the blocked dependency; never hide placeholder functionality behind a working button.
