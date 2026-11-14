# 14 — Customer Reviews, Complaints and Service Recovery

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Framing
Reviews are fictional in-world feedback, not reviews posted on real app stores. Their goal is to communicate player actions and shop identity, not add opaque punishment. Complaint content should point to an explicit game rule and allow recovery through ordinary gameplay.

## Triggers
`service_completed`, `published_optional_challenge_failed`, `verified_shop_event_resolved`; each has a named review template and policy. A missed visual interaction or lost browser session cannot count as a review-worthy failure. A customer can submit one review per eligible encounter, resolved by deterministic policy rather than generated text from sensitive player data.

## Example resolution loop
1. Player completes verified mission; satisfaction observation recorded.
2. Feedback service chooses localized template for that observation band.
3. UI shows one short quote with `What's counted` details and optional `Try another service` action.
4. Service recovery mission is authored in Batch 4/5, optional and solvable without payment.
5. Completed recovery produces a new independent receipt; no rewriting the old observation.

## Moderation and content authoring
Human-authored review templates are versioned, safe for a broad audience and translated. Avoid mockery, body-shaming, classism or fake threats. The player can mute repetitive feedback. A simulated critic's dramatic voice line has no authoritative effect unless paired with an explicit declared reward policy.

## Scope
First trusted reputation slice can ship without review feed. Reviews and complaint recovery are future opt-in content modules and must not block core merging.
