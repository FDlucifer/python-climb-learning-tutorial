import serial
import time
import face_recognition
import cv2
import numpy
import os


ser = serial.Serial('COM3', 9800, timeout=1)
time.sleep(2)

def main_function():
    print("correct face!")

text = []

while True:
    line = ser.readline().decode("utf-8")
    if line == "":
        pass
    else:
        try:
            text.append(int(line))
            print(text)
        except:
            if (line[0]) == 'A':
                if text == []:
                    pass
                else:
                    text.pop()
                    print(text)

            if (line[0]) == 'B':
                if text == []:
                    pass
                else:
                    if text == [1,2,3]:
                        print("correct password")
                    else:
                        print("incorrect password")

            elif (line[0]) == 'C':
                video = cv2.VideoCapture(0)

                face = face_recognition.load_image_file("1.jpg")
                faceencoding = face_recognition.face_encodings(face)[0]

                face_encodings_list = [faceencoding]

                face_encodings = []
                s = True
                face_coordinates = []

                while True:
                    _, frame = video.read()
                    resized_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
                    resized_frame_rdb = frame[:, :, ::-1]

                    if s:
                        face_coordinates = face_recognition.face_locations(resized_frame_rdb)
                        face_encodings = face_recognition.face_encodings(resized_frame_rdb, face_coordinates)

                        for faces in face_encodings:
                            matchs = face_recognition.compare_faces(face_encodings_list, faces)
                            if matchs[0] == True:
                                video.release()
                                cv2.destroyAllWindows()
                                main_function()
                    cv2.imshow('face scan:', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                video.release()
                cv2.destroyAllWindows()