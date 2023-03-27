from turtle import Turtle

FONT = font=("Courier", 50, "normal")
ALIGNMENT = align="center"
LEFT_SCORE = (-70, 240)
RIGHT_SCORE = (70, 240)

class Scoreboard(Turtle):
    def __init__(self, side) -> None:
        super().__init__()
        if side == "left":
            side = LEFT_SCORE
        if side == "right":
            side = RIGHT_SCORE
        self.hideturtle()
        self.up()
        self.lscore = 0
        self.rscore = 0
        self.print_score()
        
    def add_score_l(self):
        self.lscore += 1
        self.print_score()
        
    def add_score_r(self):
        self.rscore += 1
        self.print_score()
        
    def print_score(self):
        self.clear()
        self.goto(LEFT_SCORE)
        self.color("White")
        self.write(self.lscore, align=ALIGNMENT ,font=FONT )
        self.goto(RIGHT_SCORE)
        self.write(self.rscore, align=ALIGNMENT ,font=FONT )
        

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)