MOVE_DISTANCE = 20
from turtle import Turtle
import time
class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]



    def create_snake(self):
        for x in range(3):
            y = [-20, 0, 20]
            turtle = Turtle("square")
            turtle.color("white")
            turtle.speed("fastest")
            turtle.penup()
            turtle.goto(y[x], 0)
            self.body.append(turtle)

    def move(self):
        for num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[num - 1].xcor()
            new_y = self.body[num - 1].ycor()
            self.body[num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
