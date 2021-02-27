from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.goto(0,-290)
        self.setheading(90)
        self.color("white")
        self.pensize(10)
        self.make_line()
        
    
    def make_line(self):
        self.speed("fastest")
        for i in range(20):
            self.forward(10)
            self.penup()
            self.forward(20)
            self.pendown()

