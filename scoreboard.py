from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, location):
        super().__init__()
        self.location = location
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(location)
        self.write(self.score, align="center", font=("Courier", 30, "normal"))

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(self.score, align="center", font=("Courier", 30, "normal"))
