from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard 


paddle = Turtle()
screen=Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)    #animation gets turned off

#Calling of all classes
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
#screen listening and paddle controlling
screen.listen()
screen.onkey(r_paddle.go_Up, "Up")
screen.onkey(r_paddle.go_Down, "Down")
screen.onkey(l_paddle.go_Up, "w")
screen.onkey(l_paddle.go_Down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detecting collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_Y()

    #Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_X()
        
    # right paddle misses the ball    
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    #Detect left side
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        
screen.exitonclick()