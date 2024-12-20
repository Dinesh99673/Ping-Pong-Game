from turtle import Screen, Turtle
import time

def takeup():
    y1 = Block.ycor()
    Block.goto(430,y1+20)
    Block1.goto(-430,y1+20)

def takedown():
    y1 = Block.ycor()
    Block.goto(430,y1-30)
    Block1.goto(-430,y1-30)


screen = Screen()
screen.setup(width=900,height=700)
screen.bgcolor("black")
screen.title("Ping Pong Game")

segments = []

screen.listen()
screen.onkey(takeup,"Up")
screen.onkey(takedown,"Down")

num = 420
for i in range(6):
    seg = Turtle("square")
    seg.shapesize(4,0.5)
    seg.color("white")
    seg.penup()
    seg.goto((0,num-120))
    segments.append(seg)
    num-=120

Block = Turtle("square")
Block.shapesize(4,1)
Block.color("white")
Block.penup()
Block.goto((430,0))

Block1 = Turtle("square")
Block1.shapesize(4,1)
Block1.color("white")
Block1.penup()
Block1.goto((-430,0))





screen.exitonclick()