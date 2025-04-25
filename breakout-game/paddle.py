from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.7, stretch_len=7)
        self.speed('fastest')
        self.penup()
        self.goto(0, -250)
        self.moving_left = False
        self.moving_right = False

    def move(self):
        if self.moving_left and self.xcor() > -350:
            self.setx(self.xcor() - 20)
        if self.moving_right and self.xcor() < 350:
            self.setx(self.xcor() + 20)

    def start_going_left(self):
        self.moving_left = True

    def start_going_right(self):
        self.moving_right = True

    def stop_going_left(self):
        self.moving_left = False
        
    def stop_going_right(self):
        self.moving_right = False