from turtle import *
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.speed('fastest')
        self.penup()
        self.random_food_pos()

    def random_food_pos(self):
        food_posx = random.randint(-370, 370)
        food_posy = random.randint(-270, 270)
        self.goto(food_posx, food_posy)
