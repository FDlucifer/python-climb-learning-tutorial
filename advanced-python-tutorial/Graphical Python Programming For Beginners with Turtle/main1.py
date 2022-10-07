import random
import turtle

t = turtle.Turtle()
t.color("red", "blue")

def draw_square(turtle_obj, size):
    turtle_obj.forward(size)
    turtle_obj.left(90)
    turtle_obj.forward(size)
    turtle_obj.left(90)
    turtle_obj.forward(size)
    turtle_obj.left(90)
    turtle_obj.forward(size)
    turtle_obj.left(90)

t.getscreen().bgcolor("#000000")
t.color("white", "yellow")
t.speed(100)

def draw_star(turtle_obj, size):
    for _ in range(5):
        turtle_obj.forward(size)
        turtle_obj.left(216)

for _ in range(50):
    x, y = random.randint(-300, 300), random.randint(-300, 300)

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    draw_star(t, random.randint(5, 25))
    t.end_fill()

t.clear()

turtle.done()

