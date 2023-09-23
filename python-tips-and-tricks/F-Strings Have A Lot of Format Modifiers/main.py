name = "mike"
age = 25
weight = 80.65784
win_rate = 0.67
net_worth = 134234534345

import locale

locale.setlocale(locale.LC_NUMERIC, "de_DE.utf-8")

print(
    f"{name} is {age:X} years old and weights {weight:.2f} kg and wins {win_rate:.2%} and is worth ${net_worth:n}"
)

day = 7
month = 6
year = 2023
print(f"{day:07}.{month:02}.{year}")

sentence = "each column has a width of ten"
table = ""
for word in sentence.split(" "):
    table += f"{word:^10}"
print(table)

import datetime

current = datetime.datetime.now()
print(f"{current:%d}")

