from snake import *
from food import *
from score import *
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
point = Scoreboard()

screen.listen()
screen.onkeypress(snake.go_up, "Up")
screen.onkeypress(snake.go_down, "Down")
screen.onkeypress(snake.go_left, "Left")
screen.onkeypress(snake.go_right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.random_food_pos()
        point.score += 1
        snake.extend_body()
        point.update_score()

    # collision with walls
    if snake.head.xcor() > 380 or snake.head.xcor() < -380:
        game_on = False
        point.high_score_update()
        point.game_over()
    elif snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        point.high_score_update()
        point.game_over()

    # detect collision with snake body
    no_head_body = snake.snakes[1:len(snake.snakes)]            # snake body excluding the head
    for any_snake_body in no_head_body:
        if snake.head.distance(any_snake_body) < 10:
            game_on = False
            point.high_score_update()
            point.game_over()

screen.exitonclick()
