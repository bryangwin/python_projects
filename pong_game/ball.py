from turtle import Turtle



class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.x = 10
        self.y = 10
        
    def move(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x, y)    
        
    def bounce(self):
        self.y *= -1
        
    def paddle_bounce(self):
        self.x *= -1
        
    def reset_ball(self):
        self.x *= -1
        self.goto(0,0)
        