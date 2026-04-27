from turtle import Turtle
import settings

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + settings.PADDLE_MOVE_DISTANCE
        if new_y < settings.PADDLE_BOUNDARY:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - settings.PADDLE_MOVE_DISTANCE
        if new_y > -settings.PADDLE_BOUNDARY:
            self.goto(self.xcor(), new_y)