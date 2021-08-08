import turtle
import pong_game
import snake_game


class GameElements(turtle.Turtle):
    def __init__(self, scoreboard, ball, paddle_1, paddle_2, game_screen):
        turtle.Turtle.__init__(self)
        self.scoreboard = scoreboard
        self.ball = ball
        self.paddle_1 = paddle_1
        self.paddle_2 = paddle_2
        self.game_screen = game_screen
        self.running = True

    def reset(self):
        self.scoreboard.clear( )
        self.ball.goto(0, 0)
        self.ball.dx = 0.10
        self.ball.dy = -0.10
        if pong_game.response == 'horizontal':
            self.scoreboard.write(f"Home ({pong_game.color_paddle_1.title()}): {pong_game.score_player_a} Away ({pong_game.color_paddle_2.title()}): {pong_game.score_player_b} ", align="center", font=("Verdana", 18, "normal"))
        elif pong_game.response == 'vertical':
            self.scoreboard.write(f"Home ({pong_game.color_paddle_1.title()}): {pong_game.score_player_a}\nAway ({pong_game.color_paddle_2.title()}): {pong_game.score_player_b} ", align="center", font=("Verdana", 18, "normal"))
        
    def return_to_main(self):

        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        self.game_screen.clear()
        self.running = False
        game_window = turtle.Screen()
        game_window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        game_window.title("PlayTime")
        game_window.bgcolor("black")

        # Import main image
        game_window.bgpic("hello.gif")
        # Update the screen
        game_window.update( )

        # Keyboard Binding
        game_window.listen()
        game_window.onkeypress(pong_game.mode_choose, "p")
        game_window.onkeypress(snake_game.run_game, "s")
