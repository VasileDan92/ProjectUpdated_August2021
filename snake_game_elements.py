import turtle
import pong_game
import snake_game


class GameElements(turtle.Turtle):
    def __init__(self, scoreboard, head, vitamin, game_screen):
        turtle.Turtle.__init__(self)
        self.scoreboard = scoreboard
        self.head = head
        self.vitamin = vitamin
        self.game_screen = game_screen
        self.running = True

    def reset(self):
        self.scoreboard.clear( )
        self.head.goto(0, 0)
        self.vitamin.goto(0, 150)
        with open("snake_high_score.txt", mode="r") as data:
            high_score = int(data.read( ))
        self.scoreboard.write(f"Score: 0 High Score: {high_score}", align="center", font=("Verdana", 16, "normal"))

    def return_to_main(self):
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        self.game_screen.clear( )
        self.running = False
        game_window = turtle.Screen( )
        game_window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        game_window.title("PlayTime")
        game_window.bgcolor("black")

        # Import main image
        game_window.bgpic("hello.gif")
        # Update the screen
        game_window.update( )

        # Keyboard Binding
        game_window.listen( )
        game_window.onkeypress(pong_game.mode_choose, "p")
        game_window.onkeypress(snake_game.run_game, "s")
