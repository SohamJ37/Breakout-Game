from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.game_is_on = True
        self.shapesize(stretch_wid=0.3, stretch_len=5)
        self.goto(0, -150)

    def move_right(self):
        if self.xcor() < 240:
            self.forward(20)

    def move_left(self):
        if self.xcor() > -250:
            self.back(20)
