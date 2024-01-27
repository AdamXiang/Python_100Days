from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
## 用來建立新的形狀
# RET_COORDINATE= ((-50, 10), (50, 10), (50, -10), (-50, -10))
# screen.register_shape(name="rectangle", shape=RET_COORDINATE)
# paddle.shape("rectangle")
screen = Screen()
screen.setup(width=800, height=600)
screen.title(titlestring="Pong Game")
screen.bgcolor("black")
screen.tracer(0)

#  建立球拍
r_paddle = Paddle(position=(350, 0))
l_paddle = Paddle(position=(-350, 0))

#  建立球
ball = Ball()

#  建立記分板
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True

while is_game_on:
    screen.update()  # update 要配合loop不斷更新
    time.sleep(ball.move_speed)  #  讓每次更新延遲0.5秒，也就是每次都暫停0.5秒
    ball.move()

    #  偵測球有沒有撞到牆
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #  偵測球有沒有撞到球拍
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #  偵測如果球拍沒有擊到球
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

