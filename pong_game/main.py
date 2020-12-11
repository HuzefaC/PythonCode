from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

BOUNCE_DISTANCE_TOP = 280
BOUNCE_DISTANCE_BOTTOM = -280
BOUNCE_DISTANCE_PADDLE = 50
BOUNCE_DISTANCE_RIGHT = 320
BOUNCE_DISTANCE_LEFT = -320

RESET_DISTANCE_RIGHT = 360
RESET_DISTANCE_LEFT = -360

WIN_SCORE = 10


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
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=paddle_right.go_up)
screen.onkeypress(key="Down", fun=paddle_right.go_down)
screen.onkeypress(key="w", fun=paddle_left.go_up)
screen.onkeypress(key="s", fun=paddle_left.go_down)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Bounce off top or bottom
    if ball.ycor() > BOUNCE_DISTANCE_TOP or ball.ycor() < BOUNCE_DISTANCE_BOTTOM:
        ball.bounce_y()

    # Bounce off the paddle
    if (ball.distance(paddle_right) < BOUNCE_DISTANCE_PADDLE and ball.xcor() > BOUNCE_DISTANCE_RIGHT)\
            or (ball.distance(paddle_left) < BOUNCE_DISTANCE_PADDLE and ball.xcor() < BOUNCE_DISTANCE_LEFT):
        ball.bounce_x()
    elif ball.xcor() > RESET_DISTANCE_RIGHT:
        scoreboard.increase_score("left")
        ball.reset_position()
    elif ball.xcor() < RESET_DISTANCE_LEFT:
        scoreboard.increase_score("right")
        ball.reset_position()
    elif scoreboard.left_score >= WIN_SCORE:
        scoreboard.game_over("left")
        game_is_on = False
    elif scoreboard.right_score >= WIN_SCORE:
        scoreboard.game_over("right")
        game_is_on = False

screen.exitonclick()
