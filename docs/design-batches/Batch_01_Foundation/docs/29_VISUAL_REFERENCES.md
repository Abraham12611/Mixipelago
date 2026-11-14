# 29 — Visual References, Mockup Mapping and Production Guardrails

## Two distinct source classes

### 1. `../references/original_screenshots/`

Ten screenshots supplied by the product owner showing an external tropical drink merge game. These establish genre context: portrait UI, beach/backdrop, central wood table, customer order bubbles, score/coin counters, drink evolution row, booster icons, loading/result states and advertised island/renovation progression. **They are NOT approved production assets**. Some are promotional images; do not infer their exact gameplay/UI is already implemented. No source-game title, characters or copyrighted UI fragments should be shipped.

### 2. `../references/generated_concepts/`

Mixipelago exploratory mockups generated in the earlier design discussion. They are a **conceptual visual moodboard**; some are intentionally exuberant and need a cleaner production interpretation. Rebuild each screen in independent React/Phaser elements and original production artwork.

| File | Intended reference | Production translation |
|---|---|---|
| `mixipelago_tropical_merge_island.png` | Brand lockup/hero | Derive separate icon + logo assets; do not embed as one massive splash sprite everywhere |
| `glossy_tropical_mixipelago_logo.png` | Standalone wordmark | Rebuild in scalable/vector or transparent optimized layers; check typography |
| `mixipelago_tropical_paradise_game_screen.png` | Title screen | Simplify art, one strong Play, compact navigation |
| `mixipelago_tropical_merge_adventure.png` | Portrait gameplay concept | Build real interactive scene; remove overdone merge diagram from live board |
| `mixipelago_tropical_merge_game_ui.png` | Desktop gameplay concept | Three-column layout with actual responsive panels |
| `mixipelago_tropical_adventure_map.png` | Island path map | Chunked zoom/pan map with node hitboxes and authored graph |
| `tropical_juice_bar_renovation.png` | Shop upgrades | React shop categories and cards + layered scene assets |
| `mixipelago_tropical_leaderboard.png` | Seasonal leaderboards | Structured ranked list + verified data + privacy controls |

## Art direction interpretation

Extract **style traits**, not identical compositions: bright lagoon/ocean atmosphere, warm wood, fruit-garnished glasses, friendly illustrated UI, shallow soft shadows and 2.5D depth. Make it distinct through disciplined spacing, fewer ornament clusters, restrained purple, original characters and cleaner typography.

## Production asset creation checklist

- Separate backgrounds, props, drinks, character states, particles and panel assets.
- Choose consistent orthographic/light angle for all drink assets.
- All source prompts/AI outputs/paintovers/3D exports tracked with licensing and review.
- Make buttons real interactive controls with focus/disabled/pressed states.
- No clickable interaction baked into flattened screenshot images.
- Ensure small-screen legibility and tested tap zones.
- Check generated mockups for unreadable/impossible typography before creating final vector labels.

## Important disclaimer

Reference images in this documentation pack are for **internal design/engineering understanding**. They are included to help artists and engineers see the mood and proposed screens; licensing/ownership review applies before any production use or public redistribution.
