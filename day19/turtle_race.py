from turtle import Turtle, Screen
import random


colors = ['red', 'orange', 'cyan', 'green', 'blue', 'indigo', 'violet']

turtle_list = []


screen = Screen()
screen.setup(width=500, height=400)


start_x = -200
start_y = 125

# Create six turtles and set their positions
for i in range(6):
    turtle_i = Turtle()
    turtle_i.shape('turtle')
    turtle_i.color(colors[i])
    turtle_i.penup()
    turtle_i.goto(start_x, start_y - 50 * i)
    turtle_list.append(turtle_i)

user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win?")
    
if user_bet:
    race_on = True

while race_on:
    for t in turtle_list:
        if t.xcor() > 230:
            winning_color = t.pencolor()   
            race_on = False    
        move = random.randint(0, 20)
        t.forward(move)
 
       
if user_bet == winning_color:
    print(f"You win! The {winning_color} turtle won the race. ")
else:
    print(f"You lose. The {winning_color} turtle won the race. ")
    

screen.exitonclick()
