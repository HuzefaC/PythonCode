# import turtle as t
from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.back(10)


def move_right():
    angle = turtle.heading()
    turtle.setheading(angle - 5)


def move_left():
    angle = turtle.heading()
    turtle.setheading(angle + 5)


def clear_screen():
    turtle.clear()
    turtle.reset()


screen.listen()
screen.onkeypress(fun=move_forwards, key="w")
screen.onkeypress(fun=move_backwards, key="s")
screen.onkeypress(fun=move_right, key="d")
screen.onkeypress(fun=move_left, key="a")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()
