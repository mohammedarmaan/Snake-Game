from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

score = 0
snake = Snake()
food = Food()
sb = Scoreboard()


screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        print(score)
        game_is_on = False
        sb.game_over()

    if snake.head.distance(food) < 15:
        sb.inc_score()
        food.refresh()
        snake.extend()

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            sb.game_over()

screen.exitonclick()
