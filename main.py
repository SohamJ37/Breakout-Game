import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from blocks import Blocks

window = Screen()
window.tracer(0)
window.bgcolor("black")
window.setup(600, 550)
window.listen()

paddle = Paddle()
ball = Ball(paddle)
block = Blocks(ball)
block.create_block()


window.onkeypress(paddle.move_left, "Left")
window.onkeypress(paddle.move_right, "Right")
window.onkeypress(ball.start_game, "Up")


while paddle.game_is_on:
    window.update()

    ball.detect_collision_with_walls()
    ball.detect_collision_with_paddle()
    block.detect_collision_with_ball(ball)

    if ball.game_is_on:
        ball.forward(3)
        time.sleep(0.01)

    ball.end_game()

window.mainloop()
