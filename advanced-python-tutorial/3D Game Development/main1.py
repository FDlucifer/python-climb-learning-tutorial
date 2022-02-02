# pip install ursina

from sklearn.preprocessing import scale
from ursina import *

app = Ursina()
player = Entity(model="cube", color=color.blue, scale_y=2)

def update():
    player.x += held_keys["d"] * 0.1
    player.x -= held_keys["a"] * 0.1
    player.y += held_keys["w"] * 0.1
    player.y -= held_keys["s"] * 0.1
    player.rotation_x += held_keys["r"] * 5
    player.rotation_y += held_keys["r"] * 5

app.run()