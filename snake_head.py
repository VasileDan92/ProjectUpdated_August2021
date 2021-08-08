import turtle
import snake_game


class SnakeHead(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color(snake_game.snake_color)
        self.penup( )
        self.goto(0, 0)
        self.direction = "stop"

    def go_up(self):
        if self.direction != "down":
            self.direction = "up"

    def go_down(self):
        if self.direction != "up":
            self.direction = "down"

    def go_right(self):
        if self.direction != "left":
            self.direction = "right"

    def go_left(self):
        if self.direction != "right":
            self.direction = "left"

    # Change the direction of head
    def move(self):
        if self.direction == "up":
            y = self.ycor( )  # y coordinate of the turtle
            self.sety(y + 20)
        if self.direction == "down":
            y = self.ycor( )  # y coordinate of the turtle
            self.sety(y - 20)
        if self.direction == "left":
            x = self.xcor( )  # y coordinate of the turtle
            self.setx(x - 20)
        if self.direction == "right":
            x = self.xcor( )  # y coordinate of the turtle
            self.setx(x + 20)
