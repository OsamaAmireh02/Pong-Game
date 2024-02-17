from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 0.1
        self.y = 0.1

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.setpos(new_x, new_y)

    def y_bounce(self):
        self.y *= -1

    def x_bounce(self):
        self.x *= -1

    def reset_ball(self):
        self.setpos(0, 0)

