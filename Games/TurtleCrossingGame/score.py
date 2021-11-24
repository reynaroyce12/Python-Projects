# from turtle import *
from cars import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-370, 250)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 20, "normal"))
