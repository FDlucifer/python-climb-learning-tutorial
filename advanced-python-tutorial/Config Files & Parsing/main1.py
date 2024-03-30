import random
from configparser import ConfigParser

config = ConfigParser()
config.read("number_guessing.ini")

user = input("what is your username: ")
if user == "SUDO":
    password = input("Password: ")
    if password != "12345":
        print("wrong!")
        exit(0)

try:
    config_data = config[user]
except:
    print("user not found!")
    exit(0)

number = random.randint(1, 10 ** (int(config_data['numberdigits'])))
max_tries = int(config_data['numbertries'])
tries = 0
done = False

while not done:
    guess = input("Guess: ")
    if guess == "cheat":
        if "cheats" in config_data.keys() and config_data["cheats"] == "on":
            print(f"you won! the number was {number}!")
            exit(0)
        else:
            print("you are not allowed to cheat!")
            exit(0)

    else:
        guess = int(guess)
    
    tries += 1

    if guess == number:
        print(f"you won! the number was {number}!")
        print(f"it took you {tries} tries!")
    else:
        if tries == max_tries:
            print(f"you lost after {tries} tries!")
            print(f"the number was {number}!")
            exit(0)
        else:
            if guess > number:
                print("too high!")
            else:
                print("too low!")