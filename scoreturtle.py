from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial" , 12 , "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.change_score()

    def change_score(self):
        self.clear()
        self.goto(x=0 , y=280)
        self.write(arg=f"score: {self.score}" , move=True , align=ALIGNMENT , font=FONT)
        self.score += 1
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER" , align=ALIGNMENT , font=FONT)