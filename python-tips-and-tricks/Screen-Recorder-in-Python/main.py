import cv2
import numpy as np
import pyautogui
import time

SCREEN_SIZE = (1920, 1080)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

fps = 120
prev = 0

while True:
    time_elapsed = time.time() - prev
    img = pyautogui.screenshot()
    if time_elapsed > 1.0/fps:
        prev = time.time()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)

    cv2.waitKey(100)

cv2.destroyAllWindows()
out.release()