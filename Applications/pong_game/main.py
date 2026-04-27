from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import settings
import time

# Screen setup
screen = Screen()
screen.setup(width=settings.SCREEN_WIDTH, height=settings.SCREEN_HEIGHT)
screen.bgcolor(settings.BG_COLOR)
screen.title(settings.TITLE)
screen.tracer(0)

# Objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Game state
game_is_on = True
game_paused = False

# Controls
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

def toggle_pause():
    global game_paused
    game_paused = not game_paused

screen.onkey(toggle_pause, "space")

# Game loop
while game_is_on:
    if not game_paused:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # AI mode
        if settings.SINGLE_PLAYER:
            if l_paddle.ycor() < ball.ycor():
                l_paddle.go_up()
            elif l_paddle.ycor() > ball.ycor():
                l_paddle.go_down()

        # Wall collision
        if ball.ycor() > settings.WALL_LIMIT or ball.ycor() < -settings.WALL_LIMIT:
            ball.bounce_y()

        # Paddle collision
        if ((ball.distance(r_paddle) < settings.PADDLE_DISTANCE and ball.xcor() > settings.RIGHT_PADDLE_X) or
            (ball.distance(l_paddle) < settings.PADDLE_DISTANCE and ball.xcor() < settings.LEFT_PADDLE_X)):
            ball.bounce_x()

        # Miss detection
        if ball.xcor() > settings.OUT_OF_BOUNDS:
            ball.reset_position()
            scoreboard.l_point()

        if ball.xcor() < -settings.OUT_OF_BOUNDS:
            ball.reset_position()
            scoreboard.r_point()

        # Game Over
        if scoreboard.l_score == settings.WIN_SCORE:
            scoreboard.game_over("Left Player")
            game_is_on = False

        if scoreboard.r_score == settings.WIN_SCORE:
            scoreboard.game_over("Right Player")
            game_is_on = False

screen.exitonclick()