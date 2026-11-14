# Batch 11 — Stories, Characters, Quests & Rival Businesses

**Status:** design and engineering pack · 2026-11-14 · not an implemented feature.

## Product promise
Short, charming, optional story arcs and rival businesses that give emotional meaning to island progress without turning a quick puzzle session into forced dialogue.

## Source-of-truth boundaries
- Batch 02 alone owns fixed-step Rapier physics, collision/merge arbitration, and immutable simulation outcome semantics. No new feature writes physical contacts or awards rewards from visual effects.
- Batch 03 owns the eight-tier alpha ladder and newly merged drink auto-serving to oldest compatible active order; Batch 04 owns mission goals, stars and win/loss state.
- Batch 05 owns campaign graph visibility/unlocks; Batch 06 owns wallet and financial ledger; Batch 07 owns XP/skills; Batch 08 owns reward/collectible entitlements; Batch 09 owns customer/relationship facts while shop reputation settlement remains under Batch 06.
- Client previews and unverified sessions are not currency, XP, competitive score, badge provenance, or trusted activity evidence. All durable grants derive from unique verified receipts.
- Ranked play freezes the physics/scoring/content/seed profile and disables non-normalized world, shop, skill, story, social and cosmetic advantages.
- Every stage is a proposal, not a claim of implementation. Manual browser and gameplay acceptance belongs to the owner. Engineers open PRs and do not self-merge.

**This batch specifically owns:** Narrative definitions, dialogue choices and story flags, quest orchestration, approved rival behaviors and the player chronicle.

**External integrations:** Batch 05 campaign, Batch 09 customers, Batch 06 shops and rewards, Batch 08 collectibles, Batch 10 incidents and Batch 12 festivals.

## Documents and reading order
- [01 — Narrative direction and optional story promise](01_NARRATIVE_DIRECTION_AND_OPTIONAL_STORY_PROMISE.md)
- [02 — Narrative world bible and canon hierarchy](02_NARRATIVE_WORLD_BIBLE_AND_CANON_HIERARCHY.md)
- [03 — Story acts, episodes and campaign beats](03_STORY_ACTS_EPISODES_AND_CAMPAIGN_BEATS.md)
- [04 — Character registry and persistent roles](04_CHARACTER_REGISTRY_AND_PERSISTENT_ROLES.md)
- [05 — Quest taxonomy and progression objectives](05_QUEST_TAXONOMY_AND_PROGRESSION_OBJECTIVES.md)
- [06 — Quest DSL and prerequisites](06_QUEST_DSL_AND_PREREQUISITES.md)
- [07 — Dialogue graph and conversational UI](07_DIALOGUE_GRAPH_AND_CONVERSATIONAL_UI.md)
- [08 — Choices, consequences and reversibility](08_CHOICES_CONSEQUENCES_AND_REVERSIBILITY.md)
- [09 — Relationship and affinity flags](09_RELATIONSHIP_AND_AFFINITY_FLAGS.md)
- [10 — Recurring rival owners and businesses](10_RECURRING_RIVAL_OWNERS_AND_BUSINESSES.md)
- [11 — Rival challenge system and scoring fairness](11_RIVAL_CHALLENGE_SYSTEM_AND_SCORING_FAIRNESS.md)
- [12 — NPC schedule, presence and return appearances](12_NPC_SCHEDULE_PRESENCE_AND_RETURN_APPEARANCES.md)
- [13 — Quests linked to missions, shops and islands](13_QUESTS_LINKED_TO_MISSIONS_SHOPS_AND_ISLANDS.md)
- [14 — Narrative reward policy and integrity](14_NARRATIVE_REWARD_POLICY_AND_INTEGRITY.md)
- [15 — Story history, Chronicle and recap](15_STORY_HISTORY_CHRONICLE_AND_RECAP.md)
- [16 — Branching, reconvergence and save migration](16_BRANCHING_RECONVERGENCE_AND_SAVE_MIGRATION.md)
- [17 — Narrative world and dynamic incidents](17_NARRATIVE_WORLD_AND_DYNAMIC_INCIDENTS.md)
- [18 — Festival storytelling and calendar coordination](18_FESTIVAL_STORYTELLING_AND_CALENDAR_COORDINATION.md)
- [19 — Narrative UI, transitions and accessibility](19_NARRATIVE_UI_TRANSITIONS_AND_ACCESSIBILITY.md)
- [20 — Character art, voice and localization pipeline](20_CHARACTER_ART_VOICE_AND_LOCALIZATION_PIPELINE.md)
- [21 — Content Studio for story and quest authors](21_CONTENT_STUDIO_FOR_STORY_AND_QUEST_AUTHORS.md)
- [22 — Story domain API, events and TypeScript](22_STORY_DOMAIN_API_EVENTS_AND_TYPESCRIPT.md)
- [23 — Story schema, RLS, retention and migrations](23_STORY_SCHEMA_RLS_RETENTION_AND_MIGRATIONS.md)
- [24 — Security, content moderation and abuse](24_SECURITY_CONTENT_MODERATION_AND_ABUSE.md)
- [25 — QA, storyline consistency and replay](25_QA_STORYLINE_CONSISTENCY_AND_REPLAY.md)
- [26 — Narrative analytics and author feedback](26_NARRATIVE_ANALYTICS_AND_AUTHOR_FEEDBACK.md)
- [27 — Release slices, dependencies and parallel tickets](27_RELEASE_SLICES_DEPENDENCIES_AND_PARALLEL_TICKETS.md)
- [28 — ADR, traceability, glossary and owner decisions](28_ADR_TRACEABILITY_GLOSSARY_AND_OWNER_DECISIONS.md)

## Supporting machine-readable files
- `../examples/catalog/catalog.draft.json` — feature-gated sample definitions, never production-approved.
- `../examples/schemas/catalog.schema.json` — strict JSON schema for the sample catalog.
- `../examples/tests/pure-rule-vectors.json` — expected pure-rule behavior.
- `../examples/tests/invalid-case-mutations.json` — intentionally invalid content mutation cases.
- `../examples/contracts/api-examples.json` — endpoint and event shapes; not deployed routes.
- `../examples/contracts/domain-reference.ts` — typed rule reference; not integrated runtime code.
- `../examples/sql/schema_draft.sql` — illustrative PostgreSQL design, NOT an approved migration.
- `../tools/validate_batch11.py` — local static validator (requires `jsonschema`).

## Target release policy
Story introduction and one optional quest chain after basic map/player persistence (candidate v0.5.3); branching arcs and simulated rival businesses expand later behind distinct gates.

## Engineer order
1. Freeze character and quest IDs and authored scene graph
2. Implement read-only dialogue and skip/Chronicle
3. Add server-verified quest flags and repeat-safe choice command
4. Integrate one verified story quest/reward handoff
5. Add optional rival challenge and localized voice later

## Acceptance not implied
Schema, fixture and documentation validation do not prove actual game physics solvability, performance, user delight, secure production APIs, compliance or manual UI approval. Those are separate implementation gates.

## Companion document references
- `Batch 01 / docs/11_WORLDS_AND_EVENTS_OVERVIEW.md`
- `Batch 05 / docs/03_GRAPH_DOMAIN_MODEL_AND_INVARIANTS.md`
- `Batch 09 / docs/00_INDEX_AND_README.md`
