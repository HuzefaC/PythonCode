from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
LEFT = (-100, 250)
RIGHT = (100, 250)
CENTER = (0, 0)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(LEFT)
        self.write(f"{self.left_score}", align=ALIGNMENT, font=FONT)
        self.goto(RIGHT)
        self.write(f"{self.right_score}", align=ALIGNMENT, font=FONT)

    def game_over(self, winner):
        self.goto(CENTER)
        if winner == "left":
            self.write("Game Over!! Left Player won.", align=ALIGNMENT, font=FONT)
        else:
            self.write("Game Over!! Right Player won.", align=ALIGNMENT, font=FONT)

    def increase_score(self, player):

        if player == "left":
            self.left_score += 1
        else:
            self.right_score += 1
        self.clear()
        self.update_scoreboard()

