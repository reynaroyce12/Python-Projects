from block import *
from ball import *
from score import *
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Ping Pong Game')
screen.tracer(0)

right_block = Block(350, 0)
left_block = Block(-350, 0)
first_ball = Ball(0, 0)
point = Scoreboard()

screen.listen()
screen.onkeypress(right_block.go_up, "u")
screen.onkeypress(right_block.go_down, "n")
screen.onkeypress(left_block.go_up, "r")
screen.onkeypress(left_block.go_down, "c")

game_on = True

while game_on:
    time.sleep(first_ball.ball_speed)
    screen.update()
    first_ball.move()

    # Detecting collision with the blocks

    if first_ball.distance(right_block) < 50 and first_ball.xcor() > 320 or first_ball.distance(
            left_block) < 50 and first_ball.xcor() < -320:
        first_ball.ball_speed *= 0.9
        first_ball.move_x *= -1

    # Detecting collision with the left and right walls

    if first_ball.xcor() > 380:
        point.update_left()
        first_ball.reset_x()

    elif first_ball.xcor() < -380:
        point.update_right()
        first_ball.reset_x()


screen.exitonclick()
