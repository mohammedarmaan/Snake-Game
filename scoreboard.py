from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):

        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"SCORE: {self.score}", align="center", font=("courier", 15, "normal"))

    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=("courier", 40, "normal"), align="center")