from functools import reduce
import collections

from attr import field

Scientists = collections.namedtuple('Scientists', [
    'name',
    'field',
    'born',
    'nobel'
])

scientists = [
    Scientists(name='lucifer11', field='computer', born=1997, nobel=True),
    Scientists(name='lucifer12', field='fuck1', born=1883, nobel=False),
    Scientists(name='lucifer13', field='fuck2', born=2000, nobel=True),
    Scientists(name='lucifer14', field='fuck3', born=2001, nobel=False),
    Scientists(name='lucifer15', field='fuck4', born=2002, nobel=True),
    Scientists(name='lucifer16', field='fuck5', born=2003, nobel=False),
]

from pprint import pprint

pprint(scientists)

names_and_ages = tuple(map(lambda x: {'name': x.name, 'age': 2022 - x.born}, scientists))
pprint(names_and_ages)

total_age = reduce(lambda acc, val: acc + val['age'], names_and_ages, 0)
print(total_age)
print(sum(x['age'] for x in names_and_ages))

def reducer(acc, val):
    acc[val.field].append(val.name)
    return acc

scientists_by_field = reduce(
    reducer,
    scientists,
    {'computer': [], 'fuck1': [], 'fuck2': [], 'fuck3': [], 'fuck4': [], 'fuck5': []}
)

pprint(scientists_by_field)

import collections

scientists_by_field1 = reduce(
    reducer,
    scientists,
    collections.defaultdict(list)
)

pprint(scientists_by_field1)

import functools

scientists_by_field2 = functools.reduce(
    lambda acc, val: {**acc, **{val.field: acc[val.field] + [val.name]}},
    scientists,
    {'computer': [], 'fuck1': [], 'fuck2': [], 'fuck3': [], 'fuck4': [], 'fuck5': []}
)

pprint(scientists_by_field2)

