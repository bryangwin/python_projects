from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.up()
        self.setheading(90)
        self.goto(0, -275)
    
    def move_forward(self):
        self.forward(10)
        
    def move_backward(self):
        self.backward(10)
        
    def reset_player(self):
        self.hideturtle()
        self.goto(0, -275)
        self.showturtle()