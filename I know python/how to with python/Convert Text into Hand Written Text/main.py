# pip install pywhatkit
import pywhatkit

text = input("enter the text here: ")
pywhatkit.text_to_handwriting(text, rgb=[0,255,0])