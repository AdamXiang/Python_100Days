import turtle as t
import random
# import colorgram
## 抽出圖片中的顏色
# colors = colorgram.extract('image.jpg', 35)
#
# rgb_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_list.append(rgb)
## End
leo = t.Turtle()
screen = t.Screen()
screen.colormode(255)
leo.speed(0)
color_list = [(226, 231, 236), (58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171),
              (234, 226, 204), (224, 234, 230), (142, 178, 203), (139, 82, 105), (208, 90, 69),(237, 225, 233),
              (188, 80, 120), (69, 105, 90), (133, 182, 135), (133, 133, 74), (64, 156, 92), (47, 156, 193),
              (183, 192, 201), (213, 177, 191), (19, 58, 92), (20, 68, 113), (113, 123, 149), (227, 174, 166),
              (172, 203, 183), (156, 206, 217), (69, 58, 47), (72, 64, 53), (111, 46, 59), (53, 70, 64),
              (119, 46, 39), (48, 65, 61)]

# dot 跟 penup 搭配，不需要使用pendown，因為 dot 就是畫下去
def set_start():
    screen.screensize(3000, 2500)
    leo.penup()
    leo.setposition(-250, -250)


def hirst_dot():
    leo.dot(20, random.choice(color_list))
    leo.forward(50)


def set_position():
    xy = leo.pos()
    leo.penup()
    leo.setposition(-250, xy[1] + 50)

leo.hideturtle()
set_start()

for n in range(10):
    for _ in range(10):
        hirst_dot()
    set_position()

screen.exitonclick()