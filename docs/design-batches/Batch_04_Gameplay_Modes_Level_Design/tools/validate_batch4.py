#!/usr/bin/env python3
"""Batch 4 offline content & pure-rule validator.
This script does NOT execute Rapier physics, prove mission solvability, or test UI.
Requires: pip install jsonschema
Run: python tools/validate_batch4.py
"""
from pathlib import Path
import json, math, sys, hashlib
from decimal import Decimal, ROUND_HALF_UP
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=json.loads((ROOT/'examples/schemas/mission.schema.json').read_text())
SCORES={1:10,2:25,3:60,4:140,5:320,6:720,7:1600,8:3500}
ERRORS=[]


def err(context,message): ERRORS.append(f'{context}: {message}')

def find_primary(obj):
    if obj.get('schemaVersion')==1:
        goal=obj['goal'];return {'type':goal['type'],'target':goal['count']}
    return obj['objectives']['primary']

def check_obj(obj,context):
    if obj.get('type') in {'allOf','anyOf','sequence'}:
        for k,ch in enumerate(obj['children']): check_obj(ch,f'{context}.children[{k}]')
        return
    if obj['type']=='produce_tier' and obj['tier']==1:
        err(context,'tier 1 is not naturally created by a pair merge in alpha')

def check_mission(p):
    m=json.loads(p.read_text())
    label=str(p.relative_to(ROOT))
    for e in sorted(Draft202012Validator(SCHEMA).iter_errors(m),key=lambda e:list(map(str,e.path))):
        err(label,f'JSON Schema: {"/".join(map(str,e.path))}: {e.message}')
    if any(x.startswith(label+': JSON Schema') for x in ERRORS): return
    b=m['board']; width=b['width']; height=b['height']; line=b['dangerLineY']
    if not 0<line<height:err(label,'dangerLineY must be strictly inside board')
    if not b['startingDrinks'] and not m['spawn']['firstItems'] and not m['spawn']['pool']:err(label,'no accessible drinks')
    if len(b['startingDrinks'])>b['maxActiveDrinks']:err(label,'starting body count exceeds maxActiveDrinks')
    for i,body in enumerate(b['startingDrinks']):
        if not (0.34<=body['x']<=width-0.34 and 0.34<=body['y']<=height-0.34):
            err(label,f'startingDrinks[{i}] outside usable collider bounds')
    # Approximate spawn overlap only, not a full rigid-body test.
    for i,a in enumerate(b['startingDrinks']):
        for j,bb in enumerate(b['startingDrinks'][i+1:],i+1):
            if (a['x']-bb['x'])**2+(a['y']-bb['y'])**2 < (2*0.34*0.99)**2:
                err(label,f'initial drinks {i},{j} overlap nominal colliders')
    spawn=m['spawn']
    if not spawn['firstItems'] and not spawn['pool']:err(label,'spawn has neither authored queue nor weighted pool')
    if 'orders' in m:
        orders=m['orders'];ids=[o['id'] for o in orders['initial']]
        if len(ids)!=len(set(ids)):err(label,'duplicate order IDs')
        if len(ids)>orders['maxVisible']:err(label,'initial order count exceeds maxVisible')
        if m['mode']=='service' and m['schemaVersion']==1 and not orders['initial']:
            err(label,'v1 service must have initial orders')
    if m['schemaVersion']==2:
        if m['releaseStatus']=='live':err(label,'sample v2 mode published as live without implementation/replay evidence')
        if not m.get('featureFlag'):err(label,'draft mode has no feature gate')
        check_obj(find_primary(m),label)
        t=m.get('clock');budget=m.get('budget',{})
        if m['mode']=='rush_hour' and not t:err(label,'rush hour needs active-tick clock')
        if m['mode']=='precision' and 'shotsMax' not in budget:err(label,'precision needs shotsMax')
        if m['mode']=='survival' and not m.get('waves'):err(label,'survival needs waves')
        if m['mode']=='endless' and m['rewards']['previewCoins']!=0:err(label,'endless preview reward should be zero in sandbox draft')
        stars=m.get('starCriteria',{})
        if 'two' in stars and 'three' in stars:
            a=stars['two'];c=stars['three']
            if a['kind']==c['kind']:
                if a['kind'] in {'shots_at_most','active_ticks_at_most'} and c['value']>a['value']:
                    err(label,'three-star threshold weaker than two-star threshold')
                if a['kind']=='score_at_least' and c['value']<a['value']:
                    err(label,'three-star score lower than two-star score')
            if a['kind']=='shots_at_most' and 'shotsMax' in budget and a['value']>budget['shotsMax']:
                err(label,'two-star shots threshold above shots budget')
        if m['mode']=='vip_service' and not m.get('orders',{}).get('orderLines'):
            err(label,'vip draft missing future orderLines')
    return m

def halfup(v):return int(Decimal(str(v)).quantize(Decimal('1'),rounding=ROUND_HALF_UP))

def pure_vector(v):
    ins=v['inputs'];k=v['kind'];expect=v['expected']
    if k=='tier_merge':
        a,b=ins['a'],ins['b'];out=a+1 if a==b and 1<=a<8 else None
        got={'outputTier':out,'baseScore':SCORES[out] if out else 0}
    elif k=='chain_score':
        factor=min(3,1+.25*max(0,ins['depth']-1))
        got={'mergePoints':halfup(SCORES[ins['outputTier']]*factor)}
    elif k=='orders_served':
        got={'count':len({e['id'] for e in ins['events'] if e['kind']=='order_fulfilled'})}
    elif k=='terminal_priority':
        if ins['goalComplete']:got={'status':'won','reason':'goal_completed'}
        elif ins['dangerExpired']:got={'status':'lost','reason':'danger'}
        elif ins['shotsExpired']:got={'status':'lost','reason':'shots_exhausted'}
        elif ins['timerExpired']:got={'status':'lost','reason':'timed_out'}
        else:got={'status':'running','reason':'none'}
    elif k=='timer':got={'remainingTicks':max(0,ins['limitTicks']-ins['activeTicks'])}
    elif k=='shots':
        n=sum(1 for x in ins['committed'] if x)
        got={'shotsFired':n,'remainingShots':max(0,ins['maxShots']-n)}
    elif k=='preview_coins':
        seen=set();reward=0
        for oid,coins in zip(ins['uniqueOrderIds'],ins['orderRewards']):
            if oid in seen:continue
            seen.add(oid);reward+=coins
        got={'orderPreviewCoins':reward,'missionPreviewCoins':ins['missionBonus'],'total':reward+ins['missionBonus']}
    elif k=='objective':
        got={'count':sum(1 for t in ins['producedTiers'] if t==ins['tier'])}
    else:raise ValueError('unknown vector type '+k)
    if got!=expect:err(v['id'],f'expected {expect!r}, computed {got!r}')


def main():
    Draft202012Validator.check_schema(SCHEMA)
    missions=list(sorted((ROOT/'examples/missions').glob('*.json')))
    for p in missions:check_mission(p)
    vectors=json.loads((ROOT/'examples/tests/objective-rule-vectors.json').read_text())['vectors']
    for v in vectors:pure_vector(v)
    # Verify copied previous fixture byte-level if source is installed adjacent; portability-safe otherwise.
    prior=Path('/mnt/data/Mixipelago_Batch_03_Drinks_Recipes_Discovery/examples/missions/coconut-cove-001.json')
    if prior.exists() and prior.read_bytes()!=(ROOT/'examples/missions/coconut-cove-001.json').read_bytes():
        err('coconut-cove-001','does not match Batch 3 source bytes')
    docfiles=list((ROOT/'docs').glob('*.md'))
    if len(docfiles)!=39:err('docs',f'expected 39 chapters including index, found {len(docfiles)}')
    for p in docfiles:
        if len(p.read_text().strip())<800:err(str(p.name),'suspiciously short chapter')
    if ERRORS:
        print('FAIL —',len(ERRORS),'validation issues')
        for e in ERRORS:print(' -',e)
        return 1
    print(f'PASS — {len(missions)} mission samples, {len(vectors)} rule vectors, {len(docfiles)} chapters; structural and pure logic checks only')
    print('NOTE: No Rapier simulation, winning replay, manual UI test, API test or release deployment was performed.')
    return 0
if __name__=='__main__':sys.exit(main())
