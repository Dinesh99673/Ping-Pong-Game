from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x,new_y))

    #To bouunce the Ball by the walls (only up and down wall)
    def bouncedByWall(self):
        self.y_move *= -1

    #To Bounce the Ball by the Paddle and to increase the speed of the ball at every Bounce for Difficulty
    def bouncedByPaddle(self):
        self.move_speed *= 0.9
        self.x_move *= -1

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.x_move *= -1
