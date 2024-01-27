from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)  # 因為一開始square是20*20
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        self.setpos(self.xcor(), self.ycor() + 20)


    def go_down(self):
        self.setpos(self.xcor(), self.ycor() - 20)
