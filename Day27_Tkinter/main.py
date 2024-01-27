from tkinter import *
# converter = 0
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=30, pady=10)


def listen_buttom():
    after_con = int(input.get()) * 1.609344
    result_label["text"] = round(after_con)

label = Label(text=" ", padx=10)
label.grid(column=0, row=0)

input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

button = Button(text="Calculate", bg="white", command=listen_buttom)
button.grid(column=1, row=2)

result_label = Label(text="0", padx=10, width=10)
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

des_label = Label(text="is equal to", padx=10)
des_label.grid(column=0, row=1)



window.mainloop()