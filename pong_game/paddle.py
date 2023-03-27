from turtle import Turtle

RIGHT_POS = (350, 0)
LEFT_POS = (-350, 0)

class Paddle(Turtle):
    def __init__(self, side) -> None:
        super().__init__()
        if side == "left":
            side = LEFT_POS
        elif side == "right":
            side = RIGHT_POS
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.up()
        self.goto(side)    
        
        
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)