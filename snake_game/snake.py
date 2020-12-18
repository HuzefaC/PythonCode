import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.tail = self.snake[-1]

    def create_snake(self):
        """Creates a snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = t.Turtle("square")
        segment.speed("fastest")
        segment.penup()
        segment.goto(position)
        segment.color("white")
        self.snake.append(segment)

    def extend(self):
        position = (self.tail.position())
        self.add_segment(position)

    def move(self):
        """Moves the snake"""
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        """Changes snakes direction to up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Changes snakes direction to down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Changes snakes direction to left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Changes snakes direction to right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
        self.tail = self.snake[-1]


