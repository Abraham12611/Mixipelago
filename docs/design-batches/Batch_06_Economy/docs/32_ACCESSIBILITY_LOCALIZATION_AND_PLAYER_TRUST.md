# 32 — Accessibility, Localization and Player Trust

**Status:** Batch 6 design/engineering handoff · 2026-11-14 · Proposed, not shipped.

## Accessibility
Never communicate currency or purchase success by color alone. Every statistic and price needs a text label, keyboard access, adequate contrast, touch targets, and localization-safe layout. Announce wallet changes to assistive tech without spamming; respect reduced motion and muted sound.

## Currency disclosure
Say `Coins` and show an in-game icon. Avoid representations that could imply the coins have withdrawable monetary value. Transaction history should clarify earned, spent and compensated, with source and timestamp. If refunds/ads/real money are introduced later, clearly separate commerce receipts from soft-currency ledger.

## Localization
Store integers, not formatted numeric strings. Format numbers and pluralizations by locale. Percent effects state whether they mean percentage points versus relative percentages. Don't imply 1,000 coins in a comma-decimal locale means one coin.

## Well-being
Avoid FOMO-based automatic loss, destructive inactivity debt, aggressive loss aversion and misleading 'free' labels. Events with deadlines must offer paths that respect play schedules. Make opt-in regional social comparisons privacy-preserving.
