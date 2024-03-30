# pip install ursina

from sklearn.preprocessing import scale
from ursina import *

app = Ursina()
cube = Entity(model="cube", color=color.red, Texture="white_cube", scale=2)

def update():
    cube.rotation_x = cube.rotation_x + 0.25
    cube.rotation_y = cube.rotation_y + 0.5

app.run()