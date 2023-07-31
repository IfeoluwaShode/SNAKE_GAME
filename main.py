import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Ifeoluwa's Snake game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()


screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # DETECTS COLLISION WITH FOOD, TRACKS SCORE, and INCREASE SNAKE'S LENGTH
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_tracker()

    # DETECTS WHEN GAME ENDS
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    # DETECTS WHEN SNAKE HEAD TOUCH TAIL
    for index in range(1, len(snake.snake_list)-1):
        if snake.head.distance(snake.snake_list[index]) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
