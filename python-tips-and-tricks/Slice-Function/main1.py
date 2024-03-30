numbers = [10, 90, 20, 55, 65, 70, 5, 15, 85, 95]

LASTFOUR = slice(-4, None)
FIRSTFOUR = slice(4)
EVERY_OTHER = slice(0, None, 3)
SOMETHING = slice(2, 7, 2)

print(numbers[LASTFOUR])
print(numbers[FIRSTFOUR])
print(numbers[EVERY_OTHER])
print(numbers[SOMETHING])

mytext = "fuck world! how are you?"
print(mytext[EVERY_OTHER])