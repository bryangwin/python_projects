from turtle import Turtle

FONT = font=("Courier", 20, "normal")
ALIGNMENT = align="center"

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.up()
        self.goto(0, 275)
        self.color("White")
        self.write(f"Score: {self.score} ", align=ALIGNMENT ,font=FONT )
        
    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} ", align=ALIGNMENT ,font=FONT )

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)