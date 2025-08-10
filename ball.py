from turtle import Turtle


def safe_heading(angle):
    if -10 < angle % 360 < 10 or 170 < angle % 360 < 190:
        angle += 20
    return angle


class Ball(Turtle):
    def __init__(self, paddle):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -135)
        self.left(90)
        self.game_is_on = False
        self.speed(1)
        self.paddle = paddle

    def start_game(self):
        self.game_is_on = True

    def detect_collision_with_walls(self):
        if self.xcor() < -290:
            self.setheading(safe_heading(180 - self.heading()))
            self.setx(-289)
        elif self.xcor() > 290:
            self.setheading(safe_heading(180 - self.heading()))
            self.setx(289)
        elif self.ycor() > 255:
            self.setheading(safe_heading(-self.heading()))
            self.sety(254)

    def detect_collision_with_paddle(self):
        if -135 > self.ycor() > -145:
            if self.paddle.xcor() - 25 <= self.xcor() <= self.paddle.xcor() + 25:
                self.setheading(safe_heading(-self.heading()))
                self.sety(-134)
                print("centre")
            elif self.paddle.xcor() - 75 <= self.xcor() < self.paddle.xcor() - 25:
                self.setheading(safe_heading(-self.heading() + 30))
                self.sety(-134)
                print("left")
            elif self.paddle.xcor() - 25 < self.xcor() <= self.paddle.xcor() + 75:
                self.setheading(safe_heading(-self.heading() - 30))
                self.sety(-134)
                print("right")

    def end_game(self):
        if self.ycor() < -300:
            self.game_is_on = False
            self.paddle.game_is_on = False
