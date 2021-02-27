from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from line import Line

screen=Screen() #creating screen object from screen class.
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()
line=Line()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

screen.listen()

screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")

screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

game_is_on=True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #DETECT COLLISION WITH THE ABOVE AND BELOW WALL
    if ball.ycor()>280 or ball.ycor()<-280:
        #then ball needs to bounce.
        ball.bounce_y()
    
    # DETECT COLLISION WITH PADDLES.  
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320 :
        ball.bounce_x()

    #DETECT WHEN THE r_paddle MISSES THE BALL
    if ball.xcor()>390:
        ball.reset_position()
        scoreboard.l_point()

    #DETECT WHEN THE l_paddle MISSES THE BALL
    if ball.xcor()<-390:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()