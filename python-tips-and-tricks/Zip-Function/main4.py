from typing import AsyncGenerator

zipped = [('Mike', 50), ('Bob', 20), ('Anna', 70), ('John', 35)]

names, ages = zip(*zipped)

print(list(names))
print(list(ages))