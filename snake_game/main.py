from turtle import Screen
import turtle as t
import time
from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.tracer(0)
screen.title("Snake")


def play():
    game_on = True
    snake = Snake()
    screen.listen()
    screen.onkeypress(key="Up", fun=snake.up)
    screen.onkeypress(key="Down", fun=snake.down)
    screen.onkeypress(key="Left", fun=snake.left)
    screen.onkeypress(key="Right", fun=snake.right)
    counter = 0
    while game_on:
        screen.update()
        time.sleep(0.1)
        counter += 1
        snake.move()


play()
screen.exitonclick()


