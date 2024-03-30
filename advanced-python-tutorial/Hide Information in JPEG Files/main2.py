import PIL.Image
import io

img = PIL.Image.open('heart.png')
byte_arr = io.BytesIO()
img.save(byte_arr, format='PNG')

with open('photo.jpg', 'ab') as f:
    f.write(byte_arr.getvalue())