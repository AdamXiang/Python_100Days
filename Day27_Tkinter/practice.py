#  如果只要使用一個class，可以寫完整
#  如果要用module中很多的class再用*，表示全部import
from tkinter import *

window = Tk()

#  設置視窗標題
window.title("My First GUI Program")
#  設置視窗的高與寬
window.minsize(width=500, height=300)

#  建立label物件
my_label = Label(text="I am label!", font=("Arial", 24, "bold"))
#  讓label顯示
my_label.grid(column=0, row=0)

my_label.config(text="My text")

def button_clicked():
    sen = "I got clicked!"
    new_text = input.get()
    my_label["text"] = new_text
#  建立button物件，command表示觸發點擊的function
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button1 = Button(text="I am new!")
button1.grid(column=2, row=0)

#  建立Entry物件
input = Entry(width=10)
input.grid(column=3, row=2)
#  回傳Entry裡的文字，為字串






#  讓視窗持續開著
window.mainloop()

# def add(*num):
#     sum = 0
#     for n in num:
#         sum += n
#     return sum
#
# print(add(1,2,3,5,9,111,1235,152))
#
#
