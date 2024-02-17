from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from screen import CreateScreen

screen = Screen()
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
paddle1 = Paddle(1)
paddle2 = Paddle(2)
screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")
ball = Ball()
scoreboard = CreateScreen()
score1 = 0
score2 = 0
game_is_on = True
scoreboard.set_records(score1, score2)
while game_is_on:
    ball.move()
    screen.update()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.y_bounce()
    if (ball.distance(paddle1) < 60 and ball.xcor() > 330) or (ball.distance(paddle2) < 60 and ball.xcor() < -330):
        ball.x_bounce()

    if ball.xcor() > 400:
        score2 += 1
        scoreboard.set_records(score1, score2)
        ball.reset_ball()
    elif ball.xcor() < -400:
        score1 += 1
        scoreboard.set_records(score1, score2)
        ball.reset_ball()


screen.exitonclick()
