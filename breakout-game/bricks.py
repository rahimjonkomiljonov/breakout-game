from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]

class Brick(Turtle):
    def __init__(self):
        self.all_bricks = []

    def create_bricks(self):
        start_x = -350
        start_y = 200
        brick_width = 70
        brick_height = 20
        rows = 5
        columns = 10

        for row in range(rows):
            for column in range(columns):
                new_brick = Turtle("square")
                new_brick.color(random.choice(COLORS))
                new_brick.shapesize(stretch_wid=1, stretch_len=3)
                new_brick.penup()
                x_position = start_x + (column * (brick_width + 5))
                y_position = start_y - (row * (brick_height + 5))
                new_brick.goto(x_position, y_position)
                self.all_bricks.append(new_brick)

    def remove_brick(self, brick):
        brick.hideturtle()
        self.all_bricks.remove(brick)
        
    def reset_bricks(self):
        self.all_bricks.clear()
        self.create_bricks()