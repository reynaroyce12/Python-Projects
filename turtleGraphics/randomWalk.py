from turtle import *
import random

colors = ["red", "blue", "green", "black"]
directions = [0, 90, 180, 270]

# timmy is my turtle
tim = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor('black')
tim.shape('turtle')
tim.pensize(6)
tim.speed('fast')


def pick_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


for i in range(200):
    tim.color(pick_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))



screen.exitonclick()
