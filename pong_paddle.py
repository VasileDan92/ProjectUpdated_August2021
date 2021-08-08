import turtle


class Paddle(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup( )
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.color("blue")
        self.speed = 1

    # Moving Paddle Up
    def paddle_moving_up(self):
        # Ycor (from turtle) returns Y coordinate. Add pixels to coordinate
        y = self.ycor( )
        y += 20
        if y > 260:
            y = 260
        self.sety(y)

    def paddle_moving_right(self):
        x = self.xcor( )
        x += 20
        if x > 350:
            x = 350
        self.setx(x)

    # Moving Paddle Down
    def paddle_moving_down(self):
        y = self.ycor( )
        y -= 20
        if y < -260:
            y = -260
        self.sety(y)

    def paddle_moving_left(self):
        x = self.xcor( )
        x -= 20
        if x < -350:
            x = -350
        self.setx(x)
