from turtle import Turtle
import random

TOP = 280
BOTTOM = -280
LEFT = -280
RIGHT = 250


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.refresh()

    def refresh(self):
        random_x = random.randint(LEFT, RIGHT)
        random_y = random.randint(BOTTOM, RIGHT)
        self.goto(random_x, random_y)
