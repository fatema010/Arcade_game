from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.increase_speed = 0.1

    def move(self):
        x_value = self.xcor() + self.x_move
        y_value = self.ycor() + self.y_move
        self.goto(x_value, y_value)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.increase_speed *= 0.8

    def restart_position(self):
        self.goto(0, 0)
        self.increase_speed = 0.1
        self.x_bounce()
