import cv2
from deepface import DeepFace
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

while video.isOpened():
    _,frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for x,y,w,h in face:
        img = cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 1)
        try:
            analyze = DeepFace.analyze(frame, actions=['emotion'])
            print(analyze['dominant_emotion'])
        except:
            print("no face")

    cv2.imshow('video', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()