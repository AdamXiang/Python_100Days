import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
# 路徑去抓gif檔
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_list = []
missing_list= []

us_states = pandas.read_csv("50_states.csv")
us_states_list = us_states["state"].tolist()
# x_list = us_states["x"].tolist()
# y_list = us_states["y"].tolist()

while len(correct_list) < 50:
    #  也可以使用title()，可以讓字串中的第一個字母大寫，其他小寫
    answer = screen.textinput(title=f"{len(correct_list)}/50 States Correct", prompt="What's another state's name?").title()
    #  輸入Exit，可以離開遊戲，並獲得還未猜對state的csv
    if answer == "Exit":
        missing_list = [state for state in us_states_list if state not in correct_list]
        missing_value = pandas.DataFrame(missing_list)
        missing_value.to_csv("missing_state.csv")
        break
    if answer in us_states_list:
            correct_list.append(answer)
            states_t = turtle.Turtle()
            states_t.penup()
            states_t.hideturtle()
            state_data = us_states[us_states.state == answer]
            states_t.goto(int(state_data.x), int(state_data.y))
            states_t.write(answer, move=False)
            #  也可以使用data["state"].item() 取得單一row的state資訊

# # 透過點擊screen得到每個state相對的座標位置
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()  #  類似screen.exitonclick，但其可以讓screen保留

# screen.exitonclick()