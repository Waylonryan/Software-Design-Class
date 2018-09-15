import turtle
import math

jack = turtle.Turtle()

# def square(t):
#     for i in range(4):
#         jack.fd(100)
#         jack.lt(90

# def square(t, length):
#     for i in range(4):
#         jack.fd(length)
#         jack.lt(90)

# def polygon(t, length, n):
#     for i in range(n):
#         jack.fd(length)
#         jack.lt(360/n)

# polygon(jack, 100, 10)

# def circle(t, r):
#     circumference = 2 * math.pi * r
#     n = int(circumference / 3) + 1
#     length = circumference / n
#     polygon(t, length, n)

# circle(jack, 150)

# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = angle / n
    
    # for i in range(n):
    #     t.fd(step_length)
    #     t.lt(step_angle)
    
# arc(jack, 100, 350)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# polyline(jack, 6, 50, 70)

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

arc(jack, 100, 180)

turtle.mainloop()
