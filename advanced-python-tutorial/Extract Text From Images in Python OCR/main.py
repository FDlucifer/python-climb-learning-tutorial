# https://github.com/tesseract-ocr/tesseract
# download the binary to install
# pip install pytesseract tesseract
# pip install pillow opencv-python
# tesseract text.jpg stdout
# tesseract logos.jpg stdout --psm 11
# tesseract text.jpg test.txt

import pytesseract
import PIL.Image
import cv2

myconfig = r"--psm 6 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("text.jpg"), config=myconfig)
print(text)