# 25 — Accessibility, Privacy, Originality and Distribution Considerations

## Scope and principles

A game can be visually rich and still accessible. Browser launch must work without invasive tracking, location access or account requirements. Legal/platform policies are region-dependent; do separate legal review when native stores, minors, commerce and geographic rankings launch.

## Input and accessibility

- Touch/mouse are primary controls, but design keyboard aiming/launch alternative.
- Support visual aim guide, not only sound, to teach trajectories.
- Text size and high contrast on cream/light panels; aim for WCAG-relevant standards for DOM UI.
- Distinguish drinks by shape/garnish/pattern/tier label in addition to color.
- Separate SFX/music mute sliders, captions/text indicators for important sound cues.
- `prefers-reduced-motion`: shorten or remove excessive particle bursts, avoid unneeded camera shake and strobe.
- Pause or reduce input prompts on background, respect screen reader focus for modals.
- Touch targets ~44 CSS pixels when feasible; test small screens.
- Tutorial can be replayed, help available outside game, avoid unwinnable state from poor accessibility.

## Privacy

- Alpha local profile: no real name/email or precise location needed.
- Analytics: minimal events, pseudonymous identifiers, privacy/retention controls.
- Authentication later: account export, deletion and linked identity workflows as required.
- Leaderboards: optional geographic participation; display selected coarse region, not street/lat-long.
- Social: blocks/reports, profile visibility and moderation; no unrestricted user chat by default.
- If children are targeted/allowed, research applicable child privacy and store rules before launch.

## Content and original IP

- Treat provided third-party game screenshots as **design reference only**.
- Never ship borrowed character images, logo, UI screenshots, music or sound from reference game.
- Generated image/3D/audio outputs need source/licensing metadata and human review.
- Avoid close copies of recognizable trademarked titles and distinctive assets.
- Focus on tropical juice/mocktail theme by default; if portraying alcohol, ratings and policy may change.

## Monetization principles (future)

- No paid gambling mechanisms, real-money prize claims or hidden odds without legal/product review.
- Ranked contests favor equal equipment and fair verification.
- Transparent virtual currency purpose and expiration rules.
- Avoid high-pressure pay-to-continue loops and disasters designed to force spending.
- Purchases/ads must align with app store policies, parental controls and age ratings.

## Native release prerequisites

Privacy policy and terms, permissions manifest, account deletion, data safety labels, App Store/Play Store metadata and screenshots, accessibility/interaction testing, platform purchase policies, crash monitoring, mobile app lifecycle behavior, device-level performance. Web delivery does not automatically guarantee native approval.
