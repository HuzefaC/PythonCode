from turtle import Turtle, Screen

turtle = Turtle()


def draw_square():
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)


draw_square()

screen = Screen()
screen.exitonclick()
