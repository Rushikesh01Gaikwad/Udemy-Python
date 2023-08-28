from turtle import Turtle
Font = "Arial", 24
Alignment = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.updtescoreborad()

    def updtescoreborad(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=Alignment, font=Font)


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.updtescoreborad()
    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=Alignment, font=Font)

    def increasescore(self):
        self.score += 1
        self.clear()
        self.updtescoreborad()

