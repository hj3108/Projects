from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
DISTANCE=20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments=[]
        self.Create_Snake()
        self.head=self.segments[0]
    

    def Create_Snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position) 

    def add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.color("magenta")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments: # to move the previous segment out of the screen.
            seg.goto(10000,10000)
        self.segments.clear() #will remove all of the segments from the list of segments.
        self.Create_Snake()
        self.head=self.segments[0]


    def extend(self):
        """Adds a new segment to the existing snake when snake hits the food."""
        self.add_segment(self.segments[-1].position()) #gets hold of the last segment position i.e. the last item of segments list position and adds a segment there.

    def Move(self):
        #LOOPING THROUGH EACH OF THE SEGMENT STARTING FROM LAST SEGMENT TO THE FIRST SEGMENT.
        #(SO THAT THE TAIL FOLLOWS THE HEAD)
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y) 
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() !=DOWN:  #because if the snake is moving down we don't want it to directly move up.
            self.head.setheading(UP)
 
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
