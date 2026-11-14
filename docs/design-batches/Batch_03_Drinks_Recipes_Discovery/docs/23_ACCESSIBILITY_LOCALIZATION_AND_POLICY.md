# 23 — Accessibility, Localization, Age Suitability and Asset Rights

## Accessibility is part of the core design

Color must not be the only way to distinguish tiers. Each drink uses a unique silhouette and a readable number/label in accessible HUD, with high-contrast customer order mini-icons. Avoid revealing 'matching' only through colored glow. Provide mouse, touch and keyboard equivalents for aiming/launching where practicable.

## Controls and feedback

Offer reduced motion; allow disabling excessive shakes/sparkles; separate music and SFX volume controls; don't require sound to detect success. Collision/merge events should have optional lightweight non-auditory confirmation (sparkle/brief label). Screen reader users should be able to navigate menus and hear status text for selected drink, order requirements, next item, score and state. A fast physics board may require an alternative assisted interaction path whose achievable accessibility is evaluated honestly.

## Sprite clarity

Minimum HUD icon targets should be readable at realistic mobile sizes and under common color-vision deficiencies. Use distinct rims/containers and icon shape cues. Offer `highContrastDrinkOutline` presentation mode without changing collider or score. Support a 'simplify effects' mode for photosensitivity and performance.

## Localization contract

Store `nameKey`/description keys; never write localized display names into session events or database IDs. Prepare for languages with long words, RTL layout (menus), locale-specific number/decimal formats and currency labels. Keep drink titles short enough for tiny HUD icons; long names use ellipsis with accessible full label. Runtime string changes may ship separately from gameplay version.

## Age and content policy

The title is a family-friendly drinks-merging game. The catalog should favor mocktails, juices, smoothies, sodas, teas and fantastical nonalcoholic drinks. 'Martini' can describe a glass silhouette but marketing and art should avoid suggesting drinking alcohol is a reward for children. Review age-rating criteria and regional store requirements before publishing native apps. No real gambling or tradable randomized prize mechanics should be introduced casually.

## Rights and provenance

All generated/commissioned audio, artwork, ingredient photos, 3D models and fonts require license/provenance records and commercial-use validation. Inspirations from Merge Shooter may influence genre and aesthetic direction, but do not reuse copyrighted game art, UI screenshots, logos, characters or audio as production assets. Preserve creator credits where licenses require them. Never distribute licensed font files via public documentation packs unless permitted.

## Consent and social disclosure

Recipe album and player showcase visibility must be optional. No precision location needed for recipe features. Avoid revealing private player usernames in shareable debug logs. Account deletion should remove user-owned progression according to the applicable privacy policy while retaining only minimal legally justified aggregated records.

## Acceptance

QA verifies reduced-motion flows, focus order, touch sizing, alternate labels, noncolor distinction, translated overflow, missing font fallback, text embedded in artwork avoidance, and ownership/license metadata for each published asset.
