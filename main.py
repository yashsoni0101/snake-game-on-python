from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)   #black screen will be shown until update is called


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.rigth, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)    # movement delayed by 0.1 seconds # it means delay by 0.1 seconds and refresh the screen(update)
    snake.move()

    #detecting the food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
