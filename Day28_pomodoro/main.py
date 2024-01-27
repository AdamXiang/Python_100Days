from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repos = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    #  讓timer暫停
    global repos
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    repos = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown():
    global repos
    repos += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #  如果 repos 是第八次的話，我們要休息25分鐘
    if repos % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif repos % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    # if repos 是第一次、第三次、第五次、第七次，我們要執行 work_sec
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    #  按按鈕後，開始計時倒數，乘60，表示5分鐘
    # count_down(5 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    #  我們要format時間的顯示成 "00:00"即"分:秒"
    #  floor 可以傳回去除小數的最大整數
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        #  利用dynamic typing來解決，module不是兩位數的問題
        count_sec = "0" + f"{count_sec}"
    #  類似其他widgets的參數設定，如label.config(text="")，這表示要抓哪個canvas，改變此canvas的甚麼
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        #  多少秒後呼叫後面的function，如這個的話是一秒後呼叫
        #  如果我們想要取消計時器，必須將下面這行code用一變數存起來
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        #  如果計時器歸0的話，重新啟動
        start_countdown()
        #  當每次work的session跑完時，增加checkmark
        checkmark = ""
        #  透過repos/2可以得知現在是第幾個session
        work_sessions = floor(repos / 2)
        for _ in range(work_sessions):
            checkmark += "✔"
        check_label.config(text=checkmark)
        # if repos % 2 == 0:
        #     checkmark += "✔"
        #     check_label.config(text=checkmark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#  建立主題標籤
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

#  建立開始按鈕
start_button = Button(text="Start", bg="white", highlightthickness=0, command=start_countdown)
start_button.grid(column=0, row=2)

#  建立重新開始按鈕
reset_button = Button(text="Reset", bg="white", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

#  建立check mark label
check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

#  建立畫布物件，highlightthickness代表畫布的border，0是不要邊界的意思
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
#  建立圖片物件
tomato_img = PhotoImage(file="tomato.png")
#  在畫布上建立圖片
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)




window.mainloop()