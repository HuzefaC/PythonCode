from turtle import Screen
from player import Player
from obstacle import Obstacle
from scoreboard import Scoreboard
import time

HIT_DISTANCE = 25
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
OBSTACLE_GAP = 8
SLEEP_TIME = 0.1

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

player = Player()
obstacle = Obstacle()
scoreboard = Scoreboard()
# Event listeners
screen.onkeypress(key="Up", fun=player.move)
screen.listen()


game_is_on = True
while game_is_on:
    time.sleep(SLEEP_TIME)
    screen.update()
    obstacle.create_car()
    obstacle.move_cars()

    for ob in obstacle.all_cars:
        if ob.distance(player) < HIT_DISTANCE:
            screen.update()
            game_is_on = False
            scoreboard.game_over()
            break

    if player.is_level_completed():
        scoreboard.increase_score()
        obstacle.level_up()
screen.exitonclick()
