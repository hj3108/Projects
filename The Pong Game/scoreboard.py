from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
      super().__init__()
      self.color("red")
      self.penup()
      self.hideturtle()
      self.l_score=0
      self.r_score=0
      self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()#to prevent overwriting
        self.goto(-100,200)
        self.write(self.l_score, align="center",font=("Courier",80, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center",font=("Courier",80, "normal"))
    
    def l_point(self):
        """To give left side a point when the right paddle misses."""
        self.l_score+=1
        self.update_scoreboard()
    
    def r_point(self):
        """To give right side a point when the left paddle misses."""
        self.r_score+=1
        self.update_scoreboard()
