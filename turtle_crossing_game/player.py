from turtle import Turtle

STARTING_COORDINATES = (-100, -280)
LEVEL_UP = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.move_to_start()

    def move_to_start(self):
        self.goto(STARTING_COORDINATES)

    def move(self):
        self.forward(20)

    def is_level_completed(self):
        if self.ycor() >= LEVEL_UP:
            self.move_to_start()
            return True
        return False
