# 26 — Dialogue System, Voice, Sound Effects and Localization

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## Content-first dialogue
Use authored, versioned lines keyed by customer, situation, tone and locale. Optional variations are selected with deterministic seeded index for replayable sessions. No expensive LLM call is required per merge or customer arrival; live AI dialogue is a separate later experiment with moderation, privacy and cost controls.

## Audio design
Each segment shares short sound families (`guest.arrive`, `guest.order`, `guest.served`, `guest.celebrate`); unique voice lines are optional. Source sounds can be recorded or designed through ElevenLabs/WeLoveIndies workflows with documented commercial licenses. Runtime Web Audio/Howler mixes SFX under explicit concurrency budget so 10 chained merges do not trigger overlapping long dialogue.

## Dialogue metadata
`lineId`, `locale`, `speakerId`, `situation`, `allowedStates`, `subtitle`, `audioAssetId?`, `estimatedDurationMs`, `pronunciationNotes?`, `contentRating`, `version`. Subtitles are mandatory when voice is present, and text-only mode must remain complete. Fall back to authored English if localization missing; don't show untranslated internal keys.

## Writing rules
Give each guest a distinct tone without forcing long unskippable scenes during a fast puzzle. Avoid real-world cultural caricature and personal finance judgment. Keep lines short enough for small mobile order cards; longer character stories belong to future quest dialogue views.

## Acceptance
Voice off, SFX off, reduced motion, restart during dialogue, language switch mid-menu, missing audio file, quick successive orders, and screen-reader alternative must all work without changing gameplay event order.
