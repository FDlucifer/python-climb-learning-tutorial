import turtle

turtle.Screen().bgcolor("orange")

t = turtle.Turtle()
t.pensize(8)
t.hideturtle()
t.penup()
t.goto(-240, 0)
t.showturtle()
t.pendown()

r = 70
t.circle(r)

t.hideturtle()
t.penup()
t.goto(-80, 5)
t.showturtle()
t.pendown()

t.forward(150) # draw base

t.left(120)
t.forward(150)

t.left(120)
t.forward(150)

t.hideturtle()
t.penup()
t.goto(170, 0)
t.showturtle()
t.pendown()

t.left(120)

t.forward(140)
t.left(90)

t.forward(140)
t.left(90)

t.forward(140)
t.left(90)

t.forward(140)
t.left(90)

turtle.done()