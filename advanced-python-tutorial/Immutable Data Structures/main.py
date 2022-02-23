scientists = [
    {'name': 'Ada Lovelace', 'field': 'math', 'born': 1815, 'nobel': False},
    {'name': 'Emmy Noether', 'field': 'math', 'born': 1882, 'nobel': False},
]

print(scientists)

scientists[0]['name'] = 'lucifer11'

print(scientists)

import collections

Scientists = collections.namedtuple('Scientists', [
    'name',
    'field',
    'born',
    'nobel'
])

luci = Scientists(name='lucifer11', field='computer', born=1997, nobel=False)

print(luci.name)
print(luci.field)
print(luci.born)
print(luci.nobel)

scientists = [
    Scientists(name='lucifer11', field='computer', born=1997, nobel=False),
    Scientists(name='lucifer12', field='fuck', born=1997, nobel=False),
]

from pprint import pprint

pprint(scientists)

del scientists[0]

pprint(scientists)