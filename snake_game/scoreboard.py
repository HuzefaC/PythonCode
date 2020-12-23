from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
CENTER = (0, 0)
TOP = (0, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(CENTER)
        self.write("Game Over!!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def score_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_highscore(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def get_highscore(self):
        with open("data.txt", "r") as file:
            return int(file.read())

    def set_highscore(self, score):
        with open("data.txt", "w") as file:
            file.write(str(score))
