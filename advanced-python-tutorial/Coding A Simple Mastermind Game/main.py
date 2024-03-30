import random

colors = ["red", "green", "yellow", "blue", "purple", "orange"]
code_length = 4
max_attempts = 10

code = random.choices(colors, k=code_length)
attempts = 0

print(code)

print("welcome to the neuralnine mastermind game")
print(f"available colors: {','.join(colors)}")
print(f"code length: {code_length}, max attempts: {max_attempts}")

while attempts < max_attempts:
    guess = (
        input(f"attempt {attempts + 1}/{max_attempts}. enter your guess: ")
        .strip()
        .split()
    )
    if len(guess) != code_length or not all(color in colors for color in guess):
        print("invalid guess! make sure you have exactly four colors.")
        continue

    correct_position = sum(g == c for g, c in zip(guess, code))
    correct_color = sum(min(guess.count(c), code.count(c)) for c in set(code))
    correct_color -= correct_position

    print(f"{correct_position} colors placed correctly!")
    print(f"{correct_color} correct colors placed in wrong position!")

    if correct_position == code_length:
        print("congratulations! you won!")
        exit()

    attempts += 1

print(f"you have lost! the code was {code}")
