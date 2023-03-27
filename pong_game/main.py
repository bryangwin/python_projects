from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

line = Turtle()
line.color("white")
line.up()
line.goto(0,-400)
line.down()
line.setheading(90)

for len in range(80):
    line.forward(10)
    line.up()
    line.forward(10)
    line.down()



scoreboard = Scoreboard("right")
right_paddle = Paddle("right")
left_paddle = Paddle("left")
ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


sleep = 0.1

game_on = True
while game_on:
    
    time.sleep(sleep)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
        
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()
        sleep *= 0.8
        
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
        sleep *= 0.8
        
    if ball.xcor() < -400:
        scoreboard.add_score_r()
        ball.reset_ball()
        sleep = 0.1
    
    if ball.xcor() > 400:
        scoreboard.add_score_l()
        ball.reset_ball()
        sleep = 0.1

screen.exitonclick() 