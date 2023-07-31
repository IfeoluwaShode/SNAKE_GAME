from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.clear()
        self.goto(0, 270)
        self.hideturtle()
        self.speed("fastest")
        self.score_tracker()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=("Courier", 20, "normal"))

    def score_tracker(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score-1}", move=False, align="center", font=("Courier", 20, "normal"))
