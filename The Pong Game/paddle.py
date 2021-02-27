from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
      super().__init__()
      self.penup()
      self.shape("square")
      self.speed("fastest")
      self.shapesize(stretch_wid=5,stretch_len=1)
      self.goto(position)
      self.color("blue")
    
    def up(self):
        """Makes the paddle to move up."""
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def down(self):
        """Makes the paddle to move down."""
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)