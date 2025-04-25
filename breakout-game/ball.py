from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.reset_position()
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9  # Increase speed slightly after each bounce

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, -200)
        self.move_speed = 0.05
        self.x_move = random.choice([-10, -8, 8, 10])
        self.y_move = 10