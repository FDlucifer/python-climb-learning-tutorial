mynames = ['john', 'mike', 'anna', 'bob', 'sara']

counter = 0
for name in mynames:
    print(f'{counter}: {name}')
    counter += 1

for index, name in enumerate(mynames):
    print(f'{index}: {name}')

print(list(enumerate(mynames)))
print(dict(enumerate(mynames)))