# 20 — Player Identity, Reputation and Shop Effects

**Batch 7 design status:** proposed · Not shipped · Interfaces and tuning subject to owner approval.

## Orthogonal systems
Player RPG level is not a direct proxy for shop prestige, customer satisfaction or franchise value. Higher level permits *eligibility*, while business investments and event outcomes determine shop-specific state.

## Integration examples
- Hospitality skill `hp_warm_welcome` adds a bounded trusted tip multiplier only when the served order is eligible under Batch 6 and verified by its Order/Customer Director.
- Business skill `bg_smart_purchase` changes the **quote** for a subsequent eligible upgrade, not an already-settled invoice.
- Risk skill `rs_insurance_reader` shows policy explanations but cannot purchase a policy automatically.
- Player specialization badge may appear in a friend profile; competitive rank is separately computed from score.

## Consistency and atomicity
A shop transaction records modifier snapshot/cost quote version as part of its source receipt. Switching shops mid-purchase invalidates a stale quote. An expired temporary buff cannot be resurrected by replaying a saved client snapshot. Shop ownership validation precedes skill modifier evaluation.

## Conflict resolver
`skill source → typed modifier → Batch 6 calculation engine → capped trusted result`; the skill service does not duplicate the finance rules. Content leadership resolves cross-domain numeric disagreements in an ADR and a single published rules catalog.
