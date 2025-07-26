from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.8 , stretch_len=0.8)
        self.color("blue")
        self.penup()
        self.refresh()

    def refresh(self):
        x_location = random.randint(-280 , 280)
        y_location = random.randint(-280 , 280)
        self.goto(x=x_location , y=y_location)
