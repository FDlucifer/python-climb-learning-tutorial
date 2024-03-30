import cv2
import numpy as np
import dlib

video = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    num = 0
    for face in faces:
        x, y = face.left(), face.top()
        hi, wi = face.right(), face.bottom()
        cv2.rectangle(frame, (x,y), (hi, wi), (0,0,255), 2)
        num = num + 1

        cv2.putText(frame, 'face' + str(num), (x - 12, y - 12), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    cv2.imshow('faces', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()