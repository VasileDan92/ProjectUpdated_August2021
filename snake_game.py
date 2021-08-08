import turtle
import time
import snake_head
import snake_vitamin
import random
import snake_scoreboard
import snake_game_elements

# Color of the snake()
snake_color = ''
# Delay of 0.1 seconds
delay = 0.1
# Score and highscore. The highscore is initialized everytime with the value saved in the snake_high_score.txt file
score = 0
with open("snake_high_score.txt", mode="r") as data:
    high_score = int(data.read( ))

# List with body parts of snake: start of the game - 0 vitamins, so []
segments = []


def game_over(scoreboard, head, vitamin, game_screen, game_element):
    global high_score
    # When the game is over the highscore is overwritten in the snake_high_score.txt file
    with open("snake_high_score.txt", mode="w") as data:
        data.write(str(high_score))
    head.goto(0, 0)
    vitamin.goto(0, 150)
    scoreboard.goto(0, 230)
    scoreboard.write("Wanna play again? Y for Yes, N for No!", align="center", font=("Verdana", 16, "normal"))
    scoreboard.goto(0, 260)

    game_screen.onkeypress(game_element.reset, "y")
    game_screen.onkeypress(game_element.return_to_main, "n")


def reset_scoreboard(scoreboard):
    scoreboard.clear( )
    scoreboard.goto(0, 260)


# Starting Game
def start_snake_game(scoreboard, head, vitamin, game_screen, game_element):
    game_screen.update( )
    global score
    global high_score
    global delay

    # Check for a collision with the border
    if head.xcor( ) > 350 or head.xcor( ) < -350 or head.ycor( ) > 170 or head.ycor( ) < -170:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear( )

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        scoreboard.clear( )
        scoreboard.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                         font=("Verdana", 16, "normal"))
        game_over(scoreboard, head, vitamin, game_screen, game_element)

        # Check for a collision with the food
    if head.distance(vitamin) < 20:
        # Snake color
        global snake_color

        # Move the food to a random spot
        x = random.randint(-350, 350)
        y = random.randint(-170, 170)
        vitamin.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle( )
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(snake_color)
        new_segment.penup( )
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        scoreboard.clear( )
        scoreboard.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                         font=("Verdana", 16, "normal"))

        # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor( )
        y = segments[index - 1].ycor( )
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor( )
        y = head.ycor( )
        segments[0].goto(x, y)

    head.move( )

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear( )

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            scoreboard.clear( )
            scoreboard.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                             font=("Verdana", 16, "normal"))

            game_over(scoreboard, head, vitamin, game_screen, game_element)

    time.sleep(delay)


def run_game():
    # Creating Game Screen
    game_screen = turtle.Screen( )
    game_screen.bgpic("border.gif")
    game_screen.update( )
    game_screen.title("Welcome to Snake Game")
    game_screen.bgcolor("black")
    game_screen.setup(width=800, height=600)
    # turns off animation on the screen
    game_screen.tracer(0)

    # Choose color of the snake
    global snake_color
    snake_color = game_screen.textinput("Snake Color", "Choose the color of the snake: ")

    # Define objects
    head = snake_head.SnakeHead( )
    vitamin = snake_vitamin.SnakeVitamin( )

    # ScoreBoard
    scoreboard = snake_scoreboard.ScoreBoard( )
    scoreboard.goto(0, 260)
    scoreboard.write(f"Score: 0 High Score: {high_score}", align="center", font=("Verdana", 16, "normal"))

    # Generate Game Elements
    game_element = snake_game_elements.GameElements(scoreboard, head, vitamin, game_screen)
    game_element.running = True
    while game_element.running:
        # Keyboard binding
        game_screen.listen( )
        game_screen.onkeypress(head.go_up, "w")
        game_screen.onkeypress(head.go_down, "s")
        game_screen.onkeypress(head.go_left, "a")
        game_screen.onkeypress(head.go_right, "d")
        # Start game
        start_snake_game(scoreboard, head, vitamin, game_screen, game_element)
        # Update screen
        game_screen.update( )
    game_screen.mainloop( )
