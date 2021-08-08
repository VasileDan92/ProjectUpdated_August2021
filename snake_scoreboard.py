import turtle


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed( )
        self.shape("square")
        self.color("white")
        self.penup( )
        self.hideturtle()
        self.goto(0, 250)
