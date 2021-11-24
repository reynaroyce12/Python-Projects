from turtle import *
import random

colors = ["Red", "maroon", "Green", "Yellow", "navy", "teal"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = 3

    def create_cars(self):
        random_num = random.randint(1, 6)
        if random_num == 4:
            new_car = Turtle()
            new_car.shape('square')
            new_car.color(random.choice(colors))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            y_pos = random.randint(-200, 200)               # generating random y positions for the cars
            new_car.goto(400, y_pos)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

