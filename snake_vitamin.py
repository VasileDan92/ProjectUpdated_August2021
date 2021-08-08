import turtle
from turtle import Turtle


class SnakeVitamin(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.penup( )
        self.goto(0, 150)








