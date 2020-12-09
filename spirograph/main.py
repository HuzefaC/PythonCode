import turtle as t
import random

FULL_ANGLE = 360
t.colormode(255)
turtle = t.Turtle()
turtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def draw_spirograph(gap):
    for i in range(int(FULL_ANGLE/gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + gap)


draw_spirograph(20)
screen = t.Screen()
screen.exitonclick()
