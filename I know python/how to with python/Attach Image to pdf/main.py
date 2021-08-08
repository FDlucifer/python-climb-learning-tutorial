# pip install PIL

from PIL import Image

img1 = Image.open('1.png')
im1 = img1.convert('RGB')
im1.save('1.pdf')