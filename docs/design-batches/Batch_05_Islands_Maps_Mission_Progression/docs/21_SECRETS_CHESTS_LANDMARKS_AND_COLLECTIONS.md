# 21 — Map Secrets, Treasure, Landmarks and Collectibles

## Content types
`SecretRoute` reveals extra navigable nodes; `TreasureClaim` awards a bounded entitlement once; `ScenicLandmark` provides a lightweight interactive discovery; `CollectionMarker` displays a future Batch 8 acquisition; `GatewayLandmark` starts an island transition.

## First-release philosophy
Teach players one optional branch before adding complex collectibles. The first map release can display one **nonspendable demo treasure** at an optional node and a single hint-based hidden route. Do not introduce a paid currency or unsolved collectathon before the game has a solid puzzle loop.

## Secret definition
A secret has stable `discoveryId`, reveal trigger expression, map location, teaser copy (if rumored), full localized title (after reveal), target node IDs and optional reward-policy reference. Avoid auto-generated secrets that accidentally intersect or hide a mandatory critical path.

## Treasure definition
A chest has `nodeId`, `rewardPolicyId`, `claimScope` (once per player, or future event occurrence), an eligibility expression and `contentVersion`. Preview-only chests use `previewRewardKind` with no ledger. Future real rewards must resolve through backend-controlled approved policies.

## Player experience
Hint → discovery celebration → route highlight → player inspects optional node → completes puzzle or claims treasure → collectible/reward appears in inventory and chronicle when those systems ship. For players who don't care about secrets, mainline still progresses normally.

## UX restrictions
A pre-reveal secret's precise name, reward contents and coordinates must not be sent to public clients if meant to remain hidden. Render only public placeholder metadata. After reveal, use accessible labels and simple animations. `Claim` remains disabled during pending transaction; pressing it twice has exactly-once outcome.

## QA
Reveal condition exactly once, delayed animation recoverable, chests cannot be claimed by tampering node IDs, expired events don't strand players, secret route isn't a hidden mandatory bridge, and post-update claims aren't lost.
