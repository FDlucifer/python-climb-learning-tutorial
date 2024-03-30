# pip install opencv-python
# pip install mediapipe

import mediapipe as mp
import cv2
import numpy as np
from mediapipe.framework.formats import landmark_pb2
import time
from math import sqrt
import win32api
import pyautogui


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
click = 0

video = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence = 0.8, min_tracking_confidence = 0.8) as hands:
    while video.isOpened():
        _, frame = video.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        imageHeight, imageWidth, _ = image.shape
        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                        mp_drawing.DrawingSpec(color = (250, 44, 250), thickness = 2, circle_radius = 2),
                                        )

        if results.multi_hand_landmarks != None:
          for handLandmarks in results.multi_hand_landmarks:
            for point in mp_hands.HandLandmark:

                normalizedLandmark = handLandmarks.landmark[point]
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)

                point = str(point)

                if point == 'HandLandmark.INDEX_FINGER_TIP':
                 try:
                    indexfingertip_x = pixelCoordinatesLandmark[0]
                    indexfingertip_y = pixelCoordinatesLandmark[1]
                    win32api.SetCursorPos((indexfingertip_x*4, indexfingertip_y*5))

                 except:
                    pass

                elif point == 'HandLandmark.THUMB_TIP':
                 try:
                    thumbfingertip_x = pixelCoordinatesLandmark[0]
                    thumbfingertip_y = pixelCoordinatesLandmark[1]
                    #print("thumb",thumbfingertip_x)

                 except:
                    pass

                try:
                    #pyautogui.moveTo(indexfingertip_x,indexfingertip_y)
                    Distance_x = sqrt((indexfingertip_x - thumbfingertip_x)**2 + (indexfingertip_x - thumbfingertip_x)**2)
                    Distance_y = sqrt((indexfingertip_y - thumbfingertip_y)**2 + (indexfingertip_y - thumbfingertip_y)**2)
                    if Distance_x < 5 or Distance_x < -5:
                        if Distance_y < 5 or Distance_y < -5:
                            click = click + 1
                            if click%5 == 0:
                                print("single click")
                                pyautogui.click()
                except:
                    pass

        cv2.imshow('Hand Tracking', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

video.release()