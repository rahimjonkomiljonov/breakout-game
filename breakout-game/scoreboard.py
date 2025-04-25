from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-380, 260)
        self.write(f"Score: {self.score}", align="left", font=("Courier", 18, "normal"))
        self.goto(380, 260)
        self.write(f"Lives: {self.lives}", align="right", font=("Courier", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def decrease_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def reset(self):
        self.score = 0
        self.lives = 3
        self.update_scoreboard()