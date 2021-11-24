from turtle import *

starting_pos = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(starting_pos)
        self.setheading(90)



