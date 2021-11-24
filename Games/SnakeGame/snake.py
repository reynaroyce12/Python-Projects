from turtle import *

up = 90
down = 270
left = 180
right = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snakes = []
        self.coordinates = [(0, 0), (-20, 0), (-40, 0)]
        self.create()
        self.head = self.snakes[0]

    def create(self):
        for i in self.coordinates:
            self.add_body(i)

    def add_body(self, i):
        new_obj = Turtle('square')
        new_obj.color('white')
        new_obj.penup()
        new_obj.goto(i)
        self.snakes.append(new_obj)

    def extend_body(self):
        last_position = self.snakes[-1].position()
        self.add_body(last_position)

    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[i - 1].xcor()
            new_y = self.snakes[i - 1].ycor()
            self.snakes[i].goto(new_x, new_y)
        self.snakes[0].forward(20)

    def go_up(self):
        if self.head.heading() != down:
            self.head.setheading(up)  # getting hold of the first block(head)

    def go_down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def go_left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def go_right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
