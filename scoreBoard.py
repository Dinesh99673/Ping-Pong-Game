from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 30, "normal")

class ScoreBoard(Turtle):

    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.updateScoreBoard()
        self.hideturtle()

    def updateScoreBoard(self):
        self.write(f"{self.score}",align=ALIGNMENT,font=FONT)

    def gameOver(self):
        self.goto(0,0)
        self.write(f"GAME OVER !!",align=ALIGNMENT,font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.updateScoreBoard()