from turtle import *


class Ball(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=2)
        self.move_x = 10
        self.move_y = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.penup()
        self.goto(new_x, new_y)

        # Detecting collision of the ball with the upper and lower wall
        if self.ycor() > 280 or self.ycor() < -280:
            self.move_y *= -1

    def reset_x(self):
        self.goto(0, 0)
        self.move_x *= -1
        self.ball_speed = 0.1


