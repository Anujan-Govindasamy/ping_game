from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen=Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("pong game")
screen.tracer(0)


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()

screen.onkey(fun=r_paddle.go_up,key="Up")
screen.onkey(fun=r_paddle.go_down,key="Down")
screen.onkey(fun=l_paddle.go_up,key="w")
screen.onkey(fun=l_paddle.go_down,key="s")

game_on=True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detecting collusion with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collusion ith paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when R paddle misses the ball
    if  ball.xcor() >380 :
        ball.reset()
        scoreboard.l_score_count()

    # detect when L paddle misses the ball
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_score_count()





screen.exitonclick()