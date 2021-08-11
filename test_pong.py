import unittest
import pong_game
import pong_ball
import pong_paddle
import pong_scoreboard
import pong_game_elements
import turtle


class TestPong(unittest.TestCase):
    def test_back_to_center_horizontal(self):
        scoreboard = pong_scoreboard.ScoreBoard( )
        ball = pong_ball.Ball( )
        paddle_1 = pong_paddle.Paddle( )
        paddle_2 = pong_paddle.Paddle( )
        pong_game.response = 'horizontal'
        pong_game.back_to_center(scoreboard, ball, paddle_1, paddle_2)
        self.assertIsNone(scoreboard.clear( ))
        self.assertEqual(ball.position( ), (0, 0))
        self.assertNotEqual(ball.dx, -1 * ball.dx)
        self.assertEqual(paddle_1.position( ), (-350, 0))
        self.assertEqual(paddle_2.position( ), (+350, 0))
        pong_game.response = 'vertical'
        pong_game.back_to_center(scoreboard, ball, paddle_1, paddle_2)
        self.assertNotEqual(ball.dy, -1 * ball.dy)
        self.assertEqual(paddle_1.position( ), (0, +260))
        self.assertEqual(paddle_2.position( ), (0, -260))

    def test_game_over(self):
        scoreboard = pong_scoreboard.ScoreBoard( )
        ball = pong_ball.Ball( )
        paddle_1 = pong_paddle.Paddle( )
        paddle_2 = pong_paddle.Paddle( )
        game_screen = turtle.Screen( )
        game_element = pong_game_elements.GameElements(scoreboard, ball, paddle_1, paddle_2, game_screen)
        game_window = turtle.Screen( )
        pong_game.response = 'horizontal'
        pong_game.game_over(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
        self.assertEqual(ball.position( ), (0, 0))
        self.assertEqual(ball.dx, 0)
        self.assertEqual(ball.dy, 0)
        self.assertEqual(scoreboard.position( ), (0, 260))
        self.assertEqual(scoreboard.color( ), ("yellow", "yellow"))
        self.assertEqual(paddle_1.position( ), (-350, 0))
        self.assertEqual(paddle_2.position( ), (+350, 0))
        response = "y"
        game_element.reset( )
        self.assertEqual(ball.position( ), (0, 0))
        self.assertEqual(ball.dx, 0.10)
        self.assertEqual(ball.dy, -0.10)
        pong_game.response = 'vertical'
        pong_game.game_over(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
        self.assertEqual(scoreboard.position( ), (-270, 0))
        self.assertEqual(paddle_1.position( ), (0, +260))
        self.assertEqual(paddle_2.position( ), (0, -260))
        response = "n"
        game_element.return_to_main( )
        self.assertEqual(game_window.window_width( ), 800)
        self.assertEqual(game_window.window_height( ), 600)
        self.assertEqual(game_window.bgcolor( ), "black")
        self.assertEqual(game_window.bgpic( ), "hello.gif")

    def test_reset_scoreboard(self):
        scoreboard = pong_scoreboard.ScoreBoard( )
        pong_game.reset_scoreboard(scoreboard)
        self.assertIsNone(scoreboard.clear( ))
        self.assertEqual(scoreboard.position( ), (0, 260))

    def test_start_pong_game(self):
        scoreboard = pong_scoreboard.ScoreBoard( )
        ball = pong_ball.Ball( )
        paddle_1 = pong_paddle.Paddle( )
        paddle_2 = pong_paddle.Paddle( )
        game_screen = turtle.Screen( )
        game_element = pong_game_elements.GameElements(scoreboard, ball, paddle_1, paddle_2, game_screen)
        pong_game.response = 'horizontal'

        ball.goto(0, 300)
        ball.dy = 1
        pong_game.start_pong_game(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
        self.assertEqual(ball.ycor( ), 290)
        self.assertEqual(ball.dy, -1)
        ball.home( )

        ball.goto(0, -300)
        ball.dy = 1
        pong_game.start_pong_game(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
        self.assertEqual(ball.ycor( ), -290)
        self.assertEqual(ball.dy, -1)
        ball.home( )

        ball.goto(400, 0)
        pong_game.start_pong_game(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
        self.assertEqual(pong_game.score_player_a, 1)
        self.assertEqual(pong_game.score_player_b, 0)
        ball.home( )

        ball.goto(-400, 0)
        pong_game.start_pong_game(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
        self.assertEqual(pong_game.score_player_b, 1)
        self.assertEqual(pong_game.score_player_a, 1)
        ball.home( )

        paddle_1.goto(0, 300)
        ball.goto(-345, 300)
        ball.dx = 1
        pong_game.start_pong_game(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
        self.assertEqual(ball.position( ), (-340, 290))
        self.assertEqual(ball.dx, -1)

        paddle_2.goto(0, 300)
        ball.goto(345, 300)
        ball.dx = 1
        pong_game.start_pong_game(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
        self.assertEqual(ball.position( ), (340, 290))
        self.assertEqual(ball.dx, -1)

        pong_game.response = 'vertical'

        ball.goto(360, 0)
        ball.dx = 1
        pong_game.start_pong_game(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
        self.assertEqual(ball.xcor( ), 350)
        self.assertEqual(ball.dy, -1)
        ball.home( )

        ball.goto(-350, 0)
        ball.dx = 1
        pong_game.start_pong_game(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
        self.assertEqual(ball.xcor( ), -349)
        self.assertEqual(ball.dy, -1)
        ball.home( )

        ball.goto(0, -280)
        pong_game.start_pong_game(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
        self.assertEqual(pong_game.score_player_a, 1)
        self.assertEqual(pong_game.score_player_b, 1)
        ball.home( )

        ball.goto(0, 292)
        # pong_game.start_pong_game(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
        self.assertEqual(pong_game.score_player_b, 1)
        self.assertEqual(pong_game.score_player_a, 1)
        ball.home( )

        paddle_2.goto(300, 0)
        ball.goto(300, -265)
        ball.dy = 1
        pong_game.start_pong_game(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
        self.assertEqual(ball.position( ), (301, -260))
        self.assertEqual(ball.dy, -1)

        paddle_1.goto(345, 0)
        ball.goto(345, 265)
        ball.dy = 1
        pong_game.start_pong_game(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
        self.assertEqual(ball.position( ), (346, 260))
        self.assertEqual(ball.dy, -1)

    def test_mode_chose(self):
        game_screen = turtle.Screen( )
        pong_game.mode_choose( )
        self.assertEqual(game_screen.bgcolor( ), "black")
        self.assertEqual(game_screen.window_width( ), 800)
        self.assertEqual(game_screen.window_height( ), 600)

    def test_run_game(self):
        game_screen = turtle.Screen( )
        paddle_1 = pong_paddle.Paddle( )
        paddle_2 = pong_paddle.Paddle( )
        ball = pong_ball.Ball( )
        pong_game.response = 'horizontal'
        pong_game.run_game( )
        self.assertEqual(game_screen.bgcolor( ), "black")
        self.assertEqual(game_screen.window_width( ), 800)
        self.assertEqual(game_screen.window_height( ), 600)

        self.assertEqual(paddle_1.shape( ), "square")
        self.assertEqual(paddle_2.shape( ), "square")
        self.assertEqual(ball.shape( ), "circle")
        self.assertEqual(ball.color( ), ("white", "white"))
        self.assertEqual(ball.position( ), (0, 0))


if __name__ == '__main__':
    unittest.main( )
