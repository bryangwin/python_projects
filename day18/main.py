from turtle import Turtle, Screen
import turtle
timmy = Turtle()

turtle.colormode(255)
timmy.shape("classic")
timmy.color("green")

import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

# # Define a list of possible colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]
timmy.speed(500)
end = 360

def draw_sprio(gap):
    for _ in range(int(360/gap)):    
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)
        
draw_sprio(1)

# # Generate a list of 8 random colors
# random.choice(colors)

# angle_list = [0, 90, 180, 270]
# timmy.pensize(10)


# for _ in range(200):
#     timmy.setheading(random.choice(angle_list))
#     timmy.forward(50)
#     timmy.color(random_color())


# sides = 3
# for _ in range(8):
#     timmy.color(random.choice(colors))  
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(360/sides)
#     sides += 1 
           



screen = Screen()
screen.exitonclick()

