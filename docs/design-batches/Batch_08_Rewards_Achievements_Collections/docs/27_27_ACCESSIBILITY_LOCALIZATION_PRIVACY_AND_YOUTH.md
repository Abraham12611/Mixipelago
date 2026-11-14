# 27 — Accessibility, Localization, Privacy and Player Protection

**Batch 8 design status:** proposed · not shipped · values and release targets require implementation review.

## Accessibility
Readable achievement requirements, semantic headings, named buttons, complete keyboard navigation, screen-reader status announcements and visible focus indicators. Achievement progress requires numbers and descriptions, never color alone. Collections should have alt descriptions and text-mode item lists independent of gallery art. Reward confirmations must not rely on audible clues.

## Localization
All catalog names, hints, secret spoilers, descriptions and policy explanations use localization keys. Keep numeric values, expiry timestamps and reward quantities outside translated strings. Right-to-left layouts may reorder the list but not the logical rank or progress count. Display UTC windows in user locale with unambiguous dates.

## Privacy
An achievement may reveal sensitive behavior unintentionally (location event, spending habit, social membership). Default profile display to private/unlisted for newly acquired items unless user chooses otherwise. Avoid publishing precise location through 'local champion' trophies; external sharing is opt-in.

## Younger players
No manipulative streak loss threats, obscure loot odds, forced purchases or dangerous social competition. Honor parental controls and age-appropriate reward displays; review platform ratings and legal requirements before adding paid randomness or public social profiles.

## Equity
Limited-time programs should have reasonable windows and no essential power lock. Reduced-motion, low-bandwidth and accessibility modes must not disqualify basic achievements unless the challenge explicitly depends on standardized ranked conditions.
