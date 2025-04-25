from turtle import Screen, Turtle
from ball import Ball
from bricks import Brick
from paddle import Paddle
from scoreboard import Scoreboard
from tkinter import messagebox
import time
import tkinter as tk

def close_game():
    screen.bye()  # Close the turtle screen
    root.destroy()  # Destroy the tkinter root

root = tk.Tk()
root.withdraw()  # Hide the root window
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
brick_manager = Brick()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.start_going_left, "Left")
screen.onkeyrelease(paddle.stop_going_left, "Left")
screen.onkeypress(paddle.start_going_right, "Right")
screen.onkeyrelease(paddle.stop_going_right, "Right")

brick_manager.create_bricks()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    paddle.move()

    # Wall collision
    if ball.ycor() > 280:
        ball.bounce_y()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Bottom collision (missed paddle)
    if ball.ycor() < -280:
        scoreboard.decrease_lives()
        if scoreboard.lives == 0:
            continue_q = messagebox.askyesno("Game Over", f"Final Score: {scoreboard.score}\nPlay again?")
            if continue_q:
                scoreboard.reset()
                ball.reset_position()
                brick_manager.reset_bricks()
            else:
                close_game()
                break
        else:
            ball.reset_position()

    # Paddle collision
    if (-250 < ball.ycor() < -230) and (paddle.xcor() - 70 < ball.xcor() < paddle.xcor() + 70):
        ball.bounce_y()
        # Add some angle variation based on where ball hits paddle
        if ball.xcor() < paddle.xcor() - 30:
            ball.x_move = -abs(ball.x_move)
        elif ball.xcor() > paddle.xcor() + 30:
            ball.x_move = abs(ball.x_move)

    # Brick collision
    for brick in brick_manager.all_bricks[:]:
        if (brick.ycor() - 20 < ball.ycor() < brick.ycor() + 20) and (brick.xcor() - 30 < ball.xcor() < brick.xcor() + 30):
            brick_manager.remove_brick(brick)
            ball.bounce_y()
            scoreboard.increase_score()
            break

    # Win condition
    if len(brick_manager.all_bricks) == 0:
        continue_q = messagebox.askyesno("You Win!", f"Final Score: {scoreboard.score}\nPlay again?")
        if continue_q:
            scoreboard.reset()
            ball.reset_position()
            brick_manager.reset_bricks()
        else:
            close_game()
            break

screen.mainloop()  # Changed from exitonclick() to handle proper closing