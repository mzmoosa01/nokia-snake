from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.penup()
        self.color('blue')
        self.speed('fastest')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.move()

    def move(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
