from turtle import Screen

from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("orange")
screen.title("The Arcade Game")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "u")
screen.onkey(l_paddle.down, "d")

should_continue = True
while should_continue:
    time.sleep(ball.increase_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.ycor() < -320:
        ball.x_bounce()
    if ball.xcor() > 380:
        ball.restart_position()
        scoreboard.left_point()
    if ball.xcor() < -380:
        ball.restart_position()
        scoreboard.right_point()

screen.exitonclick()
