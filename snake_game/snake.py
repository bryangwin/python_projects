from turtle import Turtle, Screen


START_POS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen = Screen()
screen.listen()

class Snake:
    def __init__(self) -> None:
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        
    def create_snake(self):
        for position in START_POS:
            self.add_body(position)
                    
    def add_body(self, position):
        snake = Turtle()
        snake.up()
        snake.shape("square")
        snake.color("white")
        snake.goto(position)
        self.body.append(snake)      
        
    def extend(self):
        self.add_body(self.body[-1].position())    
                
    def move(self):
        for seg in range(len(self.body) - 1, 0, -1):
            x = self.body[seg - 1].xcor()
            y = self.body[seg - 1].ycor()
            self.body[seg].goto(x, y)
        self.head.forward(20)  
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)