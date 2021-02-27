from turtle import Screen,Turtle
from food import Food
from snake import Snake
from scoreboard import Scoreboard 
import random
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)#turn off the tracer  and doesn't display anything until we call update function.


snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")


game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1) # delay for 0.1 second and refresh the screen after updating it.
    snake.Move()
    
    #DETECT COLLISION WITH FOOD USING "distance" method.
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.score_increment()
        scoreboard.update_scoreboard()
        snake.extend()

    #DETECT COLLISION WITH WALL
    if snake.head.xcor()>280 or snake.head.xcor() <-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset()
        snake.reset()
                  
    #DETECT COLLISION WITH TAIL
    #if head collides with any segment in the tail then trigger game_over.
    for segment in snake.segments[1::]:                 
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()