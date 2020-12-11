from turtle import Screen

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)


screen.exitonclick()
