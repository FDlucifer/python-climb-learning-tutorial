import collections

from matplotlib.pyplot import sci

Scientists = collections.namedtuple('Scientists', [
    'name',
    'field',
    'born',
    'nobel'
])

scientists = [
    Scientists(name='lucifer11', field='computer', born=1997, nobel=True),
    Scientists(name='lucifer12', field='fuck1', born=1997, nobel=False),
    Scientists(name='lucifer13', field='fuck2', born=2000, nobel=True),
    Scientists(name='lucifer14', field='fuck3', born=2001, nobel=False),
    Scientists(name='lucifer15', field='fuck4', born=2002, nobel=True),
    Scientists(name='lucifer16', field='fuck5', born=2003, nobel=False),
]

from pprint import pprint

pprint(scientists)

names_and_ages = tuple(map(lambda x: {'name': x.name, 'age': 2022 - x.born}, scientists))

pprint(names_and_ages)
pprint(tuple({'name': x.name.upper(), 'age': 2022 - x.born} for x in scientists))