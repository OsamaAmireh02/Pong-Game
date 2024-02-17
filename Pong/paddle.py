from turtle import Turtle

PLAYER1 = (350, 0)
PLAYER2 = (-350, 0)


class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        if player == 1:
            self.setpos(PLAYER1)
        elif player == 2:
            self.setpos(PLAYER2)

    def go_up(self):
        new_y = self.ycor() + 10
        self.setpos(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 10
        self.setpos(self.xcor(), new_y)
