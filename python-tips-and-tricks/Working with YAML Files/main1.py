import random
import getpass
import yaml

with open("game_config.yml", "r") as f:
    config = yaml.safe_load(f)

range_min = config['range']['min']
range_max = config['range']['max']
guesses_allowed = config['guesses']
mode = config['mode']

solved = False

if mode == "single":
    correct_number = random.randint(range_min, range_max)
elif mode == "multi":
    correct_number = int(getpass.getpass("player 2, please enter the number to guess: "))
else:
    print("invalid config")
    exit()

for i in range(guesses_allowed):
    guess = int(input("enter your guess: "))
    if guess == correct_number:
        print(f"correct! you need {i + 1} tries!")
        solved = True
        break
    elif guess < correct_number:
        print("too low!")
    else:
        print("too high!")

if not solved:
    print("you lose, the number was: ", correct_number)

