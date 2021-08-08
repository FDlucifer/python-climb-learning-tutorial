import pyautogui
import time
import random

time.sleep(2)

file = open('test.txt', 'r').read()
file = file.splitlines()

for _ in range(20):
    pyautogui.typewrite(random.choice(file))
    pyautogui.press('enter')