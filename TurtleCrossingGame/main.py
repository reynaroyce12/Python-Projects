from player import *
# from cars import *
from score import *
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('dark gray')
screen.tracer(0)

player = Player()
cars = Car()
point = Scoreboard()


def go_up():
    player.forward(10)


screen.listen()
screen.onkeypress(go_up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)         # Refreshes screen every 0.1 seconds
    screen.update()

    cars.create_cars()
    cars.move_cars()

# Checking collision with the cars

    for i in cars.all_cars:             # iterating through each car in the list
        if i.distance(player) < 30:
            game_on = False
            point.game_over()

# Checking if the turtle crossed

    if player.ycor() > 280:
        # print("Yaay you win!")
        cars.car_speed += 3
        player.goto(0, -280)
        point.level += 1
        point.update()

screen.exitonclick()
