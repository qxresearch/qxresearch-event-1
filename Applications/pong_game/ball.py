from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.X_move = 10
        self.Y_move = 10
        self.move_speed = 0.1
        
    def move(self):
        new_X = self.xcor() + self.X_move
        new_Y = self.ycor() + self.Y_move
        self.goto(new_X,new_Y)
    
    def bounce_Y(self):
        self.Y_move *= -1
        
    def bounce_X(self):
        self.X_move *= -1
        self.move_speed *= 0.9
    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_X()