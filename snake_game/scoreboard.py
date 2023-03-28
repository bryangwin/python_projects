from turtle import Turtle

FONT = font=("Courier", 20, "normal")
ALIGNMENT = align="center"

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.up()
        self.goto(0, 275)
        self.color("White")
        self.update_score()
        
    def add_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("highscore.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score} ", align=ALIGNMENT ,font=FONT )
        
            
            
            
            



    # def game_over(self): 
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)