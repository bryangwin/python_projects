import turtle
from turtle import Turtle
import colorgram
import random

screen = turtle.Screen()
screen.colormode(255)
colors = colorgram.extract('image.jpg', 10)
colors_list = [(226, 226, 226), (236, 236, 236), (182, 65, 65), (213, 149, 149), (14, 24, 24), (230, 237, 237), (239, 208, 208), (241, 234, 234), (237, 62, 62), (157, 26, 26)]

tim = Turtle()

tim.up()
tim.hideturtle
tim.speed(500)
for _ in range(10):
    for _ in range(10):
        tim.color(random.choice(colors_list))
        tim.dot(20)
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)


screen.exitonclick()