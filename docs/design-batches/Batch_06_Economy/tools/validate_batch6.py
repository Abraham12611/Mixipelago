#!/usr/bin/env python3
"""Batch 6 static demo verification. Does NOT test real database writes or gameplay."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def load(p): return json.loads((root/p).read_text())
cat=load('examples/catalog/economy-catalog.draft.json'); schema=load('examples/schemas/economy-catalog.schema.json'); tests=load('examples/tests/economy-rule-vectors.json'); rewards=load('examples/catalog/reward-policies.draft.json')
try:
 import jsonschema
 jsonschema.validate(cat,schema)
except ImportError:
 assert schema['properties']['schemaVersion']['const']==cat['schemaVersion']
 print('jsonschema not installed; basic invariant checks only')
ids=[u['id'] for u in cat['upgrades']]
assert len(ids)==len(set(ids))
for u in cat['upgrades']:
 assert len(u['levels'])==u['maxLevel']
 assert all(lev['level']==n for n,lev in enumerate(u['levels'],1))
 assert all(lev['priceCoins']>=0 for lev in u['levels'])
 assert not (u['cosmeticOnly'] and any(lev['effect'] for lev in u['levels']))
 assert set(u['requires']).issubset(ids)
for t in tests['prices']:
 price=max(t['minPrice'],(t['base']*(10000-t['discountBps']))//10000)
 assert price==t['expected'],('pricing',t,price)
for t in tests['wallet']:
 assert (t['balance']>=t['cost'])==t['expected']
for t in tests['vipChance']:
 assert min(t['capBps'],t['baseBps']+sum(t['bonusBps']))==t['expected']
for t in tests['idempotency']:
 got='REPLAY_RECEIPT' if t['sameActor'] and t['sameKey'] and t['sameFingerprint'] else 'IDEMPOTENCY_CONFLICT'
 assert got==t['expected']
assert all(p['requiresVerifiedReceipt'] for p in rewards['policies'])
assert all(p.get('replayCoins',0)==0 for p in rewards['policies'])
print(f"PASS: {len(ids)} draft upgrades; {sum(len(v) for v in tests.values() if isinstance(v,list))} rule vectors; reward policy invariants")
