dict1 = {'a': 1, 'b': 7}
dict2 = {'b': 4, 'c': 8}

# update

dict2.update(dict1)
print(dict2)

dict3 = {**dict1, **dict2}
print(dict3)

dict3 = dict(dict1.items() | dict2.items())
print(dict3)