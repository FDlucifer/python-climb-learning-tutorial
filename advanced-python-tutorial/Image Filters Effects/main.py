# pip install pilgram
# pip install pillow

import PIL.Image
import pilgram

img = PIL.Image.open("beauty.jpg")

pilgram.lofi(img).save("filtered.jpg")
pilgram.inkwell(img).save("filtered2.jpg")
pilgram.kelvin(img).save("filtered3.jpg")

pilgram.css.saturate(img, 2).save("filtered4.jpg")
pilgram.css.hue_rotate(img, 20).save("filtered5.jpg")
pilgram.css.hue_rotate(img, -200).save("filtered6.jpg")