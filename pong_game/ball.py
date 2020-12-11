from turtle import Turtle

MOVEMENT_DISTANCE = 10
MOVEMENT_SPEED = 0.1
SPEED_INCREMENT_FACTOR = 0.9
REVERSE_DIRECTIONS = -1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = MOVEMENT_DISTANCE
        self.move_y = MOVEMENT_DISTANCE
        self. move_speed = MOVEMENT_SPEED

    def move(self):
        self.goto(self.xcor() + self.move_x,  self.ycor() + self.move_y)

    def bounce_y(self):
        self.move_y *= REVERSE_DIRECTIONS

    def bounce_x(self):
        self.move_x *= REVERSE_DIRECTIONS
        self.move_speed *= SPEED_INCREMENT_FACTOR

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = MOVEMENT_SPEED

