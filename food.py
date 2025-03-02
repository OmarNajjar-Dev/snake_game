from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self, shape="circle", color="red", size=0.5):
        """Initializes the food with a given shape, color, and size."""
        super().__init__()
        self.shape(shape)
        self.color(color)
        self.shapesize(size)
        self.penup()
        self.appear()  # Place the food at a random location

    def appear(self):
        """Moves the food to a random position on the screen."""
        random_x = randint(-370, 370)
        random_y = randint(-320, 320)
        self.goto(random_x, random_y)