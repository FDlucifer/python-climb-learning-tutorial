import pyautogui
import time

def auto():
    pyautogui.moveTo(1268, 995)
    pyautogui.rightClick()
    time.sleep(0.1)
    pyautogui.moveTo(1416, 1369)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.moveTo(2023, 1047)
    pyautogui.click()
    time.sleep(0.1)

for i in range(100):
    auto()
    time.sleep(0.2)

print(pyautogui.position())
