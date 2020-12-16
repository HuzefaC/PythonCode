from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")
LEVEL_POSITION = (-250, 250)
CENTER = (0, 0)
STARTING_LEVEL = 1


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = STARTING_LEVEL
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(LEVEL_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(CENTER)
        self.write("Game Over!!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_scoreboard()
