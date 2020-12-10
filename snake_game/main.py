from turtle import Screen
import time
from snake import Snake

# Setup the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)

# Removes tracing
screen.tracer(0)

screen.title("Snake")


def play():
    """This function starts the game"""
    game_on = True
    snake = Snake()

    # Listening to key events
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
