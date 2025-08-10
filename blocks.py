from turtle import Turtle
import random
from ball import safe_heading


class Blocks:
    def __init__(self, ball):
        self.list_of_blocks = []
        self.list_of_colors = ['#ff595e', '#1982c4', '#8ac926', '#ffca3a']
        self.ball = ball

    def create_block(self):
        starting_x = -180
        starting_y = 200
        for i in range(5):
            for j in range(10):
                block = Turtle()
                block.penup()
                block.goto(starting_x, starting_y)
                block.color(random.choice(self.list_of_colors))
                block.shape('square')
                block.shapesize(stretch_wid=1, stretch_len=2)
                self.list_of_blocks.append(block)
                starting_x += 42
            starting_x = -180
            starting_y -= 22

    def detect_collision_with_ball(self, ball):
        if self.list_of_blocks:
            for block in self.list_of_blocks:

                # Get block edges
                block_left = block.xcor() - 30
                block_right = block.xcor() + 30
                block_top = block.ycor() + 20
                block_bottom = block.ycor() - 20

                # Ball position
                ball_x = ball.xcor()
                ball_y = ball.ycor()

                # Check collision
                if block_left < ball_x < block_right and block_bottom < ball_y < block_top:

                    # Determine collision side
                    overlap_x = min(abs(ball_x - block_left), abs(ball_x - block_right))
                    overlap_y = min(abs(ball_y - block_top), abs(ball_y - block_bottom))

                    if overlap_x < overlap_y:
                        # Side collision
                        ball.setheading(safe_heading(180 - ball.heading()))
                    else:
                        # Top/bottom collision
                        ball.setheading(safe_heading(-ball.heading()))

                    # Remove block
                    block.goto(1000, 1000)
                    self.list_of_blocks.remove(block)

                    # Push ball slightly out to prevent stuck
                    ball.forward(3)
                    break
        else:
            self.ball.game_is_on = False
            self.ball.paddle.game_is_on = False
