# pip install deepface

import cv2
from deepface import DeepFace
import numpy as np

imgpath = "D:\\1.program\\python\\python2\\python-practise\\I know python\\how to with python\\Real time emotion detection\\1.jpg"
image = cv2.imread(imgpath)

analyze = DeepFace.analyze(image, actions=['emotion'])
print(analyze)