# 36 — Customer Content Studio: Authoring and Publish Gates

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Admin capabilities
Manage customer definitions, fictional traits, segment membership, localized dialogue, portrait manifest, favorite recipe tags, region eligibility, weighted pools, optional VIP contracts, satisfaction/reputation policy versions and safe fallbacks. Every publishable entity has a preview, validation report and audit history.

## Workflow
Author draft -> validate references (mission, recipe, asset, locale) -> generate seeded preview distribution -> test feasibility and cap policy -> accessibility/content review -> staging with selected mission fixtures -> owner manual UI review -> publish immutable hash -> monitor -> rollback gate if needed.

## Required editor warnings
- An order target has no enabled recipe in linked mission.
- A VIP/critic can be selected in a tutorial or ranked standardized mode.
- Pool weights are missing, negative or result in no eligible guest.
- A customer portrait/dialogue has missing locale fallback or commercial license metadata.
- Two customer definitions share ID across incompatible identities.
- Timers active in an alpha/no-timer mission.

## RBAC and audit
Content editors may create drafts but cannot self-credit economic rewards or skip required approval for high-value policies. Distinguish content author, reviewer, publisher and finance/operations permissions; record who approved changes. Publishing should be atomic per manifest version and reversible for future encounters without rewriting settled history.

## Pilot scope
First tools can be JSON+schema with a CLI validator and a tiny internal React preview screen. A full drag-and-drop customer editor should wait until recurring character production volume justifies it.
