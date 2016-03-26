def draw_snowflake(sentiment):
    from Tkinter import *
    import turtle
    import random
    sentiment +=1
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
        blah.tracer(100)
        blah.pensize(2)

    # Make all the turtles point in the right directions
    b.left(45)
    c.left(90)
    d.left(135)
    e.left(180)
    f.left(225)
    g.left(270)
    h.left(315)

    ts = turtle.getscreen()


    for i in range(random.randrange(0, 200)): #this should be lower with positive sentiment
        turn = random.randrange(0, round(360/(sentiment*10))) #this should be lower with positive sentiment
        length = random.randrange(0, 30) #this should be higher with positive sentiment
        for blah in turtles:
            blah.right(turn)
            blah.forward(length)


    for i in range(random.randrange(0, 1000)): #this should be lower with positive sentiment
        turn = -1 * random.randrange(0, round(361/(sentiment*10))) #this should be lower with positive sentiment
        length = random.randrange(0, 30) #this should be higher with positive sentiment
        for blah in turtles:
            blah.right(turn)
            blah.forward(length)

    ts.getcanvas().postscript(file="duck.eps")
    turtle.done()


if __name__ == "__main__":
    print draw_snowflake(-0.2)