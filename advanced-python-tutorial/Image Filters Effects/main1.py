# pip install pilgram
# pip install pillow

import PIL.Image
import pilgram

img = PIL.Image.open("beauty.jpg")
img2 = PIL.Image.open("cloud.jpg")

pilgram.css.blending.color(img, img2).save("blended.jpg")
pilgram.css.blending.darken(img, img2).save("blended2.jpg")
pilgram.css.blending.lighten(img, img2).save("blended3.jpg")
pilgram.css.blending.difference(img, img2).save("blended4.jpg")
pilgram.css.blending.multiply(img, img2).save("blended5.jpg")