#!/usr/bin/env python3
"""Static Batch 8 content and pure-rule validation. Does NOT test live game/DB."""
import json, pathlib, datetime, collections, sys
root=pathlib.Path(__file__).resolve().parents[1]
def load(s): return json.loads((root/s).read_text())
cat=load('examples/catalog/reward-catalog.draft.json')
vec=load('examples/tests/reward-rule-vectors.json')
sch=load('examples/schemas/reward-catalog.schema.json')
try:
 import jsonschema
 jsonschema.Draft202012Validator.check_schema(sch)
 jsonschema.validate(cat,sch)
except ImportError:
 print('NOTICE: jsonschema missing; structural checks only. pip install jsonschema')
if cat['status']!='draft': raise AssertionError('sample catalog must stay draft')
for key in ('achievements','items','rewardPolicies','albums','chests'):
 ids=[x['id'] for x in cat[key]]
 assert len(ids)==len(set(ids)),f'duplicate {key} IDs'
items={x['id'] for x in cat['items']}; policies={x['id'] for x in cat['rewardPolicies']}
for a in cat['achievements']:
 assert a['rewardPolicyId'] in policies
 r=a['rule']; assert r['kind'] in ('distinct_count','milestone')
 if r['kind']=='distinct_count': assert r.get('threshold',0)>0 and r.get('counter')
 else: assert r.get('key')
for p in cat['rewardPolicies']:
 for r in p['rewards']: assert r['itemId'] in items and r['quantity']>0
for album in cat['albums']:
 for item in album['items']: assert item in items
 for milestone in album['milestones']:
  assert milestone['rewardPolicyId'] in policies and milestone['count']<=len(album['items'])
for chest in cat['chests']:
 assert chest['rewardPolicyId'] in policies
 if chest['type']=='weighted':
  assert sum(a['weight'] for a in chest['odds'])==10000
  assert all(a['itemId'] in items for a in chest['odds'])
for x in vec['counterCases']: assert len(set(x['sourceIds']))==x['expected']
for x in vec['thresholdCases']:
 res=[t for t in sorted(set(x['thresholds'])) if x['from']<t<=x['to']]
 assert res==x['expected']
for x in vec['albumCases']:
 owned=len(set(x['eligible']).intersection(x['owned']))
 assert owned==x['expectedOwned'] and round(100*owned/len(set(x['eligible'])))==x['expectedPercent']
for x in vec['claimCases']: assert (x['sourceKey'] not in x['previous'])==x['expectedCanGrant']
for x in vec['utcDayCases']:
 day=datetime.datetime.fromisoformat(x['iso'].replace('Z','+00:00')).astimezone(datetime.timezone.utc).date().isoformat()
 assert day==x['expected']
for x in vec['oddsCases']:
 assert (x['expectedTotal']==10000)==x['valid']
 assert sum(x['weights'])==x['expectedTotal']
for p in (root/'docs').glob('*.md'):
 for link in __import__('re').findall(r'\]\(([^)#]+)(?:#[^)]*)?\)',p.read_text()):
  if '://' not in link and not link.startswith('#') and not (p.parent/link).exists():
   raise AssertionError(f'broken link {p}: {link}')
assert len(list((root/'docs').glob('*.md')))==45
print('PASS: 44 chapters + index, JSON schema (when installed), catalog and', sum(len(x) for x in vec.values()),'pure rule vectors')
print('Candidate artifacts:',len(cat['achievements']),'achievements,',len(cat['items']),'items,',len(cat['albums']),'albums,',len(cat['rewardPolicies']),'policies; all sample content remains draft')
