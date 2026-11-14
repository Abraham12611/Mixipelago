#!/usr/bin/env python3
"""Static catalog/schema and pure-rule vectors. No live backend, device or physics proof."""
from pathlib import Path
import json, copy, sys
import jsonschema  # pip install jsonschema
ROOT = Path(__file__).resolve().parents[1]
BATCH = 18

def evaluator(num, rule, x):
 if num==16:
  ids=['citrus-shot','sunny-lemon','sunset-splash','blossom-fizz','coral-martini','mint-lagoon','ocean-cloud','crown-of-isles']
  if rule=='tier_id':return ids[x['tier']-1] if 1<=x['tier']<=8 else None
  if rule=='fallback':return 'rendered-asset' if x['available'] else 'ui.drink.labeled-placeholder'
  if rule=='cosmetic_affects_physics':return False
 if num==17:
  if rule=='play':return x['unlocked'] and x['voices']<x['limit'] and x['eventId'] not in x['seen']
  if rule=='gain':return round(min(1.0,max(0.0,x['master']))*min(1.0,max(0.0,x['bus'])),4)
 if num==18:
  if rule=='grant':return x['verified'] and not x['alreadyGranted'] and not x['preview']
  if rule=='actor':return bool(x['tokenActor']) and x['tokenActor']==x['resourceOwner']
 if num==19:
  if rule=='permission':return bool(x['actor']) and (x['owner']==x['actor'] or x['isAdmin'])
  if rule=='proof':return x['signed'] and x['pinned'] and x['normalized']
 if num==20:
  if rule=='purchase':return all([x['featureOn'],x['providerVerified'],x['skuPublished']])
  if rule in ('ranked_paid_effect','ads_mandatory'):return False
 if num==21:
  if rule=='quality':return 'low' if x['ramMiB']<2500 or x['gpuBudgetMiB']<64 else ('high' if x['ramMiB']>=5000 and x['gpuBudgetMiB']>=160 else 'mid')
  if rule=='offline_verified':return False
  if rule=='requires_update':return x['clientSchema']<x['minSchema']
 raise ValueError((num,rule,x))


def load(path): return json.loads((ROOT/path).read_text(encoding='utf-8'))
def validate(cat):
    key = {16:'assets',17:'cues',18:'endpoints',19:'threats',20:'offers',21:'devices'}[BATCH]
    if cat.get('batch') != BATCH: return False
    if cat.get('productionReady') is not False or cat.get('gateEnabled') is not False: return False
    if cat.get('status') != 'draft' or not cat.get('catalogVersion'): return False
    if not isinstance(cat.get(key),list) or len(cat[key]) < 5: return False
    ids=[x.get('id') for x in cat[key]]
    if any(not isinstance(x,str) or not x for x in ids) or len(ids)!=len(set(ids)): return False
    if BATCH == 16:
        if [x.get('tier') for x in cat[key]] != list(range(1,9)): return False
        if any(x.get('licenseState')=='approved' or x.get('available') for x in cat[key]): return False
    if BATCH == 17 and any(x.get('maxVoices',0)<=0 or x.get('rightsState')=='approved' for x in cat[key]): return False
    if BATCH == 18 and any(x.get('method') in ('POST','PATCH','PUT','DELETE') and not x.get('idempotencyRequired') for x in cat[key]): return False
    if BATCH == 20 and (any(x.get('enabled') for x in cat[key]) or cat['ads']['enabled'] or cat['paidRandomRewards']['enabled']): return False
    if BATCH == 21 and (any(x.get('supported') for x in cat[key]) or cat['nativeLaunchEnabled']): return False
    return True

def main():
    cat=load('examples/catalog/catalog.draft.json')
    schema=load('examples/schemas/catalog.schema.json')
    assert schema['properties']['batch']['const']==BATCH
    jsonschema.validate(cat,schema)
    assert validate(cat), 'Draft catalog invalid'
    vectors=load('examples/tests/pure-rule-vectors.json')['vectors']
    for idx,t in enumerate(vectors):
       got=evaluator(BATCH,t['rule'],t['input'])
       assert got==t['expected'], f'vector {idx}: {got!r} != {t["expected"]!r}'
    bad=load('examples/tests/invalid-case-mutations.json')['mutations']
    key={16:'assets',17:'cues',18:'endpoints',19:'threats',20:'offers',21:'devices'}[BATCH]
    for case in bad:
       altered=copy.deepcopy(cat)
       kind=case['kind']
       if kind=='duplicate-id': altered[key].append(copy.deepcopy(altered[key][0]))
       elif kind=='enable-production': altered['gateEnabled']=True
       elif kind=='wrong-batch': altered['batch']=999
       elif kind=='missing-id': altered[key][0].pop('id',None)
       else: raise AssertionError(f'unknown mutation {kind}')
       try:
           jsonschema.validate(altered,schema)
           schema_pass=True
       except jsonschema.ValidationError:
           schema_pass=False
       assert not (schema_pass and validate(altered)), f'mutation incorrectly accepted: {kind}'
    print(f'PASS batch {BATCH}: catalog, {len(vectors)} rule vectors, {len(bad)} invalid mutations')

if __name__=='__main__': main()
