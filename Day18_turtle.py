import random
from turtle import Turtle, Screen
from random import randrange, choice
screen = Screen()
adam_turtle = Turtle()
adam_turtle.shape("turtle")


# pen_color = ["cyan", "brown", "DarkGoldenrod1", "DarkSalmon", "DeepPink4", "LightCoral", "ForestGreen", "tomato"]
direction = [0, 90, 180, 270]


# 畫正方形
def square():
    for n in range(4):
        adam_turtle.forward(100)
        adam_turtle.right(90)


# draw different shapes
def draw_shape(num):
    change_color()
    angle = 360 / num
    for _ in range(num):
        adam_turtle.forward(100)
        adam_turtle.right(angle)


# 畫虛線
def dash_line():
    for n in range(15):
        adam_turtle.forward(10)
        adam_turtle.dot(10, "white")
        # 或者可以使用 penup()，讓畫筆拿起來，走了10步後，再用pendown()，把筆放下


# 換畫筆顏色
def change_color():
    # adam_turtle.pencolor(choice(pen_color))
    R = randrange(0, 257, 10)
    G = randrange(0, 257, 10)
    B = randrange(0, 257, 10)
    # 改變colormode使得能夠接受到255
    screen.colormode(255)
    adam_turtle.color(R, G, B)


# 畫各種不同形狀
def draw_different_picture():
    for shape_of_sides in range(3, 11):
        draw_shape(shape_of_sides)


# random walk
adam_turtle.pensize(15)
adam_turtle.speed(0)
def random_walk():
    speed = 1
    for _ in range(200):
        change_color()
        # adam_turtle.pensize(_)
        adam_turtle.setheading(choice(direction))
        adam_turtle.forward(30)
        # if speed <= 10 and _ / 10 == 0:
        #     speed += 1
        #     adam_turtle.speed(speed)
        # elif _ > 200:
        #     adam_turtle.speed(0)


draw_different_picture()
# random_walk()
screen.exitonclick()
