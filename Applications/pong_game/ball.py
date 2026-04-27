from turtle import Turtle
import settings

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = settings.BALL_X_MOVE
        self.y_move = settings.BALL_Y_MOVE
        self.move_speed = settings.INITIAL_SPEED

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= settings.SPEED_INCREMENT

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = settings.INITIAL_SPEED
        self.bounce_x()