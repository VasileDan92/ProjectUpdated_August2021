# Creating a Paddle Pong Game in Python

# Create Graphics using turtle
from snake_game import run_game
import turtle
import pong_game_elements
import pong_paddle
import pong_ball
import pong_scoreboard

# The game mode
response = ''

# Creating Score
score_player_a = 0
score_player_b = 0

# Colors of the paddles
color_paddle_1 = ''
color_paddle_2 = ''


# Ball comes back to center after a goal in both game modes
def back_to_center(scoreboard, ball, paddle_1, paddle_2):
    global response
    ball.goto(0, 0)
    scoreboard.clear( )
    if response == 'horizontal':
        ball.dx *= -1
        paddle_1.goto(-350, 0)
        paddle_2.goto(+350, 0)
    elif response == 'vertical':
        ball.dy *= -1
        paddle_1.goto(0, +260)
        paddle_2.goto(0, -260)


# The game was finished
def game_over(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element):
    global response
    ball.goto(0, 0)
    ball.dx = 0
    ball.dy = 0

    if response == 'horizontal':
        scoreboard.goto(0, 230)
        scoreboard.write("Wanna play again? Y for Yes, N for No!", align="center", font=("Verdana", 18, "normal"))
        scoreboard.goto(0, 260)
    elif response == 'vertical':
        scoreboard.goto(-160, 20)
        scoreboard.write("Wanna play again? Y for Yes, N for No!", align="center", font=("Verdana", 18, "normal"))
        scoreboard.goto(-270, 0)

    scoreboard.color("yellow")
    # Choose to continue or finish the game
    game_screen.onkeypress(game_element.reset, "y")
    game_screen.onkeypress(game_element.return_to_main, "n")

    if response == 'horizontal':
        paddle_1.goto(-350, 0)
        paddle_2.goto(+350, 0)
    elif response == 'vertical':
        paddle_1.goto(0, +260)
        paddle_2.goto(0, -260)


# Reset the scoreboard after the games has finished
def reset_scoreboard(scoreboard):
    scoreboard.clear( )
    scoreboard.goto(0, 260)


# Start Game
def start_pong_game(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element):
    global response
    global score_player_a
    global score_player_b
    global color_paddle_1
    global color_paddle_2

    # Move the ball which starts from 0.
    ball.setx(ball.xcor( ) + ball.dx)
    ball.sety(ball.ycor( ) + ball.dy)

    # Border Checking - Top and Down Border - Compare Coordinate. When it hits a certain point, it needs to bound
    if response == 'horizontal':
        if ball.ycor( ) > 290:
            ball.sety(290)
            # Reversing the direction
            ball.dy *= -1

        if ball.ycor( ) < -290:
            ball.sety(-290)
            # Reversing the direction
            ball.dy *= -1

        # Border Checking - Left and Right
        if ball.xcor( ) > 390:
            # Coming back to center
            back_to_center(scoreboard, ball, paddle_1, paddle_2)
            score_player_a += 1
            scoreboard.write(
                f"Home ({color_paddle_1.title( )}): {score_player_a} Away ({color_paddle_2.title( )}): {score_player_b}".format(
                    score_player_a, score_player_b), align="center",
                font=("Verdana", 18, "normal"))
            if score_player_a == 2:
                reset_scoreboard(scoreboard)
                scoreboard.color(color_paddle_1)
                scoreboard.write("Game Over! Home won", align="center", font=("Verdana", 18, "normal"))
                game_over(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
                score_player_a = 0
                score_player_b = 0

        if ball.xcor( ) < -390:
            # Coming back to center
            back_to_center(scoreboard, ball, paddle_1, paddle_2)
            score_player_b += 1
            scoreboard.clear( )
            scoreboard.write(
                f"Home ({color_paddle_1.title( )}): {score_player_a} Away ({color_paddle_2.title( )}): {score_player_b}".format(
                    score_player_a, score_player_b), align="center",
                font=("Verdana", 18, "normal"))
            if score_player_b == 2:
                reset_scoreboard(scoreboard)
                scoreboard.color(color_paddle_2)
                scoreboard.write("Game Over! Away won", align="center", font=("Verdana", 18, "normal"))
                game_over(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
                score_player_a = 0
                score_player_b = 0

        # Paddle and Ball Collisions - avoid ball going after the paddle
        if (-340 > ball.xcor( ) > -350) and (paddle_1.ycor( ) + 50 > ball.ycor( ) > paddle_1.ycor( ) - 50):
            ball.setx(-340)
            ball.dx *= -1

        if (340 < ball.xcor( ) < 350) and (paddle_2.ycor( ) + 50 > ball.ycor( ) > paddle_2.ycor( ) - 50):
            ball.setx(340)
            ball.dx *= -1
    elif response == 'vertical':
        # Border Checking - Left and Right Border - Compare Coordinate. When it hits a certain point, it needs to bound
        if ball.xcor( ) > 350:
            ball.setx(350)
            # Reversing the direction
            ball.dx *= -1

        if ball.xcor( ) < -350:
            ball.setx(-350)
            # Reversing the direction
            ball.dx *= -1

        # Border Checking - Up and Down
        if ball.ycor( ) < -290:
            # Coming back to center
            back_to_center(scoreboard, ball, paddle_1, paddle_2)
            score_player_a += 1
            scoreboard.write(
                f"Home ({color_paddle_1.title( )}): {score_player_a}\nAway ({color_paddle_2.title( )}): {score_player_b}".format(
                    score_player_a, score_player_b), align="center",
                font=("Verdana", 18, "normal"))
            if score_player_a == 2:
                reset_scoreboard(scoreboard)
                scoreboard.color(color_paddle_1)
                scoreboard.goto(-250, 70)
                scoreboard.write("Game Over! Home won", align="center", font=("Verdana", 18, "normal"))
                game_over(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
                score_player_a = 0
                score_player_b = 0

        if ball.ycor( ) > 290:
            # Coming back to center
            back_to_center(scoreboard, ball, paddle_1, paddle_2)
            score_player_b += 1
            scoreboard.clear( )
            scoreboard.write(
                f"Home ({color_paddle_1.title( )}): {score_player_a}\nAway ({color_paddle_2.title( )}): {score_player_b}".format(
                    score_player_a, score_player_b), align="center",
                font=("Verdana", 18, "normal"))
            if score_player_b == 2:
                reset_scoreboard(scoreboard)
                scoreboard.color(color_paddle_2)
                scoreboard.goto(-250, 70)
                scoreboard.write("Game Over! Away won", align="center", font=("Verdana", 18, "normal"))
                game_over(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
                score_player_a = 0
                score_player_b = 0

        # Paddle and Ball Collisions - avoid ball going after the paddle

        if (-260 > ball.ycor( ) > -270) and (paddle_2.xcor( ) - 50 < ball.xcor( ) < paddle_2.xcor( ) + 50):
            ball.sety(-260)
            ball.dy *= -1

        if (260 < ball.ycor( ) < 270) and (paddle_1.xcor( ) - 50 < ball.xcor( ) < paddle_1.xcor( ) + 50):
            ball.sety(260)
            ball.dy *= -1


def mode_choose():
    global response
    # Creating Game Screen
    game_screen = turtle.Screen( )
    game_screen.bgpic("black.gif")
    game_screen.update( )
    game_screen.title("Welcome to Pong Game")
    game_screen.bgcolor("black")
    game_screen.setup(width=800, height=600)
    response = game_screen.textinput("Game Mode", "Choose the game mode: Horizontal or Vertical")
    game_screen.listen( )
    if response.lower( ) == 'horizontal' or response.lower( ) == 'vertical':
        run_game( )


# Run the Game after P was pressed on the main menu and the game mode was selected or the game was restarted
def run_game():
    global response

    # Creating Game Screen
    game_screen = turtle.Screen( )
    game_screen.bgpic("black.gif")
    game_screen.update( )
    game_screen.title("Welcome to Pong Game")
    game_screen.bgcolor("black")
    game_screen.setup(width=800, height=600)
    # Stop window from updating
    # Game speed is increased
    game_screen.tracer(0)

    # Paddle 1
    paddle_1 = pong_paddle.Paddle( )
    # Set shape and color of Paddle 1
    paddle_1.shape("square")
    global color_paddle_1
    color_paddle_1 = game_screen.textinput("Paddle 1", "Type the color of the first paddle:")
    paddle_1.color(color_paddle_1)
    # Set position of the Paddle 1
    if response == 'horizontal':
        paddle_1.goto(-350, 0)
    elif response == 'vertical':
        # The paddle needs to pe reshaped for the second game mode
        paddle_1.shapesize(stretch_wid=1, stretch_len=4)
        paddle_1.goto(0, 260)

    # Paddle 2
    paddle_2 = pong_paddle.Paddle( )
    # Set shape and color of Paddle 2
    paddle_2.shape("square")
    global color_paddle_2
    color_paddle_2 = game_screen.textinput("Paddle 2", "Type the color of the second paddle:")
    paddle_2.color(color_paddle_2)
    # Set position of the Paddle 2
    if response == 'horizontal':
        paddle_2.goto(+350, 0)
    elif response == 'vertical':
        paddle_2.shapesize(stretch_wid=1, stretch_len=4)
        paddle_2.goto(0, -260)

    # Ball
    ball = pong_ball.Ball( )
    # Set shape and color of ball
    ball.shape("circle")
    ball.color("white")
    # Set position on the middle
    ball.goto(0, 0)

    # Scoreboard
    scoreboard = pong_scoreboard.ScoreBoard( )
    if response == 'horizontal':
        scoreboard.goto(0, 260)
        scoreboard.write(
            f"Home ({color_paddle_1.title( )}): {score_player_a} Away ({color_paddle_2.title( )}): {score_player_b}",
            align="center", font=("Verdana", 18, "normal"))
    elif response == 'vertical':
        scoreboard.goto(-270, 0)
        scoreboard.write(
            f"Home ({color_paddle_1.title( )}): {score_player_a}\nAway ({color_paddle_2.title( )}): {score_player_b}",
            align="center", font=("Verdana", 18, "normal"))

    # Generate Game Elements
    game_element = pong_game_elements.GameElements(scoreboard, ball, paddle_1, paddle_2, game_screen)
    game_element.running = True
    while game_element.running:
        # Keyboard binding
        game_screen.listen( )
        if response == 'horizontal':
            # Paddle 1 Moving up and down
            game_screen.onkeypress(paddle_1.paddle_moving_up, "w")
            game_screen.onkeypress(paddle_1.paddle_moving_down, "s")
            # Paddle 2 Moving up and down
            game_screen.onkeypress(paddle_2.paddle_moving_up, "i")
            game_screen.onkeypress(paddle_2.paddle_moving_down, "k")
        elif response == 'vertical':
            # Paddle 1 Moving left and right
            game_screen.onkeypress(paddle_1.paddle_moving_left, "w")
            game_screen.onkeypress(paddle_1.paddle_moving_right, "s")
            # Paddle 2 Moving left and right
            game_screen.onkeypress(paddle_2.paddle_moving_left, "i")
            game_screen.onkeypress(paddle_2.paddle_moving_right, "k")

        # Start game
        start_pong_game(scoreboard, ball, paddle_1, paddle_2, game_screen, game_element)
        # Update screen
        game_screen.update( )
