from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        with open ("e:/Python Tutorials/programs/app brewery/Turtle Crossing Game/data.txt") as data:
            self.high_score=data.read() 
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} Highest Level: {self.high_score}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
    
    def level_detection(self):
        if self.level>int(self.high_score):
            self.high_score=self.high_score
            with open("e:/Python Tutorials/programs/app brewery/Turtle Crossing Game/data.txt","w") as data:
                data.write(f"{self.level}")
