from turtle import Screen, Turtle, colormode
import random

LENGTH = 20
ANGLE = 90

colormode(255)
turtle = Turtle()
turtle.pensize(10)
turtle.speed("fastest")

direction = [0, 90, 180, 270]

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


for i in range(200):
    # TODO Generate a random direction
    random_direction = random.choice(direction)
    # TODO Generate a random color
    turtle.color(random_color())
    turtle.forward(20)
    turtle.setheading(random_direction)

screen = Screen()
screen.colormode(255)
screen.exitonclick()
