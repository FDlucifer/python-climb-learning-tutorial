# pip install opencv-python mediapipe

import cv2
from cv2 import VideoCapture
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic

cap = VideoCapture("video.mp4")
background = VideoCapture("background.mp4")

with mp_holistic.Holistic(
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5) as holistic:
    while cap.isOpened():
        _, image = cap.read()
        _, backgroundimage = background.read()

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = holistic.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        mp_drawing.draw_landmarks(
            backgroundimage,
            result.face_landmarks,
            landmark_drawing_spec = None,
            connection_drawing_spec = mp_drawing_styles.get_default_face_mesh_contours_style())

        mp_drawing.draw_landmarks(
            backgroundimage,
            result.pose_landmarks,
            mp_holistic.POSE_CONNECTIONS,
            landmark_drawing_spec = mp_drawing_styles.get_default_pose_landmarks_style())

        cv2.imshow("srivalli", cv2.flip(backgroundimage, 1))
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

cap.release()