import unittest
import turtle
import snake_game_elements
import snake_head
import snake_vitamin
import snake_scoreboard

class TestSnake(unittest.TestCase):
    def test_game_over(self):
        head = snake_head.SnakeHead()
        vitamin = snake_vitamin.SnakeVitamin()
        scoreboard = snake_scoreboard.ScoreBoard()
        game_screen = turtle.Screen()
        game_window = turtle.Screen()
        game_element = snake_game_elements.GameElements(scoreboard, head, vitamin, game_screen)
        snake_game_elements.snake_game.game_over(scoreboard, head, vitamin, game_screen, game_element)
        self.assertEqual(head.position(), (0, 0))
        self.assertEqual(vitamin.position(), (0, 150))
        self.assertEqual(scoreboard.position(), (0, 260))
        game_element.reset()
        self.assertEqual(head.position(), (0, 0))
        self.assertEqual(vitamin.position(), (0, 150))
        game_element.return_to_main()
        self.assertEqual(game_window.window_height(), 600)
        self.assertEqual(game_window.window_width(), 800)
        self.assertEqual(game_window.bgcolor(), "black")
        self.assertEqual(game_window.bgpic(), "hello.gif")
    
    def test_reset_scoreboard(self):
        scoreboard = snake_scoreboard.ScoreBoard()
        snake_game_elements.snake_game.reset_scoreboard(scoreboard)
        self.assertEqual(scoreboard.position(), (0, 260))

    def test_start_snake_game(self):
        head = snake_head.SnakeHead()
        vitamin = snake_vitamin.SnakeVitamin()
        scoreboard = snake_scoreboard.ScoreBoard()
        game_screen = turtle.Screen()
        game_window = turtle.Screen()
        game_element = snake_game_elements.GameElements(scoreboard, head, vitamin, game_screen)
        head.goto(360, 180)
        snake_game_elements.snake_game.score = 10
        snake_game_elements.snake_game.start_snake_game(scoreboard, head, vitamin, game_screen, game_element)
        self.assertEqual(snake_game_elements.snake_game.score, 0)
        self.assertEqual(head.position(), (0, 0))


if __name__ == '__main__':
    unittest.main()