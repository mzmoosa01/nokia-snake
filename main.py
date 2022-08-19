from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
game_on = True


def setup_game():
    global screen
    global game_on
    game_on = True
    screen.setup(600, 600)
    screen.bgcolor('black')
    screen.title('snake')

    my_snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.tracer(0)
    screen.listen()
    screen.onkey(fun=my_snake.left, key='Left')
    screen.onkey(fun=my_snake.right, key='Right')
    screen.onkey(fun=my_snake.up, key='Up')
    screen.onkey(fun=my_snake.down, key='Down')
    screen.onkey(fun=reset_game, key='r')
    start_game(my_snake, food, scoreboard)


def start_game(my_snake, food, scoreboard):
    global game_on

    while game_on:
        screen.update()
        time.sleep(0.1)
        my_snake.move()

        # Handle collision with food
        if my_snake.head.distance(food) < 15:
            food.move()
            scoreboard.add_score()
            my_snake.grow()

        # handle collision with sides
        if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
            game_on = False
            scoreboard.game_over()

        # Handle collision with tail
        for segment in my_snake.segments[1:]:
            if my_snake.head.distance(segment) < 10:
                game_on = False
                scoreboard.game_over()


def reset_game():
    global screen
    global game_on
    if not game_on:
        screen.clear()
        setup_game()


setup_game()
screen.exitonclick()
