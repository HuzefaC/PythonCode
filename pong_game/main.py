from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

PADDLE_LEFT_START_POSITION = (-350,  0)
PADDLE_RIGHT_START_POSITION = (350,  0)

PADDLE_RIGHT_START_POSITION_X = 350
PADDLE_RIGHT_START_POSITION_Y = 0

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)

paddle_left = Paddle(PADDLE_LEFT_START_POSITION)
paddle_right = Paddle(PADDLE_RIGHT_START_POSITION)
ball = Ball()

screen.listen()
screen.onkeypress(key="Up", fun=paddle_right.go_up)
screen.onkeypress(key="Down", fun=paddle_right.go_down)
screen.onkeypress(key="w", fun=paddle_left.go_up)
screen.onkeypress(key="s", fun=paddle_left.go_down)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
