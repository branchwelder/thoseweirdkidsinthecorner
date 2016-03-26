import turtle
import random

# Create the turtles
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
e = turtle.Turtle()
f = turtle.Turtle()
g = turtle.Turtle()
h = turtle.Turtle()


turtles = [a, b, c, d, e, f, g, h]

for blah in turtles:
    blah.speed(0)
    blah.tracer(100000)
    blah.pensize(2)

# Make all the turtles point in the right direction
b.left(45)
c.left(90)
d.left(135)
e.left(180)
f.left(225)
g.left(270)
h.left(315)

turn = random.randrange(0, 361)

for i in range(random.randrange(0, 1000)):
    turn = random.randrange(0, 10)
    length = random.randrange(0, 10)
    for blah in turtles:
        blah.right(turn)
        blah.forward(length)

for blah in turtles:
    blah.forward(400)

for i in range(random.randrange(0, 1000)):
    turn = random.randrange(0, 361)
    length = random.randrange(0, 20)
    for blah in turtles:
        blah.right(turn)
        blah.forward(length)

# Step 4: We're done!
turtle.done()
