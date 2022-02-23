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

fs = filter(lambda x: x.nobel is True, scientists)
print(next(fs))
print(next(fs))
print(next(fs))

pprint(tuple(filter(lambda x: x.nobel is True, scientists)))
pprint(tuple(filter(lambda x: x.field == 'computer' and x.nobel, scientists)))

for x in scientists:
    if x.nobel is True:
        print(x)

def nobel_filter(x):
    return x.nobel is True

pprint(tuple(filter(nobel_filter, scientists)))
pprint(tuple([x for x in scientists if x.nobel is True]))