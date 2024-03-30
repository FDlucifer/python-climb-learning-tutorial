import itertools

i = 0

while True:
    print(i)
    i += 5
    if i == 5000:
        break

for i in range(0, 5000, 5):
    print(i)