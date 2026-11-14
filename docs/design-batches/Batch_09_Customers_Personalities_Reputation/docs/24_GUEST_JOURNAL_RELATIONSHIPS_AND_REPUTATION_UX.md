# 24 — Guest Journal, Loyalty and Shop Reputation Screens

**Batch 9 status:** proposal · Not deployed · Cross-batch compatibility required.

## IA extension
Future screens: `Guest Journal` under Player Profile or Shop; `Recurring Guest Detail`; `Shop Reputation`; optional `Feedback History`. The initial v0.4.2 slice only needs a straightforward shop reputation overview and a read-only explanation of recent verified observations. A full guest journal is a later release behind `CUSTOMER_RELATIONSHIPS_ENABLED`.

## Detail screen content
Guest portrait, name, fictional role, island association, favorite recipe tags, relationship tier and threshold progress, earned souvenirs and previous **verified** encounter summaries. Unknown or secret traits stay undisclosed until genuinely discovered. Guest journal should never display the real player's contact list or real location.

## Reputation component
Display reputation separately from prestige and player level: icon, current band, meaning in plain language, a short receipt-backed explanation of the most recent change, and the next known eligible benefit. If an update is pending, label it pending instead of making the progress bar permanent.

## Failure and cross-device
A stale cache may show an older badge until sync, but must not offer fake claimable rewards. Two devices editing privacy options should use revision checks. A deleted or retired guest still has a stable read-only history entry if eligible, with privacy-friendly account deletion flows.

## Accessibility
Text description for relationship meter, screen reader announcements only for confirmed changes, keyboard navigation in desktop cards, and no excessive success/negative audio cues. Reduce motion keeps all content and actions available.
