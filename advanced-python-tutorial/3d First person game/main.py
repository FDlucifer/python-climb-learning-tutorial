# pip install ursina
# https://github.com/pokepetter/ursina/tree/master/ursina/textures

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

set = Ursina()

Sky(texture="sky_default")
player = FirstPersonController()

blocks = []

player = Entity(
    model = 'cube',
    color = color.black,
    scale_y = 2
)

player.x += held_keys['d'] * .1
player.x -= held_keys['a'] * .1

sword = Entity(
    parent = camera.ui,
    model = 'cube',
    texture = 'bow_arrow.png',
    position = Vec2(0.406, -0.42))

for i in range(20):
    for j in range(20):
        block = Button(
            color = color.white,
            model = 'cube',
            position = (j, 0, i),
            texture = 'brick',
            parent = scene,
            origin_y = 0.5)
        blocks.append(block)

set.run()