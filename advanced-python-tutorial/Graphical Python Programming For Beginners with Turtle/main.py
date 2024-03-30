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

t.begin_fill()
draw_square(t, 200)
t.end_fill()

t.penup()
t.forward(200)
t.pendown()

t.begin_fill()
draw_square(t, 200)
t.end_fill()

turtle.done()

