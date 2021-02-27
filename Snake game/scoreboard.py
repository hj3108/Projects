from turtle import Turtle
ALIGNMENT= "center"
FONT=("Courier",14,"normal")

class Scoreboard(Turtle):
    def __init__(self):
       super().__init__()
       with open("e:/Python Tutorials/programs/app brewery/Snake game/data.txt") as data:
           self.high_score=int(data.read())
       self.color("white")
       self.penup()
       self.hideturtle()
       self.goto(0,270)
       self.score=0
       self.write(f"Score: {self.score} High Score:{self.high_score} ",align=ALIGNMENT,font=FONT)
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}",align=ALIGNMENT,font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def score_increment(self):
        self.score=self.score+1

    def reset(self):
        if self.score>int(self.high_score):
            self.high_score=self.score
            with open("e:/Python Tutorials/programs/app brewery/Snake game/data.txt","w") as data:
                data.write(f"{self.high_score}")
            
        self.score=0
        self.update_scoreboard()
    
    
       

     