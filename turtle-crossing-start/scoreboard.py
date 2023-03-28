from turtle import Turtle

FONT = font=("Courier", 24, "normal")
ALIGNMENT = align="center"

class Scoreboard(Turtle):
    def __init__ (self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.up()
        self.color("black")
        self.goto(0, 275)
        self.write(f"Level: {self.level} ", align=ALIGNMENT ,font=FONT )

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level} ", align=ALIGNMENT ,font=FONT )

        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT ,font=FONT )