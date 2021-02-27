from turtle import Turtle
import random

class Food(Turtle): #inherited turtle class to food class.

   def __init__(self):
      super().__init__()
      self.shape("circle")
      self.penup()  #so that it doesn't draw.
      self.shapesize(0.5,0.5)
      self.color("blue")
      self.speed("fastest") #because we don't have to look at the animation of the food being created at the centre of the screen and moving to the desired location 
      self.refresh()
      #We are able to use these methods only because we have inherited it from turtle class.
       
   def refresh(self):
      random_x=random.randint(-270,270)
      random_y=random.randint(-270,270)
      self.goto(random_x,random_y)
