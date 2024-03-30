# pip install pywhatkit
import pywhatkit

question = input("enter the question here: ")
answer = input("enter the answer: ")
pywhatkit.text_to_handwriting("question " + question + "\n" + "answer "+ answer, rgb=[0,0,255])
