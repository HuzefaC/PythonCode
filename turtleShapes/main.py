from turtle import Turtle, Screen
import random

SIDE_LENGTH = 100
TOTAL_ANGLE = 360

colors = ["medium slate blue", "medium purple", "medium orchid", "magenta", "hot pink", "salmon",
          "crimson", "tomato", "gold", "spring green", "medium sea green", "sky blue", "steel blue"]

turtle = Turtle()


def draw_shapes(sides):
    angle = TOTAL_ANGLE/sides
    for i in range(sides):
        turtle.forward(SIDE_LENGTH)
        turtle.right(angle)


for _ in range(3, 11):
    turtle.color(random.choice(colors))
    draw_shapes(_)

screen = Screen()
screen.exitonclick()
