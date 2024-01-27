from tkinter import *
import pandas as pd
import random, json

BACKGROUND_COLOR = "#B1DDC6"

try:  #  從我們尚未學會的字卡打開
    not_learned_french_words = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:  #  如果我們是第一次開啟此APP，我們要創一個新的字卡集
    french_words = pd.read_csv("./data/french_words.csv")
    dict_french_words = french_words.to_dict(orient="records")
else:  #  如果try沒有問題的話，從尚未學會的字卡，重新用dict的方式開啟
    dict_french_words = not_learned_french_words.to_dict(orient="records")

def is_remember():
    global current_card, countdown
    window.after_cancel(countdown)
    current_card = random.choice(dict_french_words)
    fcard.itemconfig(title, text="French", fill="black")
    fcard.itemconfig(vocabulary, text=f"{current_card['French']}", fill="black")
    fcard.itemconfig(image, image=card_front)
    countdown = window.after(5000, change_card)

def change_card():
    fcard.itemconfig(image, image=card_back)
    fcard.itemconfig(title, text="English", fill="white")
    fcard.itemconfig(vocabulary, text=f"{current_card['English']}", fill="white")


def save_card():
    global current_card, countdown
    dict_french_words.remove(current_card)
    #  重新呼叫新的卡片
    is_remember()
    #  將尚未記起來的字卡，儲存起來
    data = pd.DataFrame(dict_french_words)
    #  index=False表示在存成CSV檔時，不要再加上row index
    data.to_csv("./data/words_to_learn.csv", index=False)


# -------------------------------------------------------





window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
#  建立一個新的字典，當我們隨機選取時，可暫存資訊，供翻卡使用
current_card = {}


countdown = window.after(3000, change_card)


wrong = PhotoImage(file="./images/wrong.png")
right = PhotoImage(file="./images/right.png")
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

fcard = Canvas(width=800, height=526)
#  建立front圖片
image = fcard.create_image(400, 263, image=card_front)
fcard.grid(row=0, column=0, columnspan=2)
fcard.config(bg=BACKGROUND_COLOR, highlightthickness=0)

#  建立Title文字
title = fcard.create_text(400, 150, text="", font=("Aerial", 40, "italic"))

#  建立vocabulary文字
vocabulary = fcard.create_text(400, 263, text="", font=("Aerial", 60, "bold"))
wrong_button = Button(image=wrong, highlightthickness=0, command=is_remember)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right, highlightthickness=0, command=save_card)
right_button.grid(row=1, column=1)


is_remember()


window.mainloop()
