# pip install SpeechRecognition pyfirmata

import speech_recognition as sr
from pyfirmata import Arduino, SERVO, util
from time import sleep

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

port = 'COM3'
pin = 10
board = Arduino(port)

board.digital[pin].mode = SERVO

def rotate(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

with mic as source:
    r.adjust_for_ambient_noise(source)
    while True:
        audio = r.listen(source)
        try:
            if r.recognize_google(audio) == 'switch on':
                print("switch is on")
                for i in range(0, 45):
                    rotate(pin, i)
            else:
                print("something")
        except:
            print("no audio")