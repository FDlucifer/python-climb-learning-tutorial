# pip install deepface opencv-python pandas

import cv2
from deepface import DeepFace

img = cv2.imread("faces/man.jpg")
results = DeepFace.analyze(img, actions=("gender", "age", "race", "emotion"))
print(results)

