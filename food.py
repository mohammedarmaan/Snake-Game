import turtle
import random


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed('fastest')
        self.goto(x=random.randint(-250, 250), y=random.randint(-250, 250))

    def refresh(self):
        self.goto(x=random.randint(-250, 250), y=random.randint(-250, 250))

