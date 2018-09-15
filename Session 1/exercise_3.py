import turtle
import math

jack = turtle.Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t ,r):
    arc(t, r, 360)

# arc(jack, 100, 300)
# jack.lt(60)
# arc(jack, 100, 120)
# jack.lt(120)
# arc(jack, 100, 120)
# jack.lt(120)
# arc(jack, 100, 120)
# jack.lt(60)
# arc(jack, 100, 60)
# jack.lt(60)
# arc(jack, 100, 120)
# jack.lt(120)
# arc(jack, 100, 120)
# jack.lt(120)
# arc(jack, 100, 120)

# This is the start of design 2

circle(jack, 100)
turtle.left(180)
turtle.circle((-50), 180)
turtle.circle(50, 180)
turtle.up()
turtle.goto(0,60)
turtle.down()
turtle.circle(10, 360)
turtle.up()
turtle.goto(0,160)
turtle.down()
turtle.circle(10, 360)



turtle.mainloop()


