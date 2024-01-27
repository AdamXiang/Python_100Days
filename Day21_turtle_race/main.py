from turtle import Turtle, Screen

leo = Turtle()
screen = Screen()
leo.shape("turtle")
leo.color("tomato")

def move_forward():
    leo.forward(10)


def move_backword():
    leo.backward(10)


def counter_clockwise():
    leo.left(36)


def clockwise():
    leo.right(36)


def end_game():
    leo.clear()
    leo.penup()
    leo.home()
    leo.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backword)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=end_game)
screen.exitonclick()
