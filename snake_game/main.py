from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

TOP_END = 250
BOTTOM_END = -280
LEFT_END = -280
RIGHT_END = 280
FOOD_DISTANCE = 15
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600


# Setup the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)

# Removes tracing
screen.tracer(0)

screen.title("Snake")


def play():
    """This function starts the game"""
    game_on = True
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # Listening to key events
    screen.listen()
    screen.onkeypress(key="Up", fun=snake.up)
    screen.onkeypress(key="Down", fun=snake.down)
    screen.onkeypress(key="Left", fun=snake.left)
    screen.onkeypress(key="Right", fun=snake.right)

    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Increment the score
        if snake.head.distance(food) < FOOD_DISTANCE:
            scoreboard.increase_score()
            food.refresh()

        # Detect wall collision
        if snake.head.xcor() > RIGHT_END or snake.head.xcor() < LEFT_END \
                or snake.head.ycor() > TOP_END or snake.head.ycor() < BOTTOM_END:
            scoreboard.game_over()
            game_on = False


play()
screen.exitonclick()
