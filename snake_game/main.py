from turtle import Turtle, Screen
import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()
        
    if snake.head.xcor() > 285 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()
        
    for seg in snake.body[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()