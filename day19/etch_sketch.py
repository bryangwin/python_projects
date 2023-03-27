from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
    
def turn_left():
    tim.left(5)
    
def turn_right():
    tim.right(5)
    
def move_backard():
    tim.backward(10)
    
def reset_screen():
    tim.clear()
    tim.reset()
    
    
    
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backard)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset_screen)

screen.exitonclick()

