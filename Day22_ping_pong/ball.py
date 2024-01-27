from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 15
        self.move_speed = 0.1  #  給 time.sleep 用的時間，暫停幾秒

    def move(self):
        new_x = self.xcor()
        new_y = self.ycor()
        self.goto(new_x + self.x_move, new_y + self.y_move)

    def bounce_y(self):  #  當撞到牆時，改變 Y axis 的方向
        self.y_move = -self.y_move

    def bounce_x(self):  #  當撞到牆時，改變 X axis 的方向，還有增加速度（X改變，表示打到球拍）
        self.x_move = -self.x_move
        self.move_speed *= 0.9  #  讓時間停越來越短

    def reset_position(self):
        self.home()
        self.bounce_x()
        self.move_speed = 0.1  #  reset move speed
