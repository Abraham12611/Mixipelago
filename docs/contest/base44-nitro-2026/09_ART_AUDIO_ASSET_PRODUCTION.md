# 09 — Original Art, Audio and Asset Production

## Art direction

Mixipelago's look is **illustrated tropical 2.5D**, not a copy of any referenced merge game's screenshots. Warm dawn sunlight, soft sand and turquoise ocean, readable glass silhouettes, cheerful fictional customers and calm tropical signage. Motion is anchored to contact clarity rather than fireworks.

## Initial asset inventory

| Asset family | Approximate deliverables | QA |
|---|---:|---|
| Eight drink tiers | 8 game sprites, 8 HUD/order icons, shared shadows | distinguishable at 40–64px |
| Coconut Cove island | 1 map scene, 3 chapter variations, mission markers | scalable mobile and desktop |
| Game board | 1 table base, rail effects, launcher/aim arrow, danger line | consistent hit testing |
| Customer portraits | 3–4 original portraits + 2 expressions each | original silhouettes, alt labels |
| Interface | logo/wordmark, buttons, bars, panels, states | readable contrast |
| FX | merge/splash/combo/serve/win/loss, limited particles | respects reduced motion |
| SFX | shot, slide, bump, merge per family, serve, menu, win, lose | no clipping, mute |
| Music | 1 original looping ambient theme, optional finale variation | nonintrusive, rights verified |
| Promotional | square cover, widescreen banner, authentic screenshots/clip | no misleading claims |

Treat counts as **production estimates**, not evidence of existing assets.

## Render pipeline

1. Author sketches and style board; get owner approval of direction.
2. Produce **original** vector/paint/3D masters or compliant AI-generated assets.
3. Export transparent sprites or WebP/PNG in predictable view angle; atlas for related frames.
4. Assign immutable asset IDs; include dimensions, checksum, licence and safe origin.
5. Provide lower-resolution mobile assets and browser fallbacks; avoid giant uncompressed sprite atlases.
6. Validate visible sprite center against intended stable circular collider; do not change physics radius from image canvas.
7. Check color blindness, silhouette reading, overlap depth ordering and compression artifacts.
8. Verify original music/SFX licensing including contest promotional usage.

## Audio system

- Separate buses: master, music, SFX, ambient. Persist volume locally.
- Play sounds only from semantic gameplay events (merge/serve/win); dedupe events by unique ID.
- Browser autoplay restrictions: start AudioContext/resume only after user gesture.
- Simultaneous impacts: polyphony cap and mix ducking to prevent clipping.
- Hide audio controls only if audio truly unavailable; visuals carry equivalent meaning.

## Rights approval

All final files need creator/tool, date, licence terms, origin file, sha256 and owner signoff. Reject copied screenshot crops, game logos, unlicensed recorded tracks or recognizable fictional media characters.

## Production priority

Get the board, eight drinks, launcher, orders and result UI right **before** expanding backgrounds. If schedule is tight, use fewer original portraits, one music loop, and modular original FX.
