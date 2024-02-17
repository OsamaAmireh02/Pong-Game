from turtle import Turtle


class CreateScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def screen_setup(self):
        self.goto(0, -270)
        self.setheading(90)
        self.pencolor("white")
        self.pensize(7)
        for _ in range(0, 10):
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)

    def set_records(self, record1, record2):
        self.clear()
        self.screen_setup()
        self.goto(15, 220)
        self.write(f"{record1}", font=("Arial", 50, "bold"))
        self.goto(-50, 220)
        self.write(f"{record2}", font=("Arial", 50, "bold"))


