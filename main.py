from turtle import Screen, Turtle
import time
import paddle
import ball
import scoreBoard

#Screen Configuration
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)

r_paddle = paddle.Paddle((380,0))
l_paddle = paddle.Paddle((-380,0))
ball = ball.Ball()
r_scoreBoard = scoreBoard.ScoreBoard((50,260))
l_scoreBoard = scoreBoard.ScoreBoard((-50,260))


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s") 

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect Collision with wall (upper and lower)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncedByWall()

    #Detect Collision wuth Paddle
    if (ball.distance(r_paddle.position()) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle.position()) < 50 and ball.xcor() < -340):
        ball.bouncedByPaddle()

    #To detect if right Paddle missed the ball or not
    if ball.xcor() > 390:
        ball.reset_position()
        l_scoreBoard.increase()

    #To detect if left Paddle missed the ball or not
    if ball.xcor() < -390:
        ball.reset_position()
        r_scoreBoard.increase()



screen.exitonclick()