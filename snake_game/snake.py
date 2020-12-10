import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = t.Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.snake.append(segment)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        heading = self.snake[0].heading()
        if heading == 0.0:
            self.snake[0].left(90)
        elif heading == 180.0:
            self.snake[0].right(90)

    def down(self):
        heading = self.snake[0].heading()
        if heading == 0.0:
            self.snake[0].right(90)
        elif heading == 180.0:
            self.snake[0].left(90)

    def left(self):
        heading = self.snake[0].heading()
        if heading == 90.0:
            self.snake[0].left(90)
        elif heading == 270.0:
            self.snake[0].right(90)

    def right(self):
        heading = self.snake[0].heading()
        if heading == 90.0:
            self.snake[0].right(90)
        elif heading == 270.0:
            self.snake[0].left(90)
