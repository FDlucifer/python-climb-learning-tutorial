import random
import turtle

turtle.color("red", "blue")

turtle.begin_poly()
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_poly()

p = turtle.get_poly()
turtle.register_shape("Square", p)

turtle.goto(-200, -200)
turtle.shape("Square")

turtle.done()
