from turtle import Turtle
LOCATIONS = [(-20, 0), (0, 0), (20, 0)]


class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for pos in LOCATIONS:
            self.add_snake(pos)

    def add_snake(self, pos):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(pos)
        self.snake_list.append(tim)

    def extend(self):
        self.add_snake(self.snake_list[-1].position())

    def move(self):
        for num in range(len(self.snake_list)-1, 0, -1):
            new_x = self.snake_list[num-1].xcor()
            new_y = self.snake_list[num-1].ycor()
            self.snake_list[num].goto(new_x, new_y)
        self.head.forward(20)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.seth(0)
