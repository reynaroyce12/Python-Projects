from turtle import *
import random

# timmy is my turtle - object

num_sides_list = []  # list containing number of sides of figure
colors = ["navy", "light blue", "steel blue", "dark slate gray", "dark red", "light coral"]

timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(2)


def input_sides():
    n = int(input("How many figures do you have: "))
    for i in range(1, n + 1):
        num_sides = int(input(f"Enter the side for figure {i} - "))
        num_sides_list.append(num_sides)

    for i in num_sides_list:  # looping through each figures
        timmy.color(random.choice(colors))
        for j in range(i):  # looping till the number of sides in each figure
            angle = 360 / i
            timmy.forward(100)
            timmy.right(angle)


input_sides()

screen = Screen()
screen.exitonclick()
