from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))

scoreboard_1 = Scoreboard((40, 250))
scoreboard_2 = Scoreboard((-40, 250))

screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")

screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")

ball = Ball()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall (top and bottom)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle
    elif ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when paddle misses ball
    elif ball.xcor() > 380:
        scoreboard_2.update_scoreboard()
        ball.reset_position()

    elif ball.xcor() < -380:
        scoreboard_1.update_scoreboard()
        ball.reset_position()

screen.exitonclick()
