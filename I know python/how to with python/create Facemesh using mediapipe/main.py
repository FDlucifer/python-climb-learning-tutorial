# pip install mediapipe
# pip install opencv-python

import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    height, width, _ = frame.shape
    result = face_mesh.process(frame)
    try:
        for facial_landmarks in result.multi_face_landmarks:
            for i in range(0, 468):
                landmrk = facial_landmarks.landmark[i]
                locx = int(landmrk.x * width)
                locy = int(landmrk.y * height)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                cv2.circle(frame, (locx, locy), 1, (0, 200, 0), 0)
                cv2.imshow("Image", frame)
    
    except:
        cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()