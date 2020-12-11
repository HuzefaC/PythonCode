from turtle import Turtle


PADDLE_MOVEMENT = 20
PADDLE_LENGTH_STRETCH = 1
PADDLE_WIDTH_STRETCH = 5


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=PADDLE_WIDTH_STRETCH, stretch_len=PADDLE_LENGTH_STRETCH)
        self.goto(position)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
