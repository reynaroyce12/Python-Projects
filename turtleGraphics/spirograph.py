from turtle import *
import random

# tim is my turtle
tim = Turtle()
screen = Screen()
screen.bgcolor('black')
tim.shape('turtle')
tim.speed('fastest')
colors = ["blue", "green", "red", "white", "yellow"]


for i in range(100):
    tim.circle(150)
    tim.left(5)
    tim.color(random.choice(colors))


tim.hideturtle()
screen.exitonclick()
