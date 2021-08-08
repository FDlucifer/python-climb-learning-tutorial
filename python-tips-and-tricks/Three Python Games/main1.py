import random

number = random.randint(0, 10000)
tries = 0
found = False

while not found:
    guess = int(input("guess: "))
    tries += 1
    if guess == number:
        found = True
        print(f"you found the number {number} after {tries} tries!")
    elif guess > number:
        print(f"the number you are looking for is less than {guess}!")
    else:
        print(f"the number you are looking for is greater than {guess}!")