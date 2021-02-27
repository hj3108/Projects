from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
      super().__init__()
      self.penup()
      self.shape("circle")
      self.speed("fastest")
      self.goto(0,0)
      self.color("magenta")
      self.x_move=10
      self.y_move=10
      self.move_speed=0.1

    def move(self):
        """Moves the ball on the screen."""
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
    
    def bounce_y(self):
        """Bounces the ball in y-axis when it touches the above and below walls."""
        self.y_move*=-1

    def bounce_x(self):
        """Bounces the ball in x-axis when it touches the paddle."""
        self.x_move*=-1
        self.move_speed*=0.9

    def reset_position(self):
        """Resets the position back to (0,0)."""
        self.goto(0,0)
        self.move_speed=0.1 #to reset speed back to normal when one of the player looses.
        self.bounce_x()



        
      
        