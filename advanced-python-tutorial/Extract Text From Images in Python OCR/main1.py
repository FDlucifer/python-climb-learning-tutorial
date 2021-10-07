import pytesseract
import PIL.Image
import cv2

myconfig = r"--psm 11 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("logos.jpg"), config=myconfig)
print(text)