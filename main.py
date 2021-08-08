# Main Menu for Games

import turtle
import pong_game

# Define values for width and height
import snake_game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

while True:
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
