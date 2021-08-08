import random
import os
import time

colors = "RGBY"
simon = ""

for score in range(0, 10):
    simon += random.choice(colors)
    for color in simon:
        print(color)
        time.sleep(1.5)
        os.system("cls")

    guess = input("Repeat: ")
    os.system("cls")
    if guess != simon:
        break

print(f"game over! your final score is {score}!")